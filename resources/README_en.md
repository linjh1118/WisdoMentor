# WisdoMentor
<p align="center"> <img src="title_logo.svg" style="width: 40%;" id="title-icon">  </p>
<!-- <p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center"> -->
<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
<a href="" target="_blank" style="margin-left: 6px">🤗</a> <a href="https://modelscope.cn/models/linjh1118/WidsoMenter-8B/summary" target="_blank" style="margin-left: 6px">HuggingFace</a>  • | 
<a href="" target="_blank" style="margin-left: 10px">🤖</a> <a href="https://modelscope.cn/models/linjh1118/WidsoMenter-8B/summary" target="_blank" style="margin-left: 6px">ModelScope</a>  • |
<a href="" target="_blank" style="margin-left: 10px">📃</a> <a href="https://arxiv.org" target="_blank" style="margin-left: 6px">[Wisdom-8B @ arxiv]</a>
  
</p>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
🍭 <a href="http://wisdomentor.jludreamworks.com" target="_blank"  style="margin-left: 6px">Try WisdoMentor</a> • |
<a href="" target="_blank" style="margin-left: 10px">💬</a> <a href="./resources/wechat.jpg" target="_blank"  style="margin-left: 6px">WeChat</a> 
</p>

<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
<a href="./resources/README_en.md" target="_blank"  style="margin-left: 6px">English Readme</a>  • |
<a href="./README.md" target="_blank"  style="margin-left: 6px">中文 Readme</a> 
</p>



