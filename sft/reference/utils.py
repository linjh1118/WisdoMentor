from collections import defaultdict, Counter
import os
import random
random.seed(888)
import re
from tqdm import tqdm
import sys
import math

def get_lines(file, n=None, do_strip=True, drop_func=None, file_prefix=None):
    """封装版的readlines，支持截取和过滤，PS: 默认strip，and过滤空行"""
    if os.path.isfile(file):
        with open(file, 'r') as f:
            lines = f.readlines()
    else:
        # `file` is a dir
        file_dir = file
        items = [item for item in os.listdir(file_dir) if not os.path.isdir(os.path.join(file_dir, item))]
        items = [item for item in items if item.startswith(file_prefix)]
        print(items)
        items = [os.path.join(file_dir, item) for item in items]
        lines = []
        for path in items:
            if os.path.isdir(path):
                continue
            with open(path, 'r') as f:
                lines += f.readlines()
    # base filter
    lines = [line for line in lines if len(line.strip('\n')) > 0]
    if drop_func is not None:
        lines = [line for line in lines if not drop_func(line)]
        
    if n is not None:
        lines = lines[:n]
    if do_strip:
        lines = [line.strip('\n') for line in lines]
    return lines

import json

def get_info(file=None, keys=None, json_keys=[], drop_func=None, lines=None):
    """
    从第一列为nid的file中获取字典nid2info。需要传入keys，其实就是col_names。json_keys表示哪些列是json，需要json.loads。
    下面给出了使用示例.  会自动去重
    """
    if lines is None:
        lines = get_lines(file, do_strip=True, drop_func=drop_func)
    nid2info = defaultdict(lambda: defaultdict())
    assert keys[0] == 'nid'
    keys = keys[1:]
    for line in tqdm(lines, desc='parsing info from lines'):
        items = line.split('\t')
        nid = items[0]
        if nid in nid2info:
            continue
        for key, item in zip(keys, items[1:]):
            if key in json_keys:
                item = json.loads(item)
            nid2info[nid][key] = item
    return nid2info

# file_path = 'interests/data/s_100'
# nid2info = get_info(file_path, keys=['nid', 'title', 'url', 'cat', 'sub_cat', 'knowledge', 'num', 'text'], json_keys={'knowledge'})     
    
def get_cnt_of_line(file, col_idx):
    lines = get_lines(file, do_strip=True)
    return Counter([line.split('\t')[col_idx] for line in lines])


def sample_lines(file, col_idx, keys, size):
    """从总特征文件中，第col_idx列表示垂类，我们采样keys中的垂类，且每垂类采样size个。"""
    lines = get_lines(file, do_strip=True)
    key2rest = {key: size for key in keys}
    final_lines = []
    lines = random.sample(lines, len(lines))
    for line in lines:
        items = line.split('\t')
        term = items[col_idx]
        if term not in key2rest:
            continue
        if 0 < key2rest[term]:
            final_lines.append(line)
            key2rest[term] -= 1
    # test
    print(Counter([line.split('\t')[col_idx] for line in final_lines]))
    # re-organize
    final_lines = sorted(final_lines, 
                         key=lambda line: list(keys).index(line.split('\t')[col_idx])
                         )
    
    return final_lines
        
# 再写一些基础的正则

# def min_output(file, item_pattern, n_query):
#     with open(file, "r") as f:
#         big_str = f.read()
#     pattern = r": ############\n(.*?)\n############ Done ############"
#     matches = re.findall(pattern, big_str, re.DOTALL)
#     print(f'n_query: {n_query}, n_ans_matches: {len(matches)}, deterioration_rates: {len(matches) / n_query: 0.4f}')
    
#     for m in matches:
#         for line in m.split('\n'):
#             res_lst = line.split('\n')
#             title_lst = []
#             for line in res_lst:
#                 if re.search('^[0-9]+(.|、)\s*', line) is not None:
#                     if len(line) >= 10:
#                         new_title = re.sub('^[0-9]+(.|、)\s*', '', line)
#                         title_lst.append(new_title)


