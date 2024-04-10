# WisdoMentor-3B
WisdoMentor-3B: A LLM for undergraduates |  博导智言(辅助大学生 学习)
<p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
🤗 <a href="" target="_blank" style="margin-left: 10px">HuggingFace</a>  • 
🤖 <a href="" target="_blank" style="margin-left: 10px">ModelScope</a>  • 
💬 <a href="https://github.com/linjh1118/WisdoMentor-3B" target="_blank"  style="margin-left: 10px">WeChat</a>   
</p>

# 目录

- [📚 模型介绍](#模型介绍)
- [📊 Benchmark 结果🏆🏆🏆](#Benchmark-结果)
- [🌏 推理和部署](#推理和部署)
- [📕 声明、协议](#声明协议)

# 新闻

[11/4/2024] 🔥🔥🔥**我们发布了第一版WidsoMenter-7B模型**

# 模型介绍

- WidsoMentor吉梦智创推出的**零基础AI辅助教育大模型**，采用**250万**篇Arxiv高质量人工智能论文训练

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
| **WisdoMentor-7B**       |            |          |           | 

## 数学

# 推理和部署

推理所需的模型权重、源码、配置即将发布在 Hugging Face

## 安装依赖
```shell
pip install -r requirements.txt
```

## Python 代码推理

# 声明、协议

## 声明

我们在此声明，我们的开发团队并未基于 WidsoMentor 模型开发任何应用，无论是在 iOS、Android、网页或任何其他平台。我们强烈呼吁所有使用者，不要利用 WidsoMentor 模型进行任何危害国家社会安全或违法的活动。另外，我们也要求使用者不要将 WidsoMentor 模型用于未经适当安全审查和备案的互联网服务。我们希望所有的使用者都能遵守这个原则，确保科技的发展能在规范和合法的环境下进行。

## 协议
社区使用 WidsoMentor 模型需要遵循 [Apache 2.0](https://github.com/baichuan-inc/Baichuan2/blob/main/LICENSE)。WidsoMentor 模型支持商业用途，如果您计划将 WidsoMentor 模型或其衍生品用于商业目的，请您确认您的主体符合以下情况：
  1. 您或您的关联方的服务或产品的日均用户活跃量（DAU）低于100万。
  2. 您或您的关联方不是软件服务提供商、云服务提供商。
  3. 您或您的关联方不存在将授予您的商用许可，未经百川许可二次授权给其他第三方的可能。


