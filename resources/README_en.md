# WisdoMentor
<p align="center"> <img src="resources/title_logo.svg" style="width: 40%;" id="title-icon">  </p>
<!-- <p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center"> -->
<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
<a href="" target="_blank" style="margin-left: 6px">🤗</a> <a href="" target="_blank" style="margin-left: 6px">HuggingFace</a>  • | 
<a href="" target="_blank" style="margin-left: 10px">🤖</a> <a href="" target="_blank" style="margin-left: 6px">ModelScope</a>  • |
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

# 模型介绍

- WidsoMentor吉梦智创推出的**零基础AI辅助教育大模型**，采用**250万**篇Arxiv高质量人工智能论文训练。
- 采用**Bonito Instruct**、**Self Instruct**、**Involve Instruct**等多种指令生成方法，通过门控技术实现多方法的有机融合。
- 嵌入**RAG**技术，保证WisdoMentor回答的准确性和时效性。
- 接入**Agent**方法，在回答中嵌入可以被参阅的高质量回答网页，提供回答之外更多的知识细节。

# Model Introduction
- WidsoMentor, developed by JiMengZhiChuang, is a zero-based AI-assisted education mega-model trained on 2.5 million high-quality research papers from Arxiv in the field of artificial intelligence.
- It incorporates various instruction generation methods such as Bonito Instruct, Self Instruct, and Involve Instruct, achieving an organic fusion of multiple approaches through gating techniques.
- It embeds RAG (Retrieval-Augmented Generation) technology to ensure the accuracy and timeliness of WidsoMentor's responses.
- It adopts the Agent approach to integrate high-quality answer webpages that can be referenced within the answers, providing additional knowledge details beyond the responses.

# Benchmark 结果

我们在[通用](#通用领域)、[数学](#数学)等多个领域的权威数据集上对模型进行了测试

## 通用领域

我们对WisdoMentor分别在通用领域数据集C-Eval、MMLU、CMMLU等三个权威数据集上进行测试，分别涵盖了全面的中文基础模型评测、英文基础模型评测和中文语境下的理解和推理能力。

### 7B 模型结果

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

## 数学
## 代码

----

# 推理和部署

接下来我们展示使用 [FastChat](https://github.com/lm-sys/FastChat)，[Transformers](#import-from-transformers)，[ModelScope](#import-from-modelscope) 和 [Web demo](#dialogue) 进行推理。
对话模型采用了 [chatml 格式](./chat/chat_format.md) 来支持通用对话和智能体应用。
为了保障更好的使用效果，在用 [Transformers](#import-from-transformers) 或 [ModelScope](#import-from-modelscope) 进行推理前，请按如下指令安装依赖。

### 安装依赖

```shell
git clone https://www.modelscope.cn/linjh1118/WisdoMentor-8b
conda create --name WisdoMentor python=3.11.8
conda activate WisdoMentor
pip install -r requirements.txt
```

### 通过 FastChat 部署推理
```python
git clone https://www.modelscope.cn/linjh1118/WisdoMentor-8b path_to_local_WisdoMentor-8b
cd path_to_local_WisdoMentor-8b
python -m fastchat.serve.cli --model-path path_to_local_WisdoMentor-8b
问: 介绍下bert和gpt有什么区别
答: Bert (Bidirectional Encoder Representations from Transformers) 和 GPT (Generative Pre-trained Transformers)都是预训练的自然语言处理模型，但它们的预训练任务和应用场景有所不同。 Bert通过双向的编码器结构预训练，能够捕捉到句子的上下文信息，具有非常好的语言理解和语义表示能力。Bert预训练的任务是通过将句子的两部分分别用双语标记，然后预测这两个部分之间的关系来完成的。Bert在自然语言处理任务中表现出色，如文本分类、情感分析、命名实体识别、文本匹配、问答系统和文本摘要等。 GPT是基于单向的编码器结构，与BERT不同。GPT预训练的任务是通过将文本中的单词和句子分别标识，然后预测下一个单词来完成的。GPT在自然语言处理任务中也表现出色，如文本生成、对话系统、机器翻译、问答系统等。 虽然Bert和GPT预训练的任务不同，但它们都是预训练的自然语言处理模型，在处理特定任务时可以进行微调，从而实现更好的性能。选择使用BERT还是GPT取决于具体任务的需求和目标。
```

### 通过 ModelScope 加载

通过以下的代码从 ModelScope 加载 WisdoMentor-8b 模型 （可根据本地算力条件，修改模型名称，替换成不同尺寸的WisdoMentor）

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

### 通过 Transformers 加载

通过以下的代码从 Transformers 加载 WisdoMentor-8b 模型 （可根据本地算力条件，修改模型名称，替换成不同尺寸的WisdoMentor）

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("linjh1118/WisdoMentor-8b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("linjh1118/WisdoMentor-8b", device_map="auto",trust_remote_code=True, torch_dtype=torch.float16)
# 4-bit 量化
# pip install -U bitsandbytes
# 8-bit: model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", trust_remote_code=True, load_in_8bit=True)
# 4-bit: model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="auto", trust_remote_code=True, load_in_4bit=True)
model = model.eval()
response, history = model.chat(tokenizer, "请介绍下Bert和GPT的区别", history=[])
print(response)
response, history = model.chat(tokenizer, "请介绍下Self-Attention机制", history=history)
print(response)
```


# 声明、协议

## 声明

我们在此声明，我们的开发团队并未基于 WidsoMentor 模型开发任何应用，无论是在 iOS、Android、网页或任何其他平台。我们强烈呼吁所有使用者，不要利用 WidsoMentor 模型进行任何危害国家社会安全或违法的活动。另外，我们也要求使用者不要将 WidsoMentor 模型用于未经适当安全审查和备案的互联网服务。我们希望所有的使用者都能遵守这个原则，确保科技的发展能在规范和合法的环境下进行。

## 协议
社区使用 WidsoMentor 模型需要遵循 [Apache 2.0](https://github.com/baichuan-inc/Baichuan2/blob/main/LICENSE)。WidsoMentor 模型支持商业用途，如果您计划将 WidsoMentor 模型或其衍生品用于商业目的，请您确认您的主体符合以下情况：
  1. 您或您的关联方的服务或产品的日均用户活跃量（DAU）低于100万。
  2. 您或您的关联方不是软件服务提供商、云服务提供商。
  3. 您或您的关联方不存在将授予您的商用许可，未经百川许可二次授权给其他第三方的可能。


