---
title: LangChain-实战-Tools使用教程
description: ""
date: 2025-05-16T17:09:58+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---





# LangChain 函数调用教程：赋予LLM与外部世界交互的能力

大型语言模型（LLM）本身不具备直接与外部API、数据库或执行特定代码逻辑的能力。函数调用（Function Calling）是LangChain等框架提供的一种强大机制，它允许LLM根据用户指令，请求调用外部定义的函数（我们称之为“工具”），并将函数的执行结果反馈给LLM，从而让LLM能够完成更复杂、更贴近实际应用的任务。

本教程将详细介绍如何使用LangChain结合OpenAI兼容的API（如此处示例中的阿里云DashScope通义千问模型）来实现函数调用。我们将从基础概念讲起，逐步深入到使用Agent（代理）自动处理多步骤任务，以及手动处理函数调用的细节。


[langchain-实战-tools使用教程-源码](main.py)



## 目录

1.  [核心概念](#1-核心概念)
    * 什么是函数调用？
    * 什么是工具（Tool）？
    * 什么是代理（Agent）？
2.  [环境准备与模型初始化](#2-环境准备与模型初始化)
    * 安装必要的库
    * 设置API密钥
    * 初始化LLM模型
3.  [定义工具（Tools）](#3-定义工具tools)
    * 使用 `@tool` 装饰器
    * 类型提示（Type Hinting）与文档字符串（Docstrings）的重要性
4.  [使用Agent进行函数调用](#4-使用agent进行函数调用)
    * 创建提示模板（Prompt Template）
    * 创建并运行Agent
5.  [简单的函数调用（不使用Agent）](#5-简单的函数调用不使用agent)
    * 将工具转换为OpenAI函数格式
    * 模型如何指示函数调用
6.  [手动处理函数调用](#6-手动处理函数调用)
    * 解析模型的函数调用请求
    * 执行函数并返回结果
    * 获取最终回复
7.  [总结](#7-总结)

## 1. 核心概念

### 什么是函数调用？

函数调用允许LLM在回应用户时，不仅仅生成文本，还可以输出一个JSON对象，其中包含它认为应该被调用的特定函数的名称和参数。开发者可以捕获这个JSON对象，执行相应的本地/远程函数，然后将函数的执行结果返回给LLM，LLM再基于这个结果生成最终的用户回复。

### 什么是工具（Tool）？

在LangChain中，“工具”是指LLM可以调用的任何函数或功能。这些工具可以是：
* **API调用**：获取天气、股票价格、搜索信息等。
* **数据库查询**：从数据库中检索或修改数据。
* **代码执行**：运行Python脚本或任何其他代码。
* **自定义逻辑**：任何你希望LLM能够触发的特定业务逻辑。

### 什么是代理（Agent）？

代理（Agent）是LangChain中的一个核心概念。它使用LLM来决定采取哪些行动（即调用哪些工具）。与直接的函数调用不同，Agent可以进行多步骤的思考和工具调用，直到完成用户指定的复杂任务。Agent通常包含以下组件：
* **LLM**：决策核心。
* **工具（Tools）**：Agent可以使用的函数。
* **提示模板（Prompt Template）**：指导Agent如何思考和行动。
* **解析器（Output Parser）**：解析LLM的输出，判断是调用工具还是直接回复。
* **记忆（Memory，可选）**：保存对话历史或Agent的思考过程。

## 2. 环境准备与模型初始化

### 安装必要的库

首先，确保你安装了所需的Python库。

```python
# 你可能需要运行以下命令来安装（如果尚未安装）
# pip install langchain langchain-openai pydantic typing_extensions
````

### 设置API密钥

为了与LLM服务（如阿里云DashScope）通信，你需要设置相应的API密钥。通常建议通过环境变量来管理密钥。

```python
import os

# 确保你的环境变量 DASHSCOPE_API_KEY 已经设置
# 例如: os.environ["DASHSCOPE_API_KEY"] = "your_actual_api_key"
```

### 初始化LLM模型

我们使用 `ChatOpenAI` 类来与兼容OpenAI API的服务进行交互。这里我们以阿里云DashScope的 `qwen-plus` 模型为例。

```python
from langchain_openai import ChatOpenAI

# 设置阿里云DashScope模型
model = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="[https://dashscope.aliyuncs.com/compatible-mode/v1](https://dashscope.aliyuncs.com/compatible-mode/v1)",
    model="qwen-plus",  # 可按需更换模型，例如 qwen-turbo, qwen-max 等
)
```

## 3\. 定义工具（Tools）

工具是LLM可以调用的函数。LangChain提供了 `@tool` 装饰器，可以方便地将Python函数转换为LLM可理解和使用的工具。

### 使用 `@tool` 装饰器

当使用 `@tool` 装饰器时，函数的文档字符串（docstring）和类型提示（type hints）非常重要。LLM会依赖这些信息来理解工具的功能、所需的参数以及参数的类型。

  * **文档字符串 (Docstring)**：第一行应简洁描述工具的功能。后续可以详细描述参数。
  * **类型提示 (Type Hinting)**：为函数的参数和返回值提供类型信息。这有助于LLM正确地构造函数调用的参数。`pydantic.Field` 可以在类型提示中提供更丰富的元数据，例如参数描述。

以下是代码中定义的三个工具示例：

```python
from typing import List, Dict, Any, Optional
from langchain_core.tools import tool
# from langchain_core.pydantic_v1 import BaseModel, Field # 如果LangChain版本较旧
from pydantic import BaseModel, Field # 推荐用于新版本

@tool
def get_weather(location: str, unit: str = "celsius") -> str:
    """获取指定位置的当前天气。
    
    Args:
        location: 城市名称，例如 北京、上海
        unit: 温度单位，可选 'celsius' 或 'fahrenheit'
    
    Returns:
        当前天气预报
    """
    # 实际应用中应调用天气API
    # 例如，可以集成 requests 库调用一个真实的天气服务
    # mock_response = requests.get(f"[https://api.weather.com/some/path?city=](https://api.weather.com/some/path?city=){location}&unit={unit}")
    # return mock_response.json()["forecast"]
    return f"{location}当前天气晴朗，温度25{unit}"

@tool
def search_database(query: str) -> List[Dict[str, Any]]:
    """搜索数据库获取信息。
    
    Args:
        query: 搜索查询字符串，例如 "价格低于100元的笔记本电脑"
    
    Returns:
        匹配查询的结果列表，每个结果是一个包含字段和值的字典。
    """
    # 模拟数据库搜索
    # 实际应用中，这里会连接数据库（如SQLAlchemy, pymongo等）并执行查询
    # mock_data = {
    #     "产品A": {"id": 1, "name": "产品A", "price": 99.99, "category": "电子产品"},
    #     "产品B": {"id": 2, "name": "产品B", "price": 199.99, "category": "家居用品"}
    # }
    # results = [v for k, v in mock_data.items() if query.lower() in k.lower() or str(v["price"]) in query]
    # return results
    if "产品A" in query:
        return [{"id": 1, "name": "产品A", "price": 99.99}]
    return []

@tool
def create_user(name: str, email: str, age: Optional[int] = None) -> Dict[str, Any]:
    """在系统中创建新用户。
    
    Args:
        name: 用户全名
        email: 用户邮箱，必须是有效的邮箱格式
        age: 用户年龄（可选）
    
    Returns:
        创建的用户对象，包含用户ID、姓名和邮箱，如果提供了年龄则也包含年龄。
    """
    # 模拟用户创建逻辑
    # 实际应用中，这里会将用户信息存入数据库，并返回创建后的用户对象
    user_id = hash(email) % 10000 # 模拟生成ID
    user = {"id": user_id, "name": name, "email": email}
    if age is not None: # 检查 age 是否被提供
        if not isinstance(age, int) or age <= 0:
            return {"error": "Age must be a positive integer."} # 简单的验证
        user["age"] = age
    print(f"User created: {user}") # 模拟日志
    return user

# 将所有工具收集到一个列表中
tools = [get_weather, search_database, create_user]
```

**注意**：

  * `Optional[int] = None` 表示 `age` 参数是可选的，默认值为 `None`。
  * 文档字符串中清晰地描述了每个参数，这对于LLM理解如何使用工具至关重要。

## 4\. 使用Agent进行函数调用

Agent可以根据用户输入和可用工具，自主决定调用哪个（或哪些）工具来完成任务。

### 创建提示模板（Prompt Template）

提示模板用于指导Agent的行为。它通常包含系统消息、聊天历史、用户输入和 `agent_scratchpad`（Agent的思考过程和工具调用历史）。

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 创建代理所需的提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的AI助手。使用提供的工具来回答用户问题。请一步一步思考，并清晰地说明你打算调用哪个工具以及为什么。"),
    MessagesPlaceholder(variable_name="chat_history"), # 用于存储对话历史
    ("human", "{input}"), # 用户的当前输入
    MessagesPlaceholder(variable_name="agent_scratchpad"), # Agent的中间步骤，如工具调用和结果
])
```

`agent_scratchpad` 是一个特殊占位符，LangChain Agent会用它来填充LLM的中间思考步骤、工具调用请求以及工具的返回结果。

### 创建并运行Agent

LangChain提供了便捷的函数 `create_openai_functions_agent` 来基于支持函数调用的模型、工具和提示词创建Agent。然后使用 `AgentExecutor` 来运行这个Agent。

```python
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# 创建Agent
# 这个agent知道如何使用OpenAI的函数调用特性来决定调用哪个工具
agent = create_openai_functions_agent(llm=model, tools=tools, prompt=prompt)

# 创建Agent执行器
# AgentExecutor负责实际执行Agent的决策，调用工具，并将结果反馈给Agent
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # 设置为True可以看到Agent的详细执行过程
    handle_parsing_errors=True # 帮助处理LLM输出不符合预期格式时的错误
)

# 调用Agent执行器
# "input" 是用户的请求
# "chat_history" 是一个消息列表，用于维护对话上下文（在此例中为空）
result = agent_executor.invoke({
    "input": "帮我查询上海的天气，并创建一个名为张三的用户，邮箱为zhangsan@example.com，年龄30岁",
    "chat_history": []
})

print("Agent的最终输出:")
print(result["output"])
```

当 `verbose=True` 时，`AgentExecutor` 会打印出Agent的思考过程，包括：

  * LLM决定调用哪个工具以及使用什么参数。
  * 实际调用工具。
  * 工具返回的结果。
  * LLM基于工具结果生成的最终回复。

在这个例子中，Agent会首先调用 `get_weather` 工具获取上海的天气，然后调用 `create_user` 工具创建用户张三。最后，它会整合这两个操作的结果，给出一个综合的答复。

## 5\. 简单的函数调用（不使用Agent）

如果你不需要Agent的复杂决策逻辑，只想让LLM针对特定输入建议一个函数调用，可以直接使用模型本身。

### 将工具转换为OpenAI函数格式

LLM（如OpenAI模型或DashScope的兼容模型）期望函数以特定的JSON Schema格式进行描述。LangChain的 `convert_to_openai_function` 可以将使用 `@tool` 装饰的Python函数自动转换为这种格式。

```python
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_core.messages import HumanMessage

# 将我们定义的LangChain工具转换为OpenAI函数描述格式
functions_for_model = [convert_to_openai_function(t) for t in tools]

# 示例：询问北京天气
# 我们期望模型能识别出应该调用 get_weather 工具
message = HumanMessage(content="北京今天天气怎么样？顺便帮我查查价格低于150元的产品A的信息。")
response = model.invoke([message], functions=functions_for_model)

print("\n模型对简单函数调用的响应:")
print(response)
```

### 模型如何指示函数调用

如果模型决定需要调用一个或多个函数，它的响应（`AIMessage`）将包含一个 `additional_kwargs` 字典，其中有一个 `function_call` (或 `tool_calls` 对于支持并行调用的新模型) 字段。

  * **旧版 `function_call` (单个函数调用)**:
    ```json
    {
        "name": "function_name",
        "arguments": "{\"arg1\": \"value1\", \"arg2\": \"value2\"}"
    }
    ```
  * **新版 `tool_calls` (可能包含多个函数调用)**:
    ```json
    [
        {
            "id": "call_abc123", // 调用ID
            "type": "function",
            "function": {
                "name": "function_name_1",
                "arguments": "{\"arg1\": \"value1\"}"
            }
        },
        {
            "id": "call_xyz789",
            "type": "function",
            "function": {
                "name": "function_name_2",
                "arguments": "{\"arg_a\": \"value_a\"}"
            }
        }
    ]
    ```

在上面的代码示例中，`response.additional_kwargs` 会包含类似这样的内容（假设模型决定调用 `get_weather`）：

```
# response.additional_kwargs 示例
# {'function_call': {'name': 'get_weather', 'arguments': '{"location":"北京"}'}}
# 或者对于 tool_calls:
# {'tool_calls': [{'id': '...', 'type': 'function', 'function': {'name': 'get_weather', 'arguments': '{"location":"北京"}'}}]}
```

注意，此时模型**仅仅是建议**调用函数，它并没有实际执行。你需要自己编写代码来解析这个建议并执行函数。

## 6\. 手动处理函数调用

以下是如何手动处理LLM的函数调用请求的完整流程：

1.  **发送请求给LLM**：包含用户消息和可用函数列表。
2.  **检查LLM响应**：查看响应中是否包含 `function_call` 或 `tool_calls`。
3.  **如果需要函数调用**：
    a.  **解析参数**：从 `arguments` 字符串（通常是JSON）中提取函数参数。
    b.  **执行函数**：使用提取的参数调用你本地定义的相应Python函数。
    c.  **构建 `FunctionMessage` (或 `ToolMessage`)**：将函数的执行结果封装成特定的消息类型。
    d.  **再次调用LLM**：将原始用户消息、LLM的函数调用请求（`AIMessage`）、以及函数的执行结果（`FunctionMessage` 或 `ToolMessage`）一起发送给LLM。
4.  **获取最终回复**：LLM现在会利用函数的执行结果来生成一个更完整、更准确的回复。

<!-- end list -->

```python
import json
from langchain_core.messages import AIMessage, FunctionMessage, ToolMessage # ToolMessage 对应 tool_calls

# 创建原始函数的副本（不是@tool装饰的，因为我们将手动调用）
# 或者直接使用已定义的工具函数，因为它们本身就是普通Python函数
def get_weather_func(location: str, unit: str = "celsius") -> str:
    return f"{location}当前天气晴朗，温度25{unit}"

def search_database_func(query: str) -> List[Dict[str, Any]]:
    if "产品A" in query:
        return [{"id": 1, "name": "产品A", "price": 99.99}]
    return []

def create_user_func(name: str, email: str, age: Optional[int] = None) -> Dict[str, Any]:
    user = {"id": hash(email) % 10000, "name": name, "email": email}
    if age:
        user["age"] = age
    return user

# 映射函数名到实际的Python函数
available_functions = {
    "get_weather": get_weather_func,
    "search_database": search_database_func,
    "create_user": create_user_func,
}

# 步骤 1: 初始消息列表
messages = [
    HumanMessage(content="创建一个名为李四的用户，邮箱为lisi@example.com，年龄28岁。然后告诉我北京的天气。"),
]

print("\n--- 手动处理函数调用 ---")

# 步骤 2: 第一次调用LLM，并提供函数定义
# 使用之前转换好的 functions_for_model
first_response = model.invoke(messages, functions=functions_for_model)
messages.append(first_response) # 将AI的回复（可能包含函数调用请求）添加到消息历史

print(f"LLM初次响应 (AIMessage): {first_response}")

# 步骤 3: 检查并处理函数调用 (或工具调用)
# 新的模型倾向于使用 tool_calls，它可以包含多个并行调用
if first_response.tool_calls:
    print(f"LLM请求调用工具: {first_response.tool_calls}")
    for tool_call in first_response.tool_calls:
        function_name = tool_call["name"]
        function_args_str = tool_call["args"] # 注意这里是 args 而不是 arguments
        function_args = json.loads(function_args_str)
        
        if function_name in available_functions:
            function_to_call = available_functions[function_name]
            try:
                # 3b: 执行函数
                function_response_content = function_to_call(**function_args)
            except Exception as e:
                # 处理函数执行中的错误
                function_response_content = f"Error executing function {function_name}: {e}"

            # 3c: 构建 ToolMessage
            messages.append(ToolMessage(
                tool_call_id=tool_call["id"], # 必须提供原始调用的ID
                content=str(function_response_content),
                name=function_name
            ))
            print(f"已调用函数 '{function_name}'，参数: {function_args}, 返回: {function_response_content}")
        else:
            print(f"错误: 未知的函数名 {function_name}")
            messages.append(ToolMessage(
                tool_call_id=tool_call["id"],
                content=f"Error: Unknown function {function_name}",
                name=function_name
            ))
elif first_response.additional_kwargs.get("function_call"): # 兼容旧版 function_call
    print(f"LLM请求调用函数 (旧版): {first_response.additional_kwargs['function_call']}")
    function_call_data = first_response.additional_kwargs["function_call"]
    function_name = function_call_data["name"]
    function_args_str = function_call_data["arguments"]
    function_args = json.loads(function_args_str)

    if function_name in available_functions:
        function_to_call = available_functions[function_name]
        try:
            function_response_content = function_to_call(**function_args)
        except Exception as e:
            function_response_content = f"Error executing function {function_name}: {e}"
        
        # 旧版 function_call 使用 FunctionMessage
        # 注意：AIMessage 自身已经包含了 function_call 的请求，所以我们只需要追加 FunctionMessage
        # messages.append(AIMessage(content="", additional_kwargs={"function_call": function_call_data})) # 这一行在最新LangChain中通常由模型返回的AIMessage自身承担
        messages.append(FunctionMessage(content=str(function_response_content), name=function_name))
        print(f"已调用函数 '{function_name}'，参数: {function_args}, 返回: {function_response_content}")
    else:
        print(f"错误: 未知的函数名 {function_name}")
        messages.append(FunctionMessage(content=f"Error: Unknown function {function_name}", name=function_name))


# 步骤 4: 将包含函数执行结果的消息列表再次发送给LLM
if first_response.tool_calls or first_response.additional_kwargs.get("function_call"):
    print("\n向LLM发送包含工具/函数结果的更新消息...")
    final_response = model.invoke(messages) # functions 参数不需要再次传递，因为我们现在期望的是文本回复
    print("\nLLM最终回复:")
    print(final_response.content)
else:
    # 如果第一次调用LLM就没有要求函数调用，那么它的回复就是最终回复
    print("\nLLM没有请求函数调用，直接回复:")
    print(first_response.content)

```

在这个手动处理流程中：

1.  我们首先向LLM发送用户请求和可用的函数描述。
2.  LLM的回复 (`first_response`) 可能包含一个或多个 `tool_calls` (或一个 `function_call`)。
3.  我们遍历这些调用请求，查找对应的Python函数并执行它们。
4.  每个函数的执行结果都通过 `ToolMessage` (或 `FunctionMessage`) 添加回消息列表。`ToolMessage` 需要 `tool_call_id` 来关联原始的调用请求。
5.  最后，我们将更新后的消息列表（包含原始请求、LLM的工具调用指令、以及所有工具的执行结果）再次发送给LLM，以获得综合了这些信息的最终文本回复。

这种方式让你对函数调用的每一步都有完全的控制。

## 7\. 总结

函数调用是扩展LLM能力的关键技术。通过本教程，你应该理解了：

  * 如何使用 `@tool` 装饰器和类型提示来定义LLM可以使用的工具。
  * 如何使用LangChain Agent来自动化工具的选择和执行流程，以完成复杂任务。
  * 如何直接与LLM交互，让其建议函数调用，并手动执行这些函数，将结果反馈给LLM以获得最终答案。

无论是构建复杂的AI代理还是简单的任务增强，函数调用都为你提供了一种强大的方式，将LLM的智能与现实世界的应用程序和数据连接起来。通过清晰地定义工具的功能和参数，你可以有效地引导LLM利用这些工具来解决用户的问题。

```