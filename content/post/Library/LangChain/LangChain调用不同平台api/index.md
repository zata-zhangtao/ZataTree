---
title: LangChain调用不同平台api
description: ""
date: 2025-03-11T17:15:16+08:00
# image: images/index/index.png
categories:
    - Library
tags:
    - LangChain
---


## 调用阿里云api




### 🦐聊天模型

依赖
```bash
pip install langchain_openai
```

使用示例
```python
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
load_dotenv()

chatLLM = ChatOpenAI(
    api_key=os.getenv("api_key"),
    base_url=os.getenv("base_url"),
    model="qwen-plus",  # 此处以qwen-plus为例，您可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    # other params...
)


###################调用方法一########################
result = chatLLM.stream("2025年的技术趋势是什么？")
for chunk in result:
    print(chunk.content, end='', flush=True)
###################################################


###################调用方法二##########################
# 定义提示模板
prompt = PromptTemplate(
    input_variables=["question"],
    template="请简洁回答以下问题：{question}"
)

# 创建链
chain = LLMChain(llm=chatLLM, prompt=prompt)

# 运行链
question = "2025年的技术趋势是什么？"
response = chain.run(question)
print(response)
######################################################


###################调用方法三########################
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"}]
response = chatLLM.invoke(messages)
print(response.json())
###################################################
```

### 文本嵌入模型

依赖

```bash
pip install langchain-community
pip install dashscope
pip install faiss-cpu
```

```python
from langchain_community.embeddings import DashScopeEmbeddings
embeddings = DashScopeEmbeddings(
    model="text-embedding-v2",
    # other params...
)

text = "This is a test document."

query_result = embeddings.embed_query(text)
print("文本向量长度：", len(query_result), sep='')

doc_results = embeddings.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ])
print("文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep='')
```








