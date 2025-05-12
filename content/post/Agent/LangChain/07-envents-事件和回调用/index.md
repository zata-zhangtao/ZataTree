---
title: 07-回调系统：events(事件
description: ""
date: 2025-05-10T15:59:00+08:00
image: images/index/index.png
layout: "01-event.html"
categories:
    - Agent
tags:
    - LangChain
---

# LangChain 回调系统教程


[LangChain回调系统教程.ipynb](01-event.ipynb)

[LangChain回调系统教程.html](/01-event.html)

--- 

本教程展示了如何使用 LangChain 的回调系统来监控和自定义 LLM、Chain、Agent 和 Tool 的执行过程。回调系统允许你在各种事件（如 LLM 开始、Chain 结束、Tool 执行）发生时插入自定义逻辑，用于日志记录、调试或 UI 更新。

## 前置条件
- 安装必要的库：
```bash
pip install langchain langchain-openai langchain-community pandas duckduckgo-search
pip install langsmith  # 可选，用于 LangSmith 集成
```
- 设置 API 密钥（例如，阿里云百炼平台或其他 LLM 提供商）：
```python
import os
os.environ["DASHSCOPE_API_KEY"] = "your-api-key"
```

## 1. 使用内置的 StdOutCallbackHandler
`StdOutCallbackHandler` 提供详细的调试输出，显示如 `on_llm_start` 和 `on_llm_end` 等事件。

```python
from langchain_openai import ChatOpenAI
from langchain.callbacks import StdOutCallbackHandler
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate

# 初始化 LLM
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
    temperature=0
)

# 创建 StdOutCallbackHandler
stdout_handler = StdOutCallbackHandler()

# 方法 1：在构造时传入回调
llm_with_stdout = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
    temperature=0,
    callbacks=[stdout_handler]
)
response = llm_with_stdout.invoke("你好，今天你好吗？")
print("LLM 响应：", response.content)

# 方法 2：通过 config 传入回调（推荐，特别是在 LCEL 中）
response_config = llm.invoke(
    "讲一个简短的笑话。",
    config={"callbacks": [stdout_handler]}
)
print("LLM 响应（config）：", response_config.content)

# 使用回调运行 Chain
prompt = PromptTemplate.from_template("{country}的首都是哪里？")
chain = LLMChain(llm=llm, prompt=prompt)
chain_response = chain.invoke(
    {"country": "法国"},
    config={"callbacks": [stdout_handler]}
)
print("Chain 响应：", chain_response)
```

## 2. 创建自定义回调处理器
通过继承 `BaseCallbackHandler`，可以创建自定义处理器来响应特定事件。

```python
from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.outputs import LLMResult
from uuid import UUID
from typing import Any, Dict, List, Optional, Union

class MyCustomHandler(BaseCallbackHandler):
    def __init__(self, description: str = "MyHandler"):
        self.description = description
        print(f"[{self.description}] 处理器已初始化")

    def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> Any:
        print(f"\n[{self.description}] LLM 开始：\n  提示：{prompts}")

    def on_llm_end(self, response: LLMResult, *, run_id: UUID, **kwargs: Any) -> Any:
        print(f"\n[{self.description}] LLM 结束（ID: {run_id}）：")
        for generation in response.generations[0]:
            print(f"  - 文本：{generation.message.content[:100]}...")

    def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> Any:
        print(f"\n[{self.description}] Chain 开始：\n  输入：{inputs}")

    def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        print(f"\n[{self.description}] Chain 结束：\n  输出：{outputs}")

# 实例化自定义处理器
my_handler = MyCustomHandler(description="LoggerV1")

# 使用自定义处理器运行 LLM
llm.invoke("学习 LangChain 的好处是什么？", config={"callbacks": [my_handler]})
# 使用自定义处理器运行 Chain
chain.invoke({"country": "加拿大"}, config={"callbacks": [my_handler]})
```

## 3. LangChain 表达式语言（LCEL）与回调
LCEL 是构建 Chain 的现代方式，回调通过 `config` 参数无缝集成。

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 定义 LCEL Chain
prompt_lcel = ChatPromptTemplate.from_template("告诉我关于 {topic} 的一个有趣事实。")
llm_lcel = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
    temperature=0
)
parser = StrOutputParser()
chain_lcel = prompt_lcel | llm_lcel | parser

