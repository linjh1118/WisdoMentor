from utils import *
from prompt import *

# 0. load train data
all_lines = get_lines('train_data', file_prefix='gen_jiamijiami_asf2_res')
print(len(all_lines))
nid2info= get_info(keys=['nid', 'ori_jiamijiami', 'url', 'cat', 'sub_cat', 'sid', 'mv_or_news', 'jiamijiami_no_select', 'gen_jiamijiami_lst'], 
                   lines=all_lines)


# 1. chooce the best jiamijiami
for nid in nid2info:
    nid2info[nid]['gen_jiamijiami_lst'] = eval(nid2info[nid]['gen_jiamijiami_lst'])
    ori_jiamijiami, gen_jiamijiami_lst = nid2info[nid]['ori_jiamijiami'], nid2info[nid]['gen_jiamijiami_lst']
    nid2info[nid]['final_jiamijiami'] = select_gen_jiamijiami(ori_jiamijiami, gen_jiamijiami_lst)
print(len(nid2info))

# 2. concat content
lines = get_lines('......')
for l in tqdm(lines):
    items = l.strip().split('\t')
    nid, content = items[0], items[-1]
    if nid not in nid2info:
        continue
    nid2info[nid]['content'] = content

nid2info = {k:v for k, v in nid2info.items() if 'content' in v}
print(len(nid2info))
    


## 3. setting
content_dict_list = list(nid2info.values())
q_template, a_template = prompt_template.template_v1, prompt_template.template_v1_ans

## 4. get train data
qa_list = generate_qa_list(q_template, a_template, content_dict_list)
qa_2_sft_baichuan(qa_list, 'datadatadata_jiami')
show_sft_json('datadatadata_jiami', 'datadatadata_jiami_log')



