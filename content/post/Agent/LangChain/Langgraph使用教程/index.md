---
title: Langgraph使用教程
description: ""
date: 2025-06-04T10:36:30+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---

参考：

[langgraph官方文档](https://langchain-ai.github.io/langgraph/agents/agents/)


## 目录

- [相关api解析](#相关api解析)
  - [消息管理类MessagesState](#消息管理类messagesstate)

- [实战案例](#实战案例)
    - [构建基础聊天机器人](#使用-langgraph-构建基础聊天机器人)





## 相关api解析

### 消息管理类MessagesState

`MessagesState` 是 **LangGraph** 中的一个内置状态管理类，位于 `langgraph.graph` 模块，用于处理消息集合，常用于对话型工作流或聊天机器人等场景。以下是对 `MessagesState` 用法的详细中文介绍，包括其用途、结构和实际示例。

#### `MessagesState` 概述
`MessagesState` 是一个专为对话场景设计的状态类，用于存储和管理消息列表，例如用户输入、AI 回复或系统提示。它特别适合基于大语言模型（LLM）的应用，维护对话历史。

**主要特点**：
- **消息管理**：以列表形式存储消息，通常与 LangChain 的消息类型（如 `HumanMessage`、`AIMessage`、`SystemMessage`）兼容。
- **结构化状态**：提供清晰的状态模式，便于在 LangGraph 工作流中使用。
- **可扩展性**：可通过添加自定义字段扩展状态。
- **与 LangChain 集成**：无缝支持 LangChain 的消息类，适合 LLM 应用。

#### `MessagesState` 结构
`MessagesState` 是 LangGraph `State` 的子类，默认包含一个键 `"messages"`，存储消息列表。消息通常是 LangChain 的 `BaseMessage` 子类实例。

模式示例如下：
```python
from typing import List
from langchain_core.messages import BaseMessage

class MessagesState:
    messages: List[BaseMessage]
```
- **`messages`**：存储对话历史的列表，每个元素通常是 `HumanMessage`、`AIMessage` 或 `SystemMessage` 等。

#### 导入 `MessagesState`
使用 `MessagesState` 需要从 `langgraph.graph` 导入：
```python
from langgraph.graph import MessagesState
```

#### 在 LangGraph 中的用法
LangGraph 是一个用于构建状态化、图-based工作流的框架，`MessagesState` 作为图的状态定义，用于管理对话消息。以下是使用步骤：

1. **定义图并使用 `MessagesState`**：
   在创建 `StateGraph` 时指定 `MessagesState` 作为状态类。
2. **添加节点和边**：
   定义处理消息的节点（函数或逻辑），并通过边控制节点间的流程。
3. **更新消息**：
   节点可以向 `messages` 列表添加新消息或修改现有消息。
4. **编译并运行图**：
   编译图并用初始状态或输入消息运行。

#### 示例：使用 `MessagesState` 构建简单聊天机器人
以下是一个使用 `MessagesState` 构建简单聊天机器人的示例，展示如何处理用户消息并生成 AI 回复。

##### 前提条件
确保安装必要包：
```bash
pip install langgraph langchain langchain_openai
```

需要配置 LLM 提供商（如 OpenAI）的 API 密钥：
```python
import os
os.environ["OPENAI_API_KEY"] = "你的-openai-api-key"
```

##### 示例代码
```python
from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

# 定义处理消息并生成回复的节点
def chatbot_node(state: MessagesState):
    # 获取当前状态中的消息
    messages = state["messages"]
    
    # 初始化 LLM（例如 OpenAI 的聊天模型）
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # 根据对话历史生成回复
    response = llm.invoke(messages)
    
    # 返回更新后的状态，包含新的 AI 消息
    return {"messages": [response]}

# 创建使用 MessagesState 的 StateGraph
graph = StateGraph(MessagesState)

# 添加聊天机器人节点
graph.add_node("chatbot", chatbot_node)

# 定义边：START -> chatbot -> END
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

# 编译图
app = graph.compile()

# 使用初始消息运行图
initial_state = {"messages": [HumanMessage(content="你好！今天能帮我什么？")]}
result = app.invoke(initial_state)

# 打印最终状态
for message in result["messages"]:
    print(f"{message.__class__.__name__}: {message.content}")
```

##### 代码说明
1. **导入依赖**：
   - 从 `langgraph.graph` 导入 `MessagesState`。
   - 使用 LangChain 的 `HumanMessage` 和 `AIMessage` 表示用户和 AI 消息。
   - 使用 `ChatOpenAI` 作为 LLM 生成回复。

2. **定义聊天机器人节点**：
   - `chatbot_node` 函数接收当前 `MessagesState`。
   - 从状态中提取 `messages` 列表。
   - 使用 LLM 根据对话历史生成回复。
   - 返回包含新 AI 消息的字典，追加到 `messages` 列表。

3. **构建图**：
   - 创建 `StateGraph`，指定 `MessagesState` 作为状态模式。
   - 添加 `chatbot` 节点处理消息。
   - 定义边：从 `START` 到 `chatbot` 节点，再到 `END`。

4. **运行图**：
   - 编译图为可执行应用。
   - 提供初始状态，包含用户消息 `HumanMessage`。
   - 调用 `invoke` 方法运行图，最终状态包含对话历史和 AI 回复。

5. **输出**：
   输出示例：
   ```
   HumanMessage: 你好！今天能帮我什么？
   AIMessage: 我可以回答你的任何问题！有什么想聊的吗？
   ```

#### 高级用法
##### 1. **自定义 `MessagesState`**
可以通过继承 `MessagesState` 添加自定义字段。例如：
```python
from typing import List
from langgraph.graph import MessagesState
from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict

class CustomMessagesState(MessagesState):
    user_id: str
    session_id: int

# 在图中使用自定义状态
graph = StateGraph(CustomMessagesState)
```

状态将包含 `messages` 列表以及 `user_id` 和 `session_id` 字段，节点可读写这些字段。

##### 2. **条件边**
可以根据消息内容使用条件边进行路由。例如：
```python
from langgraph.graph import MessagesState, StateGraph, START, END

def router_node(state: MessagesState):
    last_message = state["messages"][-1].content.lower()
    if "帮助" in last_message:
        return "help_node"
    return "chatbot_node"

def help_node(state: MessagesState):
    return {"messages": [AIMessage(content="这里是帮助信息！")]}

def chatbot_node(state: MessagesState):
    return {"messages": [AIMessage(content="来聊聊吧！")]}

graph = StateGraph(MessagesState)
graph.add_node("chatbot", chatbot_node)
graph.add_node("help", help_node)
graph.add_edge(START, "router")
graph.add_node("router", router_node)
graph.add_conditional_edges("router", router_node, {"help_node": "help", "chatbot_node": "chatbot"})
graph.add_edge("help", END)
graph.add_edge("chatbot", END)

app = graph.compile()
result = app.invoke({"messages": [HumanMessage(content="我需要帮助")]})
print(result["messages"][-1].content)  # 输出：这里是帮助信息！
```

`router_node` 检查最后一条消息内容，路由到 `help_node` 或 `chatbot_node`。

##### 3. **流式消息**
LangGraph 支持流式处理，适合实时应用。例如：
```python
for chunk in app.stream({"messages": [HumanMessage(content="讲个笑话")]):
    for node, state in chunk.items():
        if state.get("messages"):
            print(f"{node}: {state['messages'][-1].content}")
```

这将流式输出 AI 的回复，适合实时聊天场景。

##### 4. **状态持久化**
LangGraph 支持通过检查点（checkpointer）持久化状态，适合跨会话保持对话历史。使用示例：
```python
from langgraph.checkpoint.memory import MemorySaver

# 创建内存检查点
checkpointer = MemorySaver()

# 在编译图时启用检查点
app = graph.compile(checkpointer=checkpointer)

# 运行图并指定配置以保存状态
config = {"configurable": {"thread_id": "1"}}
result = app.invoke({"messages": [HumanMessage(content="你好！")]}, config)

# 后续调用可恢复状态
result = app.invoke({"messages": [HumanMessage(content="继续聊")]}, config)
```

#### 注意事项
- **消息格式**：确保消息符合 `BaseMessage` 或兼容格式，否则可能导致错误。
- **状态更新**：节点返回的字典会更新状态，`messages` 键的值会追加到列表中。
- **性能**：对于长对话历史，确保 LLM 支持处理大量消息，或使用截断策略。
- **依赖 LangChain**：`MessagesState` 通常与 LangChain 的消息类一起使用，确保正确安装和配置。

#### 总结
`MessagesState` 是 LangGraph 中用于管理对话消息的强大工具，适合构建聊天机器人或对话型应用。通过将其与 `StateGraph` 结合，您可以轻松定义处理消息的工作流，支持条件路由、状态持久化和流式处理。上述示例展示了从基本到高级用法的实现方式，希望对您有所帮助！如果需要更具体或深入的示例，请告诉我！



## 实战案例



### 实现超长文本分段摘要并合并

当你需要用 LangGraph 处理超过模型单次处理长度（上下文窗口）的超长文本时，你的直觉是正确的：**核心思想确实类似于循环处理，但更专业、更强大的模式叫做“映射-规约”（Map-Reduce）**。

这是一种非常经典处理大数据集的方法，完美适用于长文本摘要：

1.  **切片 (Chunking)**：首先，将长文本切分成多个更小的、可以被模型一次性处理的文本块（Chunks）。
2.  **映射 (Map)**：接着，像循环一样，对**每一个**文本块独立地进行摘要。这一步可以并行处理，速度很快。你会得到多个小摘要。
3.  **规约 (Reduce)**：最后，将所有这些小摘要合并在一起，再让模型对这些摘要进行一次最终的总结，得出一个连贯、全面的最终摘要。

使用 LangGraph 来实现这个流程非常优雅，因为它能帮你清晰地定义和管理这个多步骤的工作流状态。

---


下面是一个完整的代码示例，展示了如何构建一个 Map-Reduce 摘要图。

这个代码将构建一个图，该图包含三个主要节点：`chunk_text`（切片）、`summarize_map`（映射摘要）和 `summarize_reduce`（规约摘要）。

```python
import os
from typing import TypedDict, List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langgraph.graph import StateGraph, END

# --- 1. 设置环境 (可选, 如果你已经设置了环境变量则不需要) ---
# os.environ["OPENAI_API_KEY"] = "sk-..."
# os.environ["OPENAI_BASE_URL"] = "https://api.example.com/v1" # 如果需要代理


# --- 2. 定义图的状态 (State) ---
# 状态是图在运行时传递的数据结构。它包含了所有需要跟踪的信息。
class GraphState(TypedDict):
    text: str              # 原始长文本
    chunks: List[str]      # 切分后的文本块列表
    summaries: List[str]   # 每个文本块的摘要列表
    final_summary: str     # 最终的摘要


# --- 3. 初始化模型和文本切分器 ---
# 我们需要一个LLM来进行摘要
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 文本切分器，用于将长文本切分成小块
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)


# --- 4. 定义图的节点 (Nodes) ---
# 节点是执行具体任务的函数。每个节点接收当前状态作为输入，并返回一个部分更新的状态。

def chunk_text_node(state: GraphState) -> GraphState:
    """
    节点1：将长文本切分成块。
    """
    print("--- 正在切分文本 ---")
    text = state['text']
    chunks = text_splitter.split_text(text)
    return {"chunks": chunks}

def summarize_map_node(state: GraphState) -> GraphState:
    """
    节点2 (Map): 对每个文本块进行独立摘要。
    """
    print("--- 正在对每个块进行摘要 (Map) ---")
    chunks = state['chunks']
    
    # 为每个块生成摘要的提示模板
    map_prompt = ChatPromptTemplate.from_template(
        "简要总结以下文本内容：\n\n{chunk}"
    )
    
    # 构建摘要链
    summarize_chain = map_prompt | llm
    
    # 并行处理所有块的摘要（这里用列表推导式模拟）
    summaries = summarize_chain.batch(
        [{"chunk": chunk} for chunk in chunks], 
        config={"max_concurrency": 5} # 可以设置并发数
    )
    
    # LangChain v0.2.0+ 的 .batch() 返回的是 AIMessage 列表，我们需要提取内容
    cleaned_summaries = [s.content for s in summaries]
    
    return {"summaries": cleaned_summaries}

def summarize_reduce_node(state: GraphState) -> GraphState:
    """
    节点3 (Reduce): 将所有小摘要合并成最终摘要。
    """
    print("--- 正在合并所有摘要 (Reduce) ---")
    summaries = state['summaries']
    
    # 将所有摘要连接起来
    summaries_joined = "\n\n".join(summaries)
    
    # 创建最终摘要的提示模板
    reduce_prompt = ChatPromptTemplate.from_template(
        "你收到了关于一个长文档的多个摘要。请将它们整合成一个连贯、流畅、全面的最终摘要。\n\n"
        "以下是各个部分的摘要：\n{summaries_text}"
    )
    
    # 构建最终摘要链
    reduce_chain = reduce_prompt | llm
    
    final_summary = reduce_chain.invoke({"summaries_text": summaries_joined})
    
    return {"final_summary": final_summary.content}


# --- 5. 构建并编译图 (Graph) ---
# 现在，我们将上面定义的节点和状态连接成一个工作流。

workflow = StateGraph(GraphState)

# 添加节点
workflow.add_node("chunker", chunk_text_node)
workflow.add_node("mapper", summarize_map_node)
workflow.add_node("reducer", summarize_reduce_node)

# 定义边的连接关系
workflow.set_entry_point("chunker")
workflow.add_edge("chunker", "mapper")
workflow.add_edge("mapper", "reducer")
workflow.add_edge("reducer", END) # 最终节点

# 编译图
app = workflow.compile()


# --- 6. 运行图 ---

# 准备一个超长的示例文本（这里为了演示，只用一段重复的文本模拟）
long_text = """
人工智能（AI）正在以前所未有的速度改变世界。从自动驾驶汽车到医疗诊断，AI的应用无处不在。
其核心技术包括机器学习、深度学习和自然语言处理。机器学习使计算机能够从数据中学习规律，而无需进行显式编程。
深度学习是机器学习的一个分支，它利用深度神经网络模型，在图像识别、语音识别等领域取得了巨大成功。
自然语言处理则致力于让计算机能够理解和生成人类语言，Siri和ChatGPT就是最好的例子。
然而，AI的发展也带来了挑战，如数据隐私、算法偏见和就业冲击。解决这些问题需要技术、法律和伦理的共同努力。
""" * 10 # 将文本重复10次来模拟长文本

# 使用图来处理长文本
# .invoke() 的输入是一个字典，键对应状态中的某个字段
initial_state = {"text": long_text}
final_state = app.invoke(initial_state)

# 打印最终结果
print("\n" + "="*50)
print("✅ 最终摘要：")
print(final_state['final_summary'])
```


- 代码解释

1.  **`GraphState`**：这是一个 `TypedDict`，它像一个清单，规定了在整个流程中需要跟踪的所有数据（原始文本、文本块、各块摘要、最终摘要）。LangGraph 会确保每一步的数据都符合这个结构。
2.  **`chunk_text_node`**：图的入口。它接收包含 `text` 的状态，使用 `RecursiveCharacterTextSplitter` 将其切分，然后将切分后的 `chunks` 列表放回状态中。
3.  **`summarize_map_node`**：这是 "Map" 步骤。它接收包含 `chunks` 的状态，然后使用 `summarize_chain.batch()` 方法**并行地**为每个 `chunk` 生成摘要。这比写一个 `for` 循环要高效得多。结果 `summaries` 列表被更新到状态中。
4.  **`summarize_reduce_node`**：这是 "Reduce" 步骤。它接收包含 `summaries` 的状态，将所有小摘要合并成一个字符串，然后调用 LLM 进行最后一次、也是最关键的一次整合，生成 `final_summary`。
5.  **`workflow.add_edge(...)`**：这部分定义了工作流的顺序：`chunker` -> `mapper` -> `reducer`，最后到 `END` 结束。
6.  **`app.invoke(...)`**：这是启动图的方式。你只需要提供初始状态（这里是包含长文本的字典），LangGraph 就会自动按照你定义的流程执行所有步骤，并返回包含所有计算结果的最终状态。

通过这种方式，你不仅解决了模型上下文窗口的限制，还构建了一个清晰、可维护、可扩展的自动化流程。

### 使用 LangGraph 构建基础聊天机器人

在本教程中，你将使用 LangGraph 构建一个基础的聊天机器人。这个聊天机器人将作为后续更高级教程的基础，我们将逐步添加更复杂的功能并介绍 LangGraph 的核心概念。

#### 前置要求

在开始本教程之前，请确保你有一个支持工具调用功能的 LLM。在本例中，我们将使用通义千问的 Qwen 模型。

#### 1. 安装必要的包

首先，让我们安装必要的包：

```python
!pip install -U langgraph langsmith
```

#### 2. 创建 StateGraph

现在我们将使用 LangGraph 创建一个基础的聊天机器人。这个聊天机器人将直接响应用户消息。

我们首先创建一个 StateGraph。StateGraph 对象将我们的聊天机器人定义为一个"状态机"。我们将添加节点来表示 LLM 和聊天机器人可以调用的函数，并添加边来指定机器人如何在这些函数之间转换。

State 类定义了我们的图的模式和用于处理状态更新的 reducer 函数。在我们的例子中，State 是一个 TypedDict，它有一个键：messages。add_messages reducer 函数用于将新消息追加到列表中，而不是覆盖它。

```python
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages

class State(TypedDict):
    # Messages 的类型是 "list"。`add_messages` 函数
    # 在注解中定义了如何更新这个状态键
    # （在这种情况下，它会将消息追加到列表中，而不是覆盖它们）
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)
```

让我来解释一下 `Annotated` 的作用：

`Annotated` 是 Python 的类型提示（Type Hints）系统中的一个特殊类型，它允许我们为类型添加额外的元数据。在 LangGraph 的上下文中，它被用来定义状态更新的行为。

让我们详细分析代码中的使用：

```python
from typing import Annotated

class State(TypedDict):
    messages: Annotated[list, add_messages]
```

这里 `Annotated` 的作用是：

1. **类型定义**：第一个参数 `list` 表示 `messages` 字段的类型是一个列表

2. **行为定义**：第二个参数 `add_messages` 是一个 reducer 函数，它定义了如何更新这个状态：
   - 当新的消息到来时，`add_messages` 会将这些消息追加到现有的消息列表中
   - 而不是简单地覆盖整个列表

举个例子来说明区别：

```python
# 不使用 Annotated 的情况
state = {"messages": ["消息1"]}
state["messages"] = ["消息2"]  # 这会覆盖之前的消息

# 使用 Annotated 和 add_messages 的情况
state = {"messages": ["消息1"]}
# 当新消息到来时，add_messages 会将其追加到列表中
# 结果会是 ["消息1", "消息2"]
```

在 LangGraph 中，这种设计特别有用，因为：
1. 它允许我们保持对话历史
2. 确保消息按顺序累积
3. 避免意外覆盖之前的消息

这就是为什么在聊天机器人中，我们使用 `Annotated[list, add_messages]` 来确保所有对话消息都被正确保存和累积。





#### 3. 设置 LLM

我们将使用通义千问的 Qwen 模型作为我们的 LLM。让我们初始化它并用一个简单的消息测试它。

```python
import os
from langchain_community.chat_models import ChatTongyi

llm = ChatTongyi(
    model="qwen-max"
)

# 测试 LLM
llm.invoke("你好")
```

#### 4. 添加聊天机器人节点

接下来，我们将添加一个"chatbot"节点。节点代表工作单元，通常是普通的 Python 函数。聊天机器人节点将使用我们的 LLM 来生成对用户消息的响应。

```python
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# 第一个参数是唯一的节点名称
# 第二个参数是每当节点被使用时将被调用的函数或对象
graph_builder.add_node("chatbot", chatbot)
```

#### 5. 添加入口点

我们需要添加一个入口点来告诉图每次运行时从哪里开始工作。在这种情况下，我们将 START 节点连接到我们的聊天机器人节点。

```python
graph_builder.add_edge(START, "chatbot")
```

#### 6. 编译图

在运行图之前，我们需要编译它。这将创建一个 CompiledGraph，我们可以在我们的状态上调用它。

```python
graph = graph_builder.compile()
```

#### 7. 可视化图（可选）

你可以使用 get_graph 方法和其中一个"draw"方法来可视化图。这一步是可选的，需要额外的依赖项。

```python
from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # 这需要一些额外的依赖项，是可选的
    pass
```