# 使用自定义处理器运行 LCEL Chain
lcel_response = chain_lcel.invoke(
    {"topic": "月球"},
    config={"callbacks": [my_handler]}
)
print("LCEL Chain 响应：", lcel_response)

# 流式传输与 on_llm_new_token
class StreamingTokenHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        print(f"流式传输 Token：'{token}'", end="", flush=True)

streaming_token_handler = StreamingTokenHandler()
llm_streaming = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
    temperature=0,
    streaming=True
)
chain_streaming = prompt_lcel | llm_streaming | parser

full_response_streamed = ""
for chunk in chain_streaming.stream({"topic": "黑洞"}, config={"callbacks": [streaming_token_handler, my_handler]}):
    full_response_streamed += chunk
print("\nLCEL 流式传输完整响应：", full_response_streamed)
```

## 4. Agent 和 Tool 与回调
Agent 和 Tool 会触发额外的事件，如 `on_tool_start` 和 `on_agent_action`。

```python
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType, Tool

# 定义一个工具
search_tool = Tool(
    name="DuckDuckGo 搜索",
    func=DuckDuckGoSearchRun().run,
    description="适用于回答关于当前事件或常识的问题。"
)

# 初始化 Agent
agent_llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
    temperature=0
)
agent_executor = initialize_agent(
    tools=[search_tool],
    llm=agent_llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

# 使用自定义处理器运行 Agent
agent_response = agent_executor.invoke(
    {"input": "关于火星探测车的最新消息是什么？"},
    config={"callbacks": [my_handler]}
)
print("Agent 最终响应：", agent_response["output"])
```

## 5. 异步回调
对于异步操作（如 `ainvoke` 或 `astream`），使用 `AsyncCallbackHandler`。

```python
from langchain_core.callbacks.base import AsyncCallbackHandler
import asyncio

class MyAsyncCustomHandler(AsyncCallbackHandler):
    def __init__(self, description: str = "MyAsyncHandler"):
        self.description = description
        print(f"[{self.description}] 异步处理器已初始化")

    async def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
        print(f"\n[{self.description}] (异步) LLM 开始：\n  提示：{prompts}")

    async def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        print(f"\n[{self.description}] (异步) LLM 结束")

async def main():
    my_async_handler = MyAsyncCustomHandler()
    llm_for_async = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-plus",
        temperature=0
    )
    response_async = await llm_for_async.ainvoke(
        "告诉我关于异步编程的内容。",
        config={"callbacks": [my_async_handler]}
    )
    print("异步 LLM 响应：", response_async.content)

# 运行异步代码
await main()
```

## 6. 使用 aevents API
`aevents` API 提供了一种现代的方式来异步流式传输事件。

```python
async def demonstrate_aevents():
    llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-plus",
        temperature=0
    )
    prompt = ChatPromptTemplate.from_template("Python 的三个关键特性是什么？")
    chain = prompt | llm | StrOutputParser()

    event_stream = chain.aevents({"input": "Python 的三个关键特性是什么？"}, config={"tags": ["aevents_demo"]})
    async for event in event_stream:
        print(f"事件：{event['name']}（运行 ID：{event['run_id']}）")
        if event['name'] == "on_chat_model_stream":
            print(f"    块：{event['data']['chunk']}")

# 添加到 main() 并运行：await demonstrate_aevents()
```

## 7. LangSmith 集成
配置 LangSmith 后，它会自动捕获回调事件以实现可观测性：
```bash
export LANGCHAIN_API_KEY="your-langsmith-api-key"
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_PROJECT="your-project-name"
```

无需显式回调处理器即可使用 LangSmith，但可以结合自定义处理器进行本地处理。

## 总结
- 使用 `StdOutCallbackHandler` 进行快速调试。
- 创建自定义的 `BaseCallbackHandler` 或 `AsyncCallbackHandler` 实现特定逻辑。
- 通过 `config={"callbacks": [...]}` 将回调传递给 LCEL、LLM、Chain 和 Agent。
- 使用 `aevents()` 以编程方式流式传输事件。
- 利用 LangSmith 实现高级可观测性。