# Table of Contents
- [📰 News Update](#News_Update)
- [📚 Model Introduction](#Model_Introduction)
- [📊 Benchmark Results🏆🏆🏆](#Benchmark_Results)
- [🌏 Inference and Deployment](#Inference_and_Deployment)
- [📕 Disclaimer and License](#Disclaimer_and_License)



# News_Update

[4/19/2024] 🔥🔥🔥**We have released the first version of WidsoMenter-8B model: Wisdom Block Extension. It includes more SFT data generated from blogs and injects some SFT data in Stage CPT.**

[4/11/2024] 🔥🔥🔥**We have released the first version of WidsoMenter-7B model.**


# Model Introduction
- WidsoMentor, developed by JiMengZhiChuang, is a zero-based AI-assisted education mega-model trained on 2.5 million high-quality research papers from Arxiv in the field of artificial intelligence.
- It incorporates various instruction generation methods such as Bonito Instruct, Self Instruct, and Involve Instruct, achieving an organic fusion of multiple approaches through gating techniques.
- It embeds RAG (Retrieval-Augmented Generation) technology to ensure the accuracy and timeliness of WidsoMentor's responses.
- It adopts the Agent approach to integrate high-quality answer webpages that can be referenced within the answers, providing additional knowledge details beyond the responses.

# Performance on Benchmark
We conducted tests on WidsoMentor using authoritative datasets in various domains, including General and Mathematics.

## General Domain
We evaluated WidsoMentor on three authoritative datasets in the general domain: C-Eval, MMLU, and CMMLU. These datasets cover comprehensive evaluations of Chinese and English base models, as well as comprehension and reasoning abilities in Chinese contexts.

### Performance of WisdoMentor-8B

|                          | **C-Eval** | **MMLU** | **CMMLU** |
|:------------------------:|:----------:|:--------:|:---------:|
|                          |  5-shot    |  5-shot  |  5-shot   |
| **GPT-4**                | 68.40      | 83.93    | 70.33     |
| **GPT-3.5 Turbo**        | 51.10      | 68.54    | 54.06     |
| **LLaMA-7B**             | 27.10      | 35.10    | 26.75     |
| **LLaMA2-7B**            | 28.90      | 45.73    | 31.38     |
| **MPT-7B**               | 27.15      | 27.93    | 26.00     |
| **Falcon-7B**            | 24.23      | 26.03    | 25.66     |
| **ChatGLM2-6B**          | 50.20      | 45.90    | 49.00     |
| **WisdoMentor-8B**       |            |          |           | 

## Math Ability
## Code Ability

----


# Inference and Deployment
Next, we will demonstrate inference using FastChat, Transformers, ModelScope, and Web demo.
The dialogue model adopts the chatml format to support general dialogue and agent applications.
To ensure better usability, please install the dependencies as instructed below before performing inference using Transformers or ModelScope.

### Install Dependencies
"""

```shell
git clone https://www.modelscope.cn/linjh1118/WisdoMentor-8b
conda create --name WisdoMentor python=3.11.8
conda activate WisdoMentor
pip install -r requirements.txt
```

### Deploying Inference with FastChat
```python
git clone https://www.modelscope.cn/linjh1118/WisdoMentor-8b path_to_local_WisdoMentor-8b
cd path_to_local_WisdoMentor-8b
python -m fastchat.serve.cli --model-path path_to_local_WisdoMentor-8b
问: 介绍下bert和gpt有什么区别
答: Bert (Bidirectional Encoder Representations from Transformers) 和 GPT (Generative Pre-trained Transformers)都是预训练的自然语言处理模型，但它们的预训练任务和应用场景有所不同。 Bert通过双向的编码器结构预训练，能够捕捉到句子的上下文信息，具有非常好的语言理解和语义表示能力。Bert预训练的任务是通过将句子的两部分分别用双语标记，然后预测这两个部分之间的关系来完成的。Bert在自然语言处理任务中表现出色，如文本分类、情感分析、命名实体识别、文本匹配、问答系统和文本摘要等。 GPT是基于单向的编码器结构，与BERT不同。GPT预训练的任务是通过将文本中的单词和句子分别标识，然后预测下一个单词来完成的。GPT在自然语言处理任务中也表现出色，如文本生成、对话系统、机器翻译、问答系统等。 虽然Bert和GPT预训练的任务不同，但它们都是预训练的自然语言处理模型，在处理特定任务时可以进行微调，从而实现更好的性能。选择使用BERT还是GPT取决于具体任务的需求和目标。
```

### Deploying Inference with ModelScope


Modify the code below to load the WisdoMentor-8b model from ModelScope, considering your local computational resources. You can replace the model name with different sizes of WisdoMentor.

```python
import torch
from modelscope import snapshot_download, AutoTokenizer, AutoModelForCausalLM
model_dir = snapshot_download('linjh1118/WisdoMentor-8b')
tokenizer = AutoTokenizer.from_pretrained(model_dir, device_map="auto", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", trust_remote_code=True, torch_dtype=torch.float16)
model = model.eval()
response, history = model.chat(tokenizer, "请介绍下Bert和GPT的区别", history=[])
print(response)
response, history = model.chat(tokenizer, "请介绍下Self-Attention机制", history=history)
print(response)
```

### Deploying Inference with Huggingface

Modify the code below to load the WisdoMentor-8b model from Huggingface, considering your local computational resources. You can replace the model name with different sizes of WisdoMentor.

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("linjh1118/WisdoMentor-8b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("linjh1118/WisdoMentor-8b", device_map="auto",trust_remote_code=True, torch_dtype=torch.float16)
# 4-bit Quantization
# pip install -U bitsandbytes
# 8-bit: model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", trust_remote_code=True, load_in_8bit=True)
# 4-bit: model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", trust_remote_code=True, load_in_4bit=True)
model = model.eval()
response, history = model.chat(tokenizer, "请介绍下Bert和GPT的区别", history=[])
print(response)
response, history = model.chat(tokenizer, "请介绍下Self-Attention机制", history=history)
print(response)
```


# Declaration and Agreement

## Declaration

We hereby declare that our development team has not developed any applications based on the WisdoMentor model, whether on iOS, Android, web, or any other platform. We strongly urge all users not to utilize the WisdoMentor model for any activities that may jeopardize national or social security or violate the law. Furthermore, we request users not to use the WisdoMentor model for internet services without proper security review and filing. We hope that all users will abide by this principle to ensure that technological advancements occur in a regulated and lawful environment.

## Agreement
The community's use of the WisdoMentor model must comply with the [Apache 2.0 License](https://github.com/baichuan-inc/Baichuan2/blob/main/LICENSE). The WisdoMentor model supports commercial use. If you plan to use the WisdoMentor model or its derivatives for commercial purposes, please ensure that your entity meets the following conditions:
  1. The daily active user count (DAU) of your service or product or its affiliates is less than one million.
  2. You or your affiliates are not software service providers or cloud service providers.
  3. You or your affiliates do not have the possibility of granting commercial licenses to you without the permission of JiMengZhiChuang and subsequently sublicensing them to other third parties.


