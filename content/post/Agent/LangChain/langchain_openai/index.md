---
title: langchain_openai
description: ""
date: 2025-12-28T14:09:07+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---

`langchain_openai` 是 LangChain 生态中最重要的合作伙伴包之一。随着大模型接口逐渐标准化，**“OpenAI API 格式”已经成为了事实上的工业标准**。

这意味着，虽然这个包名字叫 `openai`，但它实际上可以连接**任何**兼容 OpenAI 接口协议的模型服务。**阿里百炼（Aliyun Bailian/DashScope）正是完美支持这一协议的典范。**

下面我将分层为你详细讲解 `langchain_openai` 的核心组件，并提供一份基于阿里百炼的实战教程。

---

### 一、 `langchain_openai` 的核心模型组件

在 `langchain_openai` 包中，主要涉及以下两个核心类（Core Classes），它们对应了LLM应用开发的两大基石：

#### 1. `ChatOpenAI` (核心对话模型)

这是目前最常用的类，用于通过“聊天”接口（Chat Completion API）与模型交互。

* **用途：** 处理对话、指令跟随、逻辑推理、工具调用（Function Calling）。
* **对应阿里模型：** 通义千问系列（`qwen-plus`, `qwen-max`, `qwen-turbo`, `qwen-long` 等）。
* **特点：** 输入是消息列表（SystemMessage, HumanMessage, AIMessage），输出是 AIMessage。

#### 2. `OpenAIEmbeddings` (核心向量模型)

用于将文本转化为向量（Vector），是构建 RAG（检索增强生成）系统的基础。

* **用途：** 文本语义搜索、知识库构建。
* **对应阿里模型：** 通义千问向量模型（`text-embedding-v1`, `text-embedding-v2` 等）。

---

### 二、 阿里百炼接入教程 (基于 `langchain_openai`)

要使用 `langchain_openai` 调用阿里百炼，关键在于**“换头”**——即替换 `base_url` 和 `api_key`，其他代码逻辑与调用 GPT-4 完全一致。

#### 1. 环境准备

首先安装必要的包：

```bash
pip install langchain-openai langchain-core

```

你需要去 [阿里云百炼控制台](https://bailian.console.aliyun.com/) 获取：

1. **API Key**: (`sk-xxx`)
2. **Base URL**: 阿里百炼的 OpenAI 兼容端点为 `https://dashscope.aliyuncs.com/compatible-mode/v1`

#### 2. 实战代码：基础对话 (Chat)

这是最基础的用法，使用 `ChatOpenAI` 连接 Qwen 模型。

```python
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 配置阿里百炼的连接信息
# 建议将 API Key 放入环境变量，或者直接在代码中指定（不推荐生产环境）
ALIBABA_API_KEY = "sk-你的阿里百炼API_KEY"
ALIBABA_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"

# 初始化 ChatOpenAI
# 关键点：将 model 指向阿里的模型 ID (如 qwen-plus, qwen-max)
chat_model = ChatOpenAI(
    model="qwen-plus",  # 指定通义千问模型
    api_key=ALIBABA_API_KEY,
    base_url=ALIBABA_BASE_URL,
    temperature=0.7,
    streaming=True      # 支持流式输出
)

# 构建消息
messages = [
    SystemMessage(content="你是一个专业的Python代码助手。"),
    HumanMessage(content="请用Python写一个冒泡排序，并解释其时间复杂度。")
]

# 调用模型
response = chat_model.invoke(messages)

print(response.content)

```

#### 3. 实战代码：流式输出 (Streaming)

在大模型应用中，流式输出能显著提升用户体验。`ChatOpenAI` 原生支持此功能。

```python
# ...初始化代码同上...

print("正在生成回答：")
# 使用 .stream() 方法
for chunk in chat_model.stream(messages):
    # chunk.content 是每次生成的一小段文本
    print(chunk.content, end="", flush=True)

```

#### 4. 实战代码：向量嵌入 (Embeddings)

如果你要做 RAG（知识库助手），需要使用 `OpenAIEmbeddings` 调用阿里的 Embedding 模型。

```python
from langchain_openai import OpenAIEmbeddings

# 初始化 Embedding 模型
embeddings = OpenAIEmbeddings(
    model="text-embedding-v2", # 阿里的向量模型 ID
    api_key=ALIBABA_API_KEY,
    base_url=ALIBABA_BASE_URL,
    check_embedding_ctx_length=False # 关闭OpenAI特有的长度检查，防止报错
)

# 测试向量化
text = "阿里百炼是一个大模型服务平台。"
vector = embeddings.embed_query(text)

print(f"生成的向量维度: {len(vector)}")
print(f"向量前5位: {vector[:5]}")

```

#### 5. 高级功能：工具调用 (Tool Calling / Function Calling)

阿里百炼的 Qwen 模型对 Function Calling 的支持非常好，且完全兼容 OpenAI 的格式。

```python
from langchain_core.tools import tool

# 1. 定义一个工具
@tool
def get_weather(city: str):
    """查询某个城市的天气信息。"""
    return f"{city} 的天气是晴天，气温 25度。"

# 2. 将工具绑定到模型 (bind_tools)
llm_with_tools = chat_model.bind_tools([get_weather])

# 3. 提问触发工具
query = "杭州今天天气怎么样？"
response = llm_with_tools.invoke(query)

# 4. 打印结果
# 模型会返回一个 tool_calls 属性，而不是直接的文本
print(f"工具调用请求: {response.tool_calls}")

```

---

### 三、 为什么推荐在阿里百炼上使用 `langchain_openai`？

你可能会问：“为什么不用阿里官方的 SDK 或者 LangChain 里的 `Tongyi` 类？”

使用 `langchain_openai` 接入阿里百炼有以下 **3大核心优势**：

1. **代码零迁移成本 (Portability)**：
* 如果你的项目原本是基于 GPT-4 开发的，你**不需要改动任何业务逻辑代码**。只需要修改环境变量里的 `BASE_URL` 和 `API_KEY`，你的应用就能瞬间从 OpenAI 切换到 阿里 Qwen。这对于作为“平替”方案非常关键。


2. **生态支持最完善**：
* LangChain 社区对 `OpenAI` 类的支持是优先级的。使用标准接口，你能更容易地集成 LangGraph、LangSmith 等高级工具。


3. **统一的工具调用格式**：
* OpenAI 的 Tool Calling 格式是目前的黄金标准。阿里百炼通过兼容接口，使得 Qwen 模型可以像 GPT 一样精准地调用工具，而不需要你处理复杂的格式转换。



### 总结

* **包名**：`langchain_openai`
* **核心类**：`ChatOpenAI` (对话), `OpenAIEmbeddings` (向量)。
* **阿里百炼配置**：
* `base_url`: `https://dashscope.aliyuncs.com/compatible-mode/v1`
* `model`: `qwen-plus` / `qwen-max`



**下一步建议：**
如果你已经跑通了上面的基础代码，你是否需要了解**如何利用这些组件搭建一个基于本地知识库的问答系统（RAG）**？我可以给你提供一个结合 Qwen 和 向量检索的完整示例。