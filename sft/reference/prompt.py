from typing import List, Tuple
import json

def fill_template_with_param(q_template: str, a_template: str, content_dict: dict, example_set=None):
    return q_template.format(**content_dict), a_template.format(**content_dict)

def generate_qa_list(q_templatem, a_template, content_dict_list) -> List[Tuple[str, str]]:
    qa_list = [fill_template_with_param(q_templatem, a_template, content_dict) for content_dict in content_dict_list]
    return qa_list

def show_sft_json(test_file, log_to_where):
    with open(test_file, 'r') as f:
        samples = json.load(f)

    f = open(log_to_where, 'w')
    samples = samples[:30]
    for i, sample in enumerate(samples):
        print(f'+++++[{i}]+++++++++[{i}]+++++++[{i}]+++++++++', file=f)
        print('human:', file=f)
        print(sample['conversations'][0]['value'], file=f)
        print('gpt:', file=f)
        print(sample['conversations'][1]['value'], file=f)
        print('++++++++++++++++++++++++++++++', file=f)
    return 

def qa_2_sft_baichuan(qa_list: List[Tuple[str, str]], output_file):
    json_list = []
    print('generating json')
    for i, (q, a) in enumerate(qa_list):
        cur_data = {"id": i, "conversations": [{"from": "human", "value": q},
                                              {"from": "gpt", "value": a}]}
        json_list.append(cur_data)
    print(f'writing json to {output_file}')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(json_list, ensure_ascii=False))
    return


class prompt_template:
    
    template_v1 = '''
    你是一个热爱三体的读者，现在你的朋友想知道三体中的一些问题，你可以用你的知识帮助他。
{question}
与这个问题相关的知识：
{knowledge}

请回答问题
'''

    template_v1_ans = "答案: {ans1}"