# get_uniq_nid_list('./data/20240229/', output_file='./data/20240229/nid', n_output=None)
def get_uniq_nid_list(file_dir, output_file=None, n_output=None):
    """从包含wenan_raw_hourly数据的文件夹file_dir中 抽取独自的nid，并输出到output_file，支持输出为分隔的多个文件。"""
    files = os.listdir(file_dir)
    files = [file for file in files if file.endswith('.merge.wenan')]
    print('mining unique nid from file_list: ', files)
    files = [file_dir.rstrip('/') + '/' + file for file in files]
    nid_set = set()
    x, idx = files[0], 0 # for show progress
    for x in tqdm(files, desc=f'get_uniq_nid'):
        lines = get_lines(x)
        nid_set.update([line.split('\t')[0] for line in lines])
    print('n_nid:', len(nid_set))
    nid_list = list(nid_set)
    # 1. 无需输出
    if output_file is None:
        return nid_list
    # 2. 输出到一个文件
    if n_output is None:
        with open(output_file, 'w') as f:
            f.write('\n'.join(nid_list))
        return
    # 3. 分隔nid，输出到多个文件「使用于nid太多
    each_size = len(nid_list) // n_output
    several_nid_list = [nid_list[i:i + each_size] for i in range(0, len(nid_list), each_size)]  # 右边更大不会越界
    for idx, each_nid_list in tqdm(enumerate(several_nid_list), desc=f'writing {output_file}_part_{{idx}}'): # 动态就自己多两行set条
        cur_output_file = output_file + f'_part_{idx}'
        with open(cur_output_file, 'w') as f:
            f.write('\n'.join(each_nid_list))
            
# get_uniq_nid_list('./data/20240229/', output_file='./data/20240229/nid_file/nid', n_output=6)
        
    
def show_cnt(cnt, port=0.9, clear=None):
    
    remove_count = math.ceil(len(cnt) * (1-port))

    # 按计数值对计数器进行排序
    sorted_counter = sorted(cnt.items(), key=lambda x: x[0], reverse=True)

    # 去除偏大值
    filtered_counter = dict(sorted_counter[remove_count:])
    
    cnt = filtered_counter
    print(filtered_counter[1])
    for k, v in cnt.items():
        cnt[k] = cnt[k]
    plt.bar(cnt.keys(), cnt.values())
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of How many nid share current entity, proportion={port}')
    
    for key, value in cnt.items():
        plt.text(key, value, str(value), ha='center', va='bottom', fontsize=8)
    plt.show()
    
    
def convert_to_percentage_counter(counter):
    total_count = sum(counter.values())
    percentage_counter = Counter()

    for key, value in counter.items():
        percentage = value / total_count
        percentage = round(percentage, 3)
        percentage_counter[key] = percentage

    return percentage_counter


def list_to_file(res_list, file_path):
    print(f'write to {file_path}')
    print('n_lines: ', len(res_list))
    print(f'first 2 lines: {res_list[:2]}')
    with open(file_path, 'w') as f:
        f.write('\n'.join(res_list))
    return

import util

def cal_simi(ori_title, gen_title):
    dup_lcs_score = util.cal_lcs(ori_title, gen_title)
    dup_word_score = util.cal_dup_words(ori_title, gen_title)
    return dup_lcs_score, dup_word_score

def select_gen_title(ori_title, gen_title_lst):
    # 相似分数 2 列表
    dup_score_dic = defaultdict(list)
    dup_lcs_dic = defaultdict(list)
    for title in gen_title_lst:
        dup_lcs_score, dup_word_score = cal_simi(ori_title, title)
        dup_score_dic[dup_word_score].append(title)
        dup_lcs_dic[dup_lcs_score].append(title)

    sort_dup_score_lst = sorted(dup_score_dic.items(), key=lambda x:x[0], reverse=True) 
    sort_dup_lc_lst = sorted(dup_lcs_dic.items(), key=lambda x:x[0], reverse=True)

    # sort_dup_score_lst中的 最高分对应的标题列表。如果只有一个，就extent sort_dup_lc_lst最高分对应的标题列表
    cand_title_lst = sort_dup_score_lst[0][1] 
    if len(cand_title_lst) < 2:
        for t in sort_dup_lc_lst[0][1]:
            if t not in cand_title_lst:
                cand_title_lst.append(t)

    select_title = random.sample(cand_title_lst, 1)[0]
    return select_title