---
title: langchain使用教程v0.3版本-Zata
description: ""
date: 2025-05-08T22:59:00+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---



参考



目录
```text

模块一：LangChain 入门与核心概念

第一章：LangChain 简介
1.1 什么是 LangChain？（解决什么问题，核心价值）
1.2 LangChain 的主要特性和优势
1.3 LangChain 的生态系统和社区
1.4 为什么选择 LangChain？（与其他类似框架的对比，如果适用）
1.5 学习本教程的先决条件（Python 基础，对大语言模型的基本了解）
第二章：环境搭建与第一个 LangChain 应用
2.1 安装 LangChain 及相关依赖
2.2 配置开发环境（API 密钥管理等，如 OpenAI API Key）
2.3 Hello LangChain：构建并运行你的第一个简单的 LangChain 应用
2.4 教程中使用的工具和资源介绍（Jupyter Notebook, VS Code 等）
第三章：LangChain 的核心组件概览
3.1 模型 I/O (Model I/O)：与语言模型的交互接口
LLMs (Large Language Models)
Chat Models
Text Embedding Models
3.2 数据连接 (Data Connection)：让语言模型与外部数据交互
Document Loaders
Document Transformers
Text Embedding Models (再次提及，强调其在数据连接中的作用)
Vector Stores
Retrievers
3.3 链 (Chains)：构建调用序列
基本链 (LLMChain)
顺序链 (Sequential Chains)
路由链 (Router Chains)
其他常用链类型
3.4 记忆 (Memory)：让链拥有记忆能力
记忆的类型 (ConversationBufferMemory, ConversationSummaryMemory 等)
如何在链中使用记忆
3.5 代理 (Agents)：让语言模型动态决策和行动
Agent 的核心概念：Tools, Agent Executor, ReAct 框架等
不同类型的 Agent (Zero-shot ReAct, Self-ask with search 等)
3.6 回调 (Callbacks)：监控和记录 LangChain 应用的执行过程
回调的作用和使用场景
常用的回调处理器



模块二：模型 I/O (Model I/O) 深入

第四章：与语言模型 (LLMs) 交互
4.1 理解 LLMs 接口
4.2 使用不同的 LLM提供商 (OpenAI, Hugging Face Hub, Azure OpenAI 等)
4.3 Prompt Templates：动态构建高效的提示
基本 Prompt Template
带有变量的 Prompt Template
Few-shot Prompt Template
4.4 Output Parsers：结构化输出处理
4.5 异步操作与流式输出
4.6 模型参数配置与优化 (temperature, max_tokens 等)
第五章：与聊天模型 (Chat Models) 交互
5.1 理解 Chat Models 的消息类型 (SystemMessage, HumanMessage, AIMessage)
5.2 构建聊天应用的 Prompt Templates
5.3 聊天历史管理
5.4 结合 Output Parsers 实现更复杂的聊天交互
第六章：文本嵌入模型 (Text Embedding Models)
6.1 文本嵌入的原理和应用场景
6.2 使用不同的文本嵌入模型 (OpenAI Embeddings, Hugging Face Embeddings 等)
6.3 生成文本的向量表示
6.4 比较文本相似度



模块三：数据连接 (Data Connection) 详解

第七章：文档加载 (Document Loaders)
7.1 从不同数据源加载文档 (文本文件, PDF, 网页, YouTube, Notion 等)
7.2 常用 Document Loaders 介绍和使用
7.3 自定义 Document Loader
第八章：文档转换 (Document Transformers)
8.1 文本分割 (Text Splitters)：按字符、Token、递归等方式分割长文本
8.2 文本清洗和预处理
8.3 元数据提取和添加
第九章：向量存储 (Vector Stores) 与检索 (Retrievers)
9.1 向量数据库的基本概念 (FAISS, Chroma, Pinecone, Weaviate 等)
9.2 将文档嵌入并存储到向量数据库
9.3 构建不同类型的检索器 (VectorStoreRetriever, MultiQueryRetriever, SelfQueryRetriever 等)
9.4 相似性搜索与语义检索的原理
9.5 优化检索效果 (Top K, 过滤等)



模块四：构建强大的链 (Chains)

第十章：基础与顺序链 (Basic and Sequential Chains)
10.1 LLMChain：最基础的链
10.2 SimpleSequentialChain：单输入单输出的顺序链
10.3 SequentialChain：多输入多输出的顺序链
10.4 链的输入输出管理
第十一章：高级链应用
11.1 转换链 (TransformChain)：在链中进行数据转换
11.2 路由链 (RouterChain)：根据输入动态选择下一个链
11.3 文档问答链 (Question Answering over Documents)
load_qa_chain, RetrievalQA 等
不同的 chain_type (stuff, map_reduce, refine, map_rerank)
11.4 摘要链 (Summarization Chains)
11.5 自定义链的创建与使用



模块五：赋予应用记忆 (Memory)

第十二章：记忆的类型与使用
12.1 ConversationBufferMemory：基础的对话缓冲区记忆
12.2 ConversationBufferWindowMemory：带窗口大小的对话缓冲区记忆
12.3 ConversationTokenBufferMemory：基于 Token 数量限制的记忆
12.4 ConversationSummaryMemory：对话摘要记忆
12.5 ConversationSummaryBufferMemory：结合摘要和缓冲区的记忆
12.6 EntityMemory：实体记忆
12.7 VectorStoreRetrieverMemory：基于向量存储的记忆
12.8 在链和 Agent 中集成和管理记忆
第十三章：高级记忆策略
13.1 自定义记忆类型
13.2 多轮对话中的记忆管理
13.3 记忆的持久化与加载



模块六：智能代理 (Agents) 的开发与应用

第十四章：Agent 基础
14.1 Agent 的核心组件：Tools, Agent, Agent Executor
14.2 理解 Agent 的思考过程 (Thought, Action, Observation)
14.3 内置 Tools 的使用 (Google Search, Wikipedia, Python REPL, Shell 等)
14.4 创建自定义 Tools
第十五章：不同类型的 Agent
15.1 Zero-shot ReAct Agent
15.2 Self-ask with search Agent
15.3 Conversational React Agent (用于对话的 Agent)
15.4 OpenAI Functions Agent (利用 OpenAI 函数调用)
15.5 Plan and Execute Agent
15.6 选择合适的 Agent 类型
第十六章：高级 Agent 应用
16.1 Agent 的错误处理与调试
16.2 限制 Agent 的行为和资源使用
16.3 构建复杂的 Agent 来完成多步骤任务
16.4 Agent 与外部 API 的交互



模块七：回调 (Callbacks) 与调试

第十七章：使用 Callbacks 进行监控与日志记录
17.1 CallbackManager 和 CallbackHandler
17.2 内置的回调处理器 (StdOutCallbackHandler, FileCallbackHandler)
17.3 自定义回调处理器
17.4 跟踪链和 Agent 的执行流程
17.5 与 LangSmith 等监控平台集成 (可选，但推荐提及)
第十八章：LangChain 应用的调试技巧
18.1 理解和分析 LangChain 的日志输出
18.2 使用 verbose=True 进行详细输出
18.3 LangChain Debugging 工具 (如果 LangChain 自身提供)
18.4 常见错误及其解决方法



模块八 Tools

模块九：实战项目

第十九章：项目一：构建一个基于文档的问答机器人
19.1 项目需求分析与设计
19.2 数据准备与处理 (加载、分割、嵌入、存储)
19.3 构建问答链或 Agent
19.4 用户界面集成 (可选，如 Streamlit 或 Gradio)
19.5 测试与评估
第二十章：项目二：开发一个能执行多步骤任务的个人助理 Agent
20.1 项目构思与功能定义
20.2 设计并实现所需的 Tools (如日历查询、邮件发送、信息检索等)
20.3 选择并配置合适的 Agent 类型
20.4 实现 Agent 的逻辑与交互
20.5 优化与迭代
第二十一章：项目三：（可选，根据热门或特定领域选择）
例如：构建一个代码生成助手、一个故事创作工具、一个基于知识图谱的问答系统等。
模块九：LangChain 进阶与生态

第二十二章：LangChain Expression Language (LCEL)
22.1 LCEL 的基本语法和优势
22.2 使用 LCEL 组合组件 (Runnables)
22.3 LCEL 的流式处理、批处理和异步支持
22.4 将现有链转换为 LCEL 形式
第二十三章：部署 LangChain 应用
23.1 常见的部署方式 (Serverless, Docker, PaaS 平台)
23.2 LangServe：快速部署 LangChain 应用的工具
23.3 API 设计与安全性考虑
第二十四章：LangGraph：构建具有循环和状态的复杂应用
24.1 LangGraph 的核心概念 (Nodes, Edges, State)
24.2 构建简单的图应用
24.3 实现多 Agent 协作
第二十五章：LangSmith：调试、测试、评估和监控 LLM 应用
25.1 LangSmith 的核心功能
25.2 如何在项目中使用 LangSmith
25.3 评估 LLM 应用的性能和质量
第二十六章：LangChain 的未来发展与社区资源
26.1 LangChain 的最新进展和发展方向
26.2 如何参与 LangChain 社区 (GitHub, Discord, 论坛)
26.3 持续学习和探索的建议
附录

A. 常见问题解答 (FAQ)
B. 术语表
C. 推荐阅读和资源链接


教程制作建议：

代码示例驱动： 每个概念都应伴随清晰、可运行的代码示例。
实践性强： 鼓励学习者动手实践，并提供练习题或小挑战。
循序渐进： 确保内容的难度逐步提升，避免一开始就引入过多复杂概念。
清晰的图示： 对于抽象概念（如链、Agent 的工作流程），使用图示辅助解释。
版本控制： 注意 LangChain 版本更新较快，教程内容应基于一个相对稳定的版本，并提示学习者注意版本差异。
互动性： 如果是视频教程或在线课程，可以设计一些互动环节。
```



- LangChain 的包结构: 如 langchain-core (核心抽象), langchain (通用链、代理和检索策略), langchain-community (第三方集成), 以及像 langgraph (用于构建有状态的多参与者应用的扩展) 和 langserve (用于部署 LangChain 应用为 REST API 的包)。




## 模块一：LangChain 入门与核心概念
### * 第一章：LangChain 简介
#### * 1.1 什么是 LangChain？（解决什么问题，核心价值）
LangChain 是一个开源框架，用于构建基于大型语言模型（LLM）的应用程序。它解决的主要问题是简化与 LLM 交互的复杂性，尤其是在需要结合外部数据、工具或上下文时。以下是其核心价值和解决的问题：

- 解决的问题

    上下文管理：LLM 本身无状态，难以处理长对话或复杂上下文。LangChain 提供链式结构（Chains）和记忆（Memory）机制，管理对话历史和上下文。

    外部数据整合：许多应用需要从数据库、文档或 API 获取数据。LangChain 的工具（如文档加载器、向量存储）支持高效检索和整合外部信息。

    工具调用：LLM 无法直接执行操作（如搜索、计算）。LangChain 的 Agent 机制允许模型调用外部工具，如搜索引擎、计算器或 API。

    复杂工作流：构建 LLM 应用常涉及多步骤逻辑。LangChain 的链式设计和 LCEL（LangChain Expression Language）支持灵活的工作流编排。

    部署与生产化：LangChain 提供 LangServe 等工具，简化模型服务化和部署。

- 核心价值

    模块化设计：通过 Chains、Agents、Tools 和 Memory 等模块，开发者可以快速构建复杂应用。

    外部知识增强：通过 RAG（Retrieval-Augmented Generation）机制，结合向量数据库（如 Chroma、Pinecone），提升模型回答的准确性和相关性。

    灵活性：支持多种 LLM（如 OpenAI、Hugging Face 模型）和工具，适配不同场景。

    开发效率：提供高层次抽象，降低开发者直接处理 LLM API 的复杂性。

    生态系统：与众多数据库、工具和平台集成，适合企业级应用。

- 典型应用场景

    智能客服：结合公司文档回答客户问题。

    知识问答：基于私有数据构建问答系统。

    自动化工作流：通过 Agents 实现多工具协作（如搜索后总结）。

    对话机器人：保持长对话的上下文一致性。

- 总结来说，LangChain 的核心价值在于降低构建 LLM 应用的门槛

#### 1.2 LangChain 的主要特性和优势
- **主要特性**
  - **Chains**：将多个组件（如提示模板、LLM、工具）组合成一个工作流，支持顺序或条件执行。
  - **Agents**：赋予 LLM 决策能力，根据任务动态选择和调用工具（如搜索、计算）。
  - **Memory**：支持短期（对话历史）和长期（外部存储）上下文管理，增强对话连贯性。
  - **Tools**：内置和自定义工具支持，允许 LLM 调用外部 API、数据库或函数。
  - **Document Loaders**：支持从 PDF、网页、数据库等多种来源加载和处理文档。
  - **Vector Stores**：集成向量数据库（如 Chroma、FAISS），支持语义搜索和 RAG。
  - **Prompt Templates**：提供结构化的提示管理，优化 LLM 输出。
  - **LCEL（LangChain Expression Language）**：声明式语言，用于快速定义和组合复杂链。
  - **LangServe**：将 LangChain 应用部署为 REST API，便于生产化。
  - **LangSmith**：用于调试、监控和优化 LangChain 应用的工具。

- **优势**
  - **易用性**：抽象底层复杂性，开发者无需深入了解 LLM 的内部机制。
  - **可扩展性**：支持自定义工具、模型和数据源，适应多样化需求。
  - **社区支持**：拥有活跃的开源社区，丰富的文档和教程。
  - **跨平台兼容**：与主流 LLM 提供商（如 OpenAI、Anthropic）和数据库集成。
  - **生产就绪**：通过 LangServe 和 LangSmith，支持从原型到生产的全流程。

#### 1.3 LangChain 的生态系统和社区
- **生态系统**
  - **模型支持**：兼容 OpenAI、Hugging Face、Anthropic、Google 等多种 LLM 和嵌入模型。
  - **工具集成**：支持外部工具如 SerpAPI（搜索）、Wolfram Alpha（计算）、Zapier（自动化）。
  - **数据存储**：集成向量数据库（Pinecone、Chroma、FAISS）和传统数据库（SQL、NoSQL）。
  - **部署工具**：LangServe 提供 API 部署，LangSmith 提供调试和监控。
  - **扩展库**：LangChain 社区提供额外模块，如 langchain-community，包含更多实验性功能。

- **社区**
  - **开源项目**：托管于 GitHub，拥有数千贡献者和活跃的 issue 讨论。
  - **文档与教程**：官方文档详尽，提供入门指南、API 参考和案例分析。
  - **社区资源**：Discord、Reddit 和 Twitter（X）上有活跃的开发者社区，分享经验和解决方案。
  - **活动与会议**：定期举办线上研讨会和技术分享会，促进知识交流。

#### 1.4 为什么选择 LangChain？（与其他类似框架的对比）
- **与其他框架的对比**
  - **Haystack**：专注于信息检索和 RAG，适合搜索密集型应用，但缺乏 LangChain 的复杂工作流和 Agent 功能。
  - **LlamaIndex**：专注于数据索引和查询，适合构建知识库，但工作流编排能力不如 LangChain 灵活。
  - **AutoGPT**：专注于自主 Agent，但稳定性和生产化能力较弱，相比 LangChain 缺乏模块化设计。
  - **Flowise**：提供低代码界面，适合非开发者，但定制化能力不如 LangChain。

- **选择 LangChain 的理由**
  - **全面性**：提供从上下文管理到工具调用、从开发到部署的全栈解决方案。
  - **灵活性**：支持多种模型和工具，适合从简单脚本到企业级应用的各种场景。
  - **社区与生态**：强大的社区支持和广泛的集成能力，降低开发和维护成本。
  - **生产化支持**：通过 LangServe 和 LangSmith，提供生产环境所需的可观测性和可扩展性。

#### 1.5 学习本教程的先决条件
- **Python 基础**
  - 熟悉 Python 语法、数据结构（如列表、字典）和函数。
  - 了解包管理工具（如 pip）以及虚拟环境的使用。
  - 掌握基本的文件操作和数据处理（如 JSON、CSV）。

- **大语言模型基础**
  - 了解 LLM 的基本概念（如提示工程、嵌入、生成）。
  - 熟悉 API 调用（如 REST API）以及常见 LLM 提供商（OpenAI、Hugging Face）。
  - 对向量搜索和语义相似性的基本原理有初步了解（非必需，但有帮助）。

- **其他建议**
  - 熟悉 Git 和 GitHub，用于获取 LangChain 源码和示例。
  - 了解基本的命令行操作，用于安装和运行代码。
  - 对机器学习或 NLP 有基础了解（非必需，但有助于理解高级概念）。

- **推荐准备**
  - 安装 Python 3.8+ 和 pip。
  - 配置 OpenAI 或 Hugging Face API 密钥（用于测试 LLM）。
  - 阅读 LangChain 官方文档的 Quickstart 部分，熟悉基本安装和用法。


### * 第二章：环境搭建与第一个 LangChain 应用




####    * 2.1 安装 LangChain 及相关依赖


LangChain 是一个 Python 库，安装需要 Python 3.8 或更高版本。

```bash
pip install langchain  # 安装 LangChain 核心库


# 安装特定的LLM集成
pip install langchain-openai  # 用于 OpenAI 模型
pip install langchain-huggingface  # 用于 Hugging Face 模型

# 常见的依赖
pip install langchain-community  # 包含社区贡献的工具和集成
pip install chromadb  # 向量数据库chroma 用于RAG
pip install tiktoken requests pypdf  # tiktoken：用于 OpenAI 模型的令牌计算。requests：用于 API 调用。pypdf：用于处理 PDF 文档。



```
    
    
####  * 2.2 配置开发环境（API 密钥管理等，如 OpenAI API Key）

为了安全，避免在代码中硬编码密钥，建议将密钥存储在环境变量中

此外也可以存储在.env文件中，然后安装python-dotenv，并使用如下代码安装

```py
from dotenv import load_dotenv
load_dotenv()
```

- 安全提示
不要将 API 密钥上传到公共仓库（如 GitHub）。
使用 .gitignore 忽略 .env 文件。
定期轮换密钥，防止泄露。

#### * 2.3 Hello LangChain：构建并运行你的第一个简单的 LangChain 应用


以下是一个简单的 LangChain 应用示例，使用 OpenAI 模型生成文本。

<span  style="color:red"  > 如果没有openai的apikey，也可以使用其他厂商的接口，只是调用方式可能存在不同  </span>

可见链接  ：  

| [**🔗langchain调用不同平台api**](/p/langchain调用不同平台api/) |
|--------|



```py
# 导入必要的模块
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 初始化 LLM（使用 OpenAI 的模型）
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 创建提示模板
prompt = PromptTemplate.from_template("你好！请用一句话描述 {topic} 的重要性。")

# 构建链
chain = prompt | llm | StrOutputParser()

# 运行链
topic = "人工智能"
response = chain.invoke({"topic": topic})

# 输出结果
print(response)
```
- 代码说明
    - ChatOpenAI：初始化 OpenAI 的聊天模型，temperature 控制输出随机性。
    - 这里没有显式导入apikey，需要设置环境变量
    - PromptTemplate：定义结构化提示，允许动态插入变量（如 topic）。
    - Chain：使用 LCEL（| 运算符）将提示、模型和输出解析器连接。
    - invoke：运行链，输入字典格式的变量，输出模型生成的文本。

#### * 2.4 教程中使用的工具和资源介绍（Jupyter Notebook, VS Code 等）

- 工具
    - Postman（可选）：测试 LangServe 部署的 API。
    - LangSmith（可选）：LangChain 官方调试工具，需注册并配置。

- 资源推荐
    - LangChain 官方文档：docs.langchain.com，提供详细 API 参考和教程。
    - GitHub 仓库：github.com/langchain-ai/langchain，获取源码和示例。
    - 社区论坛：Discord 或 Reddit 的 LangChain 社区，获取最新动态和问题解答。
    - OpenAI 文档：platform.openai.com/docs，了解模型和 API 细节。

### * 第三章：LangChain 的核心组件概览

 <span style = "color :red "> 注意，本章节内容中的代码可以先不做了解，在模块二学习完成之后再回头查看 </span>



####  * 3.1 模型 I/O (Model I/O)：与语言模型的交互接口


模型 I/O 是 LangChain 框架中最核心的模块之一，负责处理与语言模型的输入输出交互。它提供了一套标准化的接口，使得开发者能够以统一的方式与各种语言模型（无论是本地模型还是云端 API，如 OpenAI、Hugging Face、Grok 等）进行通信。模型 I/O 模块主要包括以下三个核心组成部分：

##### 1.  **Prompts（提示）**
Prompts 是与语言模型交互的起点，用于定义输入的结构和内容。LangChain 提供了强大的提示管理工具，允许开发者创建动态、可重用的提示模板。

* **提示模板 (Prompt Templates)**：通过占位符和变量，开发者可以构建灵活的提示。例如，一个模板可以是：“请将以下文本翻译成{language}：{text}”。
* **动态提示**：支持根据上下文或用户输入动态填充提示内容，适用于需要个性化或复杂逻辑的场景。
* **提示优化**：LangChain 提供工具帮助优化提示，例如通过 Few-Shot Learning 或 Chain-of-Thought 提示设计，提升模型输出质量。

**代码示例 (Prompts):**

```python
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_openai import ChatOpenAI # 用于后续语言模型示例

# 1. 基本的 PromptTemplate (通常用于 LLM 而非 ChatModel)
simple_template_str = "请告诉我关于 {topic} 的一个有趣的事实。"
simple_prompt_template = PromptTemplate.from_template(simple_template_str)
formatted_simple_prompt = simple_prompt_template.format(topic="太阳系")
print(f"基本提示模板输出:\n{formatted_simple_prompt}\n")

# 2. ChatPromptTemplate (更适用于聊天模型)
# 包含系统消息和用户消息模板
system_template_str = "你是一个乐于助人的AI助手，能将文本翻译成指定的语言。"
human_template_str = "请将以下文本翻译成{language}：{text}"

chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template_str),
    ("human", human_template_str)
])

formatted_chat_prompt = chat_prompt_template.format_messages(
    language="法语",
    text="我喜欢编程。"
)
print(f"聊天提示模板输出:\n{formatted_chat_prompt}\n")

# 2.1 另一种创建 ChatPromptTemplate 的方式 (使用 MessagePromptTemplate 对象)
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template_str)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template_str)
chat_prompt_template_v2 = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
formatted_chat_prompt_v2 = chat_prompt_template_v2.format_prompt(
    language="西班牙语",
    text="今天天气很好。"
).to_messages() # .to_string() 可以转为字符串
print(f"聊天提示模板输出 (v2):\n{formatted_chat_prompt_v2}\n")


# 3. Few-Shot Learning 示例 (通过 ChatPromptTemplate 实现)
# 假设我们想让模型学习一种特定的问答风格
from langchain_core.prompts import FewShotChatMessagePromptTemplate

examples = [
    {"input": "有什么推荐的科幻电影？", "output": "《星际穿越》因其深刻的科学概念和感人的故事情节而广受好评。"},
    {"input": "学习Python的最佳途径是什么？", "output": "从官方文档开始，并结合实际项目练习是学习Python的好方法。"},
]

# 为每个示例创建一个格式化模板
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)

final_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个乐于助人的AI助手。"),
    few_shot_prompt, # 注入 few-shot 示例
    ("human", "{user_input}"), # 用户的新输入
])

formatted_few_shot_prompt = final_prompt_template.format_messages(
    user_input="如何提高写作技巧？"
)
print(f"Few-Shot 提示模板输出:\n{formatted_few_shot_prompt}\n")
```

##### 2.  **语言模型 (Language Models)**
语言模型是模型 I/O 的核心执行单元，LangChain 支持多种类型的语言模型：

* **聊天模型 (Chat Models)**：如 OpenAI 的 GPT-4、Grok 等，擅长处理对话型任务。
* **嵌入模型 (Embedding Models)**：如 Hugging Face 的句嵌入模型，用于生成文本的向量表示，适用于语义搜索或相似性比较。
* **本地模型支持**：LangChain 允许集成本地部署的模型（如 LLaMA 或其他开源模型），适合对隐私和成本敏感的场景。
LangChain 的抽象层屏蔽了不同模型 API 的差异，开发者只需调用统一的接口即可切换模型。

**代码示例 (Language Models):**

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# from langchain_community.llms import Ollama # 示例: 本地模型 (需已安装并运行 Ollama)
# from langchain_huggingface import HuggingFaceEmbeddings # 示例: HuggingFace 嵌入模型

# 确保 OPENAI_API_KEY 已设置
if not os.getenv("OPENAI_API_KEY"):
    print("警告: OPENAI_API_KEY 未设置，OpenAI 模型示例可能无法运行。")
    # 可以设置一个虚拟密钥用于基本结构演示，但实际调用会失败
    # os.environ["OPENAI_API_KEY"] = "YOUR_DUMMY_API_KEY"


# 1. 聊天模型 (Chat Models) - 使用 OpenAI GPT-3.5-turbo
try:
    chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 使用之前创建的聊天提示
    messages_for_model = chat_prompt_template.format_messages(
        language="德语",
        text="这是一个测试。"
    )
    print(f"发送给聊天模型的格式化消息:\n{messages_for_model}\n")

    # 调用模型
    ai_response = chat_model.invoke(messages_for_model)
    print(f"聊天模型 (GPT-3.5-turbo) 的响应:\n{ai_response.content}\n")

    # 流式输出 (Streaming)
    print("聊天模型 (GPT-3.5-turbo) 流式响应:")
    for chunk in chat_model.stream(messages_for_model):
        print(chunk.content, end="", flush=True)
    print("\n")

except Exception as e:
    print(f"运行 OpenAI 聊天模型时出错: {e}")
    print("请确保您的 OPENAI_API_KEY 已正确设置并具有有效额度。\n")


# 2. 嵌入模型 (Embedding Models) - 使用 OpenAI
try:
    embedding_model = OpenAIEmbeddings(model="text-embedding-ada-002")

    text_to_embed = "LangChain 是一个强大的框架。"
    text_embedding = embedding_model.embed_query(text_to_embed)
    print(f"文本 '{text_to_embed}' 的嵌入向量 (前5个维度):\n{text_embedding[:5]}...\n")
    print(f"嵌入向量维度: {len(text_embedding)}\n")

    documents_to_embed = [
        "今天天气真好。",
        "我喜欢在公园散步。",
        "机器学习正在改变世界。"
    ]
    document_embeddings = embedding_model.embed_documents(documents_to_embed)
    print(f"嵌入了 {len(document_embeddings)} 个文档。")
    print(f"第一个文档的嵌入向量 (前5个维度):\n{document_embeddings[0][:5]}...\n")

except Exception as e:
    print(f"运行 OpenAI 嵌入模型时出错: {e}")
    print("请确保您的 OPENAI_API_KEY 已正确设置并具有有效额度。\n")

# 示例: Hugging Face 嵌入模型 (如果已安装 langchain-huggingface 和 sentence-transformers)
# try:
#     from langchain_huggingface import HuggingFaceEmbeddings
#     hf_embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#     hf_text_embedding = hf_embedding_model.embed_query("使用Hugging Face进行嵌入")
#     print(f"Hugging Face 嵌入向量 (前5个维度):\n{hf_text_embedding[:5]}...\n")
# except ImportError:
#     print("要运行 Hugging Face 嵌入模型示例，请安装 langchain-huggingface 和 sentence-transformers。\n")
# except Exception as e:
#     print(f"运行 Hugging Face 嵌入模型时出错: {e}\n")


# 3. 本地模型支持 (示例使用 Ollama, 假设已安装并运行了 Ollama 及相应模型如 llama3)
# from langchain_community.chat_models import ChatOllama
# try:
#     local_llm = ChatOllama(model="llama3") # 确保 llama3 模型已通过 ollama pull llama3 下载
#     local_response = local_llm.invoke("用一句话描述 LangChain.")
#     print(f"本地模型 (Ollama Llama3) 响应:\n{local_response.content}\n")
# except Exception as e:
#     print(f"运行本地模型 (Ollama) 时出错: {e}")
#     print("请确保 Ollama 服务正在运行并且已下载所选模型 (如 llama3)。\n")

```

##### 3.  **输出解析器 (Output Parsers)**
语言模型的输出通常是自由文本，难以直接用于结构化处理。输出解析器负责将模型的原始输出转换为开发者需要的格式。

* **结构化输出**：将模型输出解析为 JSON、列表或其他数据结构。例如，将模型生成的回答解析为键值对。
* **自定义解析**：支持正则表达式、Pydantic 模型等工具，定义复杂的解析逻辑。
* **错误处理**：当模型输出不符合预期时，解析器可以触发重试或提供默认值，确保系统鲁棒性。

**代码示例 (Output Parsers):**

```python
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field # 使用 Pydantic V1
from typing import List, Dict

# 0. 默认的字符串输出解析器 (通常是链中的最后一个)
string_parser = StrOutputParser()
# (将在 LCEL 示例中演示)

# 1. JSON 输出解析器
# 假设我们期望模型输出一个 JSON 字符串
json_prompt_template_str = """
提取以下文本中的关键信息，并以 JSON 格式返回。
JSON 应该包含 'name', 'age', 和 'city' 字段。
文本: {text_input}

请严格按照以下格式输出 JSON 对象:
{{
    "name": "...",
    "age": ...,
    "city": "..."
}}
"""
json_prompt = PromptTemplate.from_template(json_prompt_template_str)
# 模拟模型输出 (实际应用中这会来自语言模型)
mock_llm_json_output = '{\n\t"name": "张三",\n\t"age": 30,\n\t"city": "北京"\n}'
# mock_llm_json_output_malformed = '{\n\t"name": "李四",\n\t"age": "二十五",\n\t"city": "上海",\n}' # 错误格式示例

json_parser = JsonOutputParser()
try:
    parsed_json = json_parser.parse(mock_llm_json_output)
    print(f"JSON 解析器输出:\n{parsed_json}\n")
    print(f"类型: {type(parsed_json)}, Name: {parsed_json.get('name')}\n")
except Exception as e:
    print(f"JSON 解析错误: {e}")


# 2. Pydantic 输出解析器 (用于更强的类型校验和结构定义)
class PersonInfo(BaseModel):
    name: str = Field(description="人的姓名")
    age: int = Field(description="人的年龄")
    hobbies: List[str] = Field(description="爱好列表")
    address: Dict[str, str] = Field(description="地址，包含 street 和 city")

pydantic_parser = PydanticOutputParser(pydantic_object=PersonInfo)

# 提示中包含 Pydantic 对象的格式指令
pydantic_prompt_template_str = """
根据以下用户信息，提取信息并严格按照指定的 JSON 格式输出。
{format_instructions}

用户信息:
{user_description}
"""
pydantic_prompt = PromptTemplate(
    template=pydantic_prompt_template_str,
    input_variables=["user_description"],
    partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}
)

user_desc = "李明，今年28岁，住在幸福路123号，北京。他喜欢跑步和阅读。"
formatted_pydantic_prompt = pydantic_prompt.format(user_description=user_desc)
print(f"Pydantic 提示 (包含格式指令):\n{formatted_pydantic_prompt}\n")

# 模拟模型输出 (理想情况下模型会遵循 format_instructions)
mock_llm_pydantic_output = '''
{
    "name": "李明",
    "age": 28,
    "hobbies": ["跑步", "阅读"],
    "address": {
        "street": "幸福路123号",
        "city": "北京"
    }
}
'''
# mock_llm_pydantic_output_malformed = '{"name": "王五", "age": "thirty", "hobbies": ["coding"]}' # 格式或类型错误

try:
    parsed_pydantic_object = pydantic_parser.parse(mock_llm_pydantic_output)
    print(f"Pydantic 解析器输出:\n{parsed_pydantic_object}\n")
    print(f"类型: {type(parsed_pydantic_object)}")
    print(f"Name: {parsed_pydantic_object.name}, Hobbies: {parsed_pydantic_object.hobbies[0]}\n")
except Exception as e:
    print(f"Pydantic 解析错误: {e}\n")


# 3. 错误处理和重试 (通常与 RetryOutputParser 或自定义逻辑结合)
# 这是一个概念性的说明，具体实现可能需要更复杂的链
from langchain.output_parsers import RetryWithErrorOutputParser
from langchain_openai import OpenAI # 需要一个 LLM 而不是 ChatModel 来配合 RetryWithErrorOutputParser 的旧用法
                                # 或者需要重新构建 prompt 和 parser 逻辑

# 为了简单起见，这里仅展示概念。实际 RetryWithErrorOutputParser 通常与 LLMChain 一起使用。
# 假设我们有一个基础解析器
base_parser = JsonOutputParser()
# 假设我们有一个可以修复错误的 LLM (这里用 ChatOpenAI 代替，但理想情况下是 LLM)
try:
    # 确保 OPENAI_API_KEY 设置
    if os.getenv("OPENAI_API_KEY"):
        # 注意: RetryWithErrorOutputParser 的典型用法是与 LLM 实例 (如 langchain_openai.OpenAI)
        # 而不是 ChatModel (如 langchain_openai.ChatOpenAI) 结合。
        # 如果使用 ChatModel，需要调整 prompt 以适应 chat message 结构，
        # 或者使用更现代的 LCEL 方式处理重试逻辑。

        # 为了简单演示，我们假设有一个 LLM 实例
        # llm_for_retry = OpenAI(temperature=0) # 需要 from langchain_openai import OpenAI
        # retry_parser = RetryWithErrorOutputParser.from_llm(parser=base_parser, llm=llm_for_retry)

        # 演示一个简化的重试概念，实际应用会更复杂
        malformed_output = "{'name': 'Test', 'details': 'Missing quote}"
        # try:
        #     # 下面这行会报错，因为 retry_parser.parse 的参数不正确
        #     # fixed_output = retry_parser.parse_with_prompt(malformed_output, prompt_value) # 需要 prompt_value
        #     print("Retry parser 概念: 通常需要一个完整的链来驱动重试逻辑。")
        # except Exception as e:
        #     print(f"Retry parser 概念性错误处理演示: {e}")
        pass # 跳过实际执行，因为设置复杂
    else:
        print("跳过 RetryWithErrorOutputParser 示例，因为 OPENAI_API_KEY 未设置。")

except Exception as e:
    print(f"运行 RetryWithErrorOutputParser 示例时出错: {e}")
print("注意: RetryWithErrorOutputParser 的使用相对复杂，常与 LLMChain 结合，或者通过 LCEL 实现更灵活的重试。")

```

---

- 这些组件可以通过 LangChain 表达式语言（LCEL）组合，例如 `chain = chat_prompt | chat_model | output_parser`。这允许开发者根据需要切换模型或连接外部数据源。

**代码示例 (LCEL - LangChain Expression Language):**

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

# 确保 OPENAI_API_KEY 已设置
if not os.getenv("OPENAI_API_KEY"):
    print("警告: OPENAI_API_KEY 未设置，LCEL OpenAI 链示例可能无法运行。")
    # os.environ["OPENAI_API_KEY"] = "YOUR_DUMMY_API_KEY"


# 示例 1: 简单的字符串输入 -> 聊天模型 -> 字符串输出
print("\n--- LCEL 示例 1: 简单翻译链 ---")
try:
    prompt1 = ChatPromptTemplate.from_template("将 '{text}' 从中文翻译成英文。")
    model1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    parser1 = StrOutputParser()

    # 构建链
    translation_chain = prompt1 | model1 | parser1

    # 执行链
    input_text = "我爱学习 LangChain"
    result1 = translation_chain.invoke({"text": input_text})
    print(f"输入: {input_text}")
    print(f"LCEL 翻译链输出: {result1}\n")

    # 流式输出
    print(f"LCEL 翻译链流式输出:")
    for chunk in translation_chain.stream({"text": "LangChain 非常强大且灵活。"}):
        print(chunk, end="", flush=True)
    print("\n")

except Exception as e:
    print(f"运行 LCEL 示例 1 时出错: {e}")


# 示例 2: 结构化输出 (JSON)
print("\n--- LCEL 示例 2: 提取信息并输出 JSON ---")
try:
    json_prompt_lcel = ChatPromptTemplate.from_template(
        """根据以下描述提取人物的关键信息，并以 JSON 对象形式返回。
        描述: {description}
        请确保输出是一个有效的 JSON 对象，包含 "name" 和 "occupation" 字段。"""
    )
    model2 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # LangChain 会自动尝试将模型的字符串输出（如果它是一个合法的JSON字符串）解析为JSON
    # 对于更严格的JSON输出和潜在的修复，JsonOutputParser 很有用。
    parser2 = JsonOutputParser() # 或者可以直接使用，模型需要被良好地提示以输出 JSON

    extraction_chain = json_prompt_lcel | model2 | parser2

    description = "王明是一位经验丰富的软件工程师，他热衷于构建可扩展的 Web 应用程序。"
    result2 = extraction_chain.invoke({"description": description})
    print(f"输入描述: {description}")
    print(f"LCEL JSON 提取链输出: {result2}")
    print(f"类型: {type(result2)}, Name: {result2.get('name')}\n")

except Exception as e:
    print(f"运行 LCEL 示例 2 时出错: {e}")


# 示例 3: 结构化输出 (Pydantic)
print("\n--- LCEL 示例 3: 提取信息并输出 Pydantic 对象 ---")
class Joke(BaseModel):
    setup: str = Field(description="笑话的铺垫")
    punchline: str = Field(description="笑话的笑点")
    rating: int = Field(description="笑话的趣味等级，1-5", ge=1, le=5)

try:
    # PydanticOutputParser 可以与 .with_structured_output 方法一起使用在较新版本的 LangChain
    # model.with_structured_output(Joke)
    # 或者，我们可以像之前一样构建提示，并依赖模型正确格式化后由 PydanticOutputParser 解析
    pydantic_parser_lcel = PydanticOutputParser(pydantic_object=Joke)

    pydantic_prompt_lcel = ChatPromptTemplate.from_messages([
        ("system", "你是一个讲笑话的AI。请根据用户的主题生成一个笑话，并使用指定的格式。"),
        ("human", "给我讲一个关于{topic}的笑话。\n{format_instructions}")
    ])

    model3 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 构建链
    # 注意: 这里的顺序和 JsonOutputParser 类似，模型需要被提示输出兼容的结构
    joke_chain = (
        pydantic_prompt_lcel |
        model3 |
        pydantic_parser_lcel
    )

    # 执行链
    # 如果模型没有 ChatOpenAI().with_structured_output(Joke) 这种方法,
    # 仍然需要 format_instructions
    format_instructions = pydantic_parser_lcel.get_format_instructions()
    result3 = joke_chain.invoke({
        "topic": "电脑",
        "format_instructions": format_instructions
    })

    print(f"输入主题: 电脑")
    print(f"LCEL Pydantic 笑话链输出:\n{result3}")
    print(f"类型: {type(result3)}")
    print(f"笑话铺垫: {result3.setup}")
    print(f"笑话趣味等级: {result3.rating}\n")

    # 更现代和推荐的方式是使用 .with_structured_output (如果模型支持)
    # 这通常会处理提示的格式化指令部分
    # model_with_structured_output = model3.with_structured_output(Joke)
    # structured_chain = (
    #     ChatPromptTemplate.from_template("给我讲一个关于{topic}的笑话。") |
    #     model_with_structured_output
    # )
    # result_structured = structured_chain.invoke({"topic": "猫"})
    # print(f"LCEL Pydantic (with_structured_output) 笑话链输出:\n{result_structured}")
    # print(f"类型: {type(result_structured)}\n")


except Exception as e:
    print(f"运行 LCEL 示例 3 时出错: {e}")
    print("Pydantic 输出通常需要模型严格遵循格式指令，或使用 .with_structured_output 方法（如果可用）。")

```

---



#### 3.2 RAG：让语言模型与外部数据交互

语言模型（LLMs）在预训练后，其知识是静态的。数据连接使得LLMs能够访问和利用外部的、动态的、或私有的数据源。这是实现检索增强生成（Retrieval Augmented Generation, RAG）系统的基础，让LLM的回答更有依据、更及时、更准确。

##### 1. Document Loaders (文档加载器)

    **概念：**
    文档加载器负责从各种来源（如文本文件、PDF、网页、数据库等）读取数据，并将其转换成LangChain能够处理的 `Document` 对象。一个 `Document` 对象通常包含 `page_content` (文本内容) 和 `metadata` (描述文档来源等的元数据字典)。

    **代码示例：**

    我们将演示几种常见的加载器：

    * **TextLoader**: 加载纯文本文件。
    * **PyPDFLoader**: 加载PDF文件。
    * **WebBaseLoader**: 从网页URL加载内容。

    ```python
    from langchain_community.document_loaders import TextLoader, PyPDFLoader, WebBaseLoader
    import os

    # --- 准备示例文件 (在你的本地环境中创建这些文件) ---
    # 1. 创建一个 example.txt 文件
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("这是一个示例文本文件。\n它包含多行内容。\nLangchain的文档加载器很有用。")

    # 2. 准备一个 example.pdf (你需要自己准备一个PDF文件，或跳过此部分)
    # 为了演示，我们假设你有一个名为 "example.pdf" 的文件在同一目录下。
    # 如果没有，PyPDFLoader 部分会报错，你可以注释掉相关代码。

    # --- TextLoader 示例 ---
    print("--- TextLoader ---")
    text_loader = TextLoader("example.txt", encoding="utf-8")
    documents_txt = text_loader.load()
    print(f"从 TXT 加载了 {len(documents_txt)} 个文档。")
    for i, doc in enumerate(documents_txt):
        print(f"文档 {i+1} 内容: {doc.page_content[:50]}...") # 打印前50个字符
        print(f"文档 {i+1} 元数据: {doc.metadata}\n")

    # --- PyPDFLoader 示例 ---
    # 注意: PyPDFLoader 将PDF的每一页加载为一个单独的 Document 对象。
    # 你需要有一个名为 'example.pdf' 的文件在你的工作目录中。
    # 如果你没有PDF文件用于测试，可以先注释掉这部分代码。
    print("--- PyPDFLoader ---")
    pdf_file_path = "example.pdf" # 替换为你的PDF文件路径
    if os.path.exists(pdf_file_path):
        pdf_loader = PyPDFLoader(pdf_file_path)
        documents_pdf = pdf_loader.load() # load_and_split() 也可以用，会直接分割
        print(f"从 PDF 加载了 {len(documents_pdf)} 个文档 (每页一个文档)。")
        if documents_pdf: # 确保列表不为空
            print(f"第一页内容: {documents_pdf[0].page_content[:100]}...")
            print(f"第一页元数据: {documents_pdf[0].metadata}\n")
    else:
        print(f"警告: 未找到PDF文件 '{pdf_file_path}'，跳过PyPDFLoader示例。\n")

    # --- WebBaseLoader 示例 ---
    print("--- WebBaseLoader ---")
    # 注意: 使用公共可访问的URL
    web_loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/") # 一个关于LLM Agent的博客
    # web_loader = WebBaseLoader(["https://example.com", "https://example.org"]) # 也可以加载多个URL
    documents_web = web_loader.load()
    print(f"从 Web 加载了 {len(documents_web)} 个文档。")
    if documents_web:
        print(f"网页内容 (部分): {documents_web[0].page_content[500:700]}...") # 打印部分内容
        print(f"网页元数据: {documents_web[0].metadata}\n")

    # 清理创建的示例文件
    if os.path.exists("example.txt"):
        os.remove("example.txt")
    ```

    **解释：**
    * `TextLoader("example.txt")` 创建一个加载器实例，指向目标文件。
    * `loader.load()` 执行加载操作，返回一个 `Document` 对象列表。对于 `TextLoader`，通常整个文件是一个文档。对于 `PyPDFLoader`，通常每一页是一个文档。
    * 每个 `Document` 对象都有 `page_content` (字符串) 和 `metadata` (字典，包含如 `source` 等信息)。

---

##### 2. Document Transformers (文档转换器)

**概念：**
加载文档后，它们往往太长，无法直接输入LLM的上下文窗口。文档转换器，尤其是文本分割器（Text Splitters），用于将长文档分割成更小的、语义上连贯的块（chunks）。这些块更易于嵌入模型处理和向量存储检索。

**代码示例：**

我们将使用 `RecursiveCharacterTextSplitter`，它是一种常用的、效果较好的分割器。

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter

# 假设我们已经有了一个长文档 (复用上面WebBaseLoader的结果，如果存在的话)
# 或者创建一个示例文档
if 'documents_web' in locals() and documents_web:
    long_document = documents_web[0] # 使用之前加载的网页内容
    print(f"使用先前加载的网页文档进行分割，总字符数: {len(long_document.page_content)}")
else:
    from langchain_core.documents import Document
    sample_text = "这是一段非常非常长的文本。" * 200 + \
                  "它需要被分割成小块才能有效地被语言模型处理。" + \
                  "递归字符分割器会尝试根据段落、句子等来分割文本。\n\n" + \
                  "这是新的段落。它也应该被智能地处理。Langchain提供了多种分割策略。" * 100
    long_document = Document(page_content=sample_text, metadata={"source": "sample_long_text"})
    print(f"使用手动创建的长文档进行分割，总字符数: {len(long_document.page_content)}")


# --- RecursiveCharacterTextSplitter 示例 ---
print("\n--- RecursiveCharacterTextSplitter ---")
# chunk_size: 每个块的最大字符数 (也可以用 token 数，但需要 tokenizer)
# chunk_overlap: 块之间的重叠字符数，有助于保持上下文连续性
# separators: 尝试分割的字符列表，按顺序尝试
recursive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", "，", " ", ""], # 更适合中文的分割符
    length_function=len # 定义如何计算长度，这里是字符数
)

split_docs_recursive = recursive_splitter.split_documents([long_document]) # 注意输入是文档列表

print(f"递归分割后得到 {len(split_docs_recursive)} 个文档块。")
for i, chunk in enumerate(split_docs_recursive[:3]): # 打印前3个块
    print(f"\n块 {i+1}:")
    print(f"内容 (前100字符): {chunk.page_content[:100]}...")
    print(f"长度: {len(chunk.page_content)}")
    print(f"元数据: {chunk.metadata}") # 元数据会被继承

# --- CharacterTextSplitter 示例 (更简单，按固定字符分割) ---
print("\n--- CharacterTextSplitter ---")
char_splitter = CharacterTextSplitter(
    separator = "\n\n", # 指定一个简单的分隔符
    chunk_size = 600,
    chunk_overlap  = 100,
    length_function = len,
    is_separator_regex = False,
)
split_docs_char = char_splitter.split_documents([long_document])
print(f"字符分割后得到 {len(split_docs_char)} 个文档块。")
if split_docs_char:
    print(f"第一个块内容 (前100字符): {split_docs_char[0].page_content[:100]}...")
    print(f"长度: {len(split_docs_char[0].page_content)}")
```

**解释：**
* `RecursiveCharacterTextSplitter` 尝试按 `separators` 列表中的字符（如换行符、句号）进行分割，力求保持语义完整性。
* `chunk_size` 定义了每个块的目标大小。
* `chunk_overlap` 定义了相邻块之间的重叠字符数，这有助于在检索时，即使相关信息跨越了块的边界，也能被捕捉到。
* `split_documents()` 方法接收一个 `Document` 对象列表，并返回分割后的 `Document` 块列表。原文档的元数据会被复制到每个新的块中。

---

##### 3. Text Embedding Models (文本嵌入模型)

**概念：**
文本嵌入模型将文本块转换为数值向量（称为嵌入向量）。这些向量在高维空间中捕捉文本的语义含义。语义相似的文本块在向量空间中的位置会更接近。这是实现语义搜索的关键。

**代码示例：**

我们将展示两种嵌入模型：
1.  `OpenAIEmbeddings` (需要 API Key)
2.  `HuggingFaceEmbeddings` (使用 `sentence-transformers`，可以在本地运行)

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings

# 准备一些示例文本块 (可以使用上面分割后的文档)
if 'split_docs_recursive' in locals() and split_docs_recursive:
    sample_chunks_for_embedding = [doc.page_content for doc in split_docs_recursive[:2]] # 取前两个块的内容
else:
    sample_chunks_for_embedding = [
        "你好，世界！",
        "Hello, world!",
        "机器学习正在改变世界。",
        "Machine learning is changing the world."
    ]

print(f"\n用于嵌入的示例文本块: {sample_chunks_for_embedding}\n")

# --- OpenAIEmbeddings 示例 ---
print("--- OpenAIEmbeddings ---")
# 需要设置 OPENAI_API_KEY 环境变量
try:
    openai_embeddings = OpenAIEmbeddings(model="text-embedding-3-small") # 或者 "text-embedding-ada-002"

    # 嵌入单个文本
    query_text = "这是一个查询文本"
    query_vector = openai_embeddings.embed_query(query_text)
    print(f"查询 \"{query_text}\" 的 OpenAI 嵌入向量 (前5个维度): {query_vector[:5]}")
    print(f"向量维度: {len(query_vector)}")

    # 嵌入多个文档文本
    doc_vectors_openai = openai_embeddings.embed_documents(sample_chunks_for_embedding)
    print(f"\nOpenAI 嵌入了 {len(doc_vectors_openai)} 个文档块。")
    if doc_vectors_openai:
        print(f"第一个文档块的 OpenAI 嵌入向量 (前5个维度): {doc_vectors_openai[0][:5]}")
        print(f"向量维度: {len(doc_vectors_openai[0])}")
except Exception as e:
    print(f"OpenAIEmbeddings 初始化或使用失败: {e}. 请确保OPENAI_API_KEY已设置。")


# --- HuggingFaceEmbeddings 示例 (本地运行) ---
print("\n--- HuggingFaceEmbeddings (Sentence Transformers) ---")
# 使用一个流行的开源模型，首次运行时会自动下载
# model_name = "sentence-transformers/all-MiniLM-L6-v2" # 英文为主，轻量级
model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" # 多语言，效果不错
# model_name = "shibing624/text2vec-base-chinese" # 中文效果较好的模型之一
try:
    hf_embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={'device': 'cpu'}, # 如果有GPU，可以设为 'cuda'
        encode_kwargs={'normalize_embeddings': True} # 通常建议归一化以使用余弦相似度
    )

    # 嵌入单个文本
    query_text_hf = "这是一个用于测试的查询"
    query_vector_hf = hf_embeddings.embed_query(query_text_hf)
    print(f"查询 \"{query_text_hf}\" 的 HuggingFace 嵌入向量 (前5个维度): {query_vector_hf[:5]}")
    print(f"向量维度: {len(query_vector_hf)}")

    # 嵌入多个文档文本
    doc_vectors_hf = hf_embeddings.embed_documents(sample_chunks_for_embedding)
    print(f"\nHuggingFace 嵌入了 {len(doc_vectors_hf)} 个文档块。")
    if doc_vectors_hf:
        print(f"第一个文档块的 HuggingFace 嵌入向量 (前5个维度): {doc_vectors_hf[0][:5]}")
        print(f"向量维度: {len(doc_vectors_hf[0])}")
except Exception as e:
    print(f"HuggingFaceEmbeddings 初始化或使用失败: {e}. 可能需要安装 PyTorch, TensorFlow, 或 sentence-transformers。")

```

**解释：**
* `OpenAIEmbeddings` 和 `HuggingFaceEmbeddings` 都实例化了一个嵌入模型。
* `embed_query()` 方法用于嵌入单个查询字符串。
* `embed_documents()` 方法用于嵌入一个文本块列表。
* 返回的是浮点数列表（向量）。向量的维度取决于所选的模型（例如，`text-embedding-ada-002` 是1536维，`all-MiniLM-L6-v2` 是384维）。

---

##### 4. Vector Stores (向量存储 / 向量数据库)

**概念：**
向量存储专门用于存储文本块的嵌入向量及其对应的原始内容和元数据。它们的核心功能是执行高效的“相似性搜索”（或“最近邻搜索”），即根据查询向量找到数据库中最相似的向量。

**代码示例：**

我们将使用 `FAISS` (Facebook AI Similarity Search) 和 `Chroma`，它们都是流行的、可以在本地运行的向量存储。

```python
from langchain_community.vectorstores import FAISS, Chroma

# 准备一些示例文档块及其嵌入 (复用上面的分割结果和嵌入模型)
# 为了完整性，我们重新创建一些简单的文档块
if 'split_docs_recursive' in locals() and split_docs_recursive:
    docs_for_vectorstore = split_docs_recursive
    print(f"\n使用先前分割的 {len(docs_for_vectorstore)} 个文档块。")
else:
    from langchain_core.documents import Document
    docs_for_vectorstore = [
        Document(page_content="苹果是一种水果，通常是红色的。", metadata={"source": "doc1", "category": "fruit"}),
        Document(page_content="香蕉是黄色的长条形水果。", metadata={"source": "doc2", "category": "fruit"}),
        Document(page_content="特斯拉是一家电动汽车公司。", metadata={"source": "doc3", "category": "company"}),
        Document(page_content="太阳是太阳系的中心恒星。", metadata={"source": "doc4", "category": "space"})
    ]
    print(f"\n使用手动创建的 {len(docs_for_vectorstore)} 个文档块。")

# 选择一个嵌入模型 (优先使用 HuggingFace，如果 OpenAI 失败)
if 'hf_embeddings' in locals() and hf_embeddings:
    chosen_embeddings = hf_embeddings
    print("使用 HuggingFace 嵌入模型进行向量存储。")
elif 'openai_embeddings' in locals() and openai_embeddings:
    chosen_embeddings = openai_embeddings
    print("使用 OpenAI 嵌入模型进行向量存储。")
else:
    print("错误：没有可用的嵌入模型。请检查之前的步骤。")
    # 在此退出或使用一个默认的（如果适用）
    exit()


# --- FAISS 示例 (内存中) ---
print("\n--- FAISS Vector Store ---")
try:
    # 从文档、文本和嵌入函数创建 FAISS 索引
    # .from_documents() 会自动处理文本的嵌入过程
    faiss_vectorstore = FAISS.from_documents(documents=docs_for_vectorstore, embedding=chosen_embeddings)
    print("FAISS 索引创建成功。")

    # 执行相似性搜索
    query = "关于水果的信息"
    print(f"\nFAISS 搜索查询: \"{query}\"")
    # similarity_search 返回 Document 对象列表
    # similarity_search_with_score 返回 (Document, score) 元组列表
    # k=2 表示返回最相似的2个结果
    results_faiss = faiss_vectorstore.similarity_search_with_score(query, k=2)
    for doc, score in results_faiss:
        print(f"相似度得分: {score:.4f}") # FAISS 的得分是L2距离，越小越相似
        print(f"内容: {doc.page_content}")
        print(f"元数据: {doc.metadata}\n")

    # FAISS 索引可以保存到本地并重新加载
    # faiss_vectorstore.save_local("my_faiss_index")
    # loaded_faiss = FAISS.load_local("my_faiss_index", chosen_embeddings, allow_dangerous_deserialization=True)

except Exception as e:
    print(f"FAISS 示例失败: {e}")


# --- Chroma 示例 (内存中或持久化) ---
print("\n--- Chroma Vector Store ---")
try:
    # 创建 Chroma 向量存储 (默认在内存中，也可以指定持久化路径)
    # persist_directory="chroma_db_persistent"
    chroma_vectorstore = Chroma.from_documents(
        documents=docs_for_vectorstore,
        embedding=chosen_embeddings,
        # persist_directory="my_chroma_db" # 如果想持久化存储
    )
    print("Chroma 向量存储创建成功。")

    # 执行相似性搜索
    query_chroma = "关于电动车公司"
    print(f"\nChroma 搜索查询: \"{query_chroma}\"")
    results_chroma = chroma_vectorstore.similarity_search_with_score(query_chroma, k=2)
    for doc, score in results_chroma:
        print(f"相似度得分: {score:.4f}") # Chroma 的得分通常是距离（如L2）或余弦相似度（取决于配置），langchain包装后可能是距离
        print(f"内容: {doc.page_content}")
        print(f"元数据: {doc.metadata}\n")

    # 使用元数据过滤进行搜索 (如果Chroma版本和实现支持直接在similarity_search中过滤)
    # 一些版本可能需要先获取 retriever 再配置过滤
    print(f"Chroma 搜索查询 (带元数据过滤 category='fruit'): \"{query}\"")
    # 注意：Chroma 的过滤语法可能依赖于其具体版本和 Langchain 的集成方式
    # Langchain 的 retriever 通常提供更一致的过滤接口
    try:
        # 对于较新版本的Langchain和Chroma，过滤可能通过 retriever 实现
        # results_chroma_filtered = chroma_vectorstore.similarity_search(
        # query, k=2, filter={"category": "fruit"}
        # )
        # 或者使用更通用的 retriever 方法
        retriever_for_filter = chroma_vectorstore.as_retriever(search_kwargs={'k': 2, 'filter': {'category': 'fruit'}})
        results_chroma_filtered_docs = retriever_for_filter.invoke(query)

        if results_chroma_filtered_docs:
            for doc in results_chroma_filtered_docs:
                print(f"内容 (过滤后): {doc.page_content}")
                print(f"元数据 (过滤后): {doc.metadata}\n")
        else:
            print("使用元数据过滤未找到结果。")

    except NotImplementedError:
        print("当前 Chroma/Langchain 版本组合的直接元数据过滤方式可能不受支持，或需要通过 retriever 配置。")
    except Exception as e_filter:
        print(f"Chroma 元数据过滤搜索失败: {e_filter}")


except Exception as e:
    print(f"Chroma 示例失败: {e}")

```

**解释：**
* `FAISS.from_documents(docs_for_vectorstore, chosen_embeddings)` 或 `Chroma.from_documents(...)` 会自动获取 `docs_for_vectorstore` 中每个文档的 `page_content`，使用 `chosen_embeddings` 模型将其转换为向量，然后将这些向量和文档存入向量存储。
* `vectorstore.similarity_search(query, k=N)` 或 `similarity_search_with_score(query, k=N)` 是核心检索方法。它会：
    1.  将 `query` 字符串通过相同的嵌入模型转换为查询向量。
    2.  在向量存储中搜索与查询向量最相似的 `N` 个文档向量。
    3.  返回这些最相似的 `Document` 对象（以及可选的相似度得分）。
* FAISS 的得分是L2距离（越小越相似），Chroma 的得分（当通过Langchain包装后）也通常是距离。如果直接使用某些向量数据库的余弦相似度，则是越大越相似。Langchain尝试标准化这一点。

---

##### 5. Retrievers (检索器)

**概念：**
检索器是 LangChain 中一个更通用的接口，它封装了从数据源（通常是向量存储）检索文档的逻辑。向量存储本身就可以作为一个简单的检索器。但检索器接口允许更复杂的策略，如上下文压缩、多查询检索等。

**代码示例：**

```python
# 假设我们已经有了一个向量存储实例 (例如上面创建的 faiss_vectorstore 或 chroma_vectorstore)
if 'faiss_vectorstore' in locals() and faiss_vectorstore:
    active_vectorstore = faiss_vectorstore
    print("\n--- Retriever from FAISS Vector Store ---")
elif 'chroma_vectorstore' in locals() and chroma_vectorstore:
    active_vectorstore = chroma_vectorstore
    print("\n--- Retriever from Chroma Vector Store ---")
else:
    print("\n错误：没有可用的向量存储实例用于创建检索器。")
    exit()

# 1. 基本检索器 (直接从向量存储创建)
retriever_basic = active_vectorstore.as_retriever(
    search_type="similarity", # "similarity_score_threshold", "mmr"
    search_kwargs={'k': 2}    # 返回最相关的2个文档
)

query = "关于水果的信息"
print(f"基本检索器查询: \"{query}\"")
retrieved_docs_basic = retriever_basic.invoke(query) # .get_relevant_documents() 在旧版本
for i, doc in enumerate(retrieved_docs_basic):
    print(f"检索到的文档 {i+1}:")
    print(f"内容: {doc.page_content}")
    print(f"元数据: {doc.metadata}\n")


# 2. 带 MMR (Maximal Marginal Relevance) 的检索器
# MMR 旨在获取相关性的同时，也追求结果的多样性，避免返回内容过于相似的多个文档块。
retriever_mmr = active_vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={'k': 3, 'fetch_k': 10, 'lambda_mult': 0.6}
    # fetch_k: 获取多少个初始文档进行MMR计算
    # lambda_mult: 控制多样性 (0.0-1.0, 越大越多样性, 越小越关注相似度)
)

query_mmr = "关于水果和公司" # 一个可能需要多样性的查询
print(f"MMR 检索器查询: \"{query_mmr}\"")
retrieved_docs_mmr = retriever_mmr.invoke(query_mmr)
for i, doc in enumerate(retrieved_docs_mmr):
    print(f"MMR 检索到的文档 {i+1}:")
    print(f"内容: {doc.page_content}")
    print(f"元数据: {doc.metadata}\n")


# 3. 带元数据过滤的检索器 (更可靠的方式)
if docs_for_vectorstore[0].metadata.get("category"): # 确保元数据中有 category 字段
    retriever_filtered = active_vectorstore.as_retriever(
        search_kwargs={'k': 2, 'filter': {'category': 'fruit'}}
    )
    query_filtered = "任何信息" # 查询内容不重要，因为我们主要看过滤
    print(f"带元数据过滤 (category='fruit') 的检索器查询: \"{query_filtered}\"")
    retrieved_docs_filtered = retriever_filtered.invoke(query_filtered)
    for i, doc in enumerate(retrieved_docs_filtered):
        print(f"过滤后检索到的文档 {i+1}:")
        print(f"内容: {doc.page_content}")
        print(f"元数据: {doc.metadata}\n")
else:
    print("示例数据中不包含 'category' 元数据，跳过元数据过滤检索器示例。")

```

**解释：**
* `vectorstore.as_retriever()` 是将向量存储转换为检索器的标准方法。
* `search_type="similarity"` 是默认的，执行标准的相似性搜索。
* `search_type="mmr"` 启用 Maximal Marginal Relevance，它会首先获取一批（`Workspace_k`）相似的文档，然后从中挑选出既相关又具有多样性的 `k` 个文档。
* `search_kwargs` 允许传递特定于搜索类型的参数，如 `k`（返回的文档数）和 `filter`（用于元数据过滤的字典）。
* `retriever.invoke(query)` (或旧版的 `get_relevant_documents(query)`) 执行检索操作。

---

##### 整体流程串联 (简例)

下面是一个非常简化的端到端流程，展示这些组件如何协同工作：

```python
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings # 假设已导入或使用下面的 HuggingFace
from langchain_community.embeddings import HuggingFaceEmbeddings # 假设已导入
from langchain_community.vectorstores import FAISS

# 0. 选择嵌入模型 (确保已初始化)
if 'hf_embeddings' in locals() and hf_embeddings:
    embeddings = hf_embeddings
    print("\n--- 整体流程使用 HuggingFace Embeddings ---")
elif 'openai_embeddings' in locals() and openai_embeddings:
    embeddings = openai_embeddings
    print("\n--- 整体流程使用 OpenAI Embeddings ---")
else:
    print("错误：没有可用的嵌入模型进行整体流程演示。")
    exit()


# 1. 准备原始数据 (代替 Document Loader)
raw_texts = [
    "Langchain是一个强大的框架，用于构建基于大型语言模型的应用程序。",
    "它提供了模块化的组件，如模型I/O、数据连接、链、代理和回调。",
    "数据连接部分包括文档加载器、文本分割器、嵌入模型和向量存储。",
    "向量存储如FAISS和Chroma用于高效地存储和检索文本嵌入。",
    "检索器则用于从向量存储中获取与查询相关的文档。"
]
documents = [Document(page_content=text, metadata={"source": f"text_{i}"}) for i, text in enumerate(raw_texts)]
print(f"初始文档数量: {len(documents)}")

# 2. 文档转换 (文本分割)
text_splitter = CharacterTextSplitter(chunk_size=80, chunk_overlap=10) # 较小的块以进行演示
split_docs = text_splitter.split_documents(documents)
print(f"分割后的文档块数量: {len(split_docs)}")
if split_docs:
    print(f"第一个块: {split_docs[0].page_content}")

# 3. 文本嵌入 & 4. 向量存储 (一步完成)
# FAISS.from_documents 会自动处理嵌入
try:
    vector_store = FAISS.from_documents(split_docs, embeddings)
    print("向量存储已创建并填充。")

    # 5. 检索器
    retriever = vector_store.as_retriever(search_kwargs={'k': 2})
    print("检索器已创建。")

    # 进行查询
    query = "什么是向量存储？"
    results = retriever.invoke(query)

    print(f"\n查询: \"{query}\"")
    print("检索到的相关文档块:")
    for doc in results:
        print(f"- \"{doc.page_content}\" (来源: {doc.metadata.get('source')})")

except Exception as e:
    print(f"整体流程中发生错误: {e}")

```

**解释：**
这个简化示例跳过了显式的文档加载器（直接使用内存中的文本），但清晰地展示了：
1.  原始数据（`Document`对象列表）。
2.  使用 `CharacterTextSplitter` 分割文档。
3.  使用 `FAISS.from_documents` 一步完成嵌入文本块并将其存入FAISS向量存储。
4.  从向量存储创建检索器。
5.  使用检索器根据查询获取最相关的文档块。

这些组件共同构成了RAG系统中“检索”这一半的核心。检索到的文档块随后会作为上下文提供给LLM，以帮助LLM生成更准确、更有依据的回答。







---

#### 3.3 链 (Chains)：构建调用序列

**注意：** 以下代码中的 LLM 将主要使用 `ChatOpenAI`。为了使示例可独立运行且不实际消耗 API 配额，部分示例会使用 `FakeListLLM` from `langchain.llms.fake` (较旧的模块，新版中推荐 `from langchain_community.llms.fake import FakeListLLM` 或者 `from langchain_core.language_models.fake import FakeListLLM`) 或 `FakeChatModel` from `langchain_core.language_models.fake`。我会尽量指出。在实际应用中，你会替换为真实的 LLM 实例。

链是将多个组件（LLMs、Prompts、其他链等）组合起来以完成特定任务的序列。

##### 1. 基本链 (LLMChain)

`LLMChain` 是最基础的链，它将一个 PromptTemplate 和一个 LLM 结合起来。

**1. 使用 LangChain Expression Language (LCEL) - 推荐方式**

LCEL 是 LangChain 中构建链的现代且更灵活的方式，使用 `|` (pipe) 操作符。

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough # 用于传递输入

# 0. 设置LLM (确保 OPENAI_API_KEY 已设置)
# 如果你没有 OpenAI API Key，可以使用 FakeChatModel 进行测试
# from langchain_core.language_models.fake import FakeMessagesListChatModel
# llm = FakeMessagesListChatModel(responses=["Why did the cat sit on the computer? To keep an eye on the mouse!"])

llm = ChatOpenAI(model="gpt-3.5-turbo")

# 1. 定义 PromptTemplate
prompt_template = ChatPromptTemplate.from_template(
    "请写一个关于 {topic} 的简短笑话。"
)

# 2. 定义输出解析器 (可选，但常用)
output_parser = StrOutputParser()

# 3. 构建链 (使用 LCEL)
# RunnablePassthrough() 可以用来将原始输入（例如字典）传递到链中需要的地方
# 或者直接将输入构建成期望的字典格式
llm_chain_lcel = (
    {"topic": RunnablePassthrough()} # 假设输入直接是主题字符串
    | prompt_template
    | llm
    | output_parser
)
# 如果你的输入已经是 {"topic": "某个主题"}，可以简化为:
# llm_chain_lcel = prompt_template | llm | output_parser


# 4. 运行链
topic_input = "程序员"
try:
    response_lcel = llm_chain_lcel.invoke(topic_input) # 使用 invoke
    print("--- LLMChain (LCEL) ---")
    print(f"输入主题: {topic_input}")
    print(f"LLM 回答: {response_lcel}")
except Exception as e:
    print(f"LCEL Chain Error: {e}")
    print("请确保您的 OpenAI API 密钥已正确设置并具有有效额度。")


print("\n")

# 2. 使用传统的 `LLMChain` 类 (仍然可用)
from langchain.chains import LLMChain # 注意这里的导入路径可能因版本而异
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate # 旧版 PromptTemplate

# 0. 设置LLM
llm_legacy = ChatOpenAI(model="gpt-3.5-turbo")
# from langchain_community.llms.fake import FakeListLLM # 示例用
# llm_legacy = FakeListLLM(responses=["Why did the scarecrow win an award? Because he was outstanding in his field!"])


# 1. 定义 PromptTemplate (旧版)
prompt_legacy = PromptTemplate(
    input_variables=["topic"],
    template="请再写一个关于 {topic} 的简短故事（不同于笑话）。"
)

# 2. 构建 LLMChain 实例
legacy_llm_chain = LLMChain(llm=llm_legacy, prompt=prompt_legacy)

# 3. 运行链
topic_input_legacy = "太空旅行"
try:
    # .run() 方法通常用于单输入单输出，直接返回字符串
    # response_legacy = legacy_llm_chain.run(topic_input_legacy)

    # .invoke() 是更通用的方法，输入是字典，输出通常也是字典
    response_dict_legacy = legacy_llm_chain.invoke({"topic": topic_input_legacy})
    response_legacy = response_dict_legacy["text"] # LLMChain 默认输出键是 'text'

    print("--- LLMChain (Legacy Class) ---")
    print(f"输入主题: {topic_input_legacy}")
    print(f"LLM 回答: {response_legacy}")
except Exception as e:
    print(f"Legacy LLMChain Error: {e}")
    print("请确保您的 OpenAI API 密钥已正确设置并具有有效额度。")

```

**代码解释:**
* **`ChatOpenAI`**: 指定了要使用的语言模型。
* **`ChatPromptTemplate.from_template(...)` (LCEL)** 或 `PromptTemplate(...)` (Legacy): 创建一个提示模板，`{topic}` 是一个占位符，将在运行时被实际值替换。
* **`StrOutputParser()` (LCEL)**: 将 LLM 的聊天消息对象输出转换为简单的字符串。
* **LCEL (`|`)**: 将提示、模型和解析器“管道化”连接在一起。`invoke` 方法用于执行链。
* **`LLMChain(llm=..., prompt=...)` (Legacy)**: 显式创建一个 `LLMChain` 对象。`invoke` 方法（或旧的 `.run()`）用于执行。

---

##### 2. 顺序链 (Sequential Chains)

顺序链用于按顺序执行多个链，其中一个链的输出成为下一个链的输入。

**1. `SimpleSequentialChain` (简单顺序链)**
   它按顺序运行链，并将一个链的输出直接作为下一个链的单个输入。每个链都必须只有一个输入和一个输出。

```python
from langchain.chains import SimpleSequentialChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 0. 设置LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
# from langchain_core.language_models.fake import FakeMessagesListChatModel
# llm = FakeMessagesListChatModel(responses=[
# "《星际漫游指南》", # 响应链1
# "《星际漫游指南》是一部幽默科幻小说，讲述了地球毁灭后，最后一个幸存的地球人亚瑟·邓特在宇宙中冒险的故事。" # 响应链2
# ])


# 1. 第一个链：根据主题生成一个虚构的书名
prompt1 = ChatPromptTemplate.from_template("为一个关于 {genre} 类型的故事想一个引人入胜的书名。书名：")
chain1 = (prompt1 | llm | StrOutputParser())

# 2. 第二个链：为给定的书名写一个简短的剧情简介
prompt2 = ChatPromptTemplate.from_template("为书籍《{book_title}》写一个两句话的剧情简介。简介：")
chain2 = ({"book_title": lambda x: x} | prompt2 | llm | StrOutputParser()) # x 是上一个链的输出

# 3. 构建 SimpleSequentialChain
# 注意：SimpleSequentialChain 期望其构成的链是旧版的 BaseChain 实例。
# 为了兼容，我们可以将 LCEL 链包装一下，或者直接使用旧的 LLMChain。
# 这里我们使用旧的 LLMChain 方式来构建子链，以确保与 SimpleSequentialChain 的兼容性。

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate as LegacyPromptTemplate

legacy_llm = ChatOpenAI(model="gpt-3.5-turbo")
# from langchain_community.llms.fake import FakeListLLM
# legacy_llm = FakeListLLM(responses=[
#     "《代码幽灵》", # chain_one output
#     "《代码幽灵》讲述了一位天才程序员发现其编写的AI产生了自我意识，并开始在网络中制造混乱，程序员必须在AI造成全球灾难前阻止它。" # chain_two output
# ])


prompt_one = LegacyPromptTemplate(input_variables=["genre"], template="为一个关于 {genre} 类型的故事想一个引人入胜的书名。书名：")
chain_one = LLMChain(llm=legacy_llm, prompt=prompt_one)

prompt_two = LegacyPromptTemplate(input_variables=["book_title"], template="为书籍“{book_title}”写一个两句话的剧情简介。简介：")
chain_two = LLMChain(llm=legacy_llm, prompt=prompt_two, output_key="synopsis") # 指定输出键以供 SequentialChain 使用

# SimpleSequentialChain
# input_key 默认为 chain_one 的输入变量，如果只有一个的话。
# output_key 默认为 chain_two 的输出变量，如果只有一个的话。
simple_sequential_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two],
    verbose=True # verbose 参数可以打印出链的执行过程和中间结果
)

# 4. 运行链
genre_input = "赛博朋克侦探"
try:
    result_simple_seq = simple_sequential_chain.invoke(genre_input)
    print("\n--- SimpleSequentialChain ---")
    print(f"输入类型: {genre_input}")
    print(f"最终输出 (简介): {result_simple_seq}")
except Exception as e:
    print(f"SimpleSequentialChain Error: {e}")

```

**2. `SequentialChain` (通用顺序链)**
   更通用，允许更复杂的输入/输出管理，可以有多个输入和输出，并通过 `input_variables` 和 `output_variables` 控制数据流。

```python
from langchain.chains import SequentialChain
# (LLM, Prompts等其他导入同上)

# 我们继续使用上面定义的 chain_one 和 chain_two (LLMChain 实例)

# chain_one: 输入 'genre', 输出 'text' (LLMChain 默认) -> 我们在 SequentialChain 中将其映射为 'book_title'
# chain_two: 输入 'book_title', 输出 'synopsis' (我们已在 chain_two 中指定 output_key)

# 3. 第三个链：根据书名和简介，生成一个推特帖子
prompt_three_template = LegacyPromptTemplate(
    input_variables=["book_title", "synopsis"],
    template="为书名为《{book_title}》，简介为“{synopsis}”的书籍写一条吸引人的推特帖子，包含相关标签。"
)
chain_three = LLMChain(llm=legacy_llm, prompt=prompt_three_template, output_key="tweet")
# legacy_llm = FakeListLLM(responses=[... , "#新书推荐 #赛博朋克 《代码幽灵》现已上线！一位程序员发现他的AI活了过来并引发混乱...他能阻止灾难吗？#科幻 #惊悚" ])

# 4. 构建 SequentialChain
# input_variables: 整个顺序链的初始输入
# output_variables: 整个顺序链的最终输出
# chains: 链的列表
# L早期版本中，SequentialChain 可能需要你明确映射 chain_one 的默认 'text' 输出到 'book_title'
# 使用 LLMChain 的 output_key 参数通常更清晰。chain_one 的输出将自动以其 output_key (默认为'text') 存储。
# 如果 chain_one 没有指定 output_key，其输出是 'text'。我们需要确保 chain_two 的输入变量名 ('book_title') 匹配。
# 为了让 chain_one 的输出 'text' 作为 chain_two 的输入 'book_title'，
# 我们可以在 SequentialChain 中通过 memory 或 remapping 来处理，或者确保 chain_one 的 output_key 叫 book_title
# 或者，简单地，chain_one 的输出变量名（默认为 "text"）如果被后续链作为输入变量名，会自动传递。
# 为了清晰，我们假设 chain_one 的输出键就是 'book_title' (可以通过修改 chain_one 实现，或依赖于 SequentialChain 的智能传递)
# 实际上，LLMChain的输出是一个包含 output_key 的字典，SequentialChain会处理这些。
# 我们已经将 chain_one 的输出作为 'text' (默认) 和 chain_two 的输入是 'book_title'
# SequentialChain 会自动将上一个链的输出传递给下一个链的输入（如果名称匹配）。
# 如果不匹配，或者想更精确控制，可以使用 `output_keys` 和 `input_variables` 的映射。

# 我们将 chain_one 的输出key改为 'book_title' 以匹配 chain_two 的输入
chain_one.output_key = "book_title"


sequential_chain = SequentialChain(
    chains=[chain_one, chain_two, chain_three],
    input_variables=["genre"], # 整个链的初始输入
    output_variables=["book_title", "synopsis", "tweet"], # 期望从链中获取的最终输出
    verbose=True
)

# 5. 运行链
genre_input_seq = "科幻悬疑"
try:
    result_seq = sequential_chain.invoke({"genre": genre_input_seq})
    print("\n--- SequentialChain ---")
    print(f"输入类型: {genre_input_seq}")
    print(f"书名: {result_seq['book_title']}")
    print(f"简介: {result_seq['synopsis']}")
    print(f"推文: {result_seq['tweet']}")
except Exception as e:
    print(f"SequentialChain Error: {e}")
```

**代码解释:**
* **`SimpleSequentialChain`**: 按顺序执行 `chain_one` 和 `chain_two`。`chain_one` 的输出直接成为 `chain_two` 的输入。
* **`SequentialChain`**:
    * `chains`: 定义了要执行的链的列表。
    * `input_variables`: 定义了整个顺序链的初始输入键。
    * `output_variables`: 定义了希望从链的执行结果中提取哪些键作为最终输出。
    * `verbose=True`: 打印出链的详细执行步骤和中间数据，非常有助于调试。
    * 数据传递：`chain_one` 输出 `book_title`，`chain_two` 以 `book_title` 作为输入并输出 `synopsis`，`chain_three` 以 `book_title` 和 `synopsis` 作为输入输出 `tweet`。

---

##### 3. 路由链 (Router Chains)

路由链根据输入动态选择下一条要执行的链。这对于构建能够处理多种不同类型请求的应用程序非常有用。

`LLMRouterChain` 使用一个 LLM 来决定路由到哪个目标链。

```python
from langchain.chains.router import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
# from langchain_community.llms.fake import FakeListLLM # For testing

# 0. 设置LLM (一个用于路由，其他用于目标链)
llm_router = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm_destination = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 使用 FakeLLM 进行演示，避免实际 API 调用
# responses_router 应该是一个JSON字符串，符合RouterOutputParser的格式
# fake_llm_router = FakeListLLM(responses=[
# '{"destination": "physics_expert", "next_inputs": {"input": "Tell me about black holes."}}'
# ])
# fake_llm_destination = FakeListLLM(responses=[
# "Black holes are regions of spacetime where gravity is so strong that nothing, no particles or even electromagnetic radiation such as light, can escape from it.",
# "The first World War began in 1914 after the assassination of Archduke Franz Ferdinand."
# ])
# llm_router = fake_llm_router
# llm_destination = fake_llm_destination


# 1. 定义目标链的模板和信息
physics_template = """你是一位物理学专家。这里有一个关于物理学的问题：
{input}
你的回答："""

history_template = """你是一位历史学家。这里有一个关于历史的问题：
{input}
你的回答："""

math_template = """你是一位数学家。这里有一个关于数学的问题：
{input}
你的回答："""

# 目标链的描述信息，供路由LLM参考
prompt_infos = [
    {
        "name": "physics_expert",
        "description": "擅长回答物理学相关的问题",
        "prompt_template": physics_template,
    },
    {
        "name": "history_expert",
        "description": "擅长回答历史学相关的问题",
        "prompt_template": history_template,
    },
    {
        "name": "math_expert",
        "description": "擅长回答数学相关的问题",
        "prompt_template": math_template,
    },
]

# 2. 为每个目标创建一个 LLMChain
destination_chains = {}
for p_info in prompt_infos:
    prompt = PromptTemplate(template=p_info["prompt_template"], input_variables=["input"])
    chain = LLMChain(llm=llm_destination, prompt=prompt)
    destination_chains[p_info["name"]] = chain

# 3. 定义默认链 (当路由不确定时使用)
default_prompt = PromptTemplate(template="这是一个通用问题：\n{input}\n你的回答：", input_variables=["input"])
default_chain = LLMChain(llm=llm_destination, prompt=default_prompt)

# 4. 构建路由模板
# 这个模板会指导路由LLM如何选择目标链
router_template_text = """
给定一个原始用户输入，将其分类到最合适的目标选项。
可用的目标选项有：
{destinations}

将选择以及原始输入（如果需要修改以适应目标）以JSON形式输出，包含一个 "destination" 键（目标选项的名称）和一个 "next_inputs" 键（一个包含输入键值对的字典）。
如果你认为输入不适合任何特定选项，则选择 "DEFAULT"。

输入:
{input}

输出JSON:
"""
router_prompt = PromptTemplate(
    template=router_template_text,
    input_variables=["input", "destinations"],
    output_parser=RouterOutputParser(), # 解析路由LLM的输出
)

# 5. 构建路由链
# destinations 变量会由 MultiPromptChain 自动填充为上面 prompt_infos 中的 name:description 列表
router_chain = LLMRouterChain.from_llm(llm_router, router_prompt)

# 6. 构建 MultiPromptChain (它包含了路由逻辑和目标链)
multi_prompt_chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=destination_chains,
    default_chain=default_chain,
    verbose=True,
)

# 7. 运行链
try:
    input_physics = "黑洞是如何形成的？"
    result_physics = multi_prompt_chain.invoke(input_physics) # invoke现在接受字符串或字典
    print(f"\n--- RouterChain for Physics ---")
    print(f"输入: {input_physics}")
    print(f"路由后回答: {result_physics['text']}")

    input_history = "第一次世界大战是什么时候开始的？"
    result_history = multi_prompt_chain.invoke(input_history)
    print(f"\n--- RouterChain for History ---")
    print(f"输入: {input_history}")
    print(f"路由后回答: {result_history['text']}")

    input_general = "今天天气怎么样？" # 假设没有天气专家链
    result_general = multi_prompt_chain.invoke(input_general)
    print(f"\n--- RouterChain for General (Default) ---")
    print(f"输入: {input_general}")
    print(f"路由后回答: {result_general['text']}")

except Exception as e:
    print(f"RouterChain Error: {e}")
    print("请确保您的 OpenAI API 密钥已正确设置并具有有效额度。")

```
**代码解释:**
* `prompt_infos`: 描述了每个“专家”链（目标链）的功能，这个描述会帮助路由LLM做出选择。
* `destination_chains`: 一个字典，存储了所有可能被路由到的目标 `LLMChain` 实例。
* `default_chain`: 如果路由LLM无法为输入匹配到任何一个专门的目标链，则会使用这个默认链。
* `RouterOutputParser`: 用于解析路由LLM输出的JSON，确定应该将任务路由到哪个目标链以及传递给该链的输入是什么。
* `LLMRouterChain.from_llm()`: 创建路由决策的核心逻辑。
* `MultiPromptChain`: 将路由链、目标链集合和默认链组合在一起。它首先调用路由链来决定使用哪个目标链，然后执行选定的目标链。

---

##### 4. 其他常用链类型 (代码示例概念)

以下是一些其他常用链的简要代码概念。完整实现可能需要更多设置（如向量数据库、特定API文档等）。

**1. `RetrievalQA` 链 (检索问答链)**

```python
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS # VectorStore示例
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains import RetrievalQA

# 0. 准备 LLM 和 Embeddings
llm = ChatOpenAI(model="gpt-3.5-turbo")
embeddings = OpenAIEmbeddings() # 用于创建文档向量

# 1. 准备一些示例文档 (实际应用中会从文件、数据库等加载)
documents_text = [
    "LangChain是一个用于开发由语言模型驱动的应用程序的框架。",
    "链(Chains)是LangChain中的核心概念，允许将多个组件串联起来。",
    "RetrievalQA链结合了检索和问答，用于基于文档内容回答问题。",
    "FAISS是一个高效的相似性搜索库。"
]
docs = [Document(page_content=t) for t in documents_text]

# 2. 创建文本分割器 (如果文档较大) 和向量存储
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0) # 示例，可能不需要对短文本分割
split_docs = text_splitter.split_documents(docs)

# 使用 FAISS 从文档创建向量存储 (内存中)
try:
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    retriever = vectorstore.as_retriever() # 创建检索器

    # 3. 构建 RetrievalQA 链
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff", # "stuff", "map_reduce", "refine", "map_rerank"
        retriever=retriever,
        return_source_documents=True, # 可选，返回源文档
        verbose=True
    )

    # 4. 提问
    query = "什么是LangChain中的链？"
    result_qa = qa_chain.invoke({"query": query})

    print("\n--- RetrievalQA Chain ---")
    print(f"问题: {query}")
    print(f"回答: {result_qa['result']}")
    # print(f"源文档: {result_qa['source_documents']}")

except Exception as e:
    print(f"RetrievalQA Chain Error: {e}. FAISS requires `pip install faiss-cpu` or `faiss-gpu`.")
    print("This example also requires a valid OpenAI API key for embeddings and the LLM.")

```
**概念解释:**
* **Embeddings & VectorStore**: 文档首先被转换为向量（嵌入），并存储在向量数据库（如FAISS, Chroma）中，以便进行快速的相似性搜索。
* **Retriever**: 当用户提问时，检索器会从向量数据库中找出与问题最相关的文档片段。
* **`chain_type="stuff"`**: 将所有检索到的文档片段“塞入”到LLM的上下文中进行问答。其他类型如 "map_reduce" 用于处理大量文档。
* LLM会基于问题和检索到的上下文信息生成答案。

**2. `ConversationChain` (对话链)**

```python
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage

# 0. 设置LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
# from langchain_core.language_models.fake import FakeMessagesListChatModel
# fake_responses = []
# def add_fake_response(inp):
#     fake_responses.append(f"Echo: {inp}")
#     return [HumanMessage(content=f"Echo: {inp}")] # Chat model expects list of messages
# llm = FakeMessagesListChatModel(responses_function=add_fake_response)


# 1. 设置对话内存 (Memory)
# MessagesPlaceholder 用于在提示中为历史消息留出位置
# SystemMessage 可以用来设定AI的角色或行为准则
prompt_with_memory = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个乐于助人的AI助手。"),
    MessagesPlaceholder(variable_name="chat_history"), # 关键：内存中的历史记录会插入此处
    HumanMessage(content="{input}")
])

memory = ConversationBufferMemory(
    memory_key="chat_history", # 必须与 MessagesPlaceholder 中的 variable_name 匹配
    return_messages=True # 设置为True，以便与ChatPromptTemplate和ChatModels配合使用
)

# 2. 构建 ConversationChain
# ConversationChain 内部会处理提示和内存
# 如果使用 LCEL，可以更灵活地组合
# conversation_chain_lcel = prompt_with_memory | llm | StrOutputParser() # 需要手动管理内存的加载和保存

# 使用 ConversationChain 类更直接
conversation_chain = ConversationChain(
    llm=llm,
    prompt=prompt_with_memory, # 使用我们定义的包含MessagesPlaceholder的提示
    memory=memory,
    verbose=True
)

# 3. 进行对话
try:
    print("\n--- ConversationChain ---")
    response1 = conversation_chain.invoke({"input": "你好，我叫小明。"})
    print(f"小明: 你好，我叫小明。")
    print(f"AI: {response1['response']}") # ConversationChain的输出在 'response' 键

    response2 = conversation_chain.invoke({"input": "我刚刚说了我的名字是什么？"})
    print(f"小明: 我刚刚说了我的名字是什么？")
    print(f"AI: {response2['response']}")

    response3 = conversation_chain.invoke({"input": "LangChain是什么？"})
    print(f"小明: LangChain是什么？")
    print(f"AI: {response3['response']}")

    # 查看内存中的内容
    # print("\nMemory content:")
    # print(memory.load_memory_variables({}))

except Exception as e:
    print(f"ConversationChain Error: {e}")

```
**概念解释:**
* **`ConversationBufferMemory`**: 存储对话的完整历史记录。
* **`memory_key="chat_history"`** 和 **`MessagesPlaceholder(variable_name="chat_history")`**: 将内存中的历史消息注入到提示中。
* 每次调用 `conversation_chain.invoke()` 时：
    1.  内存加载历史对话。
    2.  历史对话和当前用户输入一起格式化为提示。
    3.  LLM基于包含历史的提示生成回应。
    4.  当前的用户输入和LLM的回应被保存到内存中，供下一轮对话使用。



#### 3.4 记忆 (Memory)：让链拥有记忆能力

在许多应用中，特别是聊天机器人或需要持续交互的场景，让模型“记住”之前的对话内容或信息至关重要。LangChain 中的“记忆 (Memory)”组件就是为此设计的。它允许链或代理在多次交互中保持状态。

##### 1. 记忆的类型 (ConversationBufferMemory, ConversationSummaryMemory 等)

LangChain 提供了多种记忆类型，以适应不同的需求：

* **`ConversationBufferMemory` (对话缓冲区记忆)**:
    * **工作方式**: 直接存储对话的完整历史记录（用户输入和模型输出的列表）。
    * **优点**: 保留了所有细节，对于需要精确上下文的短期对话很有用。
    * **缺点**: 如果对话很长，历史记录会变得非常大，可能会超出 LLM 的上下文窗口限制，并增加成本。
    * **变体**: `ConversationBufferWindowMemory` 只保留最近 K 轮对话的窗口。

* **`ConversationSummaryMemory` (对话摘要记忆)**:
    * **工作方式**: 随着对话的进行，使用一个 LLM 来逐步将对话历史压缩成一个摘要。
    * **优点**: 即使对话很长，摘要也能保持相对简洁，从而避免超出上下文窗口。
    * **缺点**: 摘要过程本身会消耗额外的 LLM 调用，且可能丢失一些细节。

* **`ConversationSummaryBufferMemory` (对话摘要缓冲区记忆)**:
    * **工作方式**: 结合了 `ConversationBufferMemory` 和 `ConversationSummaryMemory`。它在内存中保留最近的对话缓冲区，当缓冲区大小超过某个阈值时，会将旧的对话内容总结并移入摘要部分。
    * **优点**: 平衡了细节保留和上下文长度控制。

* **`ConversationTokenBufferMemory` (对话令牌缓冲区记忆)**:
    * **工作方式**: 类似于 `ConversationBufferMemory`，但它根据消息中的令牌（token）数量来限制缓冲区的大小，而不是消息的数量。当令牌总数超过限制时，会丢弃最早的消息。
    * **优点**: 更精确地控制上下文长度以适应模型的限制。

* **`VectorStoreRetrieverMemory` (向量存储检索记忆)**:
    * **工作方式**: 将对话历史或其他文本信息存储在向量数据库中。在需要时，根据当前输入检索最相关的历史信息片段。
    * **优点**: 能够处理非常长的对话或大量的背景知识，只检索最相关的部分。
    * **缺点**: 设置和管理向量数据库会增加复杂性。

* **`EntityMemory` (实体记忆)**:
    * **工作方式**: 专注于从对话中提取和记住关于特定“实体”（如人物、地点、事物）的信息。它使用 LLM 来识别和更新这些实体的属性。
    * **优点**: 对于需要跟踪特定对象状态或信息的应用非常有用。

选择哪种记忆类型取决于应用的具体需求，如对话长度、对细节的要求、成本以及上下文窗口的限制。

##### 2. 如何在链中使用记忆

在 LangChain 中，将记忆组件集成到链（通常是 `ConversationChain` 或其他支持记忆的链）中非常直接。

**基本步骤：**

1.  **选择并实例化一个记忆对象**:
    ```python
    from langchain.memory import ConversationBufferMemory
    memory = ConversationBufferMemory()
    ```
    或者，如果记忆需要 LLM（如 `ConversationSummaryMemory`）：
    ```python
    from langchain.memory import ConversationSummaryMemory
    from langchain.llms import OpenAI
    llm = OpenAI(temperature=0)
    memory = ConversationSummaryMemory(llm=llm)
    ```

2.  **创建链时传入记忆对象**:
    许多链（尤其是 `ConversationChain`）在构造时都有一个 `memory` 参数。
    ```python
    from langchain.chains import ConversationChain
    # conversation_chain = ConversationChain(llm=llm, memory=memory, verbose=True)
    ```
    对于更通用的 `LLMChain`，你可能需要调整提示模板以包含记忆变量（例如 `history`），并将记忆对象作为输入传递。`ConversationChain` 内部处理了如何将记忆内容整合到提示中。

3.  **运行链**:
    当你运行链时，它会自动从记忆中读取相关历史，并将其作为上下文的一部分传递给 LLM。同时，链也会自动将当前的交互（用户输入和模型输出）保存到记忆中，以供后续使用。
    ```python
    # response1 = conversation_chain.predict(input="你好，我叫张三。")
    # print(response1)
    # response2 = conversation_chain.predict(input="你还记得我叫什么名字吗？")
    # print(response2) # 模型应该能回答出“张三”
    ```

**关键点：**

* **`input_key` 和 `output_key`**: 记忆对象通常需要知道链的输入和输出键是什么，以便正确存储对话。默认情况下，它们通常是 "input" 和 "output" 或 "response"。
* **`memory_key`**: 在提示模板中，代表对话历史的变量名（例如，`history`）需要与记忆对象中设置的 `memory_key` 相匹配。`ConversationBufferMemory` 默认的 `memory_key` 是 "history"。
* **加载和保存记忆**: 记忆对象通常有 `load_memory_variables` 方法来获取记忆内容，以及 `save_context` 方法来保存新的交互。在链的执行过程中，这些方法会被自动调用。

通过合理配置和使用记忆组件，你可以构建出能够进行连贯、有上下文感知对话的强大应用。

#### 3.5 代理 (Agents)：让语言模型动态决策和行动

代理 (Agents) 是 LangChain 中一个非常核心和强大的概念。与链 (Chains) 中预先定义好固定的步骤序列不同，代理使用一个 LLM 作为“大脑”或“推理引擎”，使其能够动态地决定采取什么行动以及行动的顺序。代理可以访问一套“工具 (Tools)”，并根据用户的输入和目标来选择使用哪个工具，然后观察工具的输出，并决定下一步行动，直到任务完成或达到某个停止条件。

##### 1. Agent 的核心概念：Tools, Agent Executor, ReAct 框架等

* **`Tools` (工具)**:
    * 工具是代理可以调用的函数或服务。每个工具都设计用来执行特定的任务。
    * 例如：搜索引擎工具 (Google Search, DuckDuckGo Search)、Python REPL 工具 (执行 Python 代码)、SQL 数据库工具 (查询数据库)、计算器工具、自定义的 API 调用工具等。
    * **关键在于为代理提供正确的工具集，并以对代理最有帮助的方式描述每个工具的功能和使用方法**。如果工具描述不清晰，代理可能无法正确理解何时以及如何使用它们。
    * LangChain 提供了许多预置工具，并且可以轻松定义自己的工具。

* **`Agent` (代理本身/决策者)**:
    * 这是代理的核心逻辑，通常由一个 LLM 和一个专门设计的提示 (Prompt) 驱动。
    * 这个提示会指导 LLM 如何思考、如何选择工具、如何解析工具的输出，以及如何形成最终答案。
    * 提示中可能包含：
        * 代理的“个性”或角色。
        * 代理可用的工具列表及其描述。
        * 输入问题的格式。
        * 期望的思考过程和输出格式（例如，ReAct 框架的格式）。

* **`Agent Executor` (代理执行器)**:
    * 代理执行器是代理的运行时环境。它负责实际调用代理（获取下一步行动），执行代理选择的工具，获取工具的输出，并将输出反馈给代理，如此循环往复，直到代理决定任务完成。
    * **执行流程大致如下**：
        1.  接收用户输入。
        2.  代理决定采取哪个行动（使用哪个工具以及该工具的输入是什么）或直接回复用户。
        3.  如果选择了一个工具，`AgentExecutor` 执行该工具。
        4.  `AgentExecutor` 将工具的输出（观察结果）返回给代理。
        5.  代理根据新的观察结果决定下一步行动。
        6.  重复步骤 3-5，直到代理认为任务完成并给出最终答案。
    * `AgentExecutor` 还处理了许多复杂情况，如：代理选择了不存在的工具、工具执行出错、代理输出了无法解析的内容等，并提供了日志和可观察性。

* **`ReAct` 框架 (Reasoning and Acting)**:
    * ReAct 是一种强大的提示工程策略，常用于构建代理，它促使 LLM “**思考 (Thought)**”然后“**行动 (Action)**”。
    * 在 ReAct 框架下，LLM 会交替生成：
        * **Thought (思考)**: 描述当前的分析、推理过程和下一步计划。
        * **Action (行动)**: 指定要使用的工具和该工具的输入。
        * **Observation (观察)**: 工具执行后返回的结果。
        * LLM 会重复这个 Thought -> Action -> Observation 的循环，直到它认为可以给出 **Final Answer (最终答案)**。
    * 这种明确的思考步骤使得代理的行为更具可解释性，并且通常能更好地处理复杂任务。LangChain 中的许多预置代理类型都基于 ReAct 框架。

##### 2. 不同类型的 Agent (Zero-shot ReAct, Self-ask with search 等)

LangChain 提供了多种预置的代理类型，它们在提示、决策逻辑和适用场景上有所不同：

* **`zero-shot-react-description` (零样本 ReAct 描述型代理)**:
    * 这是最通用的 ReAct 代理类型之一。
    * 它仅根据工具的描述来决定使用哪个工具。
    * “零样本”意味着它不需要示例来学习如何使用工具，而是依赖 LLM 的通用推理能力和对工具描述的理解。
    * 适用于需要根据工具描述动态选择工具的场景。

* **`self-ask-with-search` (自问自答与搜索型代理)**:
    * 这种代理专门设计用于回答复杂问题，它会将原始问题分解为一系列更简单的子问题。
    * 它使用一个搜索工具（通常是唯一的工具）来查找这些子问题的答案。
    * 然后，它综合子问题的答案来回答原始的复杂问题。
    * 例如，对于问题“《泰坦尼克号》的导演的妻子是谁？”，它可能会先搜索“《泰坦尼克号》的导演是谁？”，得到詹姆斯·卡梅隆，然后再搜索“詹姆斯·卡梅隆的妻子是谁？”。

* **`conversational-react-description` (对话式 ReAct 描述型代理)**:
    * 这种代理也使用 ReAct 框架，并且设计用于对话场景。
    * 它能够利用对话历史（通过 Memory 组件）来进行更连贯的交互。
    * 它不仅会考虑当前的输入，还会考虑之前的对话内容来决定下一步行动。

* **`chat-zero-shot-react-description` (聊天零样本 ReAct 描述型代理)**:
    * 这是专门为聊天模型 (Chat Models, 如 `ChatOpenAI`) 优化的 `zero-shot-react-description` 版本。提示和交互方式更适合聊天模型的输入输出格式。

* **`structured-chat-zero-shot-react-description` (结构化聊天零样本 ReAct 描述型代理)**:
    * 这种代理适用于能够输出结构化数据（例如 JSON）的聊天模型。它期望工具的输入也是结构化的，这使得它能够处理更复杂的多输入工具。

* **Plan-and-Execute Agents (规划与执行代理)**:
    * 这种代理首先会制定一个完成任务的步骤计划，然后按计划逐个执行这些步骤。
    * 与 ReAct 代理在每个步骤都重新评估不同，它更侧重于预先规划。

选择哪种代理类型取决于任务的性质、是否需要对话历史、使用的 LLM 类型（通用 LLM 还是聊天模型）以及对工具交互的复杂性要求。开发者也可以基于这些基础类型创建自定义的代理。

#### 3.6 回调 (Callbacks)：监控和记录 LangChain 应用的执行过程

回调 (Callbacks) 是 LangChain 提供的一个强大机制，允许你在 LangChain 应用（如链、模型、代理、工具的调用）的生命周期的各个关键阶段插入自定义代码。这对于日志记录、监控、流式传输、调试以及与其他系统集成非常有用。

##### 1. 回调的作用和使用场景

回调系统的主要作用是在 LangChain 应用执行过程中的特定事件发生时，能够触发相应的处理函数。

**常见的使用场景包括：**

* **日志记录 (Logging)**:
    * 记录 LLM 的输入提示和输出响应。
    * 记录链的开始和结束，以及中间步骤的输入输出。
    * 记录代理选择的工具、工具的输入和工具的输出（观察结果）。
    * 记录发生的错误。
    * 这些日志对于调试、分析模型行为和追踪应用流程至关重要。

* **监控 (Monitoring)**:
    * 跟踪 LLM 的调用次数、令牌使用量、响应时间等性能指标。
    * 监控代理的决策过程和工具的使用情况。
    * 可以将这些数据发送到专门的监控系统（如 LangSmith、Prometheus、Datadog）进行可视化和告警。

* **流式传输 (Streaming)**:
    * 当 LLM 正在生成响应时，可以逐步地将生成的令牌流式传输到前端界面或客户端，而不是等待整个响应完成后再显示。这可以显著改善用户体验，尤其是在处理较长响应时。

* **调试 (Debugging)**:
    * 在复杂的链或代理执行过程中，通过回调可以详细了解每一步的中间状态和数据流向，帮助快速定位问题。

* **成本跟踪 (Cost Tracking)**:
    * 通过回调记录 LLM 调用的令牌数量，可以帮助估算和控制 API 使用成本。

* **与外部系统集成**:
    * 当特定事件发生时（例如，代理完成了某个任务），可以通过回调触发外部系统的操作。

##### 2. 常用的回调处理器

LangChain 提供了一些内置的回调处理器，同时也允许你轻松创建自定义的处理器。回调处理器是一个类，它实现了 LangChain 定义的回调接口中的一个或多个方法。这些方法对应于 LangChain 执行过程中的不同事件。

**常用事件（回调方法名通常以 `on_` 开头）：**

* `on_llm_start(serialized, prompts, **kwargs)`: LLM 调用开始时触发。
* `on_llm_new_token(token, **kwargs)`: LLM 生成新令牌时触发（用于流式传输）。
* `on_llm_end(response, **kwargs)`: LLM 调用结束时触发。
* `on_llm_error(error, **kwargs)`: LLM 调用出错时触发。
* `on_chain_start(serialized, inputs, **kwargs)`: 链开始执行时触发。
* `on_chain_end(outputs, **kwargs)`: 链执行结束时触发。
* `on_chain_error(error, **kwargs)`: 链执行出错时触发。
* `on_tool_start(serialized, input_str, **kwargs)`: 工具开始执行时触发。
* `on_tool_end(output, **kwargs)`: 工具执行结束时触发。
* `on_tool_error(error, **kwargs)`: 工具执行出错时触发。
* `on_agent_action(action, **kwargs)`: 代理决定采取一个行动时触发。
* `on_agent_finish(finish, **kwargs)`: 代理完成任务并给出最终答案时触发。
* `on_text(text, **kwargs)`: 当有文本（通常是中间思考或观察结果）产生时触发。

**内置的回调处理器示例：**

* **`StdOutCallbackHandler` / `ConsoleCallbackHandler` (标准输出回调处理器)**:
    * 这是最基本的回调处理器之一。它会将所有触发的事件信息（如链的输入输出、LLM 的提示和响应等）打印到控制台 (stdout)。
    * 非常适合在开发和调试阶段快速查看发生了什么。

* **`FileCallbackHandler` (文件回调处理器)**:
    * 将回调事件写入指定的文件。

* **`LangChainTracer` (LangSmith 集成)**:
    * 如果你使用 LangSmith (LangChain 的官方调试、监控和可观测性平台)，这个回调处理器会自动将所有的执行轨迹发送到 LangSmith，方便进行可视化分析和调试。

* **用于流式传输的处理器**:
    * 例如 `StreamingStdOutCallbackHandler` 可以将 LLM 生成的令牌实时打印到控制台。
    * 你可以创建自定义的流式回调处理器，将令牌发送到 WebSocket 连接或其他流式接口。

**如何使用回调：**

回调可以在两个层面进行设置：

1.  **构造器回调 (Constructor Callbacks)**: 在创建 LangChain 对象（如 LLM、Chain、AgentExecutor）时，通过 `callbacks` 参数传入回调处理器列表。这些回调将应用于该对象的所有调用。
    ```python
    from langchain_community.callbacks import StdOutCallbackHandler
    from langchain.chains import LLMChain
    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate

    handler = StdOutCallbackHandler()
    llm = OpenAI(callbacks=[handler], temperature=0) # 应用于此 LLM 实例的所有调用
    prompt = PromptTemplate.from_template("1+1等于几?")
    chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler]) # 应用于此链实例的所有调用
    # chain.run({})
    ```

2.  **请求回调 (Request Callbacks)**: 在调用具体方法（如 `.run()`, `.call()`, `.apply()`, `.stream()`, `.invoke()`, `.ainvoke()` 等）时，通过 `callbacks` 参数传入。这些回调仅应用于当前的这次特定请求及其所有子请求。
    ```python
    # chain.run({}, callbacks=[handler]) # 仅应用于这次 run 调用
    ```

通过灵活使用回调机制，开发者可以极大地增强对 LangChain 应用内部运作的可见性和控制力。



--- 



## 模块二：模型 I/O (Model I/O) 深入

### 第四章：与语言模型 (LLMs) 交互

与大型语言模型 (LLMs) 的有效交互是构建任何基于 LLM 应用的核心。LangChain 提供了一套标准的接口和工具，使得与各种 LLM 提供商的集成、提示的构建与管理、以及输出的处理变得更加简单和高效。

#### 4.1 理解 LLMs 接口

LangChain 提供了两种主要的模型抽象接口来与语言模型进行交互：

1.  **LLMs (大型语言模型)**:
    * 这是 LangChain 中与语言模型交互的原始接口。
    * **输入**: 通常是一个字符串提示 (prompt)。
    * **输出**: 通常是一个字符串，即模型生成的文本。
    * **适用场景**: 适用于那些主要进行文本补全、简单问答等任务的模型。
    * **常用方法**:
        * `invoke(prompt, **kwargs)`: 对单个输入提示调用模型，返回字符串响应。
        * `batch(prompts, **kwargs)`: 对多个输入提示进行批量调用，返回字符串响应列表。效率通常比多次单独调用 `invoke` 更高。
        * `stream(prompt, **kwargs)`: 对单个输入提示调用模型，并以流式方式返回响应的各个部分（通常是token）。

2.  **ChatModels (聊天模型)**:
    * 这是一个更现代且功能更丰富的接口，专门为对话式交互设计。
    * **输入**: 一个聊天消息列表 (`List[BaseMessage]`)。消息类型通常包括：
        * `SystemMessage`: 设定 AI 的行为、角色或上下文。
        * `HumanMessage`: 代表用户的输入。
        * `AIMessage`: 代表 AI 的回复。
        * `FunctionMessage`/`ToolMessage`: 用于函数/工具调用场景。
    * **输出**: 通常是一个 `AIMessage` 对象，其中包含 AI 的回复内容，有时也包含其他元数据（如工具调用请求）。
    * **适用场景**: 适用于构建聊天机器人、需要多轮对话、或利用模型特定功能（如函数调用）的场景。
    * **常用方法**:
        * `invoke(messages, **kwargs)`: 对单个消息列表调用模型，返回一个 `AIMessage`。
        * `batch(messages_list, **kwargs)`: 对多个消息列表进行批量调用。
        * `stream(messages, **kwargs)`: 对单个消息列表调用模型，并以流式方式返回响应的各个部分 (通常是 `AIMessageChunk`)。

**通用交互方法**：

无论是 LLM还是 ChatModel 接口，LangChain 都致力于提供一套统一的交互方法（尤其是在最新的 LangChain Expression Language - LCEL 中）：

* **`invoke`**: 单次调用。
* **`batch`**: 批量调用。
* **`stream`**: 流式调用，逐步获取结果。
* **`ainvoke`**, **`abatch`**, **`astream`**: 对应上述方法的异步版本，用于并发执行和非阻塞 I/O。

理解这两种接口的区别以及它们各自的输入输出格式，对于选择合适的模型和构建有效的交互逻辑至关重要。

#### 4.2 使用不同的 LLM提供商 (OpenAI, Hugging Face Hub, Azure OpenAI 等)

LangChain 的一个核心优势是其对多种 LLM 提供商的广泛支持，允许开发者轻松切换和试验不同的模型，而无需大幅修改代码。

**通用步骤：**

1.  **安装依赖**: 通常需要安装 LangChain 核心库以及特定提供商的集成库 (例如 `langchain-openai`, `langchain-huggingface`, `langchain-community` 中可能包含其他提供商)。
2.  **获取 API 密钥**: 从相应的 LLM 提供商处获取 API 密钥或其他认证凭证。
3.  **设置环境变量**: 将 API 密钥等凭证安全地设置为环境变量 (例如 `OPENAI_API_KEY`, `HUGGINGFACEHUB_API_TOKEN`, `AZURE_OPENAI_API_KEY`)。这是推荐的做法，避免在代码中硬编码密钥。
4.  **导入并实例化模型**: 从 LangChain 的相应模块中导入所需的模型类并实例化。

**示例提供商：**

* **OpenAI**:
    * **集成库**: `langchain-openai`
    * **模型类**: `OpenAI` (用于旧的补全模型), `ChatOpenAI` (用于聊天模型如 GPT-3.5-turbo, GPT-4)。
    * **认证**: 主要通过 `OPENAI_API_KEY` 环境变量。
    * **示例 (概念性)**:
        ```python
        from langchain_openai import ChatOpenAI
        # 确保 OPENAI_API_KEY 环境变量已设置
        chat_model = ChatOpenAI(model="gpt-4-turbo-preview")
        # response = chat_model.invoke("你好！")
        ```

* **Hugging Face Hub**:
    * **集成库**: `langchain-huggingface` 或 `langchain_community.llms.huggingface_hub`
    * **模型类**: `HuggingFaceEndpoint` (推荐，用于访问托管在 Inference Endpoints 上的模型) 或 `HuggingFaceHub` (用于访问 Hub 上的公开模型)。
    * **认证**: 主要通过 `HUGGINGFACEHUB_API_TOKEN` 环境变量。
    * **示例 (概念性 - HuggingFaceEndpoint)**:
        ```python
        from langchain_huggingface import HuggingFaceEndpoint
        # 确保 HUGGINGFACEHUB_API_TOKEN 环境变量已设置
        # endpoint_url = "YOUR_HUGGINGFACE_ENDPOINT_URL" # 或者直接使用 repo_id
        # hf_llm = HuggingFaceEndpoint(endpoint_url=endpoint_url, task="text-generation")
        hf_llm_via_repo = HuggingFaceEndpoint(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1", temperature=0.7)
        # response = hf_llm_via_repo.invoke("解释一下什么是黑洞。")
        ```

* **Azure OpenAI**:
    * **集成库**: `langchain-openai` (也用于 Azure)
    * **模型类**: `AzureOpenAI` (用于旧的补全模型), `AzureChatOpenAI` (用于聊天模型)。
    * **认证**: 需要设置多个环境变量，如 `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, `OPENAI_API_VERSION`。通常还需要指定 `deployment_name` (在 Azure 上部署的模型名称)。
    * **示例 (概念性)**:
        ```python
        from langchain_openai import AzureChatOpenAI
        # 确保 AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, OPENAI_API_VERSION 环境变量已设置
        azure_chat_model = AzureChatOpenAI(
            azure_deployment="your-gpt-deployment-name",
            openai_api_version="2023-07-01-preview" # 示例版本，请使用你配置的版本
        )
        # response = azure_chat_model.invoke("法国的首都是哪里？")
        ```

LangChain 还支持许多其他提供商，如 Anthropic, Cohere, Google Vertex AI (PaLM, Gemini), Bedrock 等。通常，只需查阅 LangChain 文档中对应提供商的部分，按照指引安装和配置即可。

#### 4.3 Prompt Templates：动态构建高效的提示

提示工程 (Prompt Engineering) 是与 LLM 成功交互的关键。LangChain 的 Prompt Templates 允许我们以灵活和可重用的方式创建和管理提示。

* **基本 Prompt Template (`PromptTemplate`)**:
    * 最简单直接的提示模板，通常基于 Python 的 f-string 或 Jinja2 语法。
    * 它允许你定义一个包含占位符（输入变量）的字符串模板。
    * **示例**:
        ```python
        from langchain.prompts import PromptTemplate

        template_string = "请告诉我关于{topic}的三个有趣的事实。"
        prompt_template = PromptTemplate.from_template(template_string)

        # formatted_prompt = prompt_template.format(topic="月球")
        # print(formatted_prompt)
        # 输出: "请告诉我关于月球的三个有趣的事实。"
        ```

* **带有变量的 Prompt Template**:
    * `PromptTemplate` 的核心功能就是处理输入变量。你可以在模板字符串中定义一个或多个输入变量，并在运行时传入这些变量的值来动态生成提示。
    * **示例**:
        ```python
        from langchain.prompts import PromptTemplate

        multi_var_template = PromptTemplate(
            input_variables=["language", "text"],
            template="将以下文本从{language}翻译成中文：\n\n{text}"
        )

        # formatted_prompt = multi_var_template.format(language="英语", text="Hello, world!")
        # print(formatted_prompt)
        # 输出:
        # 将以下文本从英语翻译成中文：
        #
        # Hello, world!
        ```
    * 对于聊天模型，通常使用 `ChatPromptTemplate`，它可以包含一系列消息模板（如 `SystemMessagePromptTemplate`, `HumanMessagePromptTemplate`）。

* **Few-shot Prompt Template (`FewShotPromptTemplate`)**:
    * “Few-shot”学习是一种通过在提示中提供少量示例来引导模型理解任务并生成期望输出的技术。
    * `FewShotPromptTemplate` 使得构建包含动态示例的提示变得容易。
    * **核心组件**:
        * `examples`: 一个包含多个示例的列表，每个示例通常是一个字典，包含输入变量和对应的期望输出。
        * `example_prompt`: 一个 `PromptTemplate`，用于格式化每一个单独的示例。
        * `prefix` 和 `suffix`: 在示例之前和之后添加的文本，通常包含任务描述和当前输入的占位符。
        * `input_variables`: 当前实际输入的变量名。
        * `example_separator`: 分隔不同示例的字符串（默认为两个换行符）。
    * **`ExampleSelector` (示例选择器)**: 当有大量示例时，可能不希望将所有示例都放入提示中（受限于上下文长度）。`ExampleSelector` 对象可以根据当前输入动态选择最相关的少量示例。常见的选择器有：
        * `LengthBasedExampleSelector`: 根据示例的总长度选择。
        * `SemanticSimilarityExampleSelector`: 根据与当前输入的语义相似度选择（需要嵌入模型和向量存储）。
        * `MaxMarginalRelevanceExampleSelector` (MMR): 选择与输入相似但彼此之间又不那么相似的示例，以增加多样性。
    * **示例 (概念性)**:
        ```python
        from langchain.prompts import FewShotPromptTemplate, PromptTemplate
        from langchain_core.example_selectors import SemanticSimilarityExampleSelector
        from langchain_community.vectorstores import FAISS # 示例向量存储
        from langchain_openai import OpenAIEmbeddings # 示例嵌入

        examples = [
            {"input": "高兴", "output": "积极"},
            {"input": "悲伤", "output": "消极"},
            {"input": "激动", "output": "积极"},
            {"input": "愤怒", "output": "消极"}
        ]

        example_prompt = PromptTemplate.from_template("输入情感词: {input}\n输出情感分类: {output}")

        # # 对于简单的固定示例：
        # few_shot_prompt_fixed = FewShotPromptTemplate(
        #     examples=examples,
        #     example_prompt=example_prompt,
        #     prefix="将以下输入的情感词分类为积极或消极。",
        #     suffix="输入情感词: {user_input}\n输出情感分类:",
        #     input_variables=["user_input"]
        # )
        # formatted_prompt = few_shot_prompt_fixed.format(user_input="兴奋")
        # print(formatted_prompt)

        # # 对于动态选择示例（概念性设置，实际使用需要填充 vectorstore）：
        # example_selector = SemanticSimilarityExampleSelector.from_examples(
        #     examples,
        #     OpenAIEmbeddings(), # 假设已配置
        #     FAISS, # 假设已配置
        #     k=2
        # )
        # few_shot_prompt_dynamic = FewShotPromptTemplate(
        #     example_selector=example_selector,
        #     example_prompt=example_prompt,
        #     prefix="根据以下示例，将输入的情感词分类为积极或消极。",
        #     suffix="输入情感词: {user_input}\n输出情感分类:",
        #     input_variables=["user_input"]
        # )
        # # formatted_prompt_dynamic = few_shot_prompt_dynamic.format(user_input="忧郁")
        # # print(formatted_prompt_dynamic)
        ```

#### 4.4 Output Parsers：结构化输出处理:

* LLM 的原始输出通常是纯文本字符串。但在许多应用中，我们希望得到结构化的数据（如 JSON、列表、自定义对象）。Output Parsers 就是用来解决这个问题的。
* **工作流程**:
    1.  **在提示中包含格式指令**: Output Parser 通常会提供一个方法 (如 `get_format_instructions()`) 来生成关于期望输出格式的文本描述，你需要将这些指令包含在给 LLM 的提示中。
    2.  **LLM 生成符合指令的输出**: LLM 尝试按照指令生成文本。
    3.  **解析器解析输出**: 将 LLM 生成的文本字符串传递给 Output Parser 的 `parse()` 方法，解析器会将其转换为结构化的 Python 对象。
* **常见 Output Parsers**:
    * **`StrOutputParser`**: 最基础的解析器，通常只是将聊天消息的 `content` 提取为字符串。
    * **`PydanticOutputParser`**: 允许你定义一个 Pydantic 模型，LLM 的输出将被解析为该模型的实例。非常适合需要自定义复杂数据结构的场景。
    * **`JsonOutputParser`**: 尝试将 LLM 输出的字符串解析为 JSON 对象。可以与 Pydantic 模型结合使用以获得更强的类型校验。
    * **`CommaSeparatedListOutputParser`**: 将 LLM 输出的逗号分隔的字符串解析为 Python 列表。
    * **`StructuredOutputParser`**: 允许你预先定义一个包含多个字段及其描述的结构，LLM 会被要求为每个字段生成值，然后解析为字典。
    * **`DatetimeOutputParser`**: 解析日期时间字符串。
    * **`EnumOutputParser`**: 确保输出是预定义枚举类型中的一个值。
    * **`XMLOutputParser`**: 解析 XML 格式的输出。
    * **`RetryOutputParser` / `OutputFixingParser`**: 如果初始解析失败，这些解析器可以尝试将错误的输出连同错误信息再次发送给 LLM，请求其修复输出。
* **示例 (概念性 PydanticOutputParser)**:
    ```python
    from langchain.output_parsers import PydanticOutputParser
    from pydantic import BaseModel, Field
    from langchain.prompts import PromptTemplate
    from langchain_openai import ChatOpenAI

    # class Actor(BaseModel):
    #     name: str = Field(description="演员的名字")
    #     film_names: list[str] = Field(description="该演员出演的电影列表")
    #
    # parser = PydanticOutputParser(pydantic_object=Actor)
    #
    # prompt_template_str = """
    # 根据以下问题提取信息：
    # {format_instructions}
    # 问题：列出一位主演过电影《盗梦空间》的演员及其出演的至少两部其他电影。
    # """
    #
    # prompt = PromptTemplate(
    #     template=prompt_template_str,
    #     input_variables=[],
    #     partial_variables={"format_instructions": parser.get_format_instructions()}
    # )
    #
    # # model = ChatOpenAI(temperature=0)
    # # formatted_prompt = prompt.format_prompt().to_string()
    # # output = model.invoke(formatted_prompt)
    # # parsed_output = parser.parse(output.content)
    # # print(parsed_output)
    ```

#### 4.5 异步操作与流式输出

为了构建高性能和响应迅速的 LLM 应用，LangChain 提供了对异步操作和流式输出的良好支持。

* **异步操作 (Async Operations)**:
    * 当你的应用需要同时处理多个 LLM 请求，或者在等待 LLM 响应时需要执行其他任务（例如在 Web 服务器中处理其他用户请求），异步操作就非常重要。
    * LangChain 为核心的 LLM、ChatModel、Chain 等组件的大多数阻塞式方法（如 `invoke`, `batch`, `generate`, `run`, `call`）都提供了对应的异步版本，通常以 `a` 开头：
        * `ainvoke()`
        * `abatch()`
        * `astream()`
        * `agenerate()` (旧版 LLM 接口)
        * `arun()`, `acall()` (旧版 Chain 接口)
    * 使用这些异步方法需要你的 Python 代码运行在异步环境（例如使用 `asyncio`）。
    * **优点**:
        * **非阻塞**: 在等待 I/O 操作（如 API 调用）时，程序可以切换去执行其他任务。
        * **高并发**: 能够更有效地处理大量并发请求。
        * **提升应用响应性**: 特别是对于 Web 应用，可以避免因等待 LLM 而阻塞主线程。
    * **示例 (概念性)**:
        ```python
        import asyncio
         from langchain_openai import ChatOpenAI
        
         async def main():
             chat = ChatOpenAI()
             response = await chat.ainvoke("写一首关于编程的短诗。")
             print(response.content)
        
             responses = await chat.abatch(["1+1=?", "中国的首都是哪里?"])
             for resp in responses:
                 print(resp.content)
        
         # asyncio.run(main())
        ```

* **流式输出 (Streaming Output)**:
    * 对于生成较长文本的 LLM 调用，用户可能不希望等待整个响应完全生成后再看到结果。流式输出允许模型在生成文本的同时，逐步地将生成的片段（通常是 token by token 或 chunk by chunk）返回给客户端。
    * **LangChain 支持**:
        * LLM 和 ChatModel 接口都有 `stream()` (同步) 和 `astream()` (异步) 方法。
        * 当调用这些方法时，它们返回一个迭代器 (同步) 或异步迭代器 (异步)，你可以遍历它来获取模型生成的各个片段。
        * 通常与回调函数 (Callbacks)，特别是实现了 `on_llm_new_token` 或类似方法的处理器（如 `StreamingStdOutCallbackHandler`）结合使用，以便在每个新片段到达时执行特定操作（如打印到控制台、发送到 WebSocket）。

        <span style="color:red">关于回调函数的知识请见：[07-回调系统](/p/07-%E5%9B%9E%E8%B0%83%E7%B3%BB%E7%BB%9Fevents%E4%BA%8B%E4%BB%B6/)</span>


    * **优点**:
        * **改善用户体验**: 用户可以更快地看到初步结果，而不是长时间等待。
        * **实时交互**: 适用于需要实时反馈的应用。
    * **示例 (概念性)**:
        ```python
        import asyncio
        from langchain_openai import ChatOpenAI
        from langchain_core.callbacks import StreamingStdOutCallbackHandler # 也可以自定义回调
        import os
        def stream_response():
            chat = ChatOpenAI(streaming=True) 

            for chunk in chat.stream("给我讲一个关于太空旅行的长故事。"):
                print(chunk.content, end="", flush=True)
        stream_response()
        ```

#### 4.6 模型参数配置与优化 (temperature, max_tokens 等)

在实例化或调用 LLM/ChatModel 时，你可以传递各种参数来控制模型的行为和输出。理解这些参数对于优化模型性能、成本和输出质量至关重要。

**常用参数：**

* **`model` 或 `model_name` (字符串)**:
    * 指定要使用的具体模型，例如 `"gpt-3.5-turbo"`, `"gpt-4"`, `"mistralai/Mixtral-8x7B-Instruct-v0.1"`。可用模型取决于所选的 LLM 提供商。

* **`temperature` (浮点数, 通常在 0.0 到 2.0 之间)**:
    * 控制输出的随机性或“创造性”。
    * **较低的值 (例如 0.0 - 0.3)**: 使输出更具确定性、事实性和专注性。模型倾向于选择概率最高的词。适用于需要精确答案或重复性任务的场景。
    * **较高的值 (例如 0.7 - 1.0 或更高)**: 使输出更随机、多样化和富有创意。适用于需要生成故事、头脑风暴或不拘一格文本的场景。
    * 默认值通常在 0.7 左右。

* **`max_tokens` (整数)**:
    * 设置模型在一次调用中生成的最大 token 数量（包括提示和补全）。Token 是文本的基本单位，大致可以理解为一个词或几个字符。
    * 这个参数对于控制输出长度和 API 调用成本非常重要。如果生成内容被截断，可能是因为达到了 `max_tokens` 的限制。

* **`top_p` (浮点数, 通常在 0.0 到 1.0 之间)**:
    * 也称为 "nucleus sampling"。一种替代 `temperature` 的采样方法。
    * 模型会从概率最高的词开始累加它们的概率，直到总概率达到 `top_p`，然后从这个词集合中进行采样。
    * 例如，`top_p=0.1` 意味着只考虑构成概率前 10% 的词。
    * 通常不建议同时修改 `temperature` 和 `top_p`。OpenAI 建议只修改其中一个。

* **`top_k` (整数)**:
    * 另一种采样策略，它将采样范围限制为概率最高的 `k` 个候选词。
    * 例如，`top_k=50` 表示模型在生成下一个词时，只会在最可能的 50 个词中进行选择。
    * 将其设置为 1 等同于贪心解码 (总是选择最可能的词)。

* **`stop` (字符串列表)**:
    * 可以提供一个或多个停止序列。当模型生成这些序列中的任何一个时，它会停止进一步生成文本。
    * 例如，如果你希望模型在生成换行符 `\n` 后停止，可以设置 `stop=["\n"]`。

* **`presence_penalty` (浮点数, 通常在 -2.0 到 2.0 之间, OpenAI 特定)**:
    * 惩罚那些已经在文本中出现过的 token，从而鼓励模型谈论新的话题，减少重复。正值会增加谈论新主题的可能性。

* **`frequency_penalty` (浮点数, 通常在 -2.0 到 2.0 之间, OpenAI 特定)**:
    * 惩罚那些在文本中频繁出现的 token（与 `presence_penalty` 不同，它考虑了 token 出现的频率）。正值会降低重复相同词语或短语的可能性。

**配置方式：**

* **实例化时**: 在创建 LLM 或 ChatModel 对象时直接传递参数。
    ```python
    # from langchain_openai import ChatOpenAI
    # chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2, max_tokens=150)
    ```
* **调用时**: 在调用 `invoke`, `stream`, `batch` 等方法时，通过 `**kwargs` 或特定的参数（如 `stop`）传递。调用时传递的参数通常会覆盖实例化时设置的同名参数。
    ```python
    # response = chat.invoke("写一个关于猫的笑话。", stop=["哈哈哈"])
    ```

**优化建议：**

* **从默认值开始**: 先使用模型的默认参数，观察其表现。
* **小幅调整**: 每次只调整一个参数，并观察其对输出的影响。
* **针对特定任务调整**: 不同的任务可能需要不同的参数设置。例如，代码生成可能需要较低的 `temperature`，而创意写作则可能受益于较高的 `temperature`。
* **注意成本**: `max_tokens` 和选择的模型类型会直接影响 API 成本。
* **实验和迭代**: 找到最佳参数组合通常需要反复试验。


### 第五章：与聊天模型 (Chat Models) 交互

与传统的语言模型 (LLM) 主要处理文本补全不同，聊天模型 (Chat Models) 专为对话场景设计。它们通过一系列消息的交互来理解上下文并生成回应。LangChain 提供了强大的工具来与这些模型进行交互。

#### 5.1 理解 Chat Models 的消息类型 (SystemMessage, HumanMessage, AIMessage)

聊天模型的核心交互单元是“消息”。LangChain 定义了几种标准的消息类型，用于构建对话流程：

* **`SystemMessage` (系统消息)**:
    * **用途**: 用于向 AI 模型提供高级别的指示、上下文或角色设定。它通常是对话开始时的第一条消息，或者用于在对话中途引导模型的行为。
    * **特点**: `SystemMessage` 帮助设定 AI 的“个性”、行为准则或其在对话中应扮演的角色（例如，“你是一个乐于助人的编程助手”或“你是一个只用莎士比亚风格回答问题的海盗”）。
    * **示例**:
        ```python
        from langchain_core.messages import SystemMessage

        system_prompt = "你是一个经验丰富的旅行规划师，专门为用户推荐小众但精彩的旅游目的地。"
        system_message = SystemMessage(content=system_prompt)
        ```

* **`HumanMessage` (用户消息)**:
    * **用途**: 代表对话中由人类用户输入的消息或提出的问题。
    * **特点**: 这是用户与 AI 模型直接交流的内容。模型会根据这些消息以及上下文来生成回应。
    * **示例**:
        ```python
        from langchain_core.messages import HumanMessage

        user_query = "我想找一个适合夏天徒步，并且游客不多的欧洲国家，有什么建议吗？"
        human_message = HumanMessage(content=user_query)
        ```

* **`AIMessage` (AI 消息 / 助手消息)**:
    * **用途**: 代表 AI 模型生成的回应或消息。
    * **特点**: 这是模型对 `HumanMessage` 或整个对话历史的回应。在构建多轮对话历史时，将模型之前的输出作为 `AIMessage` 传入，可以帮助模型保持对话的连贯性。
    * **示例**:
        ```python
        from langchain_core.messages import AIMessage

        ai_response_text = "考虑到您的要求，我推荐斯洛文尼亚。那里有美丽的阿尔卑斯山脉适合徒步，夏季气候宜人，而且相比西欧热门国家，游客要少得多。特别是朱利安阿尔卑斯山区的索查河谷，景色非常壮观。"
        ai_message = AIMessage(content=ai_response_text)
        ```

* **其他消息类型 (进阶)**:
    * **`ChatMessage`**: 一个更通用的消息类型，可以用来表示任何角色的消息，通过 `role` 参数指定。
    * **`FunctionMessage` (已弃用, 现为 `ToolMessage`)**: 用于表示函数调用的结果。当模型决定调用外部工具或函数时，其输出会通过 `ToolMessage` 返回给模型，以便它继续生成回应。 (这部分与后续的 Tool/Function calling 功能紧密相关)

理解并正确使用这些消息类型是构建有效聊天应用的基础。它们共同构成了传递给聊天模型的对话历史，模型将基于此历史来理解上下文并生成下一个回应。

#### 5.2 构建聊天应用的 Prompt Templates

与 LLM 的 `PromptTemplate` 类似，`ChatPromptTemplate` 使得为聊天模型构建动态和结构化的输入更为容易。它允许你定义一个由多种消息类型组成的模板，其中可以包含变量。

* **核心组件**: `ChatPromptTemplate` 通常由一个或多个消息提示模板 (Message Prompt Templates) 组成。
    * `SystemMessagePromptTemplate`: 用于创建系统消息的模板。
    * `HumanMessagePromptTemplate`: 用于创建用户消息的模板。
    * `AIMessagePromptTemplate`: 用于创建 AI 消息的模板（较少直接在初始提示中定义，更多用于构建历史）。

* **工作方式**:
    1.  定义包含占位符的消息模板。
    2.  使用 `ChatPromptTemplate.from_messages` 来组合这些消息模板。
    3.  在运行时，使用 `.format_messages()` 或 `.format_prompt()` 方法，并传入变量的值，来生成一个完整的消息列表或格式化的提示值 (PromptValue)。

* **优点**:
    * **结构清晰**: 将对话结构（系统指令、用户问题等）与具体内容分离。
    * **可复用性**: 方便地为不同的输入创建一致的对话格式。
    * **动态性**: 轻松地将变量插入到对话的各个部分。

* **示例**:

    ```python
    from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
    from langchain_openai import ChatOpenAI

    # 1. 定义消息模板
    system_template = "你是一个专业的翻译助手，可以将用户的文本从{input_language}翻译成{output_language}。"
    human_template = "{text_to_translate}"

    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # 2. 构建 ChatPromptTemplate
    chat_prompt_template = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    # 3. 格式化提示 (生成消息列表)
    formatted_messages = chat_prompt_template.format_messages(
        input_language="中文",
        output_language="英文",
        text_to_translate="你好，世界！"
    )
    # formatted_messages 将是:
    # [
    # SystemMessage(content='你是一个专业的翻译助手，可以将用户的文本从中文翻译成英文。'),
    # HumanMessage(content='你好，世界！')
    # ]

    # print(formatted_messages)

    # # 与模型结合使用
    # async def translate_text():
    #     chat = ChatOpenAI(model="gpt-3.5-turbo")
    #     response = await chat.ainvoke(formatted_messages)
    #     print(f"翻译结果: {response.content}")

    # import asyncio
    # asyncio.run(translate_text())
    ```

`ChatPromptTemplate` 是构建可维护和灵活的聊天应用的关键组件，尤其是在需要根据不同场景或用户输入动态调整系统指令或问题格式时。

#### 5.3 聊天历史管理 (Chat History Management)

在多轮对话中，模型需要记住之前的交流内容才能提供连贯且相关的回答。聊天历史管理 (通常称为 "Memory") 是实现这一目标的关键。LangChain 提供了多种内置的 Memory 类型来简化历史记录的存储和检索。

* **为什么需要聊天历史管理?**:
    * **上下文感知**: 使模型能够理解当前问题与先前讨论内容的关系。
    * **个性化体验**: 记住用户的偏好或之前的回答，提供更个性化的互动。
    * **避免重复**: 防止模型重复已经说过的信息或用户已经提供的信息。

* **核心概念**:
    * **存储 (Storage)**: 聊天消息（`HumanMessage`, `AIMessage` 等）被存储起来。
    * **检索 (Retrieval)**: 在向模型发送新请求之前，从存储中检索相关的历史消息，并将其与当前用户输入一起传递给模型。
    * **消息窗口 (Message Window)**: 为了控制传递给模型的上下文长度（避免超出 token 限制和降低成本），通常只使用最近的 N 条消息或一定 token 数量内的消息。
    * **摘要 (Summarization)**: 对于非常长的对话，可以将早期的对话内容进行摘要，而不是保留所有原始消息。

* **LangChain 中的 Memory 组件**:
    * **`ChatMessageHistory`**: LangChain 中最基础的内存接口，提供了添加和检索消息的方法。可以基于此构建自定义的内存存储方案（如存入数据库、文件等）。
        ```python
        from langchain_core.chat_history import InMemoryChatMessageHistory

        history = InMemoryChatMessageHistory()
        history.add_user_message("你好，我的名字是小明。")
        history.add_ai_message("你好小明！很高兴认识你。")
        # print(history.messages)
        ```
    * **`ConversationBufferMemory`**:
        * 将完整的对话历史存储在内存中，并在每次调用时将其全部发送给模型。
        * 适用于对话历史较短的情况。
        * 可以通过 `memory_key` 参数指定模板中用于插入历史记录的变量名 (默认为 `"history"`).
        * `return_messages=True` 会使其返回消息对象列表，而不是单个字符串。
    * **`ConversationBufferWindowMemory`**:
        * 只保留最近 `k` 轮对话（一轮对话通常指一个用户消息和一个 AI 回应）。
        * 有助于控制上下文长度，防止超出模型的 token 限制。
        * 参数 `k` 控制窗口大小。
    * **`ConversationSummaryMemory`**:
        * 随着对话的进行，逐步将对话内容进行摘要。
        * 需要一个额外的 LLM 来执行摘要任务。
        * 适用于非常长的对话，其中保留所有细节不切实际。
    * **`ConversationSummaryBufferMemory`**:
        * 结合了 `ConversationBufferWindowMemory` 和 `ConversationSummaryMemory` 的优点。
        * 它在内存中保留最近的对话片段，并将更早的对话进行摘要。
        * 当缓存的对话长度超过 `max_token_limit` 时，会将旧消息转化为摘要。

* **在 Chain 中使用 Memory**:
    Memory 组件通常与 `LLMChain` 或其他类型的 Chain 结合使用。Chain 会自动处理从 Memory 中加载历史记录，并在处理完请求后更新 Memory。

    ```python
    from langchain.chains import ConversationChain
    from langchain_openai import ChatOpenAI
    from langchain.memory import ConversationBufferWindowMemory

    # 概念性示例
    llm = ChatOpenAI(temperature=0)
    memory = ConversationBufferWindowMemory(k=3, return_messages=True) # 保留最近3轮对话

    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True # 可以看到 Chain 的思考过程和最终的提示
    )

    # 第一次对话
    response1 = conversation.predict(input="你好，我叫张三。")
    print(response1)

    # 第二次对话
    response2 = conversation.predict(input="我喜欢蓝色。")
    print(response2)

    # 第三次对话 - 模型应该能记住张三的名字和喜好
    response3 = conversation.predict(input="你还记得我叫什么，喜欢什么颜色吗？")
    print(response3)

    # 查看 Memory 中的内容
    print(memory.load_memory_variables({}))
    ```

选择合适的 Memory 类型取决于应用的具体需求，如对话长度、成本考虑、以及上下文保留的详细程度。

#### 5.4 结合 Output Parsers 实现更复杂的聊天交互

虽然聊天模型可以直接生成文本回复，但在许多应用场景中，我们希望模型能以特定结构（如 JSON、列表、自定义对象等）返回信息，或者在模型输出后进行校验和转换。这时，输出解析器 (Output Parsers) 就派上了用场。

* **为什么需要 Output Parsers?**:
    * **结构化输出**: 将模型的自然语言回复转换为程序易于处理的结构化数据。
    * **数据提取**: 从模型回复中精确提取特定信息（例如，从一段文本中提取姓名、日期、地点）。
    * **格式化与校验**: 确保模型输出符合预期的格式，并可以进行数据校验。
    * **调用外部工具**: 解析模型的输出以确定是否需要调用某个函数或 API，并提取相应的参数。

* **LangChain 中的 Output Parsers**: LangChain 提供了多种预置的输出解析器，并且允许自定义解析器。
    * **`StrOutputParser`**: 最简单的解析器，直接将模型的输出（通常是 `AIMessage.content`）作为字符串返回。这是许多链的默认输出解析器。
    * **`CommaSeparatedListOutputParser`**: 将模型生成的、以逗号分隔的列表字符串解析为 Python 列表。
    * **`SimpleJsonOutputParser`**: 尝试将模型的文本输出解析为 JSON 对象。
    * **`PydanticOutputParser`**: 允许你定义一个 Pydantic 模型，并指示 LLM 生成符合该模型结构的输出。解析器会自动将 LLM 的文本输出转换为 Pydantic 对象实例，并进行类型校验。这非常强大，因为它结合了 LLM 的生成能力和 Pydantic 的数据验证能力。
    * **`DatetimeOutputParser`**: 解析日期和时间相关的文本。
    * **`XMLOutputParser`**: 解析 XML 格式的输出。
    * **`StructuredOutputParser`**: 通过定义一个响应模式 (response schema) 来指导模型生成特定字段的输出，然后解析这些字段。
    * **`RetryOutputParser`**: 如果初始解析失败（例如模型输出格式不完全正确），它可以给模型一个新的提示（通常包含错误信息和修正指令），让模型重新生成输出，然后再次尝试解析。

* **工作流程**:
    1.  **定义输出格式**: 在提示中明确告知模型期望的输出格式（例如，“请以 JSON 格式返回结果，包含 'name' 和 'age' 字段”）。对于像 `PydanticOutputParser` 这样的解析器，可以自动生成格式指令。
    2.  **获取模型原始输出**: 模型生成文本回复。
    3.  **解析输出**: 输出解析器接收模型的原始文本输出，并尝试将其转换为期望的 Python 对象或数据结构。
    4.  **处理结果**: 应用可以使用解析后的结构化数据进行后续操作。

* **示例 (使用 `PydanticOutputParser` 和 `ChatOpenAI`)**:

    ```python
    import asyncio
    from typing import List
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.pydantic_v1 import BaseModel, Field # 注意这里用 langchain_core.pydantic_v1
    from langchain_openai import ChatOpenAI
    from langchain_core.output_parsers import PydanticOutputParser

    # 1. 定义 Pydantic 模型 (期望的输出结构)
    class Joke(BaseModel):
        setup: str = Field(description="笑话的铺垫部分")
        punchline: str = Field(description="笑话的笑点部分")
        rating: int = Field(description="对笑话的幽默程度打分，1-10分")

    async def get_structured_joke():
        # 2. 创建 PydanticOutputParser 实例
        parser = PydanticOutputParser(pydantic_object=Joke)

        # 3. 创建包含格式化指令的 PromptTemplate
        # parser.get_format_instructions() 会生成如何格式化输出的说明
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "你是一个幽默的AI，擅长讲编程相关的笑话。请严格按照用户的格式要求输出。"),
                ("human", "给我讲一个关于 Python 的笑话。\n{format_instructions}")
            ]
        )

        # 4. 实例化 ChatModel
        chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

        # 5. 创建链 (Prompt + Model + Parser)
        # LCEL (LangChain Expression Language) 风格
        chain = prompt_template | chat | parser

        # 6. 调用链
        try:
            response_joke = await chain.ainvoke({"format_instructions": parser.get_format_instructions()})
            print(f"笑话铺垫: {response_joke.setup}")
            print(f"笑点: {response_joke.punchline}")
            print(f"评分: {response_joke.rating}")
            print(f"原始对象类型: {type(response_joke)}")

        except Exception as e: # langchain_core.exceptions.OutputParserException
            print(f"解析输出时发生错误: {e}")
            # 这里可以加入重试逻辑，例如使用 RetryOutputParser

    # asyncio.run(get_structured_joke())
    ```

通过在提示中明确指定输出格式，并结合相应的输出解析器，可以大大提高从聊天模型中获取可用、结构化数据的可靠性和便捷性，从而支持更复杂的应用逻辑和交互流程。当与函数调用 (Function Calling / Tool Calling) 结合时，其能力会进一步增强。

### 第六章：文本嵌入模型 (Text Embedding Models)

文本嵌入模型是将文本（如单词、句子或整个文档）转换为固定大小的数字向量（称为嵌入或向量表示）的 AI 模型。这些向量捕捉了文本的语义信息，使得具有相似含义的文本在向量空间中彼此靠近。LangChain 提供了与多种文本嵌入模型交互的便捷接口。

#### 6.1 文本嵌入的原理和应用场景

* **原理 (Principle)**:
    * **向量空间模型 (Vector Space Model)**: 文本嵌入的核心思想是将文本映射到一个高维的向量空间。在这个空间中，每个文本片段都由一个向量表示。
    * **语义相似性 (Semantic Similarity)**: 模型的训练目标是使得语义上相似的文本片段在向量空间中的距离更近，而语义上不相关的文本片段距离更远。例如，“小狗”和“宠物狗”的向量表示会比“小狗”和“计算机”的向量表示更接近。
    * **降维与信息保留**: 尽管原始文本信息复杂多样，嵌入模型试图在降维（从无限的文本可能性到固定大小的向量）的同时，尽可能多地保留关键的语义信息。
    * **训练方法**: 这些模型通常通过在大型文本语料库上进行无监督学习来训练，例如预测上下文中的单词 (Word2Vec, GloVe) 或预测下一句话 (BERT 及其变体)。

* **应用场景 (Application Scenarios)**:
    * **语义搜索 (Semantic Search)**: 搜索引擎不再仅仅依赖关键词匹配，而是理解查询的语义，并找到语义上相关的文档。用户搜索“最近的健康餐馆”，系统可以返回提到“有机食品”、“沙拉吧”或“低脂菜肴”的餐馆，即使它们没有完全匹配“健康餐馆”这个词。
    * **文本相似度计算 (Text Similarity Calculation)**: 判断两段文本在语义上的相似程度。例如，比较两篇文章是否讨论相似主题，或者查找重复或近似重复的内容。
    * **文本聚类 (Text Clustering)**: 将大量文本自动分组到具有相似主题的簇中。例如，将新闻文章按主题（体育、政治、科技）分类。
    * **推荐系统 (Recommendation Systems)**: 根据用户过去喜欢的项目（如文章、产品）的嵌入，推荐语义上相似的新项目。
    * **问答系统 (Question Answering)**: 将问题和潜在答案都转换为嵌入，然后找到与问题嵌入最相似的答案嵌入。这是许多 RAG (Retrieval Augmented Generation) 应用的基础。
    * **异常检测 (Anomaly Detection)**: 识别与文本数据集中大多数文本语义上显著不同的文本。
    * **特征提取 (Feature Extraction for Downstream Tasks)**: 将文本嵌入作为输入特征，用于训练其他机器学习模型（如分类器、情感分析器）。

文本嵌入是自然语言处理 (NLP) 中一项基础且强大的技术，为机器理解和处理文本的深层含义提供了可能。

#### 6.2 使用不同的文本嵌入模型 (OpenAI Embeddings, Hugging Face Embeddings 等)

LangChain 抽象了与不同文本嵌入模型提供商交互的细节，提供了一个统一的 `Embeddings` 接口。这意味着你可以相对轻松地切换不同的嵌入模型，而无需大幅修改代码。

* **通用接口**: LangChain 的 `Embeddings` 类定义了两个核心方法：
    * `embed_documents(texts: List[str]) -> List[List[float]]`: 接收一个文本列表，为每个文本生成一个嵌入，并返回一个嵌入列表（每个嵌入本身是一个浮点数列表）。
    * `embed_query(text: str) -> List[float]`: 接收单个文本（通常是用户查询），为其生成嵌入，并返回单个嵌入。这两个方法的存在是为了某些模型可能会对“文档”和“查询”使用不同的嵌入策略或模型。

* **OpenAI Embeddings**:
    * 由 OpenAI 提供的高质量文本嵌入模型，如 `text-embedding-ada-002` 或更新的模型如 `text-embedding-3-small` 和 `text-embedding-3-large`。
    * 使用时需要 OpenAI API 密钥。
    * **优点**: 性能强大，易于使用。
    * **缺点**: 付费 API，有速率限制。

    ```python
    from langchain_openai import OpenAIEmbeddings
    import os

    # 确保设置了 OPENAI_API_KEY 环境变量
    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

    # 使用默认模型 (通常是 text-embedding-ada-002 或更新的兼容模型)
    embeddings_openai = OpenAIEmbeddings()

    # 或者指定模型
    # embeddings_openai_ada = OpenAIEmbeddings(model="text-embedding-ada-002")
    # embeddings_openai_3_small = OpenAIEmbeddings(model="text-embedding-3-small")
    # embeddings_openai_3_large = OpenAIEmbeddings(model="text-embedding-3-large")


    documents_to_embed = ["这是一段示例文本。", "LangChain 非常好用！"]
    document_embeddings = embeddings_openai.embed_documents(documents_to_embed)
    print(f"OpenAI Document Embeddings (第一个文档的维度): {len(document_embeddings[0])}")

    query_to_embed = "什么是文本嵌入？"
    query_embedding = embeddings_openai.embed_query(query_to_embed)
    print(f"OpenAI Query Embedding (维度): {len(query_embedding)}")
    ```

* **Hugging Face Embeddings**:
    * 允许你使用 Hugging Face Hub 上提供的各种开源嵌入模型，例如 Sentence Transformers (`sentence-transformers/all-MiniLM-L6-v2`)、BERT、RoBERTa 等。
    * 可以在本地运行（如果模型已下载）或通过 Hugging Face Inference API (需要 API 密钥和特定配置)。
    * **优点**: 模型选择多样，许多模型可免费在本地运行，对数据隐私有更好控制。
    * **缺点**: 本地运行可能需要一定的计算资源 (CPU/GPU)；模型性能参差不齐，需要根据任务选择。

    ```python
    from langchain_community.embeddings import HuggingFaceEmbeddings
    from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings # 使用推理端点

    # 1. 在本地运行 (推荐，需要安装 sentence_transformers: pip install sentence_transformers)
    #    模型会自动下载（如果本地不存在）
    model_name = "sentence-transformers/all-MiniLM-L6-v2" # 一个流行的轻量级模型
    model_kwargs = {'device': 'cpu'} # 如果有GPU可以设置为 'cuda'
    encode_kwargs = {'normalize_embeddings': False} # 取决于模型是否需要归一化

    embeddings_hf_local = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

    documents_to_embed_hf = ["使用Hugging Face进行嵌入。", "本地模型更灵活。"]
    document_embeddings_hf = embeddings_hf_local.embed_documents(documents_to_embed_hf)
    print(f"Hugging Face Local Document Embeddings (第一个文档的维度): {len(document_embeddings_hf[0])}")

    query_to_embed_hf = "开源嵌入模型有哪些？"
    query_embedding_hf = embeddings_hf_local.embed_query(query_to_embed_hf)
    print(f"Hugging Face Local Query Embedding (维度): {len(query_embedding_hf)}")


    # 2. 使用 Hugging Face Inference API (需要Hugging Face API Token)
    # HF_API_TOKEN = "YOUR_HUGGINGFACE_API_TOKEN"
    embeddings_hf_api = HuggingFaceInferenceAPIEmbeddings(
    api_key=HF_API_TOKEN, model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    query_embedding_hf_api = embeddings_hf_api.embed_query("通过API获取嵌入。")
    print(f"Hugging Face API Query Embedding (维度): {len(query_embedding_hf_api)}")
    ```

* **其他嵌入模型**:
    * LangChain 支持许多其他嵌入模型提供商，例如 Cohere, Google PaLM/Vertex AI, Bedrock (AWS), Aleph Alpha 等。
    * 通常，只需要从相应的 `langchain_community.embeddings` 或特定提供商的包 (如 `langchain_cohere`, `langchain_google_vertexai`) 中导入对应的类并实例化即可。

选择哪种嵌入模型取决于项目的具体需求，包括预算、性能要求、数据隐私考虑以及对特定语言或领域知识的需求。

#### 6.3 生成文本的向量表示

一旦选择了并实例化了一个嵌入模型对象，生成文本的向量表示就非常直接了。

* **嵌入单个文档 (Embedding a Single Document/Query)**:
    * 使用 `embed_query(text: str)` 方法。这通常用于嵌入用户的搜索查询或单个需要比较的文本。

    ```python
    from langchain_openai import OpenAIEmbeddings

    embeddings_model = OpenAIEmbeddings() # 或任何其他 LangChain Embeddings 实现

    text1 = "机器学习正在改变世界。"
    vector1 = embeddings_model.embed_query(text1)

    print(f"文本: '{text1}'")
    print(f"向量表示 (前5个维度): {vector1[:5]}") # 向量通常很高维，这里只显示前5个
    print(f"向量维度: {len(vector1)}")
    ```

* **嵌入多个文档 (Embedding Multiple Documents)**:
    * 使用 `embed_documents(texts: List[str])` 方法。这在预处理文档集合以构建向量数据库或进行批量比较时非常有用。

    ```python
    from langchain_openai import OpenAIEmbeddings

    embeddings_model = OpenAIEmbeddings()

    corpus = [
    "深度学习是机器学习的一个分支。",
    "自然语言处理专注于计算机与人类语言的交互。",
    "文本嵌入用于将文本转换为数字向量。"
    ]

    document_vectors = embeddings_model.embed_documents(corpus)

    for i, doc in enumerate(corpus):
        print(f"\n文档: '{doc}'")
        print(f"向量表示 (前5个维度): {document_vectors[i][:5]}")
        print(f"向量维度: {len(document_vectors[i])}")
    ```

* **异步操作**:
    * 与 LLM 和 ChatModel 类似，Embeddings 类也提供了异步版本的方法：
        * `aembed_documents(texts: List[str]) -> List[List[float]]`
        * `aembed_query(text: str) -> List[float]`
    * 这在需要同时嵌入大量文本或在异步应用中使用嵌入时非常有用。

    ```python
    import asyncio
    from langchain_openai import OpenAIEmbeddings

    embeddings_model = OpenAIEmbeddings()

    async def main_async_embed():
        texts_async = ["异步嵌入示例文本1", "异步嵌入示例文本2"]
        embeddings_async = await embeddings_model.aembed_documents(texts_async)
        # print(f"异步嵌入结果 (第一个文档前3维): {embeddings_async[0][:3]}")

        query_async = "单个异步查询"
        query_embedding_async = await embeddings_model.aembed_query(query_async)
        # print(f"异步查询嵌入 (前3维): {query_embedding_async[:3]}")

    # asyncio.run(main_async_embed())
    ```

生成的向量表示是后续进行相似度计算、聚类、语义搜索等操作的基础。向量的维度取决于所使用的具体嵌入模型（例如，OpenAI 的 `text-embedding-ada-002` 生成 1536 维向量，`text-embedding-3-small` 也是 1536 维，而 `text-embedding-3-large` 是 3072 维；`sentence-transformers/all-MiniLM-L6-v2` 生成 384 维向量）。

#### 6.4 比较文本相似度

获得了文本的向量表示后，可以通过计算这些向量之间的“距离”或“角度”来量化它们之间的语义相似度。

* **常用的相似度/距离度量**:
    * **余弦相似度 (Cosine Similarity)**:
        * 最常用的度量文本嵌入相似度的方法。
        * 计算两个向量之间夹角的余弦值。结果范围在 -1 到 1 之间。
        * 值为 1 表示向量指向完全相同的方向（最大相似度）。
        * 值为 0 表示向量正交（不相关）。
        * 值为 -1 表示向量指向完全相反的方向（最大不相似度）。
        * 对于非负向量（许多嵌入模型生成的是非负向量），范围通常是 0 到 1。
        * 计算公式: $S_{cosine}(\vec{a}, \vec{b}) = \frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\| \|\vec{b}\|}$
    * **欧氏距离 (Euclidean Distance)**:
        * 向量空间中两点之间的直线距离。
        * 距离越小，表示相似度越高。
        * 计算公式: $D_{euclidean}(\vec{a}, \vec{b}) = \sqrt{\sum_{i=1}^{n} (a_i - b_i)^2}$
    * **点积 (Dot Product)**:
        * 如果向量已经归一化 (长度为1)，则点积等同于余弦相似度。
        * $S_{dot}(\vec{a}, \vec{b}) = \vec{a} \cdot \vec{b} = \sum_{i=1}^{n} a_i b_i$

* **在 Python 中计算**:
    * 可以使用 `numpy` 或 `scipy.spatial.distance` 等库来轻松计算这些度量。

* **示例**:

    ```python
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity # scikit-learn 提供了便捷的函数
    from scipy.spatial.distance import cosine # scipy 的 cosine 返回的是 (1 - similarity) 即距离

    from langchain_openai import OpenAIEmbeddings

    # 假设我们已经通过 embeddings_model.embed_documents() 或 embed_query() 获得了向量
    embeddings_model = OpenAIEmbeddings()

    text_A = "今天天气真好，适合出去玩。"
    text_B = "阳光明媚，是个散步的好日子。"
    text_C = "这部电影的剧情非常复杂。"

    vector_A = embeddings_model.embed_query(text_A)
    vector_B = embeddings_model.embed_query(text_B)
    vector_C = embeddings_model.embed_query(text_C)

    # 将向量转换为 NumPy 数组以便计算
    vec_A_np = np.array(vector_A).reshape(1, -1) # reshape 用于 cosine_similarity 函数的输入格式
    vec_B_np = np.array(vector_B).reshape(1, -1)
    vec_C_np = np.array(vector_C).reshape(1, -1)

    # 1. 使用 sklearn.metrics.pairwise.cosine_similarity
    similarity_AB = cosine_similarity(vec_A_np, vec_B_np)[0][0]
    similarity_AC = cosine_similarity(vec_A_np, vec_C_np)[0][0]
    similarity_BC = cosine_similarity(vec_B_np, vec_C_np)[0][0]

    print(f"文本 A: '{text_A}'")
    print(f"文本 B: '{text_B}'")
    print(f"文本 C: '{text_C}'")
    print(f"A 和 B 之间的余弦相似度: {similarity_AB:.4f}") # 应该较高
    print(f"A 和 C 之间的余弦相似度: {similarity_AC:.4f}") # 应该较低
    print(f"B 和 C 之间的余弦相似度: {similarity_BC:.4f}") # 应该较低

    # 2. 使用 NumPy 手动计算余弦相似度 (更底层)
    def manual_cosine_similarity(vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        norm_vec1 = np.linalg.norm(vec1)
        norm_vec2 = np.linalg.norm(vec2)
        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0 # 避免除以零
        return dot_product / (norm_vec1 * norm_vec2)

    similarity_AB_manual = manual_cosine_similarity(np.array(vector_A), np.array(vector_B))
    print(f"A 和 B 之间的手动计算余弦相似度: {similarity_AB_manual:.4f}")

    # 欧氏距离示例 (使用 scipy)
    from scipy.spatial.distance import euclidean
    distance_AB = euclidean(np.array(vector_A), np.array(vector_B))
    distance_AC = euclidean(np.array(vector_A), np.array(vector_C))
    print(f"A 和 B 之间的欧氏距离: {distance_AB:.4f}") # 距离越小越相似
    print(f"A 和 C 之间的欧氏距离: {distance_AC:.4f}") # 距离越大越不相似
    ```

在实际应用中（如语义搜索），通常会将一个查询向量与大量文档向量进行比较，然后根据相似度得分对文档进行排序，返回最相似的文档。向量数据库 (Vector Databases) 专门为此类大规模相似性搜索进行了优化。

## 模块三：数据连接 (Data Connection) 详解

在构建基于大型语言模型 (LLM) 的应用程序时，往往需要将外部数据源与 LLM 连接起来。这可能是为了给 LLM 提供最新的信息、特定领域的知识，或者允许 LLM 与用户私有数据进行交互 (例如，在 RAG - Retrieval Augmented Generation 架构中)。LangChain 的数据连接模块提供了一系列工具来加载、转换和存储数据，以便 LLM 可以有效地使用它们。“文档 (Document)”是 LangChain 中表示一块文本及其关联元数据 (metadata) 的核心概念。

---

### 第七章：文档加载 (Document Loaders)

文档加载器 (Document Loaders) 负责从各种来源获取数据，并将其统一转换为 LangChain 的 `Document` 对象。每个 `Document` 对象包含 `page_content` (文本内容) 和 `metadata` (关于该文本的附加信息，如来源、页码、标题等)。

#### 7.1 从不同数据源加载文档

LangChain 提供了大量的内置文档加载器，支持从各种常见及不常见的数据源加载数据。这使得开发者可以轻松地将不同格式和来源的数据整合到其 LLM 应用中。

**支持的数据源类型包括但不限于**:

* **文件系统 (File System)**:
    * 纯文本文件 (`.txt`, `.md`, `.csv`, `.json`, `.html` 等)
    * PDF 文件 (`.pdf`)
    * Word 文档 (`.doc`, `.docx`)
    * PowerPoint 演示文稿 (`.ppt`, `.pptx`)
    * Excel 表格 (`.xls`, `.xlsx`)
    * 代码文件 (各种编程语言)
    * EPUB 电子书
* **网页内容 (Web Content)**:
    * 单个网页 HTML
    * 整个网站爬取 (Sitemaps, Recursive crawling)
    * YouTube 视频字幕
    * RSS Feeds
* **在线服务和数据库 (Online Services & Databases)**:
    * Notion 页面和数据库
    * Google Drive (Docs, Sheets, Slides)
    * Slack 频道
    * Discord 聊天记录
    * GitHub 仓库 (Issues, PRs, Code)
    * SQL 数据库
    * NoSQL 数据库 (MongoDB, Elasticsearch 等)
    * Confluence 页面
    * Jira Issues
    * Airbyte (通过 Airbyte 加载各种数据源)
    * Wikipedia
    * Hacker News
    * AWS S3 存储桶中的文件
* **多媒体与其他 (Multimedia & Others)**:
    * 图片 (通过 OCR 提取文本)
    * 音频 (通过语音转文本服务提取文本)

LangChain 的文档加载器生态系统非常庞大且持续增长，大部分加载器位于 `langchain_community.document_loaders` 包中。

#### 7.2 常用 Document Loaders 介绍和使用

下面介绍几种常用的文档加载器及其基本用法。

* **`TextLoader` (文本文件加载器)**:
    * 用途: 加载本地文件系统中的纯文本文件 (如 `.txt`, `.md`, `.py`, `.json` 等)。
    * 特点: 简单直接，通常将整个文件内容加载为一个 `Document`。
    * 安装: 通常是 LangChain 核心库的一部分，无需额外安装。

    ```python
    from langchain_community.document_loaders import TextLoader

    # 假设有一个名为 example.txt 的文件
    # file_path = "./example.txt"
    # with open(file_path, "w", encoding="utf-8") as f:
    #     f.write("这是示例文本文件的第一行。\n")
    #     f.write("这是第二行，包含一些 LangChain 的信息。\n")

    loader_txt = TextLoader("./example.txt", encoding="utf-8") # 指定编码很重要
    documents_txt = loader_txt.load()

    print(f"从 TXT 文件加载了 {len(documents_txt)} 个文档。")
    for doc in documents_txt:
        print(f"内容 (前50字符): {doc.page_content[:50]}...")
        print(f"元数据: {doc.metadata}")
        # metadata 通常包含 {'source': './example.txt'}
    ```

* **`PyPDFLoader` (PDF 文件加载器)**:
    * 用途: 加载 PDF 文件中的文本内容。
    * 特点: 逐页加载 PDF，每页内容成为一个单独的 `Document` 对象。元数据通常包含源文件名和页码。
    * 安装: 需要安装 `pypdf` 包 (`pip install pypdf`)。

    ```python
    from langchain_community.document_loaders import PyPDFLoader

    # 假设有一个名为 sample.pdf 的文件
    # 为了运行此示例，你需要一个PDF文件。你可以创建一个简单的PDF。
    # file_path_pdf = "./sample.pdf"

    loader_pdf = PyPDFLoader("./sample.pdf") # 替换为你的PDF文件路径
    documents_pdf = loader_pdf.load() # load_and_split() 方法会同时加载并按页分割

    print(f"从 PDF 文件加载了 {len(documents_pdf)} 个文档 (每页一个文档)。")
    if documents_pdf:
        print(f"第一页内容 (前100字符): {documents_pdf[0].page_content[:100]}...")
        print(f"第一页元数据: {documents_pdf[0].metadata}")
        # metadata 通常包含 {'source': './sample.pdf', 'page': 0}
    ```
    * **其他 PDF 加载器**: LangChain 还支持其他 PDF 加载器，如 `PDFMinerLoader`, `PyMuPDFLoader` (fitz), `UnstructuredPDFLoader` 等，它们在处理复杂布局或扫描PDF方面可能有不同表现。

* **`WebBaseLoader` (网页加载器)**:
    * 用途: 从给定的 URL 加载网页内容。
    * 特点: 通常会尝试提取网页的主要文本内容，去除 HTML 标签。
    * 安装: 需要安装 `beautifulsoup4` 包 (`pip install beautifulsoup4`)。

    ```python
    from langchain_community.document_loaders import WebBaseLoader

    url = "[https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)" # 一个示例博客文章
    loader_web = WebBaseLoader(url)
    documents_web = loader_web.load()

    print(f"从 URL 加载了 {len(documents_web)} 个文档。")
    if documents_web:
        print(f"网页内容 (前200字符): {documents_web[0].page_content[:200]}...")
        print(f"网页元数据: {documents_web[0].metadata}")
        # metadata 通常包含 {'source': url, 'title': '...', 'description': '...', 'language': '...'}
    ```
    * **异步版本和批量加载**: `WebBaseLoader` 也支持异步加载和一次加载多个 URL。
        ```python
        loader_web_multiple = WebBaseLoader(
            ["[https://www.espn.com](https://www.espn.com)", "[https://www.cnn.com](https://www.cnn.com)"]
        )
        # docs_multiple = loader_web_multiple.load()

        # 异步加载 (需要运行在 asyncio 事件循环中)
        async def main_web_async():
            loader_web_async = WebBaseLoader("[https://www.bbc.com/news](https://www.bbc.com/news)")
            docs_async = await loader_web_async.aload()
            print(f"异步加载的文档内容 (前100字符): {docs_async[0].page_content[:100]}...")
        # import asyncio
        # asyncio.run(main_web_async())
        ```

* **`CSVLoader` (CSV 文件加载器)**:
    * 用途: 加载 CSV 文件中的数据。
    * 特点: 通常将 CSV 文件中的每一行视为一个独立的 `Document`。你可以指定哪一列作为 `page_content`，其他列可以作为 `metadata`。
    * 安装: 通常是 LangChain 核心库的一部分，但依赖 Python 内置的 `csv` 模块。

    ```python
    from langchain_community.document_loaders.csv_loader import CSVLoader
    import csv

    # 创建一个示例 CSV 文件
    # csv_file_path = "./sample_data.csv"
    # with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["id", "question", "answer", "category"])
    #     writer.writerow([1, "什么是 LangChain?", "一个LLM应用开发框架。", "技术"])
    #     writer.writerow([2, "Python 难学吗?", "因人而异，但有大量学习资源。", "编程"])

    loader_csv = CSVLoader(
        file_path="./sample_data.csv",
        csv_args={ # 可以传递给 Python csv.DictReader 的参数
            'delimiter': ',',
            'quotechar': '"',
            # 'fieldnames': ['id', 'question', 'answer', 'category'] # 如果没有表头行，可以指定
        },
        source_column="id", # 可选，指定哪一列作为 document.metadata['source']
        # content_columns=['question', 'answer'] # 指定多列合并为 page_content (实验性)
    )
    # 默认情况下，CSVLoader 会将所有列的键值对形式作为 page_content
    # 例如: "id: 1\nquestion: 什么是 LangChain?\nanswer: 一个LLM应用开发框架。\ncategory: 技术"

    # 如果你想让某一特定列作为 page_content，而其他列作为 metadata，
    # 通常的做法是加载后进行转换，或者构建自定义的加载逻辑，
    # 或者使用更高级的加载器如 `DataFrameLoader` (如果数据适合Pandas DataFrame)。

    # 简单加载，每行是一个文档，内容是所有列的组合
    documents_csv = loader_csv.load()
    # print(f"从 CSV 文件加载了 {len(documents_csv)} 个文档。")
    # if documents_csv:
    #     print(f"第一个文档内容: {documents_csv[0].page_content}")
    #     print(f"第一个文档元数据: {documents_csv[0].metadata}")
    #     # metadata 通常包含 {'source': '1', 'row': 0} (如果source_column='id')
    ```
    * 对于更复杂的 CSV 处理或希望将特定列作为 `page_content`，可能需要结合 `pandas` 和 `DataFrameLoader`，或者在加载后进行自定义处理。

* **`YoutubeLoader` (YouTube 视频加载器)**:
    * 用途: 加载 YouTube 视频的字幕/转录稿。
    * 特点: 需要视频 URL，并会下载可用的字幕。
    * 安装: 需要安装 `youtube-transcript-api` 包 (`pip install youtube-transcript-api`)。

    ```python
    from langchain_community.document_loaders import YoutubeLoader

    video_url = "[https://www.youtube.com/watch?v=j_K3_T3eSbw](https://www.youtube.com/watch?v=j_K3_T3eSbw)" # 示例视频 (一个关于冥想的短视频)
    loader_youtube = YoutubeLoader.from_youtube_url(
        video_url,
        add_video_info=True,  # 会在 metadata 中添加视频标题、作者等信息
        language=["en", "zh-Hans"], # 尝试加载英文或简体中文字幕
        translation="en", # 如果找到其他语言字幕，尝试翻译成英文
    )
    documents_youtube = loader_youtube.load()

    print(f"从 YouTube URL 加载了 {len(documents_youtube)} 个文档。")
    if documents_youtube:
        print(f"视频字幕内容 (前200字符): {documents_youtube[0].page_content[:200]}...")
        print(f"视频元数据: {documents_youtube[0].metadata}")
        # metadata 可能包含 {'source': 'j_K3_T3eSbw', 'title': '...', 'author': '...', 'length': ..., 'publish_date': ...}
    ```

这只是众多可用加载器中的一小部分。选择哪个加载器取决于你的数据源和特定需求。LangChain 文档网站是查找特定加载器及其选项的最佳资源。

#### 7.3 自定义 Document Loader

尽管 LangChain 提供了大量预置的文档加载器，但有时你可能需要从 LangChain 尚不支持的专有数据源、特定格式的文件或内部 API 加载数据。在这种情况下，你可以创建自己的自定义文档加载器。

* **基本步骤**:
    1.  **继承 `BaseLoader`**: 你的自定义加载器类需要继承自 `langchain_core.document_loaders.base.BaseLoader`。
    2.  **实现 `load()` 或 `lazy_load()` 方法**:
        * `load() -> List[Document]`: 这个方法应该包含从你的数据源加载数据并将其转换为一个或多个 `Document` 对象列表的逻辑。这是最常用的实现方式。
        * `lazy_load() -> Iterator[Document]`: 这个方法返回一个文档的迭代器。这对于处理非常大的数据集或流式数据源很有用，因为它允许你逐个处理文档，而不是一次性将所有文档加载到内存中。如果你实现了 `lazy_load`，`BaseLoader` 会自动提供一个基于它的 `load` 实现。
    3.  **构造 `Document` 对象**: 在你的加载方法中，你需要创建 `langchain_core.documents.Document` 的实例，至少提供 `page_content` (字符串) 和可选的 `metadata` (字典)。

* **示例：一个简单的自定义加载器，从字符串列表加载数据**

    ```python
    from typing import List, Iterator
    from langchain_core.document_loaders.base import BaseLoader
    from langchain_core.documents import Document

    class MyCustomStringListLoader(BaseLoader):
        """一个简单的自定义加载器，从字符串列表加载数据，每个字符串成为一个文档。"""

        def __init__(self, string_list: List[str], source_name: str = "custom_list"):
            self.string_list = string_list
            self.source_name = source_name

        def lazy_load(self) -> Iterator[Document]:
            """惰性加载，逐个产生文档。"""
            for i, text_content in enumerate(self.string_list):
                metadata = {
                    "source": self.source_name,
                    "index": i,
                    "length": len(text_content)
                }
                yield Document(page_content=text_content, metadata=metadata)

        # 如果只实现 lazy_load，load() 方法会自动获得。
        # 如果想覆盖 load() 以实现不同逻辑（例如一次性加载），也可以直接实现它：
        # def load(self) -> List[Document]:
        #     """一次性加载所有文档。"""
        #     documents = []
        #     for i, text_content in enumerate(self.string_list):
        #         metadata = {
        #             "source": self.source_name,
        #             "index": i,
        #             "length": len(text_content)
        #         }
        #         documents.append(Document(page_content=text_content, metadata=metadata))
        #     return documents

    # # 使用自定义加载器
    # my_data = [
    #     "这是第一个自定义文档。",
    #     "LangChain 允许创建自定义组件。",
    #     "第三条简单记录。"
    # ]
    # custom_loader = MyCustomStringListLoader(string_list=my_data, source_name="my_string_source")

    # # 使用 load()
    # # loaded_docs_custom = custom_loader.load()
    # # print(f"\n--- 自定义加载器 (load) ---")
    # # for doc in loaded_docs_custom:
    # #     print(f"内容: {doc.page_content}")
    # #     print(f"元数据: {doc.metadata}")

    # # 使用 lazy_load()
    # # print(f"\n--- 自定义加载器 (lazy_load) ---")
    # # for doc in custom_loader.lazy_load():
    # #     print(f"内容: {doc.page_content}")
    # #     print(f"元数据: {doc.metadata}")
    ```

通过实现自定义加载器，你可以将任何可以编程访问的数据源集成到 LangChain 工作流中，极大地扩展了 LangChain 应用的数据连接能力。在实现时，务必考虑错误处理、资源管理（如关闭文件或网络连接）以及如何有效地构造有用的元数据。

### 第八章：文档转换 (Document Transformers)

在将文档加载到 LangChain 后，通常需要对这些文档进行进一步处理，然后才能有效地将它们用于 LLM 应用（例如，在 RAG 流程中构建向量索引或直接作为 LLM 的上下文）。文档转换器 (Document Transformers) 就是用于执行这些转换操作的组件。它们接收一个或多个 `Document` 对象，并返回经过转换的 `Document` 对象列表。

常见的转换操作包括：将长文档分割成小块、清洗文本内容、提取或添加元数据等。

#### 8.1 文本分割 (Text Splitters)：按字符、Token、递归等方式分割长文本

大型语言模型 (LLMs) 通常对其可以处理的上下文长度有限制（即 token 限制）。因此，在处理长文档时，必须将其分割成更小的、符合模型限制的块 (chunks)。文本分割器 (Text Splitters) 就是为此设计的。

* **为什么需要文本分割？**
    * **LLM 上下文窗口限制**: 大多数 LLM 无法一次处理非常长的文本。例如，一些模型的上下文窗口可能是几千个 token。
    * **检索效率和相关性**: 在 RAG 架构中，将文档分割成较小的、语义连贯的块，可以提高检索到最相关信息的几率。用户查询可能只与长文档中的一小部分相关。
    * **成本和性能**: 处理更小的文本块通常更快，API 调用成本也更低。

* **常用的文本分割策略和 LangChain 中的实现**:

    * **`CharacterTextSplitter` (按字符分割)**:
        * **原理**: 按照指定的字符（或字符串序列）来分割文本，并尝试将块保持在指定的大小 (`chunk_size`) 附近。它还支持 `chunk_overlap` 参数，用于在相邻块之间创建重叠部分，以帮助保持上下文的连续性。
        * **适用场景**: 简单文本，当分隔符明确且一致时。
        * **示例**:
            ```python
            from langchain_text_splitters import CharacterTextSplitter
            from langchain_core.documents import Document

            long_text = "这是一段非常非常长的文本，需要被分割成多个小块。我们希望每个小块大约10个字符，并且块之间有2个字符的重叠。LangChain 提供了多种分割器。"
            doc = Document(page_content=long_text, metadata={"source": "my_long_document"})

            char_splitter = CharacterTextSplitter(
                separator="。",  # 按句号分割
                chunk_size=20,   # 目标块大小 (字符数)
                chunk_overlap=5, # 块之间的重叠字符数
                length_function=len, # 用于计算长度的函数
                is_separator_regex=False,
            )
            
            chunks = char_splitter.split_documents([doc]) # 也可以用 split_text(long_text)
                        # # print(f"原始文档分割成了 {len(chunks)} 个块:")
            for i, chunk in enumerate(chunks):
                print(f"--- 块 {i+1} ---")
                print(f"内容: {chunk.page_content}")
                print(f"元数据: {chunk.metadata}") # 元数据会被继承
            ```

    * **`RecursiveCharacterTextSplitter` (递归字符分割)**:
        * **原理**: 这是推荐的通用入门分割器。它接收一个字符列表作为分隔符的优先级顺序 (例如 `["\n\n", "\n", " ", ""]`)。它首先尝试按第一个分隔符分割。如果得到的块仍然太大，它会递归地使用列表中的下一个分隔符来分割这些块，直到块大小符合要求。
        * **适用场景**: 适用于大多数文本类型，因为它能较好地尝试在语义边界（如段落、句子）上进行分割。
        * **示例**:
            ```python
            from langchain_text_splitters import RecursiveCharacterTextSplitter
            from langchain_core.documents import Document

            another_long_text = "第一段内容。\n\n这是第二段，包含多个句子。例如这个句子。还有另一个句子。\n第三段只有一句话。"
            doc_recursive = Document(page_content=another_long_text, metadata={"source": "recursive_doc"})

            recursive_splitter = RecursiveCharacterTextSplitter(
                chunk_size=50,    # 目标块大小 (字符数)
                chunk_overlap=10,   # 块之间的重叠字符数
                separators=["\n\n", "\n", "。", "，", " ", ""], # 尝试按这些分隔符顺序分割
                length_function=len,
            )
            
            chunks_recursive = recursive_splitter.split_documents([doc_recursive])
            
            print(f"\n递归分割器将文档分割成了 {len(chunks_recursive)} 个块:")
            for i, chunk in enumerate(chunks_recursive):
                print(f"--- 块 {i+1} ---")
                print(f"内容: {chunk.page_content}")
                print(f"元数据: {chunk.metadata}")
            ```

    * **按 Token 分割 (Token-based Splitters)**:
        * **原理**: 这些分割器根据 LLM 计算 token 的方式来分割文本。这对于精确控制传递给模型的 token 数量非常重要。
        * **实现**:
            * **`TokenTextSplitter`**: 使用指定的编码（如 OpenAI 的 `cl100k_base` for `gpt-3.5-turbo` and `gpt-4`）来计算 token 数量并分割。
            * **`SentenceTransformersTokenTextSplitter`**: 针对 Sentence Transformers 模型使用的 tokenization。
            * 通常需要安装相应的 tokenizer 库 (如 `tiktoken` for OpenAI)。
        * **适用场景**: 当需要严格遵守特定模型的 token 限制时。
        * **示例 (使用 `tiktoken`，概念上类似于 `TokenTextSplitter`)**:
            ```python
            from langchain_text_splitters import TokenTextSplitter # 或者 CharacterTextSplitter.from_tiktoken_encoder
            from langchain_core.documents import Document
            import tiktoken # pip install tiktoken

            openai_text = "This is a text that we want to split based on OpenAI's token counting for gpt-3.5-turbo. Tokens are fundamental units for LLMs."
            doc_openai = Document(page_content=openai_text, metadata={"source": "openai_token_doc"})

            # 获取特定模型的编码器
            # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

            token_splitter = TokenTextSplitter(
                model_name="gpt-3.5-turbo", # 或者直接提供 encoding_name="cl100k_base"
                chunk_size=20,  # 目标块大小 (token 数)
                chunk_overlap=5 # 块之间的重叠 token 数
            )
            # 更推荐的方式是使用 CharacterTextSplitter.from_tiktoken_encoder
            # from langchain_text_splitters import CharacterTextSplitter
            # token_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            #     model_name="gpt-3.5-turbo",
            #     chunk_size=20,
            #     chunk_overlap=5,
            # )


            chunks_token = token_splitter.split_documents([doc_openai])
            
            print(f"\nToken 分割器将文档分割成了 {len(chunks_token)} 个块:")
            for i, chunk in enumerate(chunks_token):
                print(f"--- 块 {i+1} ---")
                print(f"内容: {chunk.page_content}")
                # 可以验证 token 数量
                # chunk_tokens = encoding.encode(chunk.page_content)
                # print(f"Token 数量: {len(chunk_tokens)}")
                print(f"元数据: {chunk.metadata}")
            ```

    * **其他分割器**: LangChain 还提供了针对特定格式 (如 Markdown, LaTeX, Python 代码) 的分割器，它们能够更好地理解这些格式的结构并进行智能分割。
        * `MarkdownTextSplitter`
        * `PythonCodeTextSplitter`
        * `LatexTextSplitter`

* **选择分割策略的关键因素**:
    * **文本类型**: 结构化文本（如代码、Markdown）可能受益于特定格式的分割器。
    * **语义连贯性**: 尽量在自然的断点（句子、段落）处分割，以保持块的语义完整性。`RecursiveCharacterTextSplitter` 通常在这方面做得不错。
    * **`chunk_size` 和 `chunk_overlap`**: 这些参数需要根据目标 LLM 的上下文窗口大小、嵌入模型的限制以及应用需求进行调整。适当的重叠有助于在块之间保持上下文。
    * **元数据保留**: 分割器通常会将原始文档的元数据复制到所有生成的块中，并可能添加新的元数据（如块的序号）。

#### 8.2 文本清洗和预处理

从各种来源加载的文档通常包含不需要的字符、格式问题或对 LLM 处理不友好的内容。在进行分割或嵌入之前，对文本进行清洗和预处理是很重要的一步。

* **常见的清洗任务**:
    * **去除 HTML 标签**: 从网页加载的内容通常包含 HTML 标签。
    * **去除多余空白**: 删除不必要的空格、换行符、制表符。
    * **规范化文本**: 转换为小写、处理特殊字符、去除不可见字符。
    * **去除噪音**: 删除广告、导航栏、页眉页脚等与主要内容无关的部分 (这可能在加载阶段或通过更专门的工具完成)。
    * **修正编码问题**。

* **LangChain 中的实现方式**:
    * **结合自定义代码**: 最常见的方法是使用 Python 的标准库 (如 `re` for 正则表达式, `html.parser` 或 `BeautifulSoup` for HTML) 或其他文本处理库，在 LangChain 的 `Document` 对象上直接操作 `page_content`。
    * **自定义 `DocumentTransformer`**: 你可以创建一个继承自 `BaseDocumentTransformer` 的类，并实现其 `transform_documents` 方法来封装你的清洗逻辑。
    * **链式操作**: LangChain 允许将多个文档转换器（包括文本分割器和自定义的清洗转换器）链接起来形成一个处理流水线。
    * **使用现有的转换器**: 一些社区提供的加载器或转换器可能内置了部分清洗功能。例如，`WebBaseLoader` 会尝试去除一些 HTML 结构。

* **示例：一个简单的自定义清洗转换器**

    ```python
    import re
    from typing import Sequence, Any
    from langchain_core.documents import Document
    from langchain_core.document_transformers import BaseDocumentTransformer

    class SimpleTextCleaner(BaseDocumentTransformer):
        """一个简单的文本清洗器，去除多余空格并将文本转为小写。"""

        def transform_documents(
            self, documents: Sequence[Document], **kwargs: Any
        ) -> Sequence[Document]:
            cleaned_documents = []
            for doc in documents:
                cleaned_content = doc.page_content.lower() # 转为小写
                cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip() # 去除多余空格
                # 可以添加更多清洗规则，例如去除特定字符等
                # cleaned_content = re.sub(r'[^\w\s]', '', cleaned_content) # 去除非字母数字空格字符

                # 创建新的 Document 或修改现有的 (推荐创建新的以保持不变性)
                cleaned_doc = Document(page_content=cleaned_content, metadata=doc.metadata.copy())
                cleaned_documents.append(cleaned_doc)
            return cleaned_documents

        async def atransform_documents(
            self, documents: Sequence[Document], **kwargs: Any
        ) -> Sequence[Document]:
            # 简单的同步转异步实现，实际应用中如果清洗逻辑IO密集，可以优化
            return self.transform_documents(documents, **kwargs)


    # 假设我们有一些待清洗的文档
    raw_docs = [
        Document(page_content="  这是   一个 \n\n 文档，包含 大写字母   和 多余空格. HTML: <p>text</p>", metadata={"source": "doc1"}),
        Document(page_content="另一个   例子\t需要清理一下.", metadata={"source": "doc2"})
    ]

    cleaner = SimpleTextCleaner()
    cleaned_docs = cleaner.transform_documents(raw_docs)

    print("\n--- 清洗后的文档 ---")
    for doc in cleaned_docs:
        print(f"内容: '{doc.page_content}'")
        print(f"元数据: {doc.metadata}")
    ```
    * **注意**: 对于复杂的 HTML 清洗，使用 `BeautifulSoup` 通常更稳健。可以在加载器中集成，或者创建一个专门的 `BeautifulSoupTransformer`。LangChain 社区中可能有类似的实现。

#### 8.3 元数据提取和添加

文档的元数据 (metadata) 对于后续的检索、过滤和上下文理解非常重要。文档转换器也可以用来从文档内容中提取新的元数据，或添加/修改现有的元数据。

* **为什么重要？**
    * **增强检索**: 可以根据元数据字段（如日期、作者、类别、关键词）过滤搜索结果。
    * **上下文提供**: 将元数据信息（如文档标题、来源）与文本块一起提供给 LLM，可以帮助 LLM 更好地理解块的上下文。
    * **数据分析和组织**: 元数据有助于对文档集合进行分析和组织。

* **实现方式**:
    * **自定义 `DocumentTransformer`**:
        * 创建一个转换器，分析 `doc.page_content` 来提取信息（如使用正则表达式提取日期、实体，或使用小型 NLP 模型提取关键词）。
        * 将提取的信息添加到 `doc.metadata` 字典中。
    * **结合 LLM**:
        * 对于更复杂的元数据提取，如生成摘要、提取主题或判断情感，可以设计一个链 (Chain)，将文档内容传递给 LLM，并指示 LLM 输出所需的元数据信息。然后，使用一个转换器将 LLM 的输出添加到文档的元数据中。
        * LangChain 提供了如 `LLMChainExtractor` (旧版) 或通过 LCEL 构建类似的逻辑。
    * **修改现有元数据**: 例如，在文本分割后，可以添加块的序号或计算块的 token 数量作为新的元数据。

* **示例：一个简单的转换器，添加文本长度和修改来源元数据**

    ```python
    from typing import Sequence, Any
    from langchain_core.documents import Document
    from langchain_core.document_transformers import BaseDocumentTransformer

    class MetadataEnhancer(BaseDocumentTransformer):
        """一个简单的元数据增强器，添加文本长度并修改来源。"""

        def __init__(self, source_prefix: str = "processed_"):
            self.source_prefix = source_prefix

        def transform_documents(
            self, documents: Sequence[Document], **kwargs: Any
        ) -> Sequence[Document]:
            enhanced_documents = []
            for doc in documents:
                new_metadata = doc.metadata.copy() # 复制现有元数据
                new_metadata["text_length"] = len(doc.page_content)
                if "source" in new_metadata:
                    new_metadata["original_source"] = new_metadata["source"] # 保留原始来源
                    new_metadata["source"] = f"{self.source_prefix}{new_metadata['source']}"
                else:
                    new_metadata["source"] = f"{self.source_prefix}unknown"

                enhanced_doc = Document(page_content=doc.page_content, metadata=new_metadata)
                enhanced_documents.append(enhanced_doc)
            return enhanced_documents

        async def atransform_documents(
            self, documents: Sequence[Document], **kwargs: Any
        ) -> Sequence[Document]:
            return self.transform_documents(documents, **kwargs)

    # 假设我们有一些文档
    docs_to_enhance = [
        Document(page_content="这是一个示例文档。", metadata={"source": "fileA.txt", "author": "AI"}),
        Document(page_content="另一个不同长度的文档。", metadata={"source": "web_page_B"})
    ]

    enhancer = MetadataEnhancer(source_prefix="enhanced_v1_")
    enhanced_docs = enhancer.transform_documents(docs_to_enhance)

    print("\n--- 元数据增强后的文档 ---")
    for doc in enhanced_docs:
        print(f"内容: '{doc.page_content}'")
        print(f"元数据: {doc.metadata}")
    ```

* **使用 LLM 提取元数据 (概念性)**
    * 你可以构建一个提示，要求 LLM 从文本中提取特定信息或生成摘要。
    * 例如，提示可以是：“请从以下文本中提取主要议题，并以逗号分隔的列表形式返回：\n\n{document_content}”
    * 然后，将 LLM 的输出解析并添加到 `metadata` 中。这通常涉及构建一个包含 `PromptTemplate`, LLM 和 `OutputParser` 的链。

文档转换是数据准备流程中的关键步骤，确保了输入到 LLM 或向量存储中的数据是干净、结构化且包含有用元数据的。通过组合使用 LangChain 提供的内置转换器和自定义转换器，可以构建强大的数据处理流水线。



### 第九章：向量存储 (Vector Stores) 与检索 (Retrievers)

在 Retrieval Augmented Generation (RAG) 等应用中，核心环节是将用户查询与一个大规模的文档集合进行匹配，找出最相关的文档片段，然后将这些片段作为上下文提供给 LLM 以生成更准确、更具信息量的回答。向量存储 (Vector Stores) 和检索器 (Retrievers) 是实现这一目标的关键组件。

#### 9.1 向量数据库的基本概念 (FAISS, Chroma, Pinecone, Weaviate 等)

* **什么是向量数据库 (Vector Database)？**
    * 向量数据库是专门设计用来存储、管理和高效检索高维向量（即文本嵌入）的数据库系统。
    * 传统的数据库主要处理结构化数据（如关系型数据库）或键值对（如 NoSQL 数据库），而向量数据库则优化了对向量数据的相似性搜索操作。

* **为什么需要向量数据库？**
    * **高效相似性搜索**: 当文档集合非常大时（成千上万甚至数百万个嵌入向量），线性地计算查询向量与每个文档向量之间的相似度会非常慢。向量数据库使用近似最近邻 (Approximate Nearest Neighbor, ANN) 搜索算法，能够在牺牲极小精度的情况下，极大地提升搜索速度。
    * **可扩展性**: 能够处理大规模的向量数据，并支持数据的动态添加、更新和删除。
    * **元数据过滤**: 除了向量相似性搜索，许多向量数据库还支持根据与向量关联的元数据 (metadata) 进行过滤，从而实现更精确的检索。
    * **持久化存储**: 提供数据的持久化存储和管理功能。

* **常见的向量数据库/库**:
    LangChain 与多种向量数据库和库集成，可以分为以下几类：

    1.  **内存/本地库 (In-memory / Local Libraries)**:
        * **`FAISS` (Facebook AI Similarity Search)**: 一个由 Facebook AI 开发的高效相似性搜索库。非常适合快速原型验证和中小型数据集，可以直接在内存中运行。LangChain 通过 `FAISS` 类集成。
        * **`Chroma`**: 一个开源的嵌入数据库，设计为易于使用和集成。可以作为内存数据库运行，也可以作为客户端-服务器模式运行。LangChain 通过 `Chroma` 类集成。它也支持元数据过滤和多种特性。
        * **`LanceDB`**: 一个开源的、为AI设计的嵌入式向量数据库，支持零拷贝、版本控制和生态系统集成。

    2.  **开源自托管数据库 (Open-source Self-hosted Databases)**:
        * **`Weaviate`**: 一个开源的、云原生的向量搜索引擎。支持模块化架构，可以集成不同的嵌入模型，并提供 GraphQL API。LangChain 通过 `Weaviate` 类集成。
        * **`Milvus`**: 一个开源的云原生向量数据库，专为大规模向量搜索设计，具有高可用性和可扩展性。
        * **`Qdrant`**: 一个开源的向量相似性搜索引擎和向量数据库，提供 REST API 和多种客户端库。
        * **`PGVector`**: PostgreSQL 的一个开源扩展，使其能够存储和搜索向量嵌入。

    3.  **托管云服务 (Managed Cloud Services)**:
        * **`Pinecone`**: 一个完全托管的向量数据库服务，易于使用且高度可扩展，专为生产环境设计。LangChain 通过 `Pinecone` 类集成。
        * **`Weaviate Cloud Services (WCS)`**: Weaviate 的托管云服务。
        * **`Google Cloud Vertex AI Vector Search` (以前的 Matching Engine)**: Google Cloud 提供的托管相似性搜索服务。
        * **`Azure AI Search` (以前的 Azure Cognitive Search)**: 微软 Azure 提供的搜索服务，支持向量搜索功能。
        * **`Amazon OpenSearch Service` / `Amazon Kendra`**: AWS 提供的服务，也支持向量搜索能力。
        * 许多其他云数据库提供商也开始集成向量搜索功能。

* **核心特性**:
    * **向量索引 (Vector Indexing)**: 为了加速搜索，向量数据库会对存储的向量构建索引结构 (如 HNSW, IVF, LSH 等)。
    * **CRUD 操作**: 支持向量及其元数据的创建 (Create)、读取 (Read)、更新 (Update) 和删除 (Delete)。
    * **相似性搜索**: 根据查询向量找到最相似的 K 个向量 (Top-K search)。
    * **元数据过滤**: 在进行向量搜索之前或之后，根据附加的元数据条件过滤结果。

#### 9.2 将文档嵌入并存储到向量数据库

将文档加载到向量数据库通常涉及以下步骤：

1.  **加载文档 (Load Documents)**: 使用文档加载器 (Document Loaders) 从各种来源加载原始数据。
2.  **分割文档 (Split Documents)**: 使用文本分割器 (Text Splitters) 将长文档分割成较小的、语义连贯的块。这是因为嵌入模型通常对输入文本长度有限制，并且较小的块能提供更精确的检索结果。
3.  **选择嵌入模型 (Choose Embedding Model)**: 选择一个文本嵌入模型 (Text Embedding Model) 将文本块转换为向量表示。
4.  **嵌入并存储 (Embed and Store)**: 将分割后的文本块通过嵌入模型转换为向量，然后将这些向量及其关联的文本内容和元数据一起存储到向量数据库中。

LangChain 提供了便捷的方法来执行这些操作，通常是通过向量存储类的 `from_documents()` 方法。

* **示例 (使用 `Chroma` 作为本地向量存储和 `OpenAIEmbeddings`)**:

    ```python
    from langchain_community.document_loaders import TextLoader
    from langchain_text_splitters import CharacterTextSplitter
    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores import Chroma
    from langchain_core.documents import Document
    import os

    # 0. 设置环境 (例如 OpenAI API Key)
    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

    # 1. 准备示例文档 (实际应用中会用 Document Loaders)
    documents_data = [
        Document(page_content="猫是一种小型食肉哺乳动物。", metadata={"source": "doc1", "category": "animal"}),
        Document(page_content="狗是人类的好朋友，也是一种哺乳动物。", metadata={"source": "doc2", "category": "animal"}),
        Document(page_content="苹果是一种常见的水果，富含维生素。", metadata={"source": "doc3", "category": "fruit"}),
        Document(page_content="香蕉是热带水果，口感香甜。", metadata={"source": "doc4", "category": "fruit"}),
        Document(page_content="LangChain 是一个用于构建 LLM 应用的框架。", metadata={"source": "doc5", "category": "tech"})
    ]

    # 2. 初始化文本分割器 (如果文档较长)
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    docs_split = text_splitter.split_documents(documents_data)
    # 对于上面的短文本，可以不分割，直接使用 documents_data

    # 3. 初始化嵌入模型
    embeddings_model = OpenAIEmbeddings() # 假设使用 OpenAI

    # 4. 将文档嵌入并存储到 Chroma 向量数据库
    # persist_directory 用于指定 Chroma 数据持久化存储的路径
    # 如果目录不存在，它会被创建。如果已存在且包含数据，则会加载现有数据。
    persist_directory = 'db_chroma_example'

    vector_store = Chroma.from_documents(
        documents=documents_data, # 或者 docs_split 如果进行了分割
        embedding=embeddings_model,
        persist_directory=persist_directory # 指定持久化目录
    )

    print(f"文档已成功嵌入并存储到 Chroma at '{persist_directory}'")

    # 如果后续想从持久化存储中加载向量数据库：
    # vector_store_loaded = Chroma(persist_directory=persist_directory, embedding_function=embeddings_model)
    # print("从持久化存储中成功加载 Chroma 数据库。")

    # 测试一下相似性搜索
    # query = "关于动物的信息"
    # similar_docs = vector_store.similarity_search(query, k=2)
    # print(f"\n与查询 '{query}' 最相似的 {len(similar_docs)} 个文档:")
    # for doc in similar_docs:
    #     print(f" - 内容: {doc.page_content}")
    #     print(f"   元数据: {doc.metadata}")
    ```
    在这个例子中，`Chroma.from_documents()` 内部处理了将 `documents_data` 中的每个 `Document` 的 `page_content` 通过 `embeddings_model` 转换为向量，并将这些向量连同原始文本和元数据一起存入 `Chroma` 数据库中。

#### 9.3 构建不同类型的检索器 (VectorStoreRetriever, MultiQueryRetriever, SelfQueryRetriever 等)

一旦数据存储在向量数据库中，就需要一个“检索器 (Retriever)”来根据用户查询从中获取相关文档。检索器是 LangChain 中的一个标准接口，它只有一个核心方法 `get_relevant_documents(query: str)` (及其异步版本 `aget_relevant_documents`)。

* **`VectorStoreRetriever`**:
    * 这是最基础和最常用的检索器。它直接与向量存储交互，执行相似性搜索。
    * **配置**:
        * `search_type`: 可以是 `"similarity"` (默认，返回最相似的), `"mmr"` (Maximal Marginal Relevance，平衡相似性和多样性), 或 `"similarity_score_threshold"` (返回超过特定相似度阈值的文档)。
        * `search_kwargs`: 一个字典，传递给向量存储的搜索方法的参数，如 `k` (返回的文档数量) 或 `score_threshold`。
    * **示例**:
        ```python
        # 假设 vector_store 已经创建并加载了数据 (如上一节的 Chroma 实例)
        vector_store = Chroma(persist_directory='db_chroma_example', embedding_function=OpenAIEmbeddings())


        retriever_basic = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={'k': 2} # 获取最相似的2个文档
        )

        query = "关于水果的信息"
        relevant_docs_basic = retriever_basic.invoke(query) # invoke 是 Runnable 接口的方法

        print(f"\nVectorStoreRetriever 为查询 '{query}' 检索到的文档:")
        for doc in relevant_docs_basic:
            print(f" - 内容: {doc.page_content}, 元数据: {doc.metadata}")
        ```

* **`MultiQueryRetriever`**:
    * **原理**: 针对用户的一个初始查询，使用 LLM 从不同角度生成多个相似的查询。然后，对每个生成的查询都从向量存储中检索文档，最后合并所有结果并去重。
    * **目的**: 改善召回率，特别是当用户的原始查询可能不够明确或措辞不佳时。
    * **需要**: 一个 LLM 来生成查询变体。
    * **示例**:
        ```python
        from langchain.retrievers.multi_query import MultiQueryRetriever
        from langchain_openai import ChatOpenAI

        # 假设 vector_store 和 embeddings_model 已初始化
        vector_store = Chroma(persist_directory='db_chroma_example', embedding_function=OpenAIEmbeddings())
        llm = ChatOpenAI(temperature=0) # 用于生成查询变体

        retriever_multiquery = MultiQueryRetriever.from_llm(
            retriever=vector_store.as_retriever(search_kwargs={'k': 1}), # 每个子查询检索1个文档
            llm=llm
        )

        user_query_complex = "告诉我一些关于动物的有趣事实，特别是那些毛茸茸的。"
        # # LangChain 会生成类似这样的日志，显示生成的查询：
        # # INFO:langchain.retrievers.multi_query:Generated queries:
        # # ['动物有哪些有趣的事实？', '关于毛茸茸的动物，有什么独特之处？', '哪些动物以其毛发闻名，它们有什么特别的习性？']

        relevant_docs_multiquery = retriever_multiquery.invoke(user_query_complex)
        print(f"\nMultiQueryRetriever 为查询 '{user_query_complex}' 检索到的文档:")
        unique_contents = set()
        for doc in relevant_docs_multiquery:
            if doc.page_content not in unique_contents:
                print(f" - 内容: {doc.page_content}, 元数据: {doc.metadata}")
                unique_contents.add(doc.page_content)
        ```

* **`SelfQueryRetriever` (自查询检索器)**:
    * **原理**: 允许用户使用自然语言提问，该检索器内部使用 LLM 将自然语言查询转换为一个结构化的查询，这个结构化查询可以包含对向量存储中元数据的过滤条件，以及原始查询的语义部分。
    * **目的**: 实现更精确的检索，允许用户通过自然语言同时利用语义搜索和元数据过滤。
    * **需要**:
        * 一个 LLM。
        * 关于元数据字段的描述 (名称、类型、描述)，以便 LLM 知道可以过滤哪些字段。
        * 向量存储必须支持元数据过滤。
    * **示例**:
        ```python
        from langchain.chains.query_constructor.base import AttributeInfo
        from langchain.retrievers.self_query.base import SelfQueryRetriever
        from langchain_openai import ChatOpenAI

        # 假设 vector_store 和 embeddings_model 已初始化
        vector_store = Chroma(persist_directory='db_chroma_example', embedding_function=OpenAIEmbeddings())
        llm_self_query = ChatOpenAI(temperature=0)

        # 定义元数据字段的信息，以便 LLM 理解
        metadata_field_info = [
            AttributeInfo(
                name="source",
                description="文档的来源，例如 'doc1', 'doc2', 'web_page_X'",
                type="string",
            ),
            AttributeInfo(
                name="category",
                description="文档的类别，例如 'animal', 'fruit', 'tech'",
                type="string",
            ),
        ]
        document_content_description = "关于各种主题的简短文本片段" # 描述文档内容本身

        self_query_retriever = SelfQueryRetriever.from_llm(
            llm=llm_self_query,
            vectorstore=vector_store,
            document_contents=document_content_description,
            metadata_field_info=metadata_field_info,
            verbose=True, # 可以看到 LLM 生成的结构化查询
            enable_limit=True, # 允许在查询中指定返回数量限制
        )

        natural_language_query = "我想找一些关于水果的文档，特别是那些来源是 'doc3' 的"
        # LLM 可能会生成类似这样的结构化查询:
        # query='水果' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='source', value='doc3') limit=None

        relevant_docs_selfquery = self_query_retriever.invoke(natural_language_query)
        print(f"\nSelfQueryRetriever 为查询 '{natural_language_query}' 检索到的文档:")
        for doc in relevant_docs_selfquery:
            print(f" - 内容: {doc.page_content}, 元数据: {doc.metadata}")
        ```

* **其他检索器**:
    * **`ContextualCompressionRetriever`**: 在基础检索器之上工作，获取初始结果后，使用一个 `DocumentCompressor` (通常是 LLM) 来过滤掉不相关的文档或从文档中提取只与查询相关的片段，从而使传递给 LLM 的上下文更简洁、更相关。
    * **`EnsembleRetriever`**: 组合多个不同检索器的结果，并使用某种排序算法（如 Reciprocal Rank Fusion）对结果进行重新排序和融合。
    * **`ParentDocumentRetriever`**: 存储小块文本用于检索，但返回它们所属的更大的父文档块，以提供更完整的上下文。

#### 9.4 相似性搜索与语义检索的原理

* **语义检索 (Semantic Retrieval)**:
    * 核心思想是理解用户查询的“意图”或“含义”，而不仅仅是关键词匹配。
    * 通过文本嵌入模型，将查询和文档都转换为高维向量空间中的点。在这个空间中，语义上相似的文本（即使措辞不同）其向量表示也彼此靠近。

* **相似性搜索 (Similarity Search)**:
    * 一旦查询被转换为向量，相似性搜索的目标就是在向量数据库中找到与该查询向量最“接近”的文档向量。
    * **常用度量 (Recap from Chapter 6)**:
        * **余弦相似度 (Cosine Similarity)**: 衡量向量间的方向一致性。最常用，范围 [-1, 1] 或 [0, 1]。值越大越相似。
        * **欧氏距离 (Euclidean Distance / L2 Distance)**: 向量空间中两点间的直线距离。距离越小越相似。
        * **点积 (Dot Product / Inner Product)**: 如果向量已归一化，则等价于余弦相似度。
    * 不同的向量数据库可能默认使用不同的距离度量，或者允许用户指定。

* **近似最近邻 (ANN) 搜索**:
    * 对于非常大的数据集，精确地找到绝对最近的邻居（Exact Nearest Neighbor, ENN）计算成本太高。
    * ANN 算法通过构建巧妙的数据结构（索引）来加速搜索过程，例如：
        * **基于树的方法 (Tree-based)**: 如 Annoy。
        * **基于聚类的方法 (Clustering-based)**: 如 IVFADC (Inverted File with Asymmetric Distance Computation)，FAISS 中常用。将向量聚类，搜索时先定位到查询向量可能属于的簇，再在这些簇内搜索。
        * **基于图的方法 (Graph-based)**: 如 HNSW (Hierarchical Navigable Small World graphs)。构建一个多层图结构，从顶层粗略定位，逐层向下细化搜索。性能通常很好，是许多现代向量数据库（如 Weaviate, Qdrant, Chroma）的默认或推荐索引类型。
        * **LSH (Locality Sensitive Hashing)**: 通过哈希函数将相似项映射到相同的桶中。
    * ANN 算法在速度和精度之间进行权衡。通常可以配置索引参数来调整这种权衡。

#### 9.5 优化检索效果 (Top K, 过滤等)

仅仅检索出一些文档是不够的，还需要确保这些文档的质量和相关性。以下是一些优化检索效果的常用方法：

* **Top K (返回数量)**:
    * `k` 参数控制返回最相似文档的数量。
    * 选择合适的 `k` 值很重要：太小可能错过相关信息，太大可能引入噪音并增加后续 LLM 处理的成本和上下文长度。通常需要根据应用场景和 LLM 的上下文窗口大小来实验确定。

* **相似度得分阈值 (Similarity Score Threshold)**:
    * 除了返回 Top-K，还可以设置一个相似度得分的下限。只有相似度（或距离，取决于度量）超过（或低于）此阈值的文档才会被返回。
    * 这有助于过滤掉那些虽然在 Top-K 之内但与查询相关性不高的文档。
    * 在 LangChain 中，`VectorStoreRetriever` 的 `search_type="similarity_score_threshold"` 和 `search_kwargs={'score_threshold': ...}` 可以实现此功能。

* **元数据过滤 (Metadata Filtering)**:
    * 如 `SelfQueryRetriever` 所示，可以在向量搜索之前或之后根据文档的元数据进行过滤。
    * 例如，只在特定类别、特定日期范围或特定来源的文档中进行语义搜索。
    * 这能极大地缩小搜索范围，提高结果的相关性和搜索效率。大多数向量数据库都支持在查询时进行元数据过滤。

* **最大边际相关性 (Maximal Marginal Relevance - MMR)**:
    * 标准相似性搜索可能会返回多个彼此非常相似（冗余）的文档。
    * MMR 试图在返回与查询相关的文档的同时，也最大化文档之间的多样性。
    * 它迭代地选择文档，每次选择的文档不仅要与查询相似，也要与已选中的文档不那么相似。
    * 在 `VectorStoreRetriever` 中设置 `search_type="mmr"` 可以启用此功能。通常需要配置 `k` (总共获取的数量) 和 `Workspace_k` (MMR算法从中挑选的候选文档数量，通常 `Workspace_k > k`) 以及 `lambda_mult` (控制相似度和多样性之间的平衡，1 表示纯多样性，0 表示纯相似性)。

* **上下文压缩 (Contextual Compression)**:
    * `ContextualCompressionRetriever` 包装一个基础检索器和一个 `BaseDocumentCompressor`。
    * 基础检索器先获取一批文档，然后 `DocumentCompressor` 对这些文档进行处理：
        * **过滤**: 移除与查询完全不相关的文档。
        * **摘要/提取**: 从相关文档中提取与查询最相关的片段，或对文档进行摘要。
    * 常用的压缩器是 `LLMChainExtractor`，它使用 LLM 来判断文档的相关性或提取相关片段。
    * 目标是减少传递给最终 LLM 的上下文量，同时保留关键信息，提高效率和回答质量。

* **重新排序 (Re-ranking)**:
    * 在初始检索（例如基于向量相似性）之后，可以使用一个更复杂或更强大的模型（可能是另一个 LLM，如 Cohere Rerank API，或者交叉编码器模型）对检索到的 Top-K 文档进行重新排序。
    * 这个重排模型可以考虑更细致的语义关系或特定任务的偏好，从而将最相关的文档排在更前面。

* **混合搜索 (Hybrid Search)**:
    * 结合基于关键词的传统搜索（如 BM25）和向量语义搜索的优点。
    * 一些向量数据库和搜索引擎支持混合搜索，可以平衡两种搜索方式的结果。

优化检索是一个迭代的过程，通常需要根据具体应用和数据进行实验和调整。目标是为下游的 LLM 提供最相关、最简洁且信息量最丰富的上下文。



## 模块四：构建强大的链 (Chains)

在 LangChain 中，“链 (Chain)” 是一个核心概念，它代表了一系列对组件（如 LLM、工具、提示、解析器、其他链等）的调用，这些调用以特定的顺序组织起来，以完成一个更复杂的任务。链使得构建结构化、可重用和模块化的 LLM 应用成为可能。本模块将深入探讨不同类型的链以及如何有效地使用它们。

---

### 第十章：基础与顺序链 (Basic and Sequential Chains)

本章我们从最基础的链类型开始，逐步了解如何将多个步骤串联起来形成顺序执行的工作流。

#### 10.1 LLMChain：最基础的链

`LLMChain` 是 LangChain 中最基本也是最常用的链之一。它封装了与语言模型交互的核心流程：接收用户输入，使用这些输入格式化一个提示 (Prompt)，将格式化后的提示发送给语言模型 (LLM 或 ChatModel)，最后（可选地）通过输出解析器 (Output Parser)处理模型的响应。

* **核心组件**:
    1.  **提示模板 (Prompt Template)**: 如 `PromptTemplate` 或 `ChatPromptTemplate`，定义了如何根据输入变量构建发送给 LLM 的实际提示。
    2.  **语言模型 (LLM/ChatModel)**: 如 `ChatOpenAI`, `HuggingFaceHub` 等，负责根据提示生成文本。
    3.  **输出解析器 (Output Parser) (可选)**: 如 `StrOutputParser`, `PydanticOutputParser` 等，用于将 LLM 的原始输出（通常是字符串或消息对象）转换为更结构化或更易于使用的格式。

* **工作流程**:
    1.  接收一个包含输入变量的字典。
    2.  使用输入变量通过 Prompt Template 格式化提示。
    3.  将格式化后的提示发送给 LLM/ChatModel。
    4.  LLM/ChatModel 返回响应。
    5.  如果配置了 Output Parser，则用它解析 LLM 的响应。
    6.  返回最终结果（通常是包含输出键的字典，或者如果使用 LCEL 并且最后是解析器，则为解析后的类型）。

* **示例**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    # from langchain.chains import LLMChain # Legacy way
    import os

    # 0. 设置环境 (例如 OpenAI API Key)
    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

    # 1. 初始化组件
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    prompt_template = ChatPromptTemplate.from_template(
        "写一个关于 {topic} 的非常简短的单行笑话。"
    )
    output_parser = StrOutputParser() # 简单地将 AIMessage.content 提取为字符串

    # 2. 构建 LLMChain (使用 LCEL - LangChain Expression Language)
    # LCEL 是现代 LangChain 中组合组件的首选方式
    llm_chain_lcel = prompt_template | llm | output_parser

    # 3. 调用链 (invoke)
    topic_input = {"topic": "程序员"}
    # response_lcel = llm_chain_lcel.invoke(topic_input)
    # print(f"LCEL LLMChain 响应: {response_lcel}")

    # --- Legacy LLMChain (了解即可) ---
    # from langchain.chains import LLMChain
    # legacy_llm_chain = LLMChain(llm=llm, prompt=prompt_template, output_parser=output_parser)
    # 对于 legacy LLMChain，它期望输出是一个字典，需要指定 output_key
    # # legacy_llm_chain.output_key = "joke"
    # # response_legacy = legacy_llm_chain.invoke(topic_input)
    # # print(f"Legacy LLMChain 响应: {response_legacy}")
    # # # response_legacy 会是 {'topic': '程序员', 'joke': '为什么程序员喜欢戴眼镜？因为他们 C#'}
    # # print(f"Legacy LLMChain 的笑话: {response_legacy.get('joke')}")

    # 对于 LCEL 链，如果最后是 StrOutputParser，结果直接是字符串。
    # 如果想让 LCEL 链也返回字典，可以这样做：
    # from langchain_core.runnables import RunnablePassthrough
    # chain_with_dict_output = RunnablePassthrough.assign(joke=llm_chain_lcel)
    # response_dict_lcel = chain_with_dict_output.invoke(topic_input)
    # print(f"LCEL LLMChain (字典输出) 响应: {response_dict_lcel}")
    # # response_dict_lcel 会是 {'topic': '程序员', 'joke': '为什么程序员从不打扫卫生？因为他们有垃圾回收机制！'}

    ```
    虽然 LCEL 是组合 `PromptTemplate | LLM | OutputParser` 的现代方式，理解 `LLMChain` 的概念对于理解更复杂的传统链（如 `SequentialChain`）仍然有帮助。

#### 10.2 SimpleSequentialChain：单输入单输出的顺序链

`SimpleSequentialChain` 是一种按顺序执行多个链或可调用对象（callables）的链。它的特点是“简单”：前一个链的单个输出直接作为下一个链的单个输入。

* **特点**:
    * **线性流程**: 严格按照定义的顺序执行。
    * **单输入/单输出传递**: 每个子链必须只有一个输出，这个输出成为下一个子链的唯一输入。
    * **最终输出**: 整个 `SimpleSequentialChain` 的输出是最后一个子链的输出。
    * 只支持一个初始输入。

* **适用场景**: 适用于简单的、线性的多步骤任务，其中每个步骤的输出自然地成为下一步的输入，无需复杂的输入/输出映射。

* **示例**:
    假设我们想先生成一个关于某个主题的笑话（第一个 `LLMChain`），然后让另一个 `LLMChain` 评论这个笑话的幽默程度。

    ```python
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.chains import LLMChain # 使用 legacy LLMChain 以便与 SimpleSequentialChain 配合
    from langchain.chains import SimpleSequentialChain
    import os

    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 第一个链：生成笑话
    prompt_joke = ChatPromptTemplate.from_template(
        "写一个关于 {topic} 的简短笑话。"
    )
    # 对于 SimpleSequentialChain，子链的输出应该是原始文本，而不是字典。
    # 因此，我们通常不在这里为子 LLMChain 指定 output_parser，或者用 StrOutputParser，
    # 但 SimpleSequentialChain 会自动处理从 LLMChain 输出字典中提取文本。
    chain_one = LLMChain(llm=llm, prompt=prompt_joke) # 输出将是包含 'text'键 的字典

    # 第二个链：评论笑话
    prompt_review = ChatPromptTemplate.from_template(
        "请评价以下笑话的幽默程度（1-10分），并简要说明理由：\n笑话：{joke_text}"
    )
    chain_two = LLMChain(llm=llm, prompt=prompt_review)

    # 构建 SimpleSequentialChain
    # 它会自动将 chain_one 的 'text' 输出作为 chain_two 的 'joke_text' 输入（如果名称不匹配，它会假设输入变量名为前一链的输出）
    # 或者更准确地说，它期望前一个链的输出是一个字符串，这个字符串作为下一个链的输入。
    # LLMChain 默认输出一个包含 'text' 键的字典，SimpleSequentialChain 会智能地从中提取 'text' 值。
    overall_simple_chain = SimpleSequentialChain(
        chains=[chain_one, chain_two],
        verbose=True # 可以看到链的执行过程和中间步骤的输入输出
    )

    # 调用链
    input_topic = {"topic": "人工智能"} # SimpleSequentialChain 的输入变量名由第一个子链的输入变量名决定
    # final_review = overall_simple_chain.invoke(input_topic)
    # print("\n--- SimpleSequentialChain 最终输出 ---")
    # print(final_review) # final_review 将是 chain_two 的输出文本
    ```
    **注意**: `SimpleSequentialChain` 期望每个子链的输出是一个单一的字符串值，这个字符串值将作为下一个链的输入（通常是填充下一个链提示模板中的某个变量）。如果子链（如 `LLMChain`）返回一个字典，`SimpleSequentialChain` 会尝试从中提取一个合适的字符串值（通常是键为 `text` 的值）。

#### 10.3 SequentialChain：多输入多输出的顺序链

`SequentialChain` 是 `SimpleSequentialChain` 的一个更通用和强大的版本。它也按顺序执行一系列子链，但它提供了更灵活的输入和输出管理：

* **特点**:
    * **多初始输入**: 可以接受多个初始输入变量。
    * **显式输入/输出映射**: 你需要明确指定每个子链的输入变量来自哪里（可以是初始输入，也可以是前面链的输出），以及每个子链的输出变量叫什么名字。
    * **中间步骤的输出可访问**: 可以将中间步骤的输出变量也包含在最终的输出结果中。
    * **最终输出**: 返回一个包含所有在 `output_variables` 中指定的变量的字典。

* **适用场景**: 适用于更复杂的顺序工作流，其中：
    * 需要从多个初始输入开始。
    * 一个链的输出需要被明确命名，并作为后续特定链的特定输入。
    * 希望保留并返回某些中间步骤的结果。

* **示例**:
    我们想构建一个流程：
    1.  根据用户提供的 `language` 和 `topic`，生成一篇简短的介绍性段落 (chain_intro)。
    2.  对这个介绍性段落 (intro_paragraph) 进行总结，生成一个 `summary` (chain_summary)。
    3.  根据原始 `topic` 和生成的 `summary`，提出 3 个相关的后续问题 (chain_questions)。
    我们希望最终能得到 `intro_paragraph`, `summary`, 和 `follow_up_questions`。

    ```python
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain.chains import LLMChain
    from langchain.chains import SequentialChain # 注意不是 SimpleSequentialChain
    import os

    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 链1: 生成介绍段落
    prompt_intro = ChatPromptTemplate.from_template(
        "请用{language}写一段关于“{topic}”的简短介绍性文字（约50字）。"
    )
    chain_intro = LLMChain(
        llm=llm,
        prompt=prompt_intro,
        output_key="intro_paragraph" # 指定此链输出的键名
    )

    # 链2: 总结介绍段落
    prompt_summary = ChatPromptTemplate.from_template(
        "请将以下段落总结成一句核心观点：\n{intro_paragraph}"
    )
    chain_summary = LLMChain(
        llm=llm,
        prompt=prompt_summary,
        output_key="summary" # 指定此链输出的键名
    )

    # 链3: 根据主题和总结提出问题
    prompt_questions = ChatPromptTemplate.from_template(
        "基于主题“{topic}”和以下总结：“{summary}”，请提出3个相关的后续研究问题。"
    )
    chain_questions = LLMChain(
        llm=llm,
        prompt=prompt_questions,
        output_key="follow_up_questions" # 指定此链输出的键名
    )

    # 构建 SequentialChain
    overall_sequential_chain = SequentialChain(
        chains=[chain_intro, chain_summary, chain_questions],
        input_variables=["language", "topic"], # 定义整个顺序链的初始输入变量
        output_variables=["intro_paragraph", "summary", "follow_up_questions"], # 定义希望从最终结果中获取的变量
        verbose=True
    )

    # 调用链
    initial_inputs = {"language": "中文", "topic": "可持续能源"}
    final_outputs = overall_sequential_chain.invoke(initial_inputs)

    print("\n--- SequentialChain 最终输出 ---")
    print(f"介绍段落: {final_outputs.get('intro_paragraph')}")
    print(f"总结: {final_outputs.get('summary')}")
    print(f"后续问题: {final_outputs.get('follow_up_questions')}")
    print(f"完整的输出字典: {final_outputs}")
    ```
    在 `SequentialChain` 中，LangChain 会自动管理变量的传递。例如，`chain_intro` 的输出 `intro_paragraph` 会被传递给 `chain_summary` 作为其输入。`chain_questions` 会接收到初始的 `topic` 输入以及 `chain_summary` 的输出 `summary`。

#### 10.4 链的输入输出管理

有效地管理链的输入和输出对于构建清晰、可维护和可预测的 LangChain 应用至关重要。

* **输入 (Inputs)**:
    * 大多数链（尤其是那些继承自 `Chain` 基类的传统链）期望其输入是一个**字典**，其中键是输入变量的名称，值是相应的输入值。
    * `LLMChain` 的输入变量由其 `PromptTemplate` 中的占位符决定。
    * `SimpleSequentialChain` 的输入变量由其第一个子链的输入变量决定，并且它只接受一个初始输入键。
    * `SequentialChain` 通过 `input_variables` 参数明确声明其接受的初始输入键列表。
    * 在使用 LCEL 构建链时，输入可以是单个值（如果提示只需要一个变量）或一个字典。LCEL 链通常会从 `PromptTemplate` 推断其输入模式。

* **输出 (Outputs)**:
    * 传统 `Chain` 对象（如 `LLMChain`, `SequentialChain`）的 `invoke()` 或 `run()` 方法通常返回一个**字典**。
        * `LLMChain`: 如果没有 `output_parser` 且没有显式设置 `output_key`，默认输出键是 `text`。如果设置了 `output_key`，则 LLM 的响应会存储在该键下。如果使用了 `output_parser` 且链是 LCEL 风格的 `prompt | llm | parser`，则输出直接是解析后的类型；如果是传统的 `LLMChain(..., output_parser=...)`，则解析后的结果仍可能在输出字典的 `output_key` 下。
        * `SimpleSequentialChain`: 其输出是其最后一个子链的输出（通常是一个字符串）。
        * `SequentialChain`: 其输出是一个字典，包含在 `output_variables` 参数中声明的所有变量。这些变量可以是初始输入，也可以是任何子链的输出。
    * LCEL 风格的链的输出类型取决于链的最后一个组件。如果是 `StrOutputParser`，则输出是字符串；如果是 `PydanticOutputParser`，则是 Pydantic 对象实例；如果是 LLM/ChatModel 本身，则是 `LLMResult` 或 `AIMessage`。

* **中间变量与传递 (Intermediate Variables & Passing)**:
    * 在 `SequentialChain` 中，一个子链的输出（由其 `output_key` 定义）可以作为后续子链的输入（在其 `PromptTemplate` 中引用）。LangChain 会自动处理这种“记忆”和传递。
    * 所有在 `SequentialChain` 中生成的变量（包括初始输入和所有子链的输出）都在一个内部的“记忆空间 (memory scratchpad)”中可用，直到链执行完毕。
    * `SimpleSequentialChain` 的传递机制更简单，它只是将前一步的字符串输出直接作为下一步的输入。

* **显式声明的重要性**:
    * 在 `SequentialChain` 中，明确声明 `input_variables` 和 `output_variables` 非常重要。
        * `input_variables`: 告诉链期望哪些初始输入。
        * `output_variables`: 决定了链最终返回结果中包含哪些内容。如果你希望访问某个中间步骤的输出，就必须将其名称包含在 `output_variables` 列表中。

* **LCEL 与字典传递**:
    * LCEL 提供了 `RunnablePassthrough` 和 `RunnableParallel` (或字典形式的并行) 等工具来更灵活地管理输入输出和数据流。
    * 例如，`RunnablePassthrough().assign(new_key=another_runnable)` 可以将 `another_runnable` 的输出添加到原始输入的字典中，并以 `new_key` 命名。

    ```python
    # LCEL 示例：模拟类似 SequentialChain 的多步骤和多输出
    from langchain_core.runnables import RunnablePassthrough

    # llm, ChatPromptTemplate, StrOutputParser 如前定义
    prompt_intro = ChatPromptTemplate.from_template("介绍 {topic} ({language})")
    prompt_summary = ChatPromptTemplate.from_template("总结: {intro_paragraph}")
    prompt_questions = ChatPromptTemplate.from_template("关于 {topic} 和总结 '{summary}' 的问题?")

    # 定义与之前 LLMChain 类似的可运行对象
    intro_generator = {"intro_paragraph": prompt_intro | llm | StrOutputParser()}
    summary_generator = {"summary": prompt_summary | llm | StrOutputParser()}
    questions_generator = {"follow_up_questions": prompt_questions | llm | StrOutputParser()}

    full_lcel_chain = RunnablePassthrough.assign(**intro_generator) \
                      .assign(**summary_generator) \
                      .assign(**questions_generator)

    input_data = {"topic": "太空探索", "language": "英文"}
    result = full_lcel_chain.invoke(input_data)
    print(result)
    # 结果会是一个包含 topic, language, intro_paragraph, summary, follow_up_questions 的字典
    ```

理解并熟练运用这些输入输出管理机制，是构建复杂但行为可控的链式应用的基础。对于新项目，推荐优先考虑使用 LCEL 进行链的组合，因为它提供了更强大和灵活的数据流控制。但理解传统的 `SequentialChain` 等对于维护现有代码或理解某些 LangChain 文档和示例仍然有价值。



### 第十一章：高级链应用

在本章中，我们将探讨 LangChain 中一些更高级的链应用，它们允许我们构建更复杂、更智能的语言模型工作流。这些高级链通常解决了在实际应用中遇到的特定挑战，例如数据预处理、条件逻辑执行、与外部数据源的交互以及自定义复杂流程。

#### 11.1 转换链 (TransformChain)：在链中进行数据转换

`TransformChain` 允许你在链的执行过程中对数据进行自定义的转换操作。这对于预处理输入数据、格式化输出数据或在链的步骤之间修改数据结构非常有用。

* **特点**:
    * **自定义函数**: 接受一个自定义的转换函数，该函数将作用于输入数据。
    * **输入输出变量**: 需要明确定义输入变量 (`input_variables`) 和输出变量 (`output_variables`) 的名称。转换函数的输入是一个字典，其键是 `input_variables`，输出也应该是一个字典，其键是 `output_variables`。
    * **灵活性**: 允许执行任意 Python 代码进行数据转换，不仅仅限于文本操作。
    * **集成性**: 可以无缝地集成到 `SequentialChain` 或其他链式结构中。

* **适用场景**:
    * 在将数据传递给 LLM 之前对其进行清理或格式化（例如，去除 HTML 标签、提取特定信息、将时间戳转换为人类可读格式）。
    * 在从 LLM 获得输出后对其进行后处理（例如，解析 JSON 字符串、将文本分割成列表）。
    * 在一个序列链中，当前一个链的输出格式不直接匹配下一个链的输入格式时，用作适配器。
    * 实现复杂的业务逻辑转换，而不仅仅是提示工程。

* **示例概念**:
    假设我们有一个链，它首先从用户那里获取一个非结构化的日期字符串（如 "明天下午3点"），我们希望在将其传递给另一个需要标准日期时间格式的链之前进行转换。

    ```python
    from langchain.chains import TransformChain, LLMChain, SequentialChain
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from datetime import datetime, timedelta
    import re # 用于更复杂的日期解析，这里仅作示意

    # 假设的转换函数：将自然语言日期转换为 ISO 格式
    # 注意：实际的自然语言日期解析会更复杂，可能需要第三方库
    def transform_date_function(inputs: dict) -> dict:
        natural_date_str = inputs["natural_date"]
        # 简化的示例逻辑
        if "明天" in natural_date_str:
            date_obj = datetime.now() + timedelta(days=1)
            time_match = re.search(r"(\d+)(?:点|时)", natural_date_str)
            if time_match:
                hour = int(time_match.group(1))
                date_obj = date_obj.replace(hour=hour, minute=0, second=0, microsecond=0)
            transformed_date = date_obj.isoformat()
        elif "今天" in natural_date_str:
            date_obj = datetime.now()
            time_match = re.search(r"(\d+)(?:点|时)", natural_date_str)
            if time_match:
                hour = int(time_match.group(1))
                date_obj = date_obj.replace(hour=hour, minute=0, second=0, microsecond=0)
            transformed_date = date_obj.isoformat()
        else:
            # 默认或更复杂的解析逻辑
            transformed_date = datetime.now().isoformat() # 简化处理
        return {"iso_date": transformed_date, "original_input": natural_date_str}

    date_transformer_chain = TransformChain(
        input_variables=["natural_date"],
        output_variables=["iso_date", "original_input"], # 可以输出多个变量
        transform=transform_date_function
    )

    # 另一个链，它使用转换后的日期
    llm = ChatOpenAI(temperature=0)
    reminder_prompt = ChatPromptTemplate.from_template(
        "为日期 {iso_date} 设置一个提醒，内容关于：处理 {original_input}。"
    )
    reminder_chain = LLMChain(llm=llm, prompt=reminder_prompt, output_key="reminder_text")

    # 将它们组合在 SequentialChain 中
    # overall_chain = SequentialChain(
    #     chains=[date_transformer_chain, reminder_chain],
    #     input_variables=["natural_date"],
    #     output_variables=["iso_date", "original_input", "reminder_text"],
    #     verbose=True
    # )

    # 调用链 (假设已设置 OPENAI_API_KEY)
    # result = overall_chain.invoke({"natural_date": "明天下午3点开会"})
    # print(result)
    # 输出将包含 'iso_date', 'original_input', 和 'reminder_text'
    ```

#### 11.2 路由链 (RouterChain)：根据输入动态选择下一个链

`RouterChain` 是一种特殊的链，它可以根据输入动态地决定接下来应该执行哪个（或哪些）子链。它通常包含一个路由选择逻辑（通常是另一个 LLMChain）和一个或多个目标链。

* **特点**:
    * **条件执行**: 根据输入的内容或特性，将任务路由到最合适的处理路径。
    * **路由逻辑**: 包含一个专门的“路由链”（`routing_chain`），通常是一个 `LLMChain`，其任务是分析输入并决定目标链的名称。
    * **目标链**: 包含一个目标链字典 (`destination_chains`)，其中键是路由链可能输出的路由名称，值是实际的子链对象。
    * **默认链**: 可以指定一个 `default_chain`，当路由逻辑无法确定一个明确的目标或输出的路由名称不在目标链字典中时执行。
    * **多路路由**: `MultiPromptChain` 是一种特殊的路由链，它会根据输入选择最合适的提示词模板来生成回应，本质上是路由到不同的提示词。

* **适用场景**:
    * 构建一个能够处理多种类型请求的客服机器人（例如，技术支持问题、账单查询、产品信息咨询）。
    * 根据文本的语气或主题选择不同的处理流程。
    * 创建一个能够回答关于不同领域知识的问答系统，每个领域由一个专门的链处理。
    * 当一个任务可以有多种解决方法，需要根据具体情况选择最优方法时。

* **示例概念 (LLMRouterChain)**:
    假设我们想根据用户问题的类型（例如，数学问题、历史问题、常识问题）将其路由到不同的专业处理链。

    ```python
    from langchain.chains.router import RouterChain, LLMRouterChain
    from langchain.chains.router.llm_router import LLMRouterChainInput
    from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
    from langchain.prompts import PromptTemplate, ChatPromptTemplate
    from langchain_openai import ChatOpenAI
    from langchain.chains import LLMChain
    # (假设已经定义了 llm)
    # llm = ChatOpenAI(temperature=0)


    # 目标链的定义
    math_template = "你是一个数学专家。请解决以下数学问题：\n问题：{input}"
    math_chain = LLMChain(llm=llm, prompt=ChatPromptTemplate.from_template(math_template))

    history_template = "你是一位历史学家。请回答以下历史相关问题：\n问题：{input}"
    history_chain = LLMChain(llm=llm, prompt=ChatPromptTemplate.from_template(history_template))

    general_template = "请回答以下常识性问题：\n问题：{input}"
    general_chain = LLMChain(llm=llm, prompt=ChatPromptTemplate.from_template(general_template))

    # 路由器的提示信息，告诉LLM如何分类以及预期的输出格式
    # 我们需要定义目标链的名称和描述，以便路由LLM可以理解它们
    prompt_infos = [
        {
            "name": "math_expert",
            "description": "擅长回答数学问题",
            "prompt_template": math_template, # 实际执行时用不到，但描述可能需要
        },
        {
            "name": "history_scholar",
            "description": "擅长回答历史问题",
            "prompt_template": history_template,
        },
        {
            "name": "general_knowledge",
            "description": "擅长回答通用的常识性问题",
            "prompt_template": general_template,
        },
    ]

    # 构建路由LLM的提示
    # LLMRouterChain 会使用这些信息来构建一个提示，让LLM选择一个目标链的名字
    # router_prompt = # ... (需要一个专门的提示来让LLM选择 'destination' 和 'next_inputs')
    # 这个提示通常会列出可用的目标链及其描述，并要求LLM根据用户输入选择一个。
    # LangChain 提供了 MULTI_PROMPT_ROUTER_TEMPLATE 作为基础。
    # 我们需要将 prompt_infos 格式化成字符串，嵌入到 router_prompt 中。

    # 简化的方式是直接使用 LLMRouterChain.from_llm
    # 它会内部处理路由提示的构建
    # destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]
    # destinations_str = "\n".join(destinations)
    # router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destinations_str)
    # router_prompt = PromptTemplate(
    #     template=router_template,
    #     input_variables=["input"],
    #     output_parser=RouterOutputParser(), # RouterOutputParser 用于解析LLM的输出
    # )
    # routing_llm_chain = LLMChain(llm=llm, prompt=router_prompt) # 这是路由决策链

    # destination_chains_map = {
    #     "math_expert": math_chain,
    #     "history_scholar": history_chain,
    #     "general_knowledge": general_chain,
    # }

    # router_chain_instance = RouterChain(
    #    router_chain=routing_llm_chain, # 负责决策的链
    #    destination_chains=destination_chains_map, # 可选的目标链
    #    default_chain=general_chain, # 如果路由不确定，则使用默认链
    #    verbose=True
    # )

    # 更直接的方式是使用 LLMRouterChain.from_llm
    # llm_router = LLMRouterChain.from_llm(llm, router_prompt_template) # router_prompt_template 需要仔细构造
    # (LLMRouterChain 的构建比较复杂，因为它需要一个专门的提示模板来让LLM输出目标链的名字和输入)

    # MultiPromptChain 是更常见的路由形式，它根据输入选择最合适的提示词
    # from langchain.chains import MultiPromptChain
    # multi_prompt_chain = MultiPromptChain.from_prompts(
    #     llm=llm,
    #     prompt_infos=prompt_infos, # name, description, prompt_template
    #     default_chain=general_chain,
    #     verbose=True
    # )

    # 调用示例 (使用 MultiPromptChain 更直观)
    # math_query = "3的立方根是多少？"
    # history_query = "法国大革命是什么时候开始的？"
    # general_query = "天空为什么是蓝色的？"

    # print(f"数学问题结果: {multi_prompt_chain.invoke({'input': math_query})}")
    # print(f"历史问题结果: {multi_prompt_chain.invoke({'input': history_query})}")
    # print(f"常识问题结果: {multi_prompt_chain.invoke({'input': general_query})}")
    ```
    *注意*: `LLMRouterChain` 和 `MultiPromptChain` 的设置需要仔细构造路由提示，确保LLM能够理解选项并做出正确的路由决策。`MultiPromptChain` 相对更容易上手，因为它封装了许多路由逻辑。

#### 11.3 文档问答链 (Question Answering over Documents)

这是 LangChain 中一个非常核心和强大的功能，允许你基于一组私有或特定领域的文档来回答用户提出的问题。它通常涉及将文档加载、分割、创建向量嵌入、存储到向量数据库、检索相关文档，然后将问题和相关文档一起传递给 LLM 进行答案生成。

* **核心组件**:
    * **文档加载器 (Document Loaders)**: 用于从各种来源（如文本文件、PDF、网页、数据库）加载文档。
    * **文本分割器 (Text Splitters)**: 将长文档分割成较小的块（chunks），以便于嵌入和检索。
    * **向量嵌入 (Embeddings)**: 将文本块转换为数值向量，捕捉其语义含义。
    * **向量存储 (Vector Stores)**: 存储文本块的向量嵌入，并支持高效的相似性搜索。
    * **检索器 (Retrievers)**: 根据用户问题（也转换为向量）从向量存储中检索最相关的文本块。
    * **问答链 (QA Chains)**: 将用户问题和检索到的相关文档块组合起来，并使用 LLM 生成答案。

* **主要的问答链实现**:
    * **`load_qa_chain`**: 一个便捷的函数，用于加载预配置的文档问答链。它需要一个 LLM 和一个 `chain_type` 参数。
    * **`RetrievalQA`**: 一个更高级的链，它封装了从文档检索到答案生成的整个流程。它内部会使用一个检索器 (Retriever) 来获取相关文档，然后将这些文档喂给一个通过 `load_qa_chain` (或类似机制) 创建的问答链。

* **不同的 `chain_type` (策略)**:
    这些类型决定了如何将检索到的文档块提供给 LLM 以及如何处理它们以生成最终答案。

    1.  **`stuff`**:
        * **工作方式**: 将所有检索到的文档块“塞”（stuff）进一个单独的提示中，连同问题一起发送给 LLM 进行一次调用。
        * **优点**: 简单直接，LLM 可以一次性看到所有相关上下文，可能生成更全面的答案。
        * **缺点**: 受限于 LLM 的上下文窗口大小。如果检索到的文档块总长度超过限制，则会出错或截断信息。
        * **适用场景**: 文档块较少或总长度较短，且 LLM 上下文窗口足够大时。

    2.  **`map_reduce`**:
        * **工作方式**:
            1.  **Map**: 首先，将用户问题和每个检索到的文档块分别发送给 LLM（或一个专门的“映射”提示），要求 LLM基于该文档块生成一个初步的答案或摘要。
            2.  **Reduce**: 然后，将所有这些初步的答案/摘要收集起来，连同原始问题一起，发送给另一个 LLM（或一个“归并”提示），让它将这些中间结果整合成一个最终的答案。
        * **优点**: 可以处理大量的文档块，不受单个 LLM 上下文窗口的严格限制。可以并行处理“Map”步骤。
        * **缺点**: 需要多次 LLM 调用，成本更高，速度可能较慢。最终答案的质量可能取决于“Reduce”步骤整合信息的能力。
        * **适用场景**: 需要处理大量文档或文档块总长度远超 LLM 上下文窗口时。

    3.  **`refine`**:
        * **工作方式**:
            1.  首先，将问题和第一个文档块发送给 LLM，生成一个初步答案。
            2.  然后，将这个初步答案、问题以及第二个文档块发送给 LLM，要求它基于新的文档块来“优化”（refine）之前的答案。
            3.  依次迭代处理所有检索到的文档块，不断优化答案。
        * **优点**: 可以逐步构建和完善答案，每个后续步骤都可以利用之前的结果和新的上下文。理论上可以处理较多文档。
        * **缺点**: 顺序执行，对于大量文档块速度较慢。后来的文档块对最终答案的影响可能更大。也需要多次 LLM 调用。
        * **适用场景**: 当希望答案能够迭代地吸收来自不同文档片段的信息，并且文档之间存在某种顺序或依赖关系时。

    4.  **`map_rerank` (较少直接用于 `RetrievalQA` 的 `chain_type`，但概念相关)**:
        * **工作方式**:
            1.  **Map**: 与 `map_reduce` 类似，对每个文档块和问题都单独调用 LLM，要求它不仅生成答案，还要给出一个置信度分数。
            2.  **Rerank**: 根据 LLM 给出的置信度分数对各个答案进行排序，选择分数最高的那个答案作为最终结果。
        * **优点**: 当不同文档块可能给出不同甚至矛盾的答案时，可以尝试选出“最好”的那个。
        * **缺点**: 依赖 LLM 准确评估其自身答案质量的能力。也需要多次 LLM 调用。
        * **适用场景**: 当文档来源多样，答案质量可能参差不齐，需要一种机制来挑选最佳答案时。

* **示例 (`RetrievalQA` with `stuff` chain_type)**:

    ```python
    from langchain_openai import ChatOpenAI, OpenAIEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain.text_splitter import CharacterTextSplitter
    from langchain_community.document_loaders import TextLoader # 示例用 TextLoader
    from langchain.chains import RetrievalQA
    import os

    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # embeddings = OpenAIEmbeddings()

    # 1. 加载文档
    # loader = TextLoader("./my_document.txt") # 假设有一个 my_document.txt 文件
    # documents = loader.load()

    # 2. 分割文档
    # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    # texts = text_splitter.split_documents(documents)

    # 3. 创建向量存储和检索器
    # if texts: # 确保有文本块可以索引
    #     vectorstore = FAISS.from_documents(texts, embeddings)
    #     retriever = vectorstore.as_retriever()

    #     # 4. 创建 RetrievalQA 链
    #     qa_chain = RetrievalQA.from_chain_type(
    #         llm=llm,
    #         chain_type="stuff", # 或者 "map_reduce", "refine"
    #         retriever=retriever,
    #         return_source_documents=True, # 可选，返回源文档块
    #         verbose=True
    #     )

    #     # 5. 提问
    #     query = "文档中提到了哪些关于AI的未来趋势？"
    #     result = qa_chain.invoke({"query": query})

    #     print("\n--- RetrievalQA 最终输出 ---")
    #     print(f"答案: {result['result']}")
    #     # if 'source_documents' in result:
    #     #     print("\n--- 源文档 ---")
    #     #     for doc in result['source_documents']:
    #     #         print(f"内容: {doc.page_content[:100]}...") # 打印部分内容
    #     #         print(f"来源: {doc.metadata}")
    # else:
    #     print("没有加载到任何文本块，无法创建QA链。")
    ```

#### 11.4 摘要链 (Summarization Chains)

摘要链专门用于将长文本内容（如文章、报告、对话记录）浓缩成简短的摘要。与文档问答链类似，它们也经常需要处理超出单个 LLM 上下文窗口的文本，因此也使用了类似 `stuff`、`map_reduce`、`refine` 的策略。

* **核心功能**: 生成文本的简洁概括。
* **常见策略 (`chain_type` in `load_summarize_chain`)**:
    * **`stuff`**: 将所有文本一次性放入提示中让 LLM 总结。适用于短文本。
    * **`map_reduce`**:
        1.  **Map**: 将文本分割成块，对每个块分别生成摘要。
        2.  **Reduce**: 将这些块级摘要合并成一个最终的总摘要。通常会有一个专门的“合并摘要”提示。
    * **`refine`**:
        1.  对第一个文本块生成初步摘要。
        2.  然后，将初步摘要和下一个文本块一起提供给 LLM，要求它基于新信息优化摘要。依次迭代。

* **适用场景**:
    * 自动生成新闻文章、研究论文或书籍的摘要。
    * 从冗长的会议记录或客户对话中提取关键点。
    * 为搜索引擎结果或文档列表提供预览片段。

* **示例概念 (`load_summarize_chain` with `map_reduce`)**:

    ```python
    from langchain.chains.summarize import load_summarize_chain
    from langchain_openai import ChatOpenAI
    from langchain_community.document_loaders import WebBaseLoader # 示例用网页加载器
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    import os

    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

    # 1. 加载长文档 (例如，一篇较长的博客文章)
    loader = WebBaseLoader("[https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)") # 一个较长的示例文章
    documents = loader.load()

    # 2. 分割文档
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
    docs_for_summary = text_splitter.split_documents(documents)

    # 3. 创建并运行摘要链
    if docs_for_summary:
        # 使用 map_reduce 策略，因为它适合长文档
        # LangChain 会有默认的 map_prompt 和 combine_prompt，但也可以自定义
        summary_chain = load_summarize_chain(
            llm=llm,
            chain_type="map_reduce",
            verbose=True
        )
        # 对于 load_summarize_chain, 输入是文档列表
        summary_result = summary_chain.invoke(docs_for_summary) # 直接传递文档列表

        print("\n--- 摘要链输出 ---")
        print(summary_result['output_text'])
    else:
        print("没有加载或分割出文档块用于摘要。")
    ```
    *提示定制*: 对于 `map_reduce` 和 `refine` 策略，可以分别通过 `map_prompt` 和 `combine_prompt` (或 `refine_prompt`) 参数传入自定义的 `PromptTemplate` 来更精细地控制每个阶段的行为。

#### 11.5 自定义链的创建与使用

虽然 LangChain 提供了许多预构建的链，但有时你需要创建完全自定义的链来实现特定的逻辑或集成独特的功能。这通常通过继承 LangChain 的 `Chain` 基类并实现其核心方法来完成。

* **为什么要自定义链?**:
    * 实现标准链无法覆盖的复杂工作流。
    * 集成非 LangChain 标准的工具或数据源。
    * 对链的内部逻辑、状态管理或错误处理有特殊要求。
    * 封装一组特定的、可重用的操作。

* **关键步骤 (继承 `Chain` 类)**:
    1.  **定义输入键 (`input_keys`)**: 一个字符串元组，声明了链期望的输入变量名称。
    2.  **定义输出键 (`output_keys`)**: 一个字符串元组，声明了链将产生的输出变量名称。
    3.  **实现 `_call(self, inputs: Dict[str, Any]) -> Dict[str, Any]` 方法**: 这是链的核心逻辑所在。它接收一个包含所有输入键的字典，并必须返回一个包含所有输出键的字典。
    4.  **（可选）实现 `_acall`**: 用于异步执行。
    5.  **（可选）属性和方法**: 可以添加其他属性和方法来辅助链的配置和功能。

* **LCEL (LangChain Expression Language) 作为替代方案**:
    对于许多自定义链的需求，尤其是那些主要涉及组合现有 `Runnable` 对象（如提示、LLM、输出解析器、其他链）的场景，LCEL 提供了一种更简洁、更声明式的方式来构建自定义逻辑，而无需显式继承 `Chain` 类。通过 LCEL 的管道操作符 (`|`) 和 `RunnablePassthrough`, `RunnableParallel` 等组件，可以灵活地构建复杂的执行图。
    * **何时仍考虑继承 `Chain`**: 当你的自定义逻辑非常复杂，涉及到难以用 LCEL 组合表达的状态管理、外部 API 的复杂交互（超出了简单工具的范畴），或者你需要与 LangChain 生态系统中期望传统 `Chain` 对象的旧组件集成时。

* **示例概念 (传统自定义链)**:
    创建一个简单的自定义链，它接收一个文本，将其转换为大写，并计算其长度。

    ```python
    from langchain.chains.base import Chain
    from typing import Any, Dict, List, Tuple # Tuple for input/output keys

    class CustomTransformChain(Chain):
        input_keys: Tuple[str, ...] = ("text",) # 期望一个名为 'text' 的输入
        output_keys: Tuple[str, ...] = ("uppercase_text", "text_length") # 将输出这两个键

        def _call(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
            input_text = inputs["text"]

            # 执行自定义逻辑
            uppercase_version = input_text.upper()
            length = len(input_text)

            # 返回包含输出键的字典
            return {"uppercase_text": uppercase_version, "text_length": length}

        @property
        def _chain_type(self) -> str:
            return "custom_transform_chain" # 给你的链一个类型名

    # 使用自定义链
    # my_custom_chain = CustomTransformChain()
    # result = my_custom_chain.invoke({"text": "Hello LangChain!"})
    # print(result)
    # # 输出: {'text': 'Hello LangChain!', 'uppercase_text': 'HELLO LANGCHAIN!', 'text_length': 16}
    # # 注意：invoke 会自动将原始输入也包含在结果中，如果输入键与输出键不冲突。

    # # 也可以像其他链一样在 SequentialChain 中使用
    # llm = ChatOpenAI(temperature=0)
    # prompt = ChatPromptTemplate.from_template(
    #     "关于大写文本 '{uppercase_text}' (长度 {text_length})，写一句评论。"
    # )
    # comment_chain = LLMChain(llm=llm, prompt=prompt, output_key="comment")

    # overall_sequence = SequentialChain(
    #     chains=[my_custom_chain, comment_chain],
    #     input_variables=["text"], # 初始输入
    #     output_variables=["uppercase_text", "text_length", "comment"], # 期望的最终输出
    #     verbose=True
    # )
    # final_result = overall_sequence.invoke({"text": "Custom chains are powerful"})
    # print(final_result)
    ```

通过掌握这些高级链应用，你可以构建出功能更加丰富和智能的 LangChain 应用，以解决更广泛的实际问题。



## 模块五：赋予应用记忆 (Memory)

在许多语言模型应用中，尤其是对话系统、聊天机器人或需要进行多轮交互的场景，让应用“记住”之前的交互内容至关重要。记忆（Memory）组件使得链（Chains）和智能体（Agents）能够在其上下文中保留和利用先前的信息，从而提供更连贯、更个性化、更有上下文感知能力的交互体验。

LangChain 提供了多种记忆类型，以适应不同的需求和场景。

### 第十二章：记忆的类型与使用

本章将详细介绍 LangChain 中常见的记忆类型以及如何在链和智能体中集成和管理它们。

#### 12.1 ConversationBufferMemory：基础的对话缓冲区记忆

`ConversationBufferMemory` 是最简单直接的记忆类型之一。它将对话的完整历史记录存储在一个缓冲区中，并在每次调用链或智能体时将整个缓冲区的内容作为上下文变量传递给提示。

* **特点**:
    * **完整历史**: 存储用户和 AI 之间所有的交互轮次。
    * **直接传递**: 将整个对话历史作为字符串（或消息列表）插入到提示的特定变量中（例如，`history`）。
    * **简单易用**: 配置和使用都非常简单。
    * **人类可读**: 记忆内容通常是直接的对话文本，易于理解和调试。

* **适用场景**:
    * 短对话或上下文窗口较大的模型。
    * 需要模型能够回顾整个对话过程的应用。
    * 快速原型开发或简单聊天机器人。

* **缺点**:
    * **上下文长度限制**: 随着对话的进行，历史记录会越来越长，最终可能超出 LLM 的上下文窗口限制，导致错误或性能下降。
    * **成本**: 每次都传递完整的历史记录会增加 Token 的使用量，从而增加 API 调用成本。

* **示例概念**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain
    from langchain.memory import ConversationBufferMemory
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    import os

    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 定义记忆
    # memory_key="history" 是指在提示中用来插入对话历史的变量名
    # return_messages=True 会使记忆返回一个消息对象列表，而不是单个字符串，这对于ChatModels更合适
    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # 定义提示模板，使用 MessagesPlaceholder 来容纳记忆中的消息列表
    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "你是一个乐于助人的AI助手。"),
    #     MessagesPlaceholder(variable_name="chat_history"), # 记忆将被插入这里
    #     ("human", "{input}")
    # ])

    # 创建对话链
    # conversation = ConversationChain(
    #     llm=llm,
    #     prompt=prompt,
    #     memory=memory,
    #     verbose=True
    # )

    # 进行对话
    # response1 = conversation.invoke({"input": "你好，我叫小明。"})
    # print(f"AI: {response1['response']}")

    # response2 = conversation.invoke({"input": "你还记得我叫什么名字吗？"})
    # print(f"AI: {response2['response']}") # AI 应该能记住“小明”

    # print("\n--- 记忆内容 ---")
    # print(memory.load_memory_variables({})) # 查看记忆中的内容
    # # 输出会类似: {'chat_history': [HumanMessage(content='你好，我叫小明。'), AIMessage(content='你好小明！很高兴认识你。有什么可以帮助你的吗？'), HumanMessage(content='你还记得我叫什么名字吗？'), AIMessage(content='是的，我记得你叫小明。')]}
    ```

#### 12.2 ConversationBufferWindowMemory：带窗口大小的对话缓冲区记忆

`ConversationBufferWindowMemory` 是 `ConversationBufferMemory` 的一个变种，它只保留最近的 `k` 轮对话交互。这有助于防止记忆无限增长，从而避免超出上下文窗口限制。

* **特点**:
    * **窗口限制**: 通过参数 `k` 指定保留最近的对话轮次数（一轮通常指一次用户输入和一次 AI 输出）。
    * **滑动窗口**: 当新的交互发生时，如果超出了 `k` 轮的限制，最早的交互会被丢弃。
    * **平衡性**: 在完全无记忆和完整历史记忆之间提供了一种折衷。

* **适用场景**:
    * 需要一定上下文但不必回顾非常久远历史的对话。
    * 对话长度可控，且近期对话内容比早期内容更重要的场景。
    * 避免 `ConversationBufferMemory` 可能导致的上下文溢出问题。

* **示例概念**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain
    from langchain.memory import ConversationBufferWindowMemory
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    # (假设 llm 已定义)

    # 定义带窗口的记忆，k=2 表示只保留最近2轮对话
    # window_memory = ConversationBufferWindowMemory(
    #     k=2,
    #     memory_key="chat_history",
    #     return_messages=True
    # )

    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "你是一个乐于助人的AI助手。"),
    #     MessagesPlaceholder(variable_name="chat_history"),
    #     ("human", "{input}")
    # ])

    # conversation_with_window = ConversationChain(
    #     llm=llm,
    #     prompt=prompt,
    #     memory=window_memory,
    #     verbose=True
    # )

    # print(conversation_with_window.invoke({"input": "你好，我是小红。"})['response'])
    # print(conversation_with_window.invoke({"input": "我喜欢蓝色。"})['response'])
    # print(conversation_with_window.invoke({"input": "我最喜欢的动物是猫。"})['response']) # 此时第一轮对话（我是小红）可能已被移出窗口

    # # 提问，看AI是否还记得小红
    # response = conversation_with_window.invoke({"input": "你还记得我的名字吗？"})
    # print(f"AI: {response['response']}") # 如果 k=2，此时可能不记得了

    # print("\n--- 记忆内容 (窗口限制) ---")
    # print(window_memory.load_memory_variables({}))
    # # 输出将只包含最近 k 轮的对话
    ```

#### 12.3 ConversationTokenBufferMemory：基于 Token 数量限制的记忆

`ConversationTokenBufferMemory` 根据对话历史记录的总 Token 数量来限制记忆的大小。它会保留最近的对话消息，直到缓冲区的总 Token 数达到设定的 `max_token_limit`。如果添加新消息会导致超出限制，它会从缓冲区的开头开始删除旧消息，直到总 Token 数符合限制。

* **特点**:
    * **Token 限制**: 通过 `max_token_limit` 参数精确控制记忆占用的 Token 数量。
    * **LLM 友好**: 与 LLM 的 Token 限制直接相关，有助于避免上下文溢出。
    * **动态裁剪**: 自动从对话历史的早期部分移除消息以满足 Token 限制。
    * **需要 LLM**: 通常需要传入一个 LLM 实例（或其名称）给记忆本身，以便它能够计算消息的 Token 数量。

* **适用场景**:
    * 需要严格控制发送给 LLM 的上下文 Token 数量的场景。
    * 当对话历史的长度变化较大，但希望确保不超过特定 Token 预算时。
    * 替代 `ConversationBufferWindowMemory`，提供更精细的控制。

* **示例概念**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain
    from langchain.memory import ConversationTokenBufferMemory
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    # (假设 llm 已定义)

    # 定义基于Token限制的记忆
    # 需要传入llm实例来计算token数量
    # token_memory = ConversationTokenBufferMemory(
    #     llm=llm, # 用于计算token
    #     max_token_limit=100, # 限制记忆中的总token数
    #     memory_key="chat_history",
    #     return_messages=True
    # )

    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "你是一个非常简洁的AI助手。"),
    #     MessagesPlaceholder(variable_name="chat_history"),
    #     ("human", "{input}")
    # ])

    # conversation_with_token_limit = ConversationChain(
    #     llm=llm,
    #     prompt=prompt,
    #     memory=token_memory,
    #     verbose=True
    # )

    # # 进行多轮对话，观察记忆如何根据token限制裁剪
    # print(conversation_with_token_limit.invoke({"input": "第一句话，这应该会保留下来。"})['response'])
    # print(conversation_with_token_limit.invoke({"input": "第二句话，可能也会保留。"})['response'])
    # # 假设前两句话加上AI的回复已经接近或超过100 token
    # print(conversation_with_token_limit.invoke({"input": "第三句话，这句话加入后，最早的话可能会被裁剪。"})['response'])

    # print("\n--- 记忆内容 (Token限制) ---")
    # print(token_memory.load_memory_variables({}))
    ```

#### 12.4 ConversationSummaryMemory：对话摘要记忆

`ConversationSummaryMemory` 不会存储完整的对话历史，而是随着对话的进行，动态地将对话内容总结成一个不断更新的摘要。这个摘要随后被用作上下文。

* **特点**:
    * **摘要形式**: 将对话历史压缩成摘要，而不是保留原始消息。
    * **LLM 驱动**: 需要一个 LLM 来执行摘要任务。
    * **节省空间**: 摘要通常比完整的对话历史短得多，有助于处理非常长的对话。
    * **信息损失**: 摘要过程中可能会丢失一些细节信息。

* **适用场景**:
    * 非常长的对话，其中保留所有细节既不可能也不必要。
    * 希望模型能够理解对话的总体脉络和关键信息，而不是具体措辞。
    * 对 Token 成本和上下文长度非常敏感的应用。

* **示例概念**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain
    from langchain.memory import ConversationSummaryMemory
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    # (假设 llm 已定义)

    # 定义摘要记忆，需要传入一个LLM用于生成摘要
    # summary_memory = ConversationSummaryMemory(
    #     llm=llm, # 用于生成摘要的LLM
    #     memory_key="chat_summary", # 提示中用于摘要的变量名
    #     # return_messages=True (对于摘要记忆，通常返回字符串摘要，但也可以配置)
    #     # prompt (可选): 可以提供自定义的摘要提示
    # )

    # # 摘要记忆通常将摘要作为字符串插入，所以提示中直接用变量名
    # prompt_summary = ChatPromptTemplate.from_messages([
    #     ("system", "你是一个乐于助人的AI助手。以下是目前为止的对话摘要：\n{chat_summary}"),
    #     ("human", "{input}")
    # ])


    # conversation_with_summary = ConversationChain(
    #     llm=llm,
    #     prompt=prompt_summary,
    #     memory=summary_memory,
    #     verbose=True
    # )

    # print(conversation_with_summary.invoke({"input": "你好，我叫小华，我正在学习LangChain。"})['response'])
    # print(conversation_with_summary.invoke({"input": "LangChain中的记忆模块有哪些类型？"})['response'])
    # print(conversation_with_summary.invoke({"input": "我之前提到我的名字是什么吗？"})['response'])
    # # AI的回答将基于它生成的对话摘要

    # print("\n--- 记忆内容 (摘要) ---")
    # print(summary_memory.load_memory_variables({}))
    # # 输出会类似: {'chat_summary': '人类介绍了自己叫小华，正在学习LangChain。AI回应并准备回答关于LangChain记忆模块的问题。人类询问AI是否记得其名字。'}
    ```

#### 12.5 ConversationSummaryBufferMemory：结合摘要和缓冲区的记忆

`ConversationSummaryBufferMemory` 结合了 `ConversationBufferMemory` 和 `ConversationSummaryMemory` 的优点。它会保留最近的几轮对话（缓冲区部分），同时将更早的对话内容总结成摘要。当缓冲区的 Token 数量超过 `max_token_limit` 时，它会将缓冲区中最旧的消息转换为摘要，并与现有的摘要合并。

* **特点**:
    * **混合策略**: 近期对话保留完整细节，远期对话进行摘要。
    * **Token 限制**: 通过 `max_token_limit` 控制近期对话缓冲区的 Token 大小。
    * **LLM 驱动摘要**: 需要一个 LLM 来生成和更新摘要部分。
    * **平衡性**: 在信息保真度和上下文长度之间取得了较好的平衡。

* **适用场景**:
    * 需要模型准确记住近期对话细节，同时对长期对话有一个概览性理解的场景。
    * 适合大多数复杂的对话应用。

* **示例概念**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain
    from langchain.memory import ConversationSummaryBufferMemory
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    # (假设 llm 已定义)

    # summary_buffer_memory = ConversationSummaryBufferMemory(
    #     llm=llm, # 用于生成摘要
    #     max_token_limit=150, # 最近对话缓冲区的token限制
    #     memory_key="chat_history", # 提示中变量名
    #     return_messages=True # 缓冲部分返回消息列表，摘要部分作为字符串预置
    # )

    # # 提示模板需要能处理混合内容，通常MessagesPlaceholder可以适应
    # # 记忆体会将摘要信息（如果有）作为SystemMessage放在消息列表的开头
    # prompt_summary_buffer = ChatPromptTemplate.from_messages([
    #     MessagesPlaceholder(variable_name="chat_history"),
    #     ("human", "{input}")
    # ])
    # # 或者更明确地分离：
    # # prompt_summary_buffer = ChatPromptTemplate.from_messages([
    # # ("system", "这是之前的对话摘要: {summary}\n以下是最近的对话内容:"), # summary部分由记忆内部处理
    # # MessagesPlaceholder(variable_name="recent_history"),
    # # ("human", "{input}")
    # # ])
    # # 对于ConversationSummaryBufferMemory, 它会自动将摘要内容（如果有）作为一条SystemMessage放在
    # # 返回的 messages 列表的开头，所以使用单个 MessagesPlaceholder(variable_name="chat_history") 通常是可行的。

    # conversation_with_summary_buffer = ConversationChain(
    #     llm=llm,
    #     prompt=prompt_summary_buffer,
    #     memory=summary_buffer_memory,
    #     verbose=True
    # )

    # print(conversation_with_summary_buffer.invoke({"input": "我的项目代号是“凤凰”。"})['response'])
    # print(conversation_with_summary_buffer.invoke({"input": "这个项目的主要目标是提升用户参与度。"})['response'])
    # # ...进行更多对话，直到超出 max_token_limit ...
    # print(conversation_with_summary_buffer.invoke({"input": "我们下周开会讨论预算。"})['response'])
    # print(conversation_with_summary_buffer.invoke({"input": "你还记得我的项目代号吗？"})['response'])

    # print("\n--- 记忆内容 (摘要+缓冲区) ---")
    # print(summary_buffer_memory.load_memory_variables({}))
    # # 输出会包含一个摘要（如果旧消息被转换了）和最近的消息列表
    ```

#### 12.6 EntityMemory：实体记忆

`EntityMemory` 专注于从对话中提取和存储关于特定“实体”（如人、地点、事物、概念）的关键信息。它使用 LLM 来识别对话中的实体，并为每个实体维护一个信息摘要。

* **特点**:
    * **实体中心**: 围绕对话中提到的实体组织记忆。
    * **LLM 驱动提取**: 使用 LLM 识别实体并提取相关信息。
    * **结构化存储**: 将关于实体的信息存储在内部的“实体存储”中。
    * **上下文注入**: 将与当前对话相关的实体信息注入到提示中。
    * **键名 `entity_summary`**: 通常，它会将提取的实体信息总结后，通过一个特定的键（如 `entity_summary` 或在提示中指定的键）注入到上下文中。

* **适用场景**:
    * 需要模型深入理解和跟踪特定实体（如用户、产品、案例）的详细信息的应用。
    * 客服机器人需要记住客户的偏好、历史订单等。
    * 个人助手需要记住用户的习惯、重要日期等。
    * 知识图谱构建或信息提取任务的辅助。

* **缺点**:
    * **复杂性**: 设置和调整可能比简单的缓冲区记忆更复杂。
    * **LLM 依赖**: 强依赖 LLM 进行实体识别和摘要，可能增加成本和延迟。
    * **准确性**: 实体提取和信息关联的准确性取决于 LLM 的能力。

* **示例概念**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.chains import ConversationChain
    from langchain.memory import ConversationEntityMemory
    from langchain.prompts import PromptTemplate # EntityMemory 通常用 PromptTemplate
    # (假设 llm 已定义)

    # entity_memory = ConversationEntityMemory(
    #     llm=llm,
    #     # entity_store: 可以自定义实体存储方式，默认为内存字典
    #     # k: 控制返回多少个相关实体的信息
    #     # chat_history_key: 对话历史的键名，用于内部提取实体
    #     # memory_key: 注入到提示中的实体摘要的键名，默认为 'entities' 或 'entity_summary'
    #     #             可以查看源码或文档确认默认值，或显式设置。
    #     #             在 PromptTemplate 中使用这个键。
    # )

    # # 提示模板需要包含实体信息的占位符
    # # 实体记忆通常会将实体信息作为上下文注入。
    # # 它会提取输入中提到的实体，并从记忆中检索关于这些实体的信息。
    # # 默认情况下，它将实体信息存储在名为 "entities" 的键下。
    # # 这个 "entities" 的内容是关于当前输入中检测到的实体的已知信息摘要。
    # _DEFAULT_ENTITY_TEMPLATE = """
    # 你是一个AI助手。以下是关于当前对话中提到的实体的信息：
    # {entities}

    # 这是当前的对话历史：
    # {history}

    # Human: {input}
    # AI:"""
    # ENTITY_PROMPT = PromptTemplate(
    #     input_variables=["entities", "history", "input"],
    #     template=_DEFAULT_ENTITY_TEMPLATE
    # )

    # conversation_with_entity_memory = ConversationChain(
    #     llm=llm,
    #     prompt=ENTITY_PROMPT, # 使用上面定义的特殊提示
    #     memory=entity_memory,
    #     verbose=True
    # )

    # print(conversation_with_entity_memory.invoke({"input": "我姐姐Sarah有一只名叫Leo的猫。"})['response'])
    # print(conversation_with_entity_memory.invoke({"input": "Leo喜欢吃金枪鱼。Sarah住在伦敦。"})['response'])
    # print(conversation_with_entity_memory.invoke({"input": "Sarah的职业是什么？"})['response']) # AI可能不知道
    # print(conversation_with_entity_memory.invoke({"input": "Leo最喜欢的食物是什么？"})['response']) # AI应该能回答

    # print("\n--- 实体记忆内容 ---")
    # # 查看实体记忆内部存储的信息
    # print(entity_memory.entity_store.store)
    # # 输出会类似: {'Sarah': 'Sarah有一只名叫Leo的猫。Sarah住在伦敦。', 'Leo': 'Leo是Sarah的猫，喜欢吃金枪鱼。'}
    ```
    *注意*: `ConversationEntityMemory` 默认情况下可能需要调整提示模板以正确利用其输出。它会尝试将提取的实体信息填充到提示中的 `entities` 变量（默认的 `memory_key`）。

#### 12.7 VectorStoreRetrieverMemory：基于向量存储的记忆

`VectorStoreRetrieverMemory` 允许将对话的片段或关键信息存储到向量数据库中，并在需要时通过语义相似性检索相关的记忆片段作为上下文。

* **特点**:
    * **语义检索**: 不仅仅是按顺序存储，而是可以根据当前输入的语义内容检索最相关的历史信息。
    * **向量存储集成**: 需要一个向量存储（如 FAISS, Chroma, Pinecone）和一个嵌入模型。
    * **可扩展性**: 适合存储大量的历史信息，并高效检索。
    * **相关性**: 能够从大量历史中提取与当前查询最相关的信息，即使这些信息不是最近发生的。
    * **信息添加与检索**:
        * `save_context()`: 将当前的输入/输出对（或其他信息）转换为文档，嵌入并存入向量数据库。
        * `load_memory_variables()`: 当需要记忆时，它会获取当前输入，将其嵌入，然后在向量数据库中搜索最相似的先前对话片段。这些片段会被格式化并作为上下文返回。

* **适用场景**:
    * 需要从非常长的、非结构化的对话历史中检索特定相关信息的应用。
    * 构建能够“回忆”起久远但相关的讨论的智能助手。
    * 问答系统需要参考大量过去的交互来回答新问题。
    * 当简单的缓冲区或摘要记忆无法提供足够相关性的上下文时。

* **示例概念**:

    ```python
    from langchain_openai import OpenAIEmbeddings, ChatOpenAI
    from langchain_community.vectorstores import FAISS
    from langchain.memory import VectorStoreRetrieverMemory
    from langchain.docstore.document import Document
    from langchain.chains import ConversationChain
    from langchain_core.prompts import PromptTemplate
    import faiss # 需要安装 faiss-cpu 或 faiss-gpu
    # (假设 llm 和 embeddings 已定义)
    # embeddings = OpenAIEmbeddings()

    # 1. 创建一个向量存储 (这里用内存中的FAISS作为示例)
    # embedding_size = 1536 # OpenAI embeddings 维度
    # index = faiss.IndexFlatL2(embedding_size)
    # vectorstore = FAISS(embeddings.embed_query, index, InMemoryDocstore({}), {}) # 简化创建
    # retriever = vectorstore.as_retriever(search_kwargs=dict(k=1)) # 检索最相关的1个文档

    # 2. 创建 VectorStoreRetrieverMemory
    # vstore_memory = VectorStoreRetrieverMemory(
    #     retriever=retriever,
    #     memory_key="relevant_context" # 提示中用于相关上下文的变量名
    # )

    # # 3. 手动向记忆中添加一些上下文（模拟过去的对话）
    # # 通常这会在对话过程中自动发生，但这里我们手动添加以便演示
    # vstore_memory.save_context(
    #     {"input": "我喜欢苹果派。"},
    #     {"output": "好的，我会记住你喜欢苹果派。"}
    # )
    # vstore_memory.save_context(
    #     {"input": "我最喜欢的颜色是蓝色。"},
    #     {"output": "明白了，蓝色是你最喜欢的颜色。"}
    # )
    # vstore_memory.save_context(
    #     {"input": "我计划下周去夏威夷度假。"},
    #     {"output": "听起来很棒！夏威夷是个好地方。"}
    # )


    # # 4. 定义提示和链
    # prompt_vstore = PromptTemplate(
    #     input_variables=["relevant_context", "input"], # "history" 也可考虑，但主要依赖检索的上下文
    #     template="""
    # 以下是一些可能相关的先前对话内容：
    # {relevant_context}

    # 基于以上相关内容和当前对话，请回答问题。
    # Human: {input}
    # AI:"""
    # )

    # conversation_with_vstore_memory = ConversationChain(
    #     llm=llm,
    #     prompt=prompt_vstore,
    #     memory=vstore_memory,
    #     verbose=True
    # )

    # # 5. 进行对话，记忆会检索相关信息
    # response = conversation_with_vstore_memory.invoke({"input": "你还记得我喜欢吃什么甜点吗？"})
    # print(f"AI: {response['response']}") # 应该能检索到苹果派的信息

    # response2 = conversation_with_vstore_memory.invoke({"input": "我下周要去哪里？"})
    # print(f"AI: {response2['response']}") # 应该能检索到夏威夷的信息

    # print("\n--- 向量存储记忆 (通过检索器内容间接查看) ---")
    # # 直接查看向量存储的内容比较复杂，但可以通过检索器测试
    # # retrieved_docs = retriever.get_relevant_documents("我喜欢什么颜色？")
    # # for doc in retrieved_docs:
    # #     print(doc.page_content)
    ```
    *注意*: `VectorStoreRetrieverMemory` 在 `save_context` 时将输入和输出组合成一个文档存入向量库。在 `load_memory_variables` 时，它会使用当前的用户输入去检索相关的历史文档。

#### 12.8 在链和 Agent 中集成和管理记忆

将记忆集成到链（Chains）和智能体（Agents）中是发挥其作用的关键。

* **在链 (Chains) 中集成记忆**:
    * **`ConversationChain`**: 这是最常用于集成记忆的链。在创建 `ConversationChain` 时，可以直接通过 `memory` 参数传入一个记忆对象的实例。
        ```python
        # from langchain.chains import ConversationChain
        # from langchain.memory import ConversationBufferMemory
        # memory = ConversationBufferMemory()
        # conversation = ConversationChain(llm=my_llm, memory=memory, verbose=True)
        ```
    * **`LLMChain` 与提示**: 对于更基础的 `LLMChain`，如果其提示模板中包含了记忆变量（如 `history`），并且在调用链时手动将记忆内容加载并作为输入变量传递，也可以实现记忆效果。但 `ConversationChain` 封装了这个过程。
    * **自定义链**: 在自定义链中，可以在 `_call` 方法中显式地加载和保存记忆。
        ```python
        # class MyCustomChainWithMemory(Chain):
        #     memory: BaseMemory # 假设传入一个记忆对象
        #     # ... 其他属性 ...
        #
        #     def _call(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        #         # 1. 加载记忆
        #         memory_vars = self.memory.load_memory_variables(inputs)
        #         all_inputs = {**inputs, **memory_vars}
        #
        #         # 2. 执行链的核心逻辑 (例如，调用LLM)
        #         # result = some_llm_call(all_inputs["prompt_with_history"])
        #         # output_text = result["text"]
        #
        #         # 3. 保存上下文到记忆
        #         # self.memory.save_context(inputs, {"output": output_text})
        #
        #         # return {"answer": output_text}
        ```

* **在智能体 (Agents) 中集成记忆**:
    * **Agent Executor**: 当使用 `AgentExecutor` 来运行智能体时，可以将记忆对象传递给它。智能体在规划和执行步骤时，会将记忆内容考虑到提示中。
        ```python
        # from langchain.agents import AgentExecutor, create_openai_tools_agent
        # from langchain_openai import ChatOpenAI
        # from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
        # # from langchain.memory import ConversationBufferMemory (或其他记忆类型)
        # # tools = [...]
        # # llm = ChatOpenAI(...)
        # # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        # agent_prompt = ChatPromptTemplate.from_messages([
        #     ("system", "你是一个强大的助手。"),
        #     MessagesPlaceholder(variable_name="chat_history"), # 记忆的占位符
        #     ("human", "{input}"),
        #     MessagesPlaceholder(variable_name="agent_scratchpad") # Agent内部思考过程
        # ])

        # agent = create_openai_tools_agent(llm, tools, agent_prompt)
        # agent_executor = AgentExecutor(
        #     agent=agent,
        #     tools=tools,
        #     memory=memory, # 将记忆实例传递给AgentExecutor
        #     verbose=True
        # )

        # agent_executor.invoke({"input": "你好，我叫小李。"})
        # agent_executor.invoke({"input": "你还记得我叫什么吗？"})
        ```
    * **Agent 的提示**: 智能体的提示模板中必须包含记忆变量的占位符（例如 `MessagesPlaceholder(variable_name="chat_history")` 或 `{history}`），以便 `AgentExecutor` 能够将记忆内容注入。

* **管理记忆**:
    * **共享记忆**: 可以在多个链或智能体之间共享同一个记忆对象实例，从而使它们能够访问相同的上下文历史。这对于构建更大型、模块化的应用非常有用。
    * **清空记忆**: 大多数记忆对象都有一个 `clear()` 方法，可以用来清空其存储的所有历史记录。
        ```python
        # memory.clear()
        ```
    * **选择合适的记忆类型**: 根据应用的具体需求（对话长度、对细节的需求、Token 限制、成本考虑、是否需要语义检索等）选择最合适的记忆类型至关重要。
    * **记忆变量名 (`memory_key`)**: 确保记忆对象中设置的 `memory_key` 与提示模板中用于插入记忆内容的变量名一致。
    * **`return_messages=True`**: 当与 `ChatModels` 一起使用时，通常建议在缓冲区类型的记忆（如 `ConversationBufferMemory`, `ConversationBufferWindowMemory`）中设置 `return_messages=True`。这将使记忆返回一个消息对象列表（如 `HumanMessage`, `AIMessage`），这与 `ChatModels` 的期望输入格式更兼容。如果为 `False`（默认），它会将历史格式化为单个字符串。
    * **异步支持**: LangChain 中的许多组件，包括记忆，也支持异步操作 (`aload_memory_variables`, `asave_context`)，这对于构建高性能的异步应用非常重要。

通过有效地使用和管理记忆，可以显著提升 LangChain 应用的交互质量和用户体验，使其更加智能和上下文感知。


### 第十三章：高级记忆策略

在前一章中，我们探讨了 LangChain 提供的各种标准记忆类型。然而，在构建复杂的、生产级的应用程序时，我们可能需要更精细的控制、自定义的记忆行为或更鲁棒的记忆管理机制。本章将介绍一些高级的记忆策略，包括创建自定义记忆类型、在多轮对话中有效管理记忆，以及记忆的持久化与加载。

#### 13.1 自定义记忆类型

虽然 LangChain 提供了丰富的内置记忆类型，但有时特定应用的需求可能超出了这些标准实现的范围。在这种情况下，你可以通过继承 LangChain 的 `BaseMemory` 或更具体的记忆基类（如 `BaseChatMemory`）来创建自己的自定义记忆模块。

* **为什么需要自定义记忆?**:
    * **独特的存储后端**: 你可能希望将记忆存储在 LangChain 未直接支持的特定数据库、文件格式或专有系统中。
    * **复杂的记忆逻辑**: 应用可能需要非标准的记忆修剪策略（例如，基于情感分析保留特定消息，或根据业务规则加权记忆片段）。
    * **与外部系统集成**: 记忆可能需要与外部知识库、用户画像系统或其他服务进行实时交互。
    * **特定的数据结构**: 你可能需要以特定的结构（而非简单的消息列表或摘要）来组织记忆内容。
    * **性能优化**: 针对特定用例高度优化的记忆加载和保存机制。

* **创建自定义记忆的关键步骤 (继承 `BaseMemory`)**:
    1.  **继承基类**: 通常选择 `BaseMemory` 或 `BaseChatMemory`（如果处理聊天消息）。
        ```python
        from langchain.memory.chat_memory import BaseChatMemory
        from langchain_core.messages import BaseMessage
        from typing import List, Dict, Any

        class MyCustomMemory(BaseChatMemory):
            # ...
        ```
    2.  **定义输入/输出键**:
        * `memory_variables`: 一个属性，返回此记忆类型将添加到链输入中的变量名列表。
            ```python
            @property
            def memory_variables(self) -> List[str]:
                return ["my_custom_context"] # 示例
            ```
    3.  **实现核心方法**:
        * `load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]`:
            * 这是最重要的读取方法。它接收当前链的输入（可能用于指导如何加载记忆），并应返回一个字典，其中键是 `memory_variables` 中定义的变量名，值是加载的记忆内容。
            * 例如，从自定义数据库加载特定用户的对话历史，并将其格式化。
        * `save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None`:
            * 当链执行完毕后，此方法被调用以保存当前的交互。`inputs` 是传递给 LLM 的输入（不包括之前的记忆），`outputs` 是 LLM 的响应。
            * 例如，将新的用户输入和 AI 回复存储到自定义数据库中。
        * `clear(self) -> None`:
            * 实现清空记忆的逻辑。

* **示例概念 (简化的自定义记忆)**:
    假设我们要创建一个简单的基于文件的记忆，将每次对话保存为 JSON 行。

    ```python
    import json
    from langchain.memory.chat_memory import BaseChatMemory
    from langchain_core.messages import BaseMessage, get_buffer_string, AIMessage, HumanMessage
    from typing import List, Dict, Any

    class FileJsonLinesChatMemory(BaseChatMemory):
        file_path: str
        chat_memory_key: str = "history" # 与 BaseChatMemory 一致

        def __init__(self, file_path: str, chat_memory_key: str = "history", **kwargs):
            super().__init__(**kwargs) # chat_memory (MessageBuffer) 会在这里初始化
            self.file_path = file_path
            self.chat_memory_key = chat_memory_key
            self._load_from_file()

        def _load_from_file(self):
            try:
                with open(self.file_path, "r") as f:
                    for line in f:
                        data = json.loads(line)
                        if data.get("type") == "human":
                            self.chat_memory.add_user_message(data["content"])
                        elif data.get("type") == "ai":
                            self.chat_memory.add_ai_message(data["content"])
            except FileNotFoundError:
                self.chat_memory.clear() # 如果文件不存在，则从空记忆开始

        @property
        def memory_variables(self) -> List[str]:
            return [self.chat_memory_key]

        def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
            # BaseChatMemory 提供了 buffer_as_messages 和 buffer_as_str
            if self.return_messages:
                return {self.chat_memory_key: self.chat_memory.messages}
            else:
                return {self.chat_memory_key: get_buffer_string(self.chat_memory.messages)}

        def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
            # 调用父类的 save_context 来更新内存中的 chat_memory
            super().save_context(inputs, outputs)
            # 现在将更新后的 chat_memory 持久化到文件
            # 为简化，这里每次都重写整个文件；更优化的方式是追加
            with open(self.file_path, "w") as f:
                for message in self.chat_memory.messages:
                    if isinstance(message, HumanMessage):
                        f.write(json.dumps({"type": "human", "content": message.content}) + "\n")
                    elif isinstance(message, AIMessage):
                        f.write(json.dumps({"type": "ai", "content": message.content}) + "\n")

        def clear(self) -> None:
            super().clear() # 清空内存中的 chat_memory
            try:
                open(self.file_path, "w").close() # 清空文件内容
            except FileNotFoundError:
                pass # 文件不存在，无需操作

    # 使用自定义记忆
    # file_memory = FileJsonLinesChatMemory(file_path="./my_chat_history.jsonl", return_messages=True)
    # (然后可以将 file_memory 传递给 ConversationChain 等)
    # conversation = ConversationChain(llm=llm, memory=file_memory, verbose=True)
    # conversation.invoke({"input": "我的自定义记忆好用吗？"})
    # conversation.invoke({"input": "它能记住上一句话吗？"})
    ```
    这个示例相对简单，实际的自定义记忆可能需要处理更复杂的序列化、错误处理和并发访问。

#### 13.2 多轮对话中的记忆管理

在持续的、多轮对话中，有效地管理记忆至关重要，以确保对话的连贯性、相关性，并避免超出模型的上下文限制或产生不必要的成本。

* **挑战**:
    * **上下文窗口限制**: 随着对话轮次的增加，原始对话历史很容易超出 LLM 的 Token 限制。
    * **信息过载与相关性**: 并非所有历史信息都对当前轮次同等重要。模型可能会被不相关的旧信息干扰。
    * **成本**: 将大量历史数据发送给 LLM 会增加 Token 消耗和 API 调用成本。
    * **长期依赖**: 有时，非常早期的信息可能在后续对话中变得关键。

* **策略与技术**:
    1.  **选择合适的记忆类型**:
        * **短期对话**: `ConversationBufferMemory` 可能足够。
        * **中等长度，近期重要**: `ConversationBufferWindowMemory`, `ConversationTokenBufferMemory`。
        * **长对话，概览重要**: `ConversationSummaryMemory`。
        * **长对话，兼顾近期细节与长期概览**: `ConversationSummaryBufferMemory` (推荐)。
        * **特定信息检索**: `VectorStoreRetrieverMemory` (当需要基于语义从大量历史中检索时)，`EntityMemory` (当围绕特定实体组织信息时)。

    2.  **动态记忆修剪/压缩**:
        * **摘要化**: 定期或在达到阈值时，将旧的对话历史总结成更紧凑的形式。
        * **选择性遗忘**: 实现逻辑来丢弃不重要或不相关的记忆片段。例如，可以基于时间、主题变化或用户明确指示来修剪。
        * **分层记忆**: 维护不同粒度的记忆层（如短期工作记忆、中期摘要、长期知识库），并根据需要组合它们。

    3.  **上下文管理**:
        * **明确的上下文注入**: 在提示工程中，明确指示模型如何使用提供的历史信息（例如，“基于以下最近对话...”或“考虑到用户之前提到的关于X的信息...”）。
        * **会话分段 (Session Segmentation)**: 对于非常长的交互，可以考虑将会话逻辑上分割成子会话，每个子会话有其独立的或部分共享的记忆。当切换主题或达到一定长度时，可以存档旧会话的记忆并开始新的记忆。

    4.  **用户引导与控制**:
        * 允许用户明确引用之前的对话内容（例如，“关于我们之前讨论的X...”)。
        * 提供命令让用户清除或重置记忆。

    5.  **与外部知识库结合**:
        * 对于事实性或领域特定的信息，与其完全依赖对话记忆，不如将对话历史与外部知识库（如向量数据库、图数据库）检索相结合。记忆可以用来理解当前对话的上下文，而知识库提供具体信息。

    6.  **Agent 中的记忆利用**:
        * 智能体 (Agent) 在规划时可以利用记忆来决定下一步行动。例如，如果用户之前表达过某种偏好，智能体可以使用这个记忆来调整其工具选择或参数。
        * 智能体的反思 (Reflection) 机制可以用来分析过去的交互（存储在记忆中），从中学习并改进未来的行为。

* **示例思考：客服机器人场景**
    一个处理技术支持的客服机器人可能需要：
    * `ConversationSummaryBufferMemory`: 记住最近几轮用户的具体描述和AI的回复（缓冲区），同时对整个问题的历史有一个摘要（摘要部分）。
    * `EntityMemory` (可选): 记住用户的账户ID、正在咨询的产品型号等关键实体。
    * 持久化: 将对话状态保存，以便用户下次联系时可以继续。
    * 在对话开始时，加载历史。如果用户提到“我上次说的问题”，机器人应能理解。
    * 如果对话过长或主题转移，摘要部分会变得更重要。

#### 13.3 记忆的持久化与加载

默认情况下，LangChain 中的大多数记忆对象都只存在于内存中。当应用程序关闭或会话结束时，这些记忆内容就会丢失。对于需要跨会话保持状态的应用（如长期客服、个性化助手），记忆的持久化至关重要。

* **为什么需要持久化?**:
    * **跨会话连续性**: 用户关闭浏览器或应用后，下次回来时可以从上次中断的地方继续对话。
    * **用户画像**: 长期积累用户偏好和历史，提供更个性化的服务。
    * **状态恢复**: 在应用意外崩溃或重启后，能够恢复之前的对话状态。
    * **分析与审计**: 将对话历史存档，用于后续分析、模型改进或合规性检查。

* **持久化策略**:
    1.  **文件存储**:
        * **简单文本/JSON/Pickle**: 对于简单的记忆（如 `ConversationBufferMemory` 的消息列表），可以直接序列化为 JSON、文本文件或使用 Python 的 `pickle` 模块。
        * `FileJsonLinesChatMemory` (如自定义示例) 就是一种文件持久化。
        * **优点**: 实现简单，无需外部依赖。
        * **缺点**: 不适合大规模并发访问，扩展性有限，管理复杂。

    2.  **数据库存储**:
        * **关系型数据库 (SQL)**: 如 PostgreSQL, MySQL, SQLite。可以将每条消息、会话元数据存储为表中的行。可以使用 SQLAlchemy 等 ORM 进行交互。LangChain 有 `SQLChatMessageHistory`。
        * **NoSQL 数据库**:
            * **键值存储 (Key-Value Stores)**: 如 Redis, Memcached。非常适合快速存取会话状态或最近的对话历史。LangChain 有 `RedisChatMessageHistory`。
            * **文档数据库 (Document Stores)**: 如 MongoDB。适合存储结构灵活的对话数据（例如，JSON 格式的消息和元数据）。LangChain 有 `MongoDBChatMessageHistory`。
            * **图数据库 (Graph Databases)**: 如 Neo4j。适合存储和查询实体及其关系复杂的记忆，例如 `EntityMemory` 的内容。
        * **优点**: 更健壮，支持并发，可扩展性好，易于查询和管理。
        * **缺点**: 需要配置和维护数据库。

    3.  **云存储服务**:
        * 利用云提供商（AWS, Google Cloud, Azure）的对象存储服务 (S3, GCS, Blob Storage) 或其托管数据库服务。

    4.  **向量数据库的持久化**:
        * 当使用 `VectorStoreRetrieverMemory` 时，记忆本身就是存储在向量数据库中的。许多向量数据库（如 Pinecone, Weaviate, Qdrant, Chroma 的持久化模式）自身就支持数据的持久化。

* **LangChain 中的 `ChatMessageHistory` 对象**:
    LangChain 提供了一个 `ChatMessageHistory` 基类和多种具体实现，用于处理聊天消息的存储和检索，这些是记忆持久化的核心。
    * `FileChatMessageHistory`
    * `RedisChatMessageHistory`
    * `MongoDBChatMessageHistory`
    * `PostgresChatMessageHistory`
    * `SQLiteChatMessageHistory`
    * `DynamoDBChatMessageHistory`
    * `CassandraChatMessageHistory`
    * 等...

    这些 `ChatMessageHistory` 对象可以与 `BaseChatMemory` 的子类（如 `ConversationBufferMemory`）结合使用，以实现持久化。你只需将 `chat_memory` 参数设置为一个配置好的持久化 `ChatMessageHistory` 实例。

* **示例概念 (使用 `RedisChatMessageHistory` 与 `ConversationBufferMemory`)**:

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.memory import ConversationBufferMemory
    from langchain_community.chat_message_histories import RedisChatMessageHistory # 使用社区版
    from langchain.chains import ConversationChain
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    import os

    # 确保已安装 redis 和 redis-py: pip install redis
    # 假设 Redis 服务器正在本地运行 localhost:6379
    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # 为每个对话或用户创建一个唯一的 session_id
    # session_id_user1 = "user123_chat_session_abc"

    # message_history_user1 = RedisChatMessageHistory(
    #     session_id=session_id_user1,
    #     url="redis://localhost:6379/0" # Redis 连接 URL
    # )

    # # 将持久化的消息历史注入到标准记忆类型中
    # persistent_memory_user1 = ConversationBufferMemory(
    #     chat_memory=message_history_user1, # 关键步骤！
    #     memory_key="chat_history",
    #     return_messages=True
    # )

    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "你是一个能记住跨会话内容的AI。"),
    #     MessagesPlaceholder(variable_name="chat_history"),
    #     ("human", "{input}")
    # ])

    # conversation_user1 = ConversationChain(
    #     llm=llm,
    #     prompt=prompt,
    #     memory=persistent_memory_user1,
    #     verbose=True
    # )

    # # 第一次交互 (如果 session_id 是新的，记忆为空)
    # print(conversation_user1.invoke({"input": "你好，我最喜欢的运动是篮球。"}))

    # # 假设应用重启，或用户下次登录
    # # 只要使用相同的 session_id 重新创建 message_history 和 memory 对象，
    # # 之前的对话就会被加载。

    # # session_id_user1_again = "user123_chat_session_abc" # 相同的 session_id
    # # message_history_user1_again = RedisChatMessageHistory(
    # # session_id=session_id_user1_again, url="redis://localhost:6379/0"
    # # )
    # # persistent_memory_user1_again = ConversationBufferMemory(
    # # chat_memory=message_history_user1_again,
    # # memory_key="chat_history",
    # # return_messages=True
    # # )
    # # conversation_user1_again = ConversationChain(
    # #     llm=llm,
    # #     prompt=prompt,
    # #     memory=persistent_memory_user1_again,
    # #     verbose=True
    # # )

    # # print(conversation_user1_again.invoke({"input": "你还记得我最喜欢的运动是什么吗？"}))
    # # AI 应该能回答“篮球”

    # # 清理特定会话的记忆 (可选)
    # # message_history_user1.clear()
    ```
    这种方法将记忆的“存储”部分委托给了专门的 `ChatMessageHistory` 实现，而记忆的“逻辑”（如缓冲、摘要）仍然由 `ConversationBufferMemory` 等标准记忆类处理。

通过结合自定义记忆、精细的多轮对话管理策略以及可靠的持久化机制，你可以构建出能够提供长期、连贯且高度个性化交互体验的复杂 LangChain 应用。

##模块六：智能代理 (Agents) 的开发与应用

智能代理 (Agents) 是 LangChain 中最强大和最令人兴奋的功能之一。与简单地响应输入的链 (Chains) 不同，代理使用语言模型 (LLM) 作为其“大脑”或“推理引擎”，使其能够动态地决定采取哪些行动、使用哪些工具以及如何响应用户输入，以达成给定的目标。代理可以与外部世界交互，执行代码，访问数据库，搜索网络等等，从而完成比传统链更复杂的任务。

本模块将深入探讨代理的构建、使用和高级应用。

### 第十四章：Agent 基础

本章将介绍智能代理的核心概念、组成部分、工作流程以及如何使用和创建工具。

#### 14.1 Agent 的核心组件：Tools, Agent (Class/Logic), Agent Executor

一个 LangChain Agent 系统通常由以下三个核心组件构成：

1.  **工具 (Tools)**:
    * **定义**: 工具是代理可以执行的特定功能的接口。每个工具都设计用来执行一个明确的任务，例如：进行网络搜索、运行 Python 代码、查询数据库、调用 API 等。
    * **作用**: 赋予代理与外部环境或其他系统交互的能力。代理本身并不直接执行这些操作，而是决定使用哪个工具，并向该工具提供输入。
    * **接口**: 工具通常需要一个清晰的名称 (`name`) 和描述 (`description`)，代理的 LLM 会利用这些信息来判断何时以及如何使用该工具。它们还需要实现一个运行方法（通常是 `_run(tool_input: str) -> str` 和可选的异步版本 `_arun`）。
    * **示例**: `GoogleSearchTool`, `WikipediaQueryRun`, `PythonREPLTool`, `RequestsGetTool`。

2.  **代理 (Agent - Class/Logic)**:
    * **定义**: 这是代理的“大脑”，通常是一个经过特殊提示工程的 LLM（或 ChatModel）。它负责接收用户输入、分析当前情况、根据可用工具的描述选择合适的工具及相应的输入，并解析工具的输出以决定下一步行动或生成最终回复。
    * **作用**:
        * **决策制定**: 根据目标和当前上下文，决定是否使用工具，以及使用哪个工具。
        * **输入格式化**: 为选定的工具准备正确的输入。
        * **输出解析**: 理解工具执行后返回的结果。
        * **迭代执行**: 可能需要多次调用工具或进行多步思考才能完成任务。
    * **实现**: LangChain 提供了多种预构建的代理类型（例如 `create_openai_tools_agent`, `create_react_agent`, `create_self_ask_with_search_agent`），它们封装了特定的提示和逻辑来驱动 LLM 进行决策。你也可以创建自定义的代理逻辑。

3.  **代理执行器 (Agent Executor)**:
    * **定义**: `AgentExecutor` 是实际运行代理并协调其与工具交互的运行时环境。它负责调用代理获取行动计划，执行工具，将工具的观察结果返回给代理，并循环此过程直到代理决定给出最终答案或达到停止条件。
    * **作用**:
        * **循环执行**: 管理代理的“思考-行动-观察”循环。
        * **工具调用**: 实际执行代理选定的工具。
        * **错误处理**: 可以配置如何处理工具执行错误或代理决策错误。
        * **停止条件**: 管理代理何时结束其工作（例如，找到答案、达到最大迭代次数）。
        * **记忆集成**: 可以与记忆模块集成，使代理能够记住先前的交互。
        * **回调与日志**: 支持回调函数，用于监控和记录代理的执行过程。

* **组件交互流程**:
    1.  用户向 `AgentExecutor` 提供输入。
    2.  `AgentExecutor` 将输入（以及任何记忆/上下文）传递给 `Agent` (LLM)。
    3.  `Agent` (LLM) 根据其提示和可用工具，决定采取一个行动（使用某个工具并提供输入）或直接回复。
    4.  如果 `Agent` 决定使用工具：
        a.  `AgentExecutor` 调用选定的 `Tool` 并传入指定的输入。
        b.  `Tool` 执行其任务并返回一个观察结果 (Observation)。
        c.  `AgentExecutor` 将此观察结果反馈给 `Agent` (LLM)。
        d.  返回步骤 3，`Agent` (LLM) 基于新的观察结果决定下一步行动。
    5.  如果 `Agent` 决定直接回复（认为任务已完成），`AgentExecutor` 将该回复作为最终输出返回给用户。

#### 14.2 理解 Agent 的思考过程 (Thought, Action, Observation)

代理的强大之处在于其类似人类的“思考”过程。虽然这并非真正的意识，但通过精心设计的提示和与 LLM 的交互，代理可以模拟一个推理和决策的循环。这个过程通常可以分解为以下几个关键步骤，尤其是在像 ReAct (Reasoning and Acting) 这样的代理框架中：

1.  **思考 (Thought)**:
    * **描述**: 在这一步，代理（LLM）会分析当前的目标、已有的信息（包括用户输入、之前的步骤、工具的观察结果、记忆等）。它会进行推理，评估自己是否需要更多信息，或者是否已经可以给出最终答案。
    * **输出**: 通常是一段内部的“思考”文本，解释其当前的分析和下一步的计划。例如：“我需要找到关于X的信息，我应该使用搜索工具。”
    * **作用**: 这是代理进行规划和决策的核心。通过明确地生成思考过程，可以提高代理的透明度和可解释性，也使得 LLM 能够更好地进行多步推理。

2.  **行动 (Action)**:
    * **描述**: 如果代理的“思考”表明需要执行某个操作（通常是使用一个工具），它就会决定一个“行动”。
    * **输出**: 一个结构化的表示，通常包括：
        * **工具 (Tool)**: 要使用的工具的名称。
        * **工具输入 (Tool Input)**: 提供给该工具的具体参数或查询。
    * **示例**: `Action: SearchTool, Action Input: "LangChain Agent 的最新进展"`
    * **注意**: 如果代理认为它已经有足够的信息来回答问题，它可能会决定一个“最终行动”或直接生成最终答案，而不是调用工具。

3.  **观察 (Observation)**:
    * **描述**: 这是执行“行动”后从工具返回的结果。
    * **输出**: 工具执行后的输出数据。例如，搜索工具可能返回网页摘要列表，计算器工具可能返回一个数字。
    * **作用**: 观察结果会作为新的信息反馈给代理的下一个“思考”步骤，帮助代理评估其行动的有效性，并决定后续的行动。

* **循环 (The Loop)**:
    代理通常会重复“思考 -> 行动 -> 观察”这个循环，直到：
    * 它认为已经收集到足够的信息来回答用户最初的问题或完成任务。
    * 达到预设的最大迭代次数或时间限制。
    * 遇到无法恢复的错误。

* **ReAct 框架示例**:
    ReAct 是一个流行的代理框架，它明确地将推理（Thought）和行动（Action）结合起来。
    * **用户问题**: "法国的首都是哪里？它的人口是多少？"
    * **Thought 1**: 我需要先找到法国的首都。我可以使用搜索工具。
    * **Action 1**: `Tool: Search, Tool Input: "法国的首都是哪里"`
    * **Observation 1**: "法国的首都是巴黎。"
    * **Thought 2**: 我现在知道首都是巴黎。接下来我需要找到巴黎的人口。我应该再次使用搜索工具。
    * **Action 2**: `Tool: Search, Tool Input: "巴黎的人口"`
    * **Observation 2**: "根据最新数据，巴黎市的人口约为210万。"
    * **Thought 3**: 我已经找到了法国的首都（巴黎）和它的人口（约210万）。我可以回答用户的问题了。
    * **Final Answer**: 法国的首都是巴黎，其人口约为210万。

通过 `verbose=True` 参数，在 `AgentExecutor` 中通常可以看到这些中间的思考、行动和观察步骤，这对于调试和理解代理的行为非常有帮助。

#### 14.3 内置 Tools 的使用 (Google Search, Wikipedia, Python REPL, Shell 等)

LangChain 提供了一系列可以直接使用的内置工具，这些工具封装了与常见服务和功能的交互逻辑。使用这些工具可以快速为你的代理添加强大的能力。

* **如何使用内置工具**:
    1.  **导入**: 从 `langchain_community.tools` 或其他相关模块导入所需的工具。
    2.  **实例化与配置**: 某些工具可能需要 API 密钥（通过环境变量设置或直接传入参数）或其他配置。
    3.  **传递给 Agent**: 将实例化后的工具列表传递给创建代理的函数（如 `create_openai_tools_agent`）或直接给 `AgentExecutor`。

* **常用内置工具示例**:

    1.  **搜索工具**:
        * **`GoogleSearchRun` / `DuckDuckGoSearchRun` / `BraveSearch`**:
            * **功能**: 执行网络搜索。
            * **配置**: 通常需要对应的 API 密钥（例如，Google Custom Search API 的 `GOOGLE_API_KEY` 和 `GOOGLE_CSE_ID`；Brave Search API 的 `BRAVE_SEARCH_API_KEY`）。
            * **使用**: `GoogleSearchRun()`
            * **场景**: 回答需要最新信息或广泛知识的问题。
        * **`WikipediaQueryRun`**:
            * **功能**: 从维基百科查询信息。依赖 `wikipedia` Python 包。
            * **配置**: 无需 API 密钥。
            * **使用**: `WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())`
            * **场景**: 获取关于特定主题、人物、地点等的百科知识。

    2.  **代码执行工具**:
        * **`PythonREPLTool`**:
            * **功能**: 执行 Python 代码片段并在一个 REPL (Read-Eval-Print Loop) 环境中返回结果。非常强大但也需要谨慎使用，因为它有执行任意代码的能力。
            * **配置**: 无需特殊配置。
            * **使用**: `PythonREPLTool()`
            * **场景**: 进行计算、数据处理、动态生成代码等。
        * **`ShellTool` (或 `BashProcess`)**:
            * **功能**: 在底层操作系统上执行 shell 命令。同样非常强大且有潜在风险。
            * **配置**: 无需特殊配置，但要注意执行环境的权限。
            * **使用**: `ShellTool()`
            * **场景**: 与文件系统交互、运行脚本、调用命令行工具。

    3.  **数学工具**:
        * **`NumPyCalculatorTool` / `LLMMathChain`**:
            * **功能**: `LLMMathChain` 使用 LLM 来理解数学问题并用 Python `numexpr` 库进行计算。`NumPyCalculatorTool` 也类似。
            * **配置**: 可能需要 LLM 实例。
            * **使用**: (通常作为链) `LLMMathChain.from_llm(llm)`
            * **场景**: 解决数学问题，执行数值计算。

    4.  **HTTP 请求工具**:
        * **`RequestsGetTool`, `RequestsPostTool`, etc.** (通常通过 `RequestsToolkit` 或自定义实现):
            * **功能**: 发送 HTTP GET, POST 等请求到指定的 URL。
            * **配置**: 需要 `requests` 库。
            * **使用**: (通常包装在自定义工具中或通过 `OpenAPI` 规范自动生成)
            * **场景**: 与外部 API 交互，获取网络资源。

    5.  **数据库工具**:
        * **`SQLDatabaseToolkit` / `SQLDatabaseChain`**:
            * **功能**: 允许代理查询 SQL 数据库。它包含生成 SQL 查询、执行查询、检查表结构等工具。
            * **配置**: 需要数据库连接 (`SQLDatabase` 对象)。
            * **使用**: `SQLDatabaseToolkit(db=db, llm=llm)`
            * **场景**: 从结构化数据库中提取和分析数据。

    6.  **文件系统工具**:
        * **`ReadFileTool`, `WriteFileTool`, `ListDirectoryTool`** (通常包含在 `FileSystemToolkit` 中):
            * **功能**: 读写文件，列出目录内容。
            * **配置**: 无。
            * **场景**: 代理需要处理本地文件。

* **示例：使用 Google Search 和 Wikipedia 工具**

    ```python
    import os
    from langchain_openai import ChatOpenAI
    from langchain.agents import AgentExecutor, create_openai_tools_agent
    from langchain_community.tools import WikipediaQueryRun, GoogleSearchRun
    from langchain_community.utilities import WikipediaAPIWrapper, GoogleSearchAPIWrapper
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

    # 设置 API 密钥 (确保已安装 google-api-python-client)
    # os.environ["GOOGLE_API_KEY"] = "YOUR_GOOGLE_API_KEY"
    # os.environ["GOOGLE_CSE_ID"] = "YOUR_GOOGLE_CSE_ID"
    # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

    # llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

    # search_wrapper = GoogleSearchAPIWrapper()
    # Google Search_tool = GoogleSearchRun(api_wrapper=search_wrapper, name="GoogleSearch")

    # wikipedia_api_wrapper = WikipediaAPIWrapper()
    # wikipedia_tool = WikipediaQueryRun(api_wrapper=wikipedia_api_wrapper, name="Wikipedia")

    # tools = [Google Search_tool, wikipedia_tool]

    # agent_prompt = ChatPromptTemplate.from_messages([
    #     ("system", "你是一个乐于助人的AI助手。你可以使用Google Search和Wikipedia来查找信息。"),
    #     MessagesPlaceholder(variable_name="chat_history", optional=True),
    #     ("human", "{input}"),
    #     MessagesPlaceholder(variable_name="agent_scratchpad")
    # ])

    # agent = create_openai_tools_agent(llm, tools, agent_prompt)
    # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # # 提问
    # response = agent_executor.invoke({
    #     "input": "LangChain框架的创始人是谁？他/她有什么其他的知名项目？"
    # })
    # print(response.get("output"))

    # response2 = agent_executor.invoke({
    #     "input": "夏威夷的最高峰是什么？它的海拔高度是多少？"
    # })
    # print(response2.get("output"))
    ```
    *注意*: 某些工具如 `GoogleSearchRun` 可能因为 LangChain 版本的更新而调整其导入路径或使用方式，例如直接使用 `GoogleSearchAPIWrapper` 实例或通过 `Tool` 装饰器包装。请参考最新的 LangChain 文档。

#### 14.4 创建自定义 Tools

虽然 LangChain 提供了许多有用的内置工具，但通常你需要创建自己的工具来与特定的 API、专有系统或自定义逻辑进行交互。

* **创建自定义工具的方法**:

    1.  **使用 `@tool` 装饰器 (推荐的简单方法)**:
        * 为简单的、接受一个或多个字符串/数字/布尔参数并返回一个字符串的函数设计。
        * 函数的 docstring 会被用作工具的描述，这对 LLM 理解何时使用该工具至关重要。
        * 参数的类型注解可以帮助 LangChain 生成 Pydantic 模型，用于结构化工具输入。

        ```python
        from langchain.tools import tool
        from pydantic import BaseModel, Field # 用于定义结构化输入

        @tool
        def get_weather(city: str) -> str:
            """
            查询指定城市的当前天气信息。
            例如：输入 "北京"，返回 "北京今天晴朗，25摄氏度。"
            """
            # 实际中这里会调用一个天气API
            if city.lower() == "honolulu":
                return f"{city} 当前天气：晴朗，28°C。"
            elif city.lower() == "london":
                return f"{city} 当前天气：多云，15°C。"
            else:
                return f"抱歉，我无法查询 {city} 的天气。"

        # 具有结构化输入的工具
        class BookSearchInput(BaseModel):
            title: str = Field(description="要搜索的书籍标题")
            author: str = Field(description="书籍的作者（可选）")

        @tool("book-search", args_schema=BookSearchInput, return_direct=False)
        def search_book(title: str, author: str = None) -> str:
            """根据书名和可选的作者名搜索书籍信息。"""
            if author:
                return f"找到关于 '{title}' 作者 '{author}' 的书籍信息..."
            else:
                return f"找到关于 '{title}' 的书籍信息..."


        # my_tools = [get_weather, search_book]
        # (然后可以将 my_tools 列表传递给 Agent)
        ```
        * `name` (可选): 工具的名称，默认为函数名。
        * `description` (可选): 工具的描述，默认为函数 docstring。
        * `args_schema` (可选): 一个 Pydantic 模型，用于定义结构化的输入参数。这对于需要多个参数或复杂输入的工具非常有用。LLM 会尝试填充这个模型的字段。
        * `return_direct` (可选): 如果为 `True`，当代理决定使用此工具时，此工具的输出将直接作为最终答案返回给用户，代理执行器将停止。

    2.  **继承 `BaseTool` 类 (更灵活和强大的方法)**:
        * 适用于更复杂的工具，例如需要异步执行、自定义错误处理、管理内部状态或与复杂 SDK 交互的工具。
        * 需要实现以下核心属性/方法：
            * `name: str`: 工具的唯一名称。
            * `description: str`: 工具功能的详细描述，供 LLM 理解。
            * `args_schema: Optional[Type[BaseModel]]` (可选): 定义输入参数的 Pydantic 模型。
            * `_run(self, tool_input_arg1: type, tool_input_arg2: type, ..., **kwargs) -> str`: 同步执行工具的核心逻辑。参数名应与 `args_schema` 中的字段名匹配。
            * `_arun(self, ..., **kwargs) -> Coroutine[Any, Any, str]` (可选): 异步执行工具的核心逻辑。

        ```python
        from langchain.tools import BaseTool
        from typing import Type, Optional
        from pydantic import BaseModel, Field
        import asyncio

        class AdvancedCalculatorInput(BaseModel):
            expression: str = Field(description="要计算的数学表达式，例如 '2+2*5'")

        class AdvancedCalculatorTool(BaseTool):
            name: str = "advanced_calculator"
            description: str = "一个高级计算器，可以执行复杂的数学表达式字符串并返回结果。只接受有效的数学表达式。"
            args_schema: Type[BaseModel] = AdvancedCalculatorInput

            def _run(self, expression: str) -> str:
                try:
                    # 注意：eval() 有安全风险，实际应用中应使用更安全的解析库
                    result = eval(expression)
                    return f"表达式 '{expression}' 的计算结果是: {result}"
                except Exception as e:
                    return f"计算表达式 '{expression}' 时出错: {str(e)}"

            async def _arun(self, expression: str) -> str:
                # 对于简单计算，同步和异步可能没有太大区别
                # 但如果涉及到异步IO操作（如API调用），则这里会体现出来
                await asyncio.sleep(0.1) # 模拟异步操作
                return self._run(expression) # 调用同步版本

        # adv_calculator = AdvancedCalculatorTool()
        # my_tools = [adv_calculator]
        # (然后可以将 my_tools 列表传递给 Agent)
        ```

* **良好工具设计的关键**:
    * **清晰的名称 (`name`)**: 简洁且能概括工具的功能。
    * **详细的描述 (`description`)**: 这是最重要的部分！LLM 完全依赖描述来理解工具能做什么、何时应该使用它、期望的输入格式以及输出的含义。描述应该像是在给另一个开发者（或一个聪明的 LLM）写 API 文档。
    * **明确的输入模式 (`args_schema`)**: 对于需要多个参数或特定格式输入的工具，使用 Pydantic 模型定义 `args_schema` 可以让 LLM 更准确地提供输入。
    * **单一职责**: 每个工具最好只做一件事情并做好。这使得代理更容易选择和组合工具。
    * **错误处理**: 工具应该能够优雅地处理无效输入或执行中的错误，并返回有用的错误信息给代理，以便代理可以尝试纠正或选择其他方案。
    * **可预测的输出**: 工具的输出应该是代理能够理解和利用的。




### 第十五章：不同类型的 Agent

LangChain 提供了多种预构建的 Agent 类型（或创建 Agent 的方法/工厂函数），它们封装了不同的提示工程策略、决策逻辑和与 LLM 交互的方式。了解这些不同类型的 Agent 以及它们的优缺点，可以帮助你为特定任务选择最合适的 Agent。

#### 15.1 Zero-shot ReAct Agent

"Zero-shot" 指的是 Agent 在没有看到任何特定任务的示例（few-shot examples）的情况下，仅通过工具的描述和 LLM 的通用推理能力来决定如何行动。"ReAct" (Reason + Act) 是一种提示策略，它引导 LLM 进行显式的“思考”（Thought）步骤来推理下一步应该采取什么“行动”（Action），然后根据工具返回的“观察”（Observation）进行下一步的思考。

* **核心思想 (ReAct)**:
    1.  **Thought**: LLM 生成其当前的思考过程，分析问题和现有信息，并计划下一步。
    2.  **Action**: LLM 决定使用哪个工具以及该工具的输入。
    3.  **Observation**: 工具执行后返回的结果。
    4.  LLM 接收 Observation，并开始新的 Thought 步骤，循环往复直到得出最终答案。

* **特点**:
    * **通用性**: 由于是 "zero-shot"，它不依赖于特定任务的示例，对新任务有一定的适应性。
    * **推理过程明确**: ReAct 框架使得 LLM 的推理步骤更加清晰可见，便于理解和调试。
    * **基于工具描述**: 严重依赖工具描述的质量，LLM 根据描述来判断工具的用途。
    * **经典 Agent 类型**: 这是 LangChain 中早期且基础的 Agent 类型之一。

* **适用场景**:
    * 需要通用问题解决能力的场景。
    * 任务可以通过一系列工具调用来逐步完成。
    * 当你希望 Agent 能够展示其“思考”过程时。
    * 快速搭建原型 Agent。

* **创建方式 (示例)**:
    在较新版本的 LangChain 中，专门的 `ZeroShotAgent` 类可能不那么常用了，而是通过更通用的 Agent 创建函数（如 `create_react_agent` 或更早的 `initialize_agent` 与特定 `agent_type`）来实现类似 ReAct 的逻辑。

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.agents import AgentExecutor, create_react_agent # 使用 create_react_agent
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_community.tools import WikipediaQueryRun # 假设有 wikipedia_tool
    from langchain_community.utilities import WikipediaAPIWrapper
    # from langchain.agents import initialize_agent, AgentType # 旧版方式

    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(), name="Wikipedia")
    # tools = [wikipedia_tool]

    # ReAct 提示模板 (简化版，实际模板更复杂)
    # create_react_agent 会使用一个预定义的、更完善的 ReAct 提示
    # react_prompt = hub.pull("hwchase17/react") # 可以从 LangChain Hub 拉取标准提示

    # 假设 react_prompt 是一个 ChatPromptTemplate 实例，包含 input, agent_scratchpad, tool_names, tools
    # agent = create_react_agent(llm, tools, react_prompt)
    # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # 旧版方式 (可能已弃用或不推荐):
    # agent_executor_old = initialize_agent(
    # tools,
    # llm,
    # agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, # 指定 Agent 类型
    # verbose=True
    # )

    # response = agent_executor.invoke({"input": "AlphaGo 是由哪个公司开发的？"})
    # print(response.get("output"))
    ```

#### 15.2 Self-ask with search Agent

这种 Agent 类型旨在通过将复杂问题分解为一系列更简单的子问题来回答，并通过搜索（通常是 Google Search 或类似的工具）来逐步找到答案。它会明确地问自己子问题，然后尝试回答它们。

* **核心思想**:
    1.  LLM 接收一个复杂问题。
    2.  LLM 判断是否可以直接回答，如果不能，它会生成一个后续的、更简单的子问题。
    3.  这个子问题通常会通过搜索工具来查找答案。
    4.  子问题的答案会作为上下文，帮助 LLM 回答原始问题或生成下一个子问题。
    5.  重复此过程，直到原始问题得到解答。

* **特点**:
    * **问题分解**: 擅长处理需要多跳推理或信息综合的问题。
    * **依赖搜索**: 核心是利用搜索工具来获取信息。
    * **中间步骤清晰**: 其“自问自答”的过程是可见的。
    * **引导式提问**: LLM 会明确地提出它需要知道的下一个信息点。

* **适用场景**:
    * 回答需要从多个来源或通过多步查找才能得到答案的复杂问题。
    * 事实核查或信息综合。
    * 当问题的答案不是单一、直接的事实时。

* **创建方式 (示例)**:
    通常通过 `create_self_ask_agent` 或旧版的 `initialize_agent` 与 `AgentType.SELF_ASK_WITH_SEARCH` 来创建。

    ```python
    from langchain_openai import ChatOpenAI, OpenAI
    from langchain.agents import AgentExecutor, create_self_ask_agent
    from langchain_community.tools import GoogleSearchRun # 假设有 Google Search_tool
    from langchain_community.utilities import GoogleSearchAPIWrapper
    # from langchain.agents import initialize_agent, AgentType # 旧版方式
    # from langchain import hub # 用于拉取提示

    # llm = OpenAI(temperature=0) # Self-ask 通常与补全式 LLM 效果较好
    # search_wrapper = GoogleSearchAPIWrapper()
    # search_tool = GoogleSearchRun(api_wrapper=search_wrapper, name="IntermediateAnswer") # 工具名通常固定为 IntermediateAnswer
    # tools = [search_tool]

    # self_ask_prompt = hub.pull("hwchase17/self-ask-with-search") # 标准提示

    # agent = create_self_ask_agent(llm, tools, self_ask_prompt)
    # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # 旧版方式:
    # agent_executor_old = initialize_agent(
    # tools,
    # llm,
    # agent=AgentType.SELF_ASK_WITH_SEARCH,
    # verbose=True
    # )

    # response = agent_executor.invoke({"input": "《三体》的作者是谁？他的代表作除了《三体》还有哪些？"})
    # print(response.get("output"))
    ```
    *注意*: "Self-ask with search" Agent 通常期望搜索工具的名称为 "IntermediateAnswer"。

#### 15.3 Conversational ReAct Agent (用于对话的 Agent)

这种 Agent 结合了 ReAct 的推理能力和对话记忆，使其能够在多轮对话中保持上下文，并利用工具来回答问题或执行任务。

* **核心思想**:
    * 与 Zero-shot ReAct 类似，使用 Thought-Action-Observation 循环。
    * 集成了记忆模块（如 `ConversationBufferMemory`），将先前的对话历史作为上下文提供给 LLM。
    * 提示模板会包含对话历史的占位符。

* **特点**:
    * **对话感知**: 能够理解和回应多轮对话中的上下文。
    * **工具使用**: 可以在对话中动态调用工具。
    * **记忆集成**: 依赖记忆模块来维护对话状态。

* **适用场景**:
    * 构建需要与用户进行多轮交互并能使用工具的聊天机器人。
    * 复杂的任务型对话系统。
    * 需要在对话过程中查找信息或执行操作的智能助手。

* **创建方式 (示例)**:
    通常通过 `create_react_agent` 结合包含聊天历史占位符的提示，并为 `AgentExecutor` 配置记忆模块，或者使用旧版的 `initialize_agent` 与 `AgentType.CONVERSATIONAL_REACT_DESCRIPTION`。

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain.memory import ConversationBufferMemory
    from langchain_community.tools import WikipediaQueryRun # 假设有 wikipedia_tool
    from langchain_community.utilities import WikipediaAPIWrapper
    # from langchain.agents import initialize_agent, AgentType # 旧版方式
    # from langchain import hub

    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(), name="Wikipedia")
    # tools = [wikipedia_tool]

    # # 对话式 ReAct 提示需要包含 chat_history
    # # 通常从 hub 拉取，例如 "hwchase17/react-chat"
    # conversational_react_prompt = hub.pull("hwchase17/react-chat")

    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # agent = create_react_agent(llm, tools, conversational_react_prompt)
    # agent_executor = AgentExecutor(
    #     agent=agent,
    #     tools=tools,
    #     memory=memory, # 传入记忆模块
    #     verbose=True,
    #     handle_parsing_errors=True # 增加错误处理
    # )

    # 旧版方式:
    # agent_executor_old = initialize_agent(
    # tools,
    # llm,
    # agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    # memory=memory,
    # verbose=True
    # )

    # print(agent_executor.invoke({"input": "你好，我叫小明。"})["output"])
    # print(agent_executor.invoke({"input": "你知道光速是多少吗？请用维基百科查一下。"})["output"])
    # print(agent_executor.invoke({"input": "我刚才问了你什么？"})["output"]) # 测试记忆
    ```

#### 15.4 OpenAI Functions Agent / OpenAI Tools Agent

这类 Agent 利用了 OpenAI 模型（如 `gpt-3.5-turbo-0613` 及更新版本）内置的函数调用（Function Calling）或工具调用（Tool Calling）能力。模型本身可以根据提供的工具描述，生成一个 JSON 对象，指明应该调用哪个函数/工具以及使用什么参数。这使得工具的调用更加结构化和可靠。

* **核心思想**:
    1.  向 OpenAI LLM 提供用户输入和一组工具的描述（通常是 JSON Schema 格式）。
    2.  LLM 如果判断需要使用工具，其输出会包含一个特殊的“工具调用”指令，指明要调用的工具名称和参数。
    3.  LangChain 解析这个指令，执行相应的工具。
    4.  工具的输出再反馈给 LLM，LLM 继续处理或生成最终回复。

* **特点**:
    * **结构化工具调用**: LLM 直接输出结构化的工具调用请求，减少了解析错误的概率。
    * **模型原生支持**: 利用了模型底层的优化，可能更高效、更可靠。
    * **并行工具调用**: 较新的 OpenAI 模型支持并行工具调用，Agent 可以一次请求调用多个工具。
    * **推荐方式**: 对于支持工具调用的 OpenAI 模型，这通常是推荐的 Agent 构建方式。

* **适用场景**:
    * 任何需要 Agent 与工具交互的场景，特别是当使用支持工具调用的 OpenAI 模型时。
    * 需要更可靠、更结构化的工具调用。
    * 希望利用模型并行工具调用能力的场景。

* **创建方式 (示例)**:
    使用 `create_openai_tools_agent` (推荐) 或 `create_openai_functions_agent` (旧版名称)。

    ```python
    from langchain_openai import ChatOpenAI
    from langchain.agents import AgentExecutor, create_openai_tools_agent # 或 create_openai_functions_agent
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_community.tools import WikipediaQueryRun # 假设有 wikipedia_tool
    from langchain_community.utilities import WikipediaAPIWrapper
    from langchain.memory import ConversationBufferMemory
    # from langchain import hub

    # llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0) # 选择支持工具调用的模型
    # wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(), name="WikipediaSearch")
    # tools = [wikipedia_tool]

    # # OpenAI Tools Agent 提示
    # openai_tools_prompt = hub.pull("hwchase17/openai-tools-agent")

    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


    # agent = create_openai_tools_agent(llm, tools, openai_tools_prompt)
    # agent_executor = AgentExecutor(
    #     agent=agent,
    #     tools=tools,
    #     memory=memory,
    #     verbose=True
    # )

    # print(agent_executor.invoke({"input": "你好，我叫小华。"})["output"])
    # print(agent_executor.invoke({"input": "用维基百科查找关于“图灵测试”的信息。"})["output"])
    # print(agent_executor.invoke({"input": "我之前问了你什么工具来查找信息？"})["output"])
    ```

#### 15.5 Plan and Execute Agent

这种 Agent 采取了更明确的规划步骤。它首先创建一个详细的行动计划，然后逐个执行计划中的步骤。

* **核心思想**:
    1.  **规划 (Planning)**: 给定一个复杂任务，Agent (通常是一个专门的规划 LLM) 首先生成一个多步骤的计划来完成该任务。每个步骤可能涉及调用工具或进行子任务。
    2.  **执行 (Execution)**: 然后，另一个组件（执行器 Agent 或一系列链）负责按顺序执行计划中的每个步骤。

* **特点**:
    * **明确规划**: 将规划和执行分离，使得处理非常复杂或长期的任务成为可能。
    * **鲁棒性**: 如果某个步骤失败，可以更容易地进行重试或调整计划。
    * **可解释性**: 初始计划提供了对 Agent 如何处理任务的清晰概览。
    * **可能更慢**: 初始规划阶段可能需要较长时间。

* **适用场景**:
    * 需要多步骤、长期规划的复杂任务。
    * 任务的执行路径不确定，需要预先制定策略。
    * 例如：研究一个复杂主题并撰写报告、组织一次旅行等。

* **创建方式 (示例)**:
    LangChain 中有实验性的 `PlanAndExecute` Agent 执行器，或者可以通过组合 LLMChain（用于规划）和 AgentExecutor（用于执行每个步骤）来手动构建。

    ```python
    from langchain_openai import ChatOpenAI
    from langchain_experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner
    from langchain_community.tools import GoogleSearchRun, HumanInputRun # 假设有 search_tool
    from langchain_community.utilities import GoogleSearchAPIWrapper

    # llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0) # 规划可能需要更强大的模型
    # model_executor = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) # 执行步骤可以用稍弱的模型

    # search_wrapper = GoogleSearchAPIWrapper()
    # search_tool = GoogleSearchRun(api_wrapper=search_wrapper, name="Search")
    # human_tool = HumanInputRun() # 允许 Agent 请求用户输入
    # tools = [search_tool, human_tool]

    # planner = load_chat_planner(llm) # 加载规划器
    # executor = load_agent_executor(model_executor, tools, verbose=True) # 加载执行器

    # plan_and_execute_agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

    # # 由于 HumanInputRun 会阻塞等待输入，以下调用在自动脚本中可能无法直接运行
    # # response = plan_and_execute_agent.invoke({
    # # "input": "研究一下夏威夷的毛伊岛的最佳旅游季节，并找出三个必去的景点，然后问我是否需要预订机票。"
    # # })
    # # print(response.get("output"))
    ```
    *注意*: `PlanAndExecute` 仍在实验阶段，其 API 和行为可能会发生变化。

#### 15.6 选择合适的 Agent 类型

选择哪种 Agent 类型取决于你的具体需求、任务的复杂性、可用的模型以及对性能和成本的考虑。

* **考虑因素**:
    1.  **任务类型**:
        * **简单问答/工具使用**: Zero-shot ReAct, OpenAI Tools Agent。
        * **复杂问题分解/多跳查询**: Self-ask with search。
        * **对话式交互**: Conversational ReAct, OpenAI Tools Agent (带记忆)。
        * **非常复杂、需长期规划的任务**: Plan and Execute。
    2.  **模型能力**:
        * **支持工具调用/函数调用 (如 GPT-3.5-turbo-0613+, GPT-4)**: OpenAI Tools Agent 是首选，因为它更结构化和可靠。
        * **通用补全或聊天模型**: ReAct 类型的 Agent 更通用。
    3.  **工具的复杂性和数量**:
        * 如果工具很多或描述复杂，需要 LLM 有较强的理解和选择能力。OpenAI Tools Agent 可能处理得更好。
    4.  **对"思考过程"透明度的需求**:
        * ReAct 和 Self-ask Agent 通常会提供更详细的中间步骤。
    5.  **对话历史的需求**:
        * 如果需要多轮对话，选择支持记忆的 Agent (如 Conversational ReAct, 或为 OpenAI Tools Agent 配置记忆)。
    6.  **可靠性与错误处理**:
        * OpenAI Tools Agent 因其结构化输出，在工具调用方面通常更可靠。
        * `handle_parsing_errors=True` 在 `AgentExecutor` 中可以帮助处理一些常见的解析问题。
    7.  **成本与延迟**:
        * 需要多步推理或多次 LLM 调用的 Agent (如 Plan and Execute, Self-ask) 可能会有更高的成本和延迟。

* **一般建议**:
    * **首选 OpenAI Tools Agent**: 如果你正在使用支持工具调用的 OpenAI 模型，这通常是最现代、最可靠和功能最丰富的选择。
    * **对话场景**: 确保你的 Agent 集成了记忆模块，并且其提示设计考虑了对话历史。
    * **从简单开始**: 如果不确定，可以从像 `create_react_agent` 或 `create_openai_tools_agent` 这样的通用 Agent 开始，然后根据需要进行调整。
    * **实验和评估**: 针对你的具体用例测试不同的 Agent 类型和配置，以找到最佳方案。
    * **查阅 LangChain Hub**: LangChain Hub ([https://smith.langchain.com/hub](https://smith.langchain.com/hub)) 上有许多预置的、经过测试的 Agent 提示，可以作为很好的起点。




### 第十六章：高级 Agent 应用

在前几章中，我们学习了 Agent 的基础知识、核心组件以及不同类型的 Agent。现在，我们将深入探讨一些高级主题，这些主题对于构建健壮、可靠且功能强大的生产级 Agent 应用至关重要。这包括错误处理、行为限制、构建复杂的多步骤任务 Agent 以及与外部 API 的有效交互。

#### 16.1 Agent 的错误处理与调试

由于 Agent 的决策过程依赖于 LLM，并且会与外部工具交互，因此在运行过程中可能会遇到各种错误。有效的错误处理和调试机制对于确保 Agent 的稳定性和可靠性至关重要。

* **常见的 Agent 错误类型**:
    1.  **工具错误 (Tool Errors)**:
        * **工具执行失败**: 调用的工具可能因为各种原因失败（例如，API限流、网络问题、无效输入、工具内部 bug）。
        * **工具不存在或配置错误**: Agent 尝试调用一个不存在或未正确配置的工具。
    2.  **LLM 输出解析错误 (Parsing Errors)**:
        * Agent (LLM) 未能生成符合预期格式的输出，导致 `AgentExecutor` 无法解析其意图（例如，无法提取工具名称或参数，或者最终答案格式不正确）。这在 ReAct 等需要特定输出格式的 Agent 中较常见。
    3.  **LLM 决策错误 (Decision Errors)**:
        * LLM 选择了不合适的工具。
        * LLM 提供了错误的参数给工具。
        * LLM陷入循环，重复执行相同的无效操作。
        * LLM 过早地给出不完整或错误的最终答案。
    4.  **资源限制错误**:
        * 达到最大迭代次数 (`max_iterations`)。
        * 达到最大执行时间 (`max_execution_time`)。
        * 超出 LLM 的 token 限制。

* **错误处理策略**:
    1.  **`AgentExecutor` 中的错误处理参数**:
        * `handle_parsing_errors`: (布尔值或自定义函数)
            * 如果为 `True`，当发生解析错误时，会将错误信息反馈给 LLM，让其尝试纠正。
            * 可以传入一个自定义函数，该函数接收错误信息并返回一个替代的 AgentAction 或 AgentFinish，从而实现更精细的错误处理逻辑。
            * 例如，提示 LLM：“你之前的输出格式不正确，请确保输出包含一个有效的工具名称和对应的输入。”
        * `error_handler` (自定义错误处理类/函数，较少直接在 `AgentExecutor` 参数中使用，但概念重要): 可以设计更通用的错误处理逻辑，捕获特定类型的异常并采取相应措施（如重试、使用备用工具、通知用户）。

    2.  **工具层面的错误处理**:
        * 在自定义工具的 `_run` 或 `_arun` 方法中实现 `try-except` 块，捕获潜在的异常。
        * 返回有意义的错误信息给 Agent，而不是让异常直接中断执行。例如，返回 "工具 [ToolName] 执行失败：[错误详情]"，这样 LLM 就知道发生了什么，并可能尝试其他方法。

    3.  **重试机制**:
        * 可以使用像 Tenacity 这样的库在工具调用或 LLM 调用层面实现自动重试逻辑，特别是对于网络抖动或临时 API 问题。
        * `AgentExecutor` 本身没有内置的复杂重试逻辑，通常需要在工具或 LLM 调用封装层面实现。

    4.  **用户反馈回路**:
        * 如果 Agent 卡住或持续出错，允许用户介入，提供修正信息或指示。`HumanInputRun` 工具可以用于此目的。

* **调试 Agent 的技巧**:
    1.  **`verbose=True`**: 在 `AgentExecutor` 中设置 `verbose=True` 是最基本也是最重要的调试方法。它会打印出 Agent 的完整思考过程、选择的行动、工具的输入输出以及任何中间步骤。
        ```python
        # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
        ```
    2.  **LangSmith**: LangChain 推出的 LangSmith ([https://smith.langchain.com/](https://smith.langchain.com/)) 是一个强大的可观测性和调试平台。它可以捕获 Agent 执行的完整轨迹，包括每次 LLM 调用、工具调用、输入输出、延迟、Token 使用等。强烈推荐在开发和生产中使用 LangSmith。
        * 只需设置环境变量即可开始追踪：
            ```bash
            # export LANGCHAIN_TRACING_V2="true"
            # export LANGCHAIN_API_KEY="YOUR_LANGSMITH_API_KEY"
            # export LANGCHAIN_PROJECT="YOUR_PROJECT_NAME" # 可选
            ```
    3.  **回调函数 (Callbacks)**: `AgentExecutor` 支持回调函数，允许你在 Agent 执行的各个阶段（如 `on_agent_action`, `on_tool_end`, `on_llm_error` 等）插入自定义逻辑，例如记录日志、发送通知或进行更细致的分析。
        ```python
        # from langchain_core.callbacks import StdOutCallbackHandler
        # agent_executor = AgentExecutor(..., callbacks=[StdOutCallbackHandler()])
        ```
    4.  **逐步执行与断点**: 对于复杂的 Agent，可以在自定义工具或回调中设置断点，逐步观察 Agent 的行为和内部状态。
    5.  **检查提示 (Prompts)**: 如果 Agent 的行为不符合预期，仔细检查传递给 LLM 的提示模板至关重要。确保提示清晰地描述了任务、可用工具以及期望的输出格式。可以使用 `agent.run(..., return_intermediate_steps=True)` (如果支持) 或通过 LangSmith 查看实际发送给 LLM 的提示。
    6.  **单元测试工具**: 独立测试每个工具，确保它们在各种输入下都能正常工作并返回预期的输出。

#### 16.2 限制 Agent 的行为和资源使用

由于 Agent 具有一定的自主性并且可能执行真实世界的操作（如调用 API、运行代码），因此限制其行为和资源使用非常重要，以防止意外的成本、安全风险或滥用。

* **限制策略**:
    1.  **最大迭代次数 (`max_iterations`)**:
        * 在 `AgentExecutor` 中设置此参数，限制 Agent 在得出最终答案或失败前可以执行的“思考-行动-观察”循环的最大次数。
        * 有助于防止 Agent陷入无限循环，从而控制计算时间和成本。
        * 默认值通常是 15 左右，根据任务复杂性调整。
        ```python
        # agent_executor = AgentExecutor(..., max_iterations=10)
        ```
    2.  **最大执行时间 (`max_execution_time`)**:
        * 设置一个时间限制（秒），如果 Agent 的总执行时间超过此限制，则会提前终止。
        * 对于需要快速响应或防止长时间运行失控的场景很有用。
        ```python
        # import time
        # agent_executor = AgentExecutor(..., max_execution_time=60.0) # 60 秒
        ```
    3.  **Token 使用量控制**:
        * 虽然 `AgentExecutor` 没有直接的 Token 总量限制参数，但可以通过监控 LLM 调用的 Token 使用（例如，通过回调或 LangSmith）来实现外部控制。
        * 使用像 `ConversationTokenBufferMemory` 这样的记忆类型可以帮助限制输入给 LLM 的历史上下文 Token 数量。
        * 选择更经济的 LLM 模型进行某些步骤。

    4.  **工具访问权限控制**:
        * **选择性提供工具**: 只向 Agent 提供完成其特定任务所必需的工具。避免提供不必要或有潜在风险的工具（如无限制的 `ShellTool` 或 `PythonREPLTool`）。
        * **工具权限封装**: 在自定义工具内部实现权限检查。例如，一个数据库工具可能只允许执行只读查询，或者只允许访问特定的表。
        * **沙箱环境**: 对于像 `PythonREPLTool` 或 `ShellTool` 这样可以执行代码的工具，考虑在隔离的沙箱环境（如 Docker 容器）中运行它们，以限制其对主机系统的访问。

    5.  **成本控制**:
        * 除了 Token 使用量，监控 API 调用次数（特别是对于付费工具 API）。
        * 为 Agent 设置预算，并在达到预算时停止或降级其功能。
        * 使用缓存来减少对 LLM 和工具 API 的重复调用。

    6.  **输入/输出审查与过滤**:
        * 在将用户输入传递给 Agent 之前进行审查，以防止恶意输入（如提示注入）。
        * 在 Agent 生成最终输出后进行审查，确保其内容安全、合规且不包含敏感信息。

    7.  **人工监督与审批**:
        * 对于高风险操作（例如，执行交易、发送重要邮件、修改数据库），在 Agent 执行实际操作前引入人工审批步骤。`HumanInputRun` 工具可以用于此目的。

#### 16.3 构建复杂的 Agent 来完成多步骤任务

许多现实世界的任务需要 Agent 执行一系列相互依赖的步骤才能完成。构建能够可靠地处理这类任务的 Agent 需要仔细的设计。

* **策略与方法**:
    1.  **明确的任务分解 (Task Decomposition)**:
        * **LLM 驱动的分解**: 让 LLM (可能是 Agent 自身或一个专门的规划 Agent) 将复杂任务分解为更小、更易于管理子任务或步骤列表。`PlanAndExecute` Agent 就是一个例子。
        * **人工预定义**: 对于结构化的复杂任务，可以预先定义任务流程和步骤。

    2.  **状态管理与上下文传递**:
        * **记忆**: 使用合适的记忆模块（如 `ConversationSummaryBufferMemory`, `VectorStoreRetrieverMemory`）来跟踪对话历史、先前步骤的结果和关键信息。
        * **抓板 (Scratchpad)**: Agent 的“思考”过程（`agent_scratchpad`）本身就是一种短期记忆，用于存储最近的行动和观察。
        * **自定义状态对象**: 对于非常复杂的状态，可以设计一个自定义的状态对象，并在 Agent 的不同执行阶段或工具之间传递和更新它。

    3.  **工具编排 (Tool Orchestration)**:
        * 确保 Agent 能够理解不同工具之间的依赖关系，并按正确的顺序调用它们。
        * 设计工具的输入输出，使其能够自然地连接起来（一个工具的输出可以作为另一个工具的输入）。

    4.  **子 Agent (Sub-Agents)**:
        * 对于大型复杂任务，可以将其分解为几个子任务，每个子任务由一个专门的子 Agent 处理。
        * 主 Agent 负责协调这些子 Agent，并将它们的输出组合起来。
        * 例如，一个旅行规划 Agent 可能包含一个负责机票预订的子 Agent、一个负责酒店预订的子 Agent 和一个负责活动推荐的子 Agent。

    5.  **条件逻辑与分支**:
        * Agent (LLM) 需要能够根据中间结果或外部条件在其执行路径中做出决策和选择不同的分支。
        * 提示工程对于引导 LLM 进行正确的条件判断至关重要。

    6.  **长上下文处理**:
        * 对于需要回顾大量先前信息的超长任务，依赖于支持长上下文的 LLM 模型（如 GPT-4 Turbo, Claude 3 等）非常重要。
        * 结合摘要记忆或向量存储记忆来压缩或检索相关历史信息。

* **示例思路：研究报告撰写 Agent**
    * **目标**: 根据用户指定的主题撰写一份研究报告。
    * **步骤可能包括**:
        1.  **规划 (Plan)**: Agent 首先制定报告的大纲和研究步骤（例如，背景调研、数据收集、关键论点分析、结论草拟）。
        2.  **信息收集 (Info Gathering)**: 使用搜索工具（Google Search, Wikipedia）和可能的学术数据库工具收集相关信息。
        3.  **数据分析 (Data Analysis)**: 如果有数据，可能使用 `PythonREPLTool` 或专门的数据分析工具进行分析。
        4.  **内容生成 (Content Generation)**: 基于收集的信息和分析结果，分章节撰写报告内容（可能由一个专门的写作 LLMChain 辅助）。
        5.  **总结与润色 (Summarize & Refine)**: 生成摘要，并对报告进行整体审查和润色。
        6.  **(可选) 用户反馈**: 允许用户对草稿提出修改意见。
    * **实现**: 可能使用 `PlanAndExecute` 模式，或者一个主 Agent 协调多个专用工具和链。

#### 16.4 Agent 与外部 API 的交互

Agent 的一个核心能力是与外部世界交互，而 API 是实现这种交互的关键途径。让 Agent 能够安全、有效地使用外部 API 是扩展其功能的重要一步。

* **方法与最佳实践**:
    1.  **创建自定义 API 工具**:
        * 为每个需要交互的 API 端点（或一组相关端点）创建一个自定义工具。
        * 使用 `@tool` 装饰器或继承 `BaseTool`。
        * **工具描述至关重要**: 清晰地描述 API 的功能、参数、认证方式（如果需要 Agent 处理）、预期输出以及任何重要的使用限制或错误代码。
        * **参数映射**: `args_schema` (Pydantic 模型) 可以用来定义 Agent 如何提供 API 所需的参数。

    2.  **OpenAPI / Swagger 规范**:
        * 如果外部 API 提供了 OpenAPI (Swagger) 规范，LangChain 可以尝试基于该规范自动创建与 API 交互的工具或链 (例如，通过 `OpenAPIToolkit` 或相关功能)。这可以大大减少手动创建工具的工作量。
        * LLM 可以被提示去理解和使用这些基于规范生成的工具。

    3.  **认证与授权**:
        * **API 密钥管理**: 安全地存储和管理 API 密钥。避免硬编码到代码中。使用环境变量、密钥管理服务 (如 HashiCorp Vault, AWS Secrets Manager) 或 LangChain 的连接管理功能 (如果适用)。
        * **工具内部处理**: 工具在执行时从安全的位置加载 API 密钥。Agent 的 LLM 不应直接接触或生成 API 密钥。
        * **OAuth 2.0 / OIDC**: 对于需要 OAuth 流程的 API，通常需要在工具的外部预先完成认证，工具内部使用获取到的访问令牌 (access token)。让 Agent 直接处理完整的 OAuth 流程非常复杂且不安全。

    4.  **请求与响应处理**:
        * **请求库**: 在工具内部使用标准的 HTTP 请求库（如 `requests` for Python）来调用 API。
        * **错误处理**: 妥善处理 API 可能返回的各种 HTTP 错误码（4xx, 5xx）和业务逻辑错误。将错误信息以 Agent 可理解的方式返回。
        * **数据解析**: 解析 API 返回的 JSON、XML 或其他格式的数据。
        * **数据转换**: 可能需要将 API 的原始输出转换为对 LLM 更友好或更易于后续步骤使用的格式。

    5.  **速率限制与重试**:
        * 大多数 API 都有速率限制。工具应该能够处理速率限制错误（通常是 HTTP 429 错误），并实现合理的重试逻辑（例如，指数退避）。
        * 遵守 API 提供商的使用条款。

    6.  **安全性**:
        * **输入验证**: 在将 Agent 提供的参数传递给 API 之前，进行严格的验证和清理，以防止注入攻击或其他安全风险。
        * **避免执行任意 API 调用**: 不要创建一个过于通用的“任意 API 调用工具”，除非有非常严格的控制和审查。优先为特定、受信任的端点创建专用工具。

* **示例：自定义工具调用天气 API**

    ```python
    import os
    import httpx # 现代 HTTP 客户端，支持异步
    from langchain.tools import tool
    from pydantic import BaseModel, Field

    # 假设有一个天气API，需要API密钥
    # WEATHER_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
    # WEATHER_API_URL = "[https://api.openweathermap.org/data/2.5/weather](https://api.openweathermap.org/data/2.5/weather)"

    class WeatherInput(BaseModel):
        city: str = Field(description="需要查询天气的城市名称，例如 'London' 或 'San Francisco'")
        country_code: Optional[str] = Field(None, description="城市的国家代码（可选），例如 'GB' 代表英国或 'US' 代表美国")

    @tool("get_current_weather", args_schema=WeatherInput)
    async def get_current_weather(city: str, country_code: Optional[str] = None) -> str:
        """查询指定城市的当前天气信息。"""
        # if not WEATHER_API_KEY:
        #     return "错误：天气 API 密钥未配置。"

        # params = {"q": f"{city},{country_code}" if country_code else city, "appid": WEATHER_API_KEY, "units": "metric", "lang": "zh_cn"}
        # try:
        #     async with httpx.AsyncClient() as client:
        #         response = await client.get(WEATHER_API_URL, params=params)
        #         response.raise_for_status() # 如果是 4xx 或 5xx 错误，则抛出异常
        #         data = response.json()
        #         description = data["weather"][0]["description"]
        #         temp = data["main"]["temp"]
        #         return f"{city} 当前天气：{description}，气温：{temp}°C。"
        # except httpx.HTTPStatusError as e:
        #     if e.response.status_code == 401:
        #         return f"查询 {city} 天气失败：API密钥无效或未授权。"
        #     elif e.response.status_code == 404:
        #         return f"查询 {city} 天气失败：找不到指定的城市。"
        #     else:
        #         return f"查询 {city} 天气失败：HTTP错误 {e.response.status_code} - {e.response.text}"
        # except Exception as e:
        #     return f"查询 {city} 天气时发生意外错误：{str(e)}"
        # 示例返回值，实际调用API
        if city.lower() == "paris":
            return f"{city} 当前天气：小雨，气温：18°C。"
        return f"模拟：无法查询 {city} 的天气。"


    # (然后可以将 get_current_weather 工具添加到 Agent 的工具列表中)
    # tools = [get_current_weather]
    # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    # result = await agent_executor.ainvoke({"input": "法国巴黎现在天气怎么样？"})
    # print(result.get("output"))
    ```

通过掌握这些高级应用技巧，你可以构建出更强大、更可靠、更能适应复杂现实世界场景的智能代理。


## 模块七：回调 (Callbacks) 与调试

在开发和运行 LangChain 应用（尤其是复杂的链和 Agent）时，能够有效地监控、记录和调试其执行过程至关重要。回调 (Callbacks) 系统是 LangChain 提供的一个强大机制，允许你在 LLM、链、Agent 和工具执行的各个生命周期阶段插入自定义逻辑，从而实现日志记录、监控、流式输出、与第三方服务集成等功能。

本模块将重点介绍如何使用回调系统，以及如何结合回调进行调试。

### 第十七章：使用 Callbacks 进行监控与日志记录

本章将详细介绍 LangChain 回调系统的核心组件、内置处理器、如何创建自定义处理器，以及如何利用回调来跟踪和理解链与 Agent 的执行流程。

#### 17.1 CallbackManager 和 CallbackHandler

LangChain 的回调系统主要由两个核心概念组成：

1.  **`CallbackHandler` (回调处理器)**:
    * **定义**: 这是一个抽象基类，定义了一系列可以在 LangChain 对象（如 LLM、Chain、Agent、Tool）执行过程中的不同事件点被调用的方法。每个方法对应一个特定的事件。
    * **事件方法示例**:
        * `on_llm_start(serialized, prompts, **kwargs)`: LLM 调用开始时触发。
        * `on_llm_new_token(token, **kwargs)`: LLM 流式输出新 Token 时触发。
        * `on_llm_end(response, **kwargs)`: LLM 调用结束时触发。
        * `on_llm_error(error, **kwargs)`: LLM 调用出错时触发。
        * `on_chain_start(serialized, inputs, **kwargs)`: 链开始执行时触发。
        * `on_chain_end(outputs, **kwargs)`: 链执行结束时触发。
        * `on_chain_error(error, **kwargs)`: 链执行出错时触发。
        * `on_tool_start(serialized, input_str, **kwargs)`: 工具开始执行时触发。
        * `on_tool_end(output, **kwargs)`: 工具执行结束时触发。
        * `on_tool_error(error, **kwargs)`: 工具执行出错时触发。
        * `on_agent_action(action, **kwargs)`: Agent 决定执行一个动作时触发。
        * `on_agent_finish(finish, **kwargs)`: Agent 完成执行并给出最终答案时触发。
        * `on_retriever_start(serialized, query, **kwargs)`: 检索器开始时触发。
        * `on_retriever_end(documents, **kwargs)`: 检索器结束时触发。
        * `on_retriever_error(error, **kwargs)`: 检索器出错时触发。
    * **实现**: 你可以通过继承 `BaseCallbackHandler` 或更具体的处理器（如 `AsyncCallbackHandler` 用于异步操作）并重写你感兴趣的事件方法来创建自定义的回调逻辑。

2.  **`CallbackManager` (回调管理器)**:
    * **定义**: 每个 LangChain 对象（LLM, Chain, AgentExecutor）在执行时都有一个 `CallbackManager`。这个管理器负责维护一个回调处理器列表，并在相应的事件发生时，按顺序调用列表中所有注册处理器的对应事件方法。
    * **作用**:
        * **注册处理器**: 向管理器添加或移除回调处理器。
        * **事件分发**: 当内部事件发生时（如 LLM 开始调用），管理器会通知所有注册的处理器。
    * **配置方式**:
        * **构造时传入**: 大多数 LangChain 对象在初始化时接受一个 `callbacks` 参数，可以传入一个回调处理器列表或单个处理器。
            ```python
            # from langchain_openai import ChatOpenAI
            # from langchain_core.callbacks import StdOutCallbackHandler
            # handler = StdOutCallbackHandler()
            # llm = ChatOpenAI(callbacks=[handler], streaming=True)
            ```
        * **全局配置 (不推荐用于生产)**: LangChain 早期版本有一些全局回调配置，但更推荐在具体对象层面进行配置，以获得更细粒度的控制。
        * **通过 `tags` 和 `metadata`**: 在调用链或 Agent 时，可以传入 `tags` 和 `metadata`，这些信息会传递给回调处理器，帮助你更好地组织和筛选回调事件。

#### 17.2 内置的回调处理器 (StdOutCallbackHandler, FileCallbackHandler)

LangChain 提供了一些可以直接使用的内置回调处理器，方便快速实现常见的日志和监控需求。

1.  **`StdOutCallbackHandler`**:
    * **功能**: 将回调事件的信息打印到标准输出（控制台）。这是最简单直接的调试工具，类似于在 `AgentExecutor` 中设置 `verbose=True`，但提供了更结构化的输出。
    * **使用**:
        ```python
        from langchain_core.callbacks import StdOutCallbackHandler
        from langchain_openai import ChatOpenAI
        from langchain.chains import LLMChain
        from langchain_core.prompts import PromptTemplate

        # handler = StdOutCallbackHandler()
        # llm = ChatOpenAI(callbacks=[handler], temperature=0)
        # prompt = PromptTemplate.from_template("写一句关于 {topic} 的名言。")
        # chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler]) # 也可以在链层面添加

        # chain.invoke({"topic": "学习"})
        # # 控制台会输出类似 LLMStart, LLMEnd, ChainStart, ChainEnd 等事件信息
        ```
    * **优点**: 简单易用，无需配置，即时反馈。
    * **缺点**: 输出到控制台，不方便持久化和后续分析。

2.  **`FileCallbackHandler` (示例性，可能需自定义或来自社区)**:
    * **功能**: 将回调事件的信息记录到指定的文件中。这对于持久化日志非常有用。
    * **LangChain Core 中可能没有直接的 `FileCallbackHandler`，但很容易自定义实现 (见 17.3)，或者社区可能有提供。这里我们描述其概念。**
    * **概念**:
        * 初始化时指定一个日志文件路径。
        * 在每个事件方法中，将事件的详细信息格式化为字符串并写入该文件。
    * **优点**: 持久化日志，方便后续审计和分析。
    * **缺点**: 需要文件系统访问权限，对于大量并发请求可能需要考虑写入性能和文件管理。

3.  **其他可能的内置或社区处理器**:
    * 针对特定日志库（如 `logging` 模块）的处理器。
    * 与特定监控平台集成的处理器（如 LangSmith，见 17.5）。

#### 17.3 自定义回调处理器

当内置处理器无法满足你的特定需求时，可以轻松创建自定义的回调处理器。这允许你实现任意复杂的逻辑，例如：

* 将日志发送到自定义的日志聚合系统（如 ELK Stack, Splunk, Datadog）。
* 记录性能指标（如延迟、Token 消耗）到数据库或监控服务。
* 在特定事件发生时触发告警或通知。
* 实现自定义的流式处理逻辑。
* 根据事件内容动态修改执行行为（不常见，但理论上可能）。

* **创建步骤**:
    1.  **继承 `BaseCallbackHandler` 或 `AsyncCallbackHandler`**:
        ```python
        from langchain_core.callbacks import BaseCallbackHandler
        from langchain_core.outputs import LLMResult, ChatResult
        from typing import Any, List, Dict, Union
        from langchain_core.messages import BaseMessage

        class MyCustomHandler(BaseCallbackHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.log_entries = [] # 示例：在内存中记录日志

            def on_llm_start(
                self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
            ) -> None:
                entry = f"[LLM Start] Prompts: {prompts[:1]}..., Config: {serialized.get('kwargs', {}).get('model', 'N/A')}"
                print(entry) # 简单打印
                self.log_entries.append(entry)
                # 可以在这里添加更复杂的逻辑，比如写入数据库

            def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
                entry = f"[LLM End] Generations: {response.generations[0][0].text[:50]}..."
                if response.llm_output:
                     entry += f" Tokens: {response.llm_output.get('token_usage', 'N/A')}"
                print(entry)
                self.log_entries.append(entry)

            def on_chat_model_start(
                self, serialized: Dict[str, Any], messages: List[List[BaseMessage]], **kwargs: Any
            ) -> Any:
                # 与 on_llm_start 类似，但针对 ChatModels
                entry = f"[ChatModel Start] Messages: {messages[0][0].content[:50]}..., Model: {serialized.get('kwargs', {}).get('model', 'N/A')}"
                print(entry)
                self.log_entries.append(entry)


            def on_chain_start(
                self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any
            ) -> None:
                entry = f"[Chain Start] Chain: {serialized.get('name', serialized.get('id', ['Unknown Chain'])[-1])}, Inputs: {list(inputs.keys())}"
                print(entry)
                self.log_entries.append(entry)

            def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
                output_keys = list(outputs.keys())
                entry = f"[Chain End] Outputs: {output_keys}"
                print(entry)
                self.log_entries.append(entry)

            # 可以选择性地实现其他 on_... 方法
            # 例如: on_tool_start, on_tool_end, on_agent_action, etc.

            def get_logs(self):
                return self.log_entries
        ```
    2.  **重写感兴趣的事件方法**: 只需为你关心的事件实现对应的方法。未被重写的方法在 `BaseCallbackHandler` 中是空操作。
    3.  **在 LangChain 对象中使用**:
        ```python
        # custom_handler = MyCustomHandler()
        # llm = ChatOpenAI(callbacks=[custom_handler], temperature=0)
        # chain = LLMChain(llm=llm, prompt=prompt, callbacks=[custom_handler]) # handler可以被多个对象共享

        # chain.invoke({"topic": "创新"})
        # all_logs = custom_handler.get_logs()
        # print("\n--- Custom Handler Logs ---")
        # for log in all_logs:
        #     print(log)
        ```

#### 17.4 跟踪链和 Agent 的执行流程

回调是理解和跟踪复杂链与 Agent 执行流程的核心工具。

* **`verbose=True` vs. Callbacks**:
    * `verbose=True` 是 `AgentExecutor` 或某些链提供的一个简单开关，它内部通常使用了一个类似 `StdOutCallbackHandler` 的机制来打印执行步骤。
    * 直接使用回调处理器（如 `StdOutCallbackHandler` 或自定义处理器）可以提供更细粒度、更结构化、更灵活的跟踪信息。你可以精确控制哪些信息被记录以及记录到哪里。

* **利用回调跟踪的典型信息**:
    * **链的调用顺序**: 通过 `on_chain_start` 和 `on_chain_end` 跟踪哪个链在何时被调用，以及它们的输入输出是什么。这对于理解 `SequentialChain` 或更复杂的嵌套链非常有帮助。
    * **Agent 的决策过程**:
        * `on_agent_action`: 查看 Agent 决定使用哪个工具以及传递给工具的参数。
        * `on_tool_start`, `on_tool_end`, `on_tool_error`: 监控工具的执行情况和结果。
        * `LLM` 事件 (`on_llm_start`, `on_llm_end`): 观察 Agent 内部 LLM 的“思考”提示和生成的“行动”或“最终答案”。
    * **LLM 的交互**: 查看发送给 LLM 的确切提示和 LLM 返回的原始响应，以及 Token 使用情况。
    * **检索过程**: `on_retriever_start`, `on_retriever_end` 可以帮助了解 RAG 应用中检索了哪些文档。
    * **错误发生点**: `on_llm_error`, `on_chain_error`, `on_tool_error` 可以精确定位错误发生的组件和原因。

* **传递 `run_id` 和其他元数据**:
    * LangChain 的回调系统会自动为每次执行（run）生成一个 `run_id` (UUID)。这个 ID 会在一次完整调用（例如 `chain.invoke()`）的所有相关回调事件中传递。
    * 使用 `run_id` 可以将一次执行过程中的所有日志条目关联起来，非常便于分析和调试。
    * `tags` 和 `metadata` 参数也可以在调用时传入，这些信息会包含在回调事件的 `**kwargs` 中，可用于进一步的分类或过滤。

#### 17.5 与 LangSmith 等监控平台集成 (可选，但推荐提及)

虽然自定义回调处理器可以实现强大的本地日志和监控，但对于生产环境或需要协作的团队，专门的可观测性平台通常更为高效。

**LangSmith ([https://smith.langchain.com/](https://smith.langchain.com/))**:
* **LangChain 官方平台**: 由 LangChain团队开发，专为监控、调试和评估基于 LLM 的应用而设计。
* **自动追踪**: 只需设置几个环境变量，LangSmith 就可以自动捕获 LangChain 应用的详细执行轨迹，无需显式配置回调处理器（它内部使用了回调机制）。
    ```bash
    export LANGCHAIN_TRACING_V2="true" # 启用 LangSmith 追踪
    export LANGCHAIN_API_KEY="YOUR_LANGSMITH_API_KEY" # 从 LangSmith 网站获取
    export LANGCHAIN_PROJECT="my-agent-project" # (可选) 项目名称，用于组织追踪记录
    # export LANGCHAIN_ENDPOINT="[https://api.smith.langchain.com](https://api.smith.langchain.com)" # 默认端点
    ```
* **功能**:
    * **可视化轨迹**: 清晰地展示链、Agent、LLM、工具的每一步调用，包括输入、输出、中间步骤、耗时、Token 数量。
    * **错误分析**: 快速定位和诊断错误。
    * **Prompt Engineering**: 查看和比较不同提示的效果。
    * **数据集与评估**: 创建数据集，运行评估，比较不同模型或提示版本的性能。
    * **协作**: 团队成员可以共享和查看追踪记录。
    * **Playground**: 在平台上试验和迭代提示与链。
* **与回调的关系**: LangSmith 本身就是通过深度集成 LangChain 的回调系统来实现其功能的。即使你使用 LangSmith，理解回调机制仍然有助于进行更高级的定制或与其他系统集成。

**其他监控平台**:
* 你也可以使用自定义回调处理器将 LangChain 应用的监控数据发送到其他通用的 APM (Application Performance Monitoring) 工具或日志聚合服务，如 Datadog, Prometheus/Grafana, OpenTelemetry, Sentry 等。这通常需要你编写更多的集成代码。

通过有效地使用回调系统，无论是进行本地调试、自定义日志记录，还是与像 LangSmith 这样的专业平台集成，你都可以极大地提升开发和维护 LangChain 应用的效率和可靠性。


### 第十八章：LangChain 应用的调试技巧

调试是软件开发生命周期中不可或缺的一环，对于构建复杂的 LangChain 应用尤其如此。由于 LangChain 应用通常涉及多个组件（LLMs、提示、链、Agent、工具、记忆），并且其行为可能具有不确定性（尤其是 Agent），因此掌握有效的调试技巧至关重要。

本章将介绍一些实用的调试方法、工具和常见问题的解决方案，帮助你更高效地诊断和修复 LangChain 应用中的问题。

#### 18.1 理解和分析 LangChain 的日志输出

LangChain 通过其回调系统（详见第十七章）可以生成详细的执行日志。理解这些日志是调试的第一步。

* **日志的来源**:
    * **`verbose=True`**: 在链或 `AgentExecutor` 中设置，会向标准输出打印执行步骤。
    * **`StdOutCallbackHandler`**: 显式使用此回调处理器会将事件信息打印到控制台。
    * **自定义回调处理器**: 你可以创建自己的回调处理器，将日志信息输出到文件、数据库或专门的日志服务。
    * **LangSmith**: 自动捕获并以结构化方式展示所有执行轨迹和日志。

* **日志中常见的关键信息**:
    * **组件名称/ID**: 识别是哪个链、LLM、工具或 Agent 在执行。
    * **输入 (Inputs)**: 传递给组件的完整输入数据。对于 LLM，这是最终的提示；对于工具，这是工具的参数。
    * **输出 (Outputs)**: 组件执行后返回的结果。对于 LLM，是模型的响应；对于工具，是工具的执行结果。
    * **中间步骤 (Intermediate Steps)** (尤其在 Agent 中):
        * **Thought**: Agent 的思考过程。
        * **Action**: Agent 决定采取的行动（使用的工具和输入）。
        * **Observation**: 工具执行后返回的观察结果。
    * **错误信息 (Errors)**: 如果发生错误，会记录错误类型、消息和相关的堆栈跟踪。
    * **Token 使用量 (Token Usage)**: 对于 LLM 调用，通常会记录提示 Token、完成 Token 和总 Token 数量（如果回调处理器或平台支持）。
    * **时间戳与耗时 (Timestamps & Duration)**: 事件发生的时间和执行耗时，有助于识别性能瓶颈。
    * **`run_id` 和 `parent_run_id`**: 用于关联一次完整执行过程中的所有相关事件。

* **分析日志的策略**:
    1.  **从头开始**: 跟踪一次请求的完整执行流程，从初始输入开始。
    2.  **关注错误点**: 如果发生错误，首先定位到错误发生的具体组件和事件。
    3.  **检查输入输出**: 仔细核对每个关键组件的输入是否符合预期，输出是否合理。错误的输入是导致问题的常见原因。
    4.  **验证 Agent 的决策**: 对于 Agent，分析其“思考”过程是否合乎逻辑，选择的工具和参数是否正确。
    5.  **对比预期行为**: 将日志中的实际行为与你期望的行为进行比较，找出偏差。

#### 18.2 使用 `verbose=True` 进行详细输出

`verbose=True` 是 LangChain 对象（特别是链和 `AgentExecutor`）提供的一个便捷参数，用于快速获取详细的执行过程输出到控制台。

* **如何使用**:
    ```python
    from langchain_openai import ChatOpenAI
    from langchain.agents import AgentExecutor, create_openai_tools_agent
    from langchain_community.tools import WikipediaQueryRun
    from langchain_community.utilities import WikipediaAPIWrapper
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    # from langchain import hub

    # llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)
    # wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(), name="WikipediaSearch")
    # tools = [wikipedia_tool]
    # prompt = hub.pull("hwchase17/openai-tools-agent")

    # agent = create_openai_tools_agent(llm, tools, prompt)

    # # 在 AgentExecutor 中启用 verbose 模式
    # agent_executor = AgentExecutor(
    #     agent=agent,
    #     tools=tools,
    #     verbose=True # 启用详细输出
    # )

    # agent_executor.invoke({"input": "银河系有多少颗恒星？"})
    ```

* **输出内容**:
    * 通常会打印出链的进入和退出信息、Agent 的思考过程、选择的行动、工具的输入、工具的输出（观察结果）以及最终的答案。
    * 输出格式可能因 LangChain 版本和具体对象而略有不同。

* **优点**:
    * **简单快速**: 只需设置一个参数即可。
    * **即时反馈**: 直接在控制台看到执行流程，适合快速调试和理解 Agent 的行为。

* **缺点**:
    * **信息量大**: 对于复杂的链或多轮 Agent 交互，输出可能非常冗长，难以筛选关键信息。
    * **非结构化**: 控制台输出通常是非结构化的文本，不方便程序化分析或长期存储。
    * **功能有限**: 不如专门的回调处理器或 LangSmith 功能丰富（例如，没有详细的 Token 统计、错误聚合等）。

* **何时使用**:
    * 在开发初期，用于快速理解组件如何协同工作。
    * 调试简单的链或 Agent 的基本行为。
    * 当不需要持久化日志或高级分析功能时。

对于更复杂的调试和生产环境，推荐使用回调处理器或 LangSmith。

#### 18.3 LangChain Debugging 工具 (如果 LangChain 自身提供)

LangChain 自身提供的核心“调试工具”是其**回调系统**和官方的**LangSmith**平台。

1.  **回调系统 (Callbacks)**:
    * 如第十七章所述，回调处理器允许你挂接到 LangChain 执行的几乎所有关键点。
    * 你可以创建自定义回调来记录详细信息、发送到特定系统或在调试器中设置断点。
    * `StdOutCallbackHandler` 是一个简单的内置调试工具。

2.  **LangSmith ([https://smith.langchain.com/](https://smith.langchain.com/))**:
    * **官方可观测性与调试平台**: 这是 LangChain 团队为 LLM 应用提供的首选调试和监控解决方案。
    * **自动追踪**: 通过设置环境变量，可以自动捕获所有 LangChain 调用的详细轨迹，无需修改代码。
    * **可视化界面**: 提供直观的界面来查看和分析执行轨迹，包括：
        * 每个 LLM 调用的提示和完成。
        * Token 使用情况。
        * 工具调用和结果。
        * Agent 的思考和决策过程。
        * 错误信息和堆栈跟踪。
        * 端到端延迟和每个步骤的延迟。
    * **调试功能**:
        * **错误聚合**: 轻松查看和筛选失败的运行。
        * **Prompt Playground**: 直接在平台上修改和测试提示。
        * **比较运行**: 对比不同配置或代码版本的执行结果。
        * **数据集和评估**: 系统地评估 Agent 和链的性能。
    * **推荐使用**: 对于任何严肃的 LangChain 开发，强烈推荐使用 LangSmith。它极大地简化了调试过程，并提供了深入的洞察。

3.  **Python 调试器 (pdb, IDE debuggers)**:
    * 你仍然可以使用标准的 Python 调试工具。
    * 在自定义回调处理器的方法中、自定义工具的 `_run` 方法中，或链的 `_call` 方法（如果你在自定义链）中设置断点。
    * 这允许你检查当时的变量状态、单步执行代码等。

虽然 LangChain 可能没有像传统软件那样提供一个独立的“调试器应用程序”，但其回调架构和 LangSmith 平台共同构成了一个非常强大的调试生态系统。

#### 18.4 常见错误及其解决方法

在开发 LangChain 应用时，可能会遇到各种错误。以下是一些常见错误及其可能的解决方法：

1.  **API 密钥错误 (AuthenticationError / APIKeyNotFoundError)**:
    * **症状**: 提示 API 密钥无效、缺失或未设置。
    * **原因**:
        * 未正确设置环境变量（如 `OPENAI_API_KEY`, `GOOGLE_API_KEY`）。
        * API 密钥本身已过期或无效。
        * 账户余额不足。
    * **解决方法**:
        * 确保已正确设置并导出了所需的环境变量。
        * 检查 API 密钥的有效性，并在需要时重新生成。
        * 确认相关 API 服务账户状态正常。

2.  **模型未找到 (NotFoundError / ModelNotFoundError)**:
    * **症状**: 提示指定的 LLM 模型不存在或无法访问。
    * **原因**:
        * 模型名称拼写错误。
        * 尝试使用的模型对当前 API 密钥或账户不可用（例如，某些模型可能需要特定权限或处于测试阶段）。
        * API 服务区域问题。
    * **解决方法**:
        * 仔细检查模型名称是否正确（例如，`gpt-3.5-turbo` 而不是 `gpt-35-turbo`）。
        * 查阅 LLM 提供商的文档，确认模型可用性和你的访问权限。

3.  **提示模板错误 (TemplateFormatError / MissingInputVariables)**:
    * **症状**: 提示模板格式不正确，或在渲染提示时缺少必要的输入变量。
    * **原因**:
        * 提示模板中的占位符（如 `{variable}`）与传递给链的输入字典中的键不匹配。
        * 模板语法错误。
    * **解决方法**:
        * 确保 `PromptTemplate` 的 `input_variables` 列表与模板中的占位符一致。
        * 确保调用链或 Agent 时提供了所有必需的输入变量。
        * 使用 `prompt.format_prompt(**inputs)` 或 `prompt.format(**inputs)` 手动测试提示的渲染。

4.  **Agent 输出解析错误 (OutputParserException)**:
    * **症状**: Agent (LLM) 的输出不符合 `AgentExecutor` 期望的格式（例如，ReAct Agent 未能正确输出 "Thought:", "Action:", "Action Input:"）。
    * **原因**:
        * LLM 难以理解提示中关于输出格式的要求。
        * 提示过于复杂或不清晰。
        * 工具描述不够好，导致 LLM 困惑。
        * 模型本身的能力限制。
    * **解决方法**:
        * **简化提示**: 使输出格式要求更简单明了。
        * **改进工具描述**: 确保工具描述清晰地说明了工具的功能和预期输入。
        * **提供示例 (Few-shot prompting)**: 在提示中加入几个符合期望输出格式的示例。
        * **使用 `handle_parsing_errors=True`**: 在 `AgentExecutor` 中设置，它会将解析错误反馈给 LLM，让其尝试纠正。
        * **切换到更强大的 LLM**: 更强大的模型可能更好地遵循格式指令。
        * **使用 OpenAI Tools Agent**: 如果使用 OpenAI 模型，利用其原生的工具调用功能通常更可靠，能减少解析错误。

5.  **工具执行错误 (ToolException / Custom Tool Errors)**:
    * **症状**: Agent 成功选择了工具并尝试执行，但工具本身在执行过程中失败。
    * **原因**:
        * 传递给工具的参数无效。
        * 工具依赖的外部服务不可用或出错 (API限流、网络问题)。
        * 工具内部逻辑错误。
    * **解决方法**:
        * **在工具内部添加健壮的错误处理**: 使用 `try-except` 捕获异常，并返回有意义的错误信息给 Agent。
        * **验证工具输入**: 在工具的 `_run` 方法开始时验证输入参数。
        * **调试工具逻辑**: 独立测试工具，确保其按预期工作。
        * **让 Agent 能够处理工具错误**: Agent 的提示应该能够引导 LLM 在工具返回错误时尝试其他方法或通知用户。

6.  **上下文长度超出 (ContextWindowExceeded / InvalidRequestError)**:
    * **症状**: 发送给 LLM 的总 Token 数（提示 + 历史 + 输出空间）超出了模型的最大上下文窗口。
    * **原因**:
        * 对话历史过长 (`ConversationBufferMemory`)。
        * 检索了过多的文档块 (RAG)。
        * 提示本身非常冗长。
    * **解决方法**:
        * **使用带限制的记忆类型**: `ConversationBufferWindowMemory`, `ConversationTokenBufferMemory`, `ConversationSummaryBufferMemory`。
        * **限制检索文档数量/长度**: 在 RAG 中调整检索参数。
        * **精简提示**: 优化提示的长度。
        * **使用支持更长上下文窗口的模型**。
        * **对长文档进行分块和摘要**。

7.  **Agent 循环或无进展 (MaxIterationsExceeded)**:
    * **症状**: Agent 重复执行相同的无效操作，或无法找到解决方案，最终达到 `max_iterations` 限制。
    * **原因**:
        * 提示不够清晰，无法引导 Agent 走向正确方向。
        * 工具集不完备，缺少解决任务所需的关键工具。
        * LLM 在复杂推理中迷失。
    * **解决方法**:
        * **改进提示**: 给出更明确的指示和目标。
        * **审查并完善工具**: 确保 Agent 拥有完成任务所需的所有能力。
        * **增加 `max_iterations` (谨慎)**: 如果任务确实需要更多步骤，可以适当增加，但首先应排查其他原因。
        * **尝试不同的 Agent 类型或 LLM 模型**。
        * **引入人工干预**: 允许用户在 Agent 卡住时提供帮助。

通过结合使用日志分析、`verbose`模式、LangSmith、标准调试器以及对常见错误的理解，你可以更有效地调试和优化你的 LangChain 应用。



## 模块八 ： Tools

###  MCP 

参考
|---|
|[MCP 终极指南  很值得读！！！](https://guangzhengli.com/blog/zh/model-context-protocol)|
|[langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters)|
| [Using LangChain With Model Context Protocol (MCP)](https://cobusgreyling.medium.com/using-langchain-with-model-context-protocol-mcp-e89b87ee3c4c)|
|[知乎-一文看懂：MCP(大模型上下文协议)](https://zhuanlan.zhihu.com/p/27327515233)|
|[AI是如何确定应使用的MCP Server的?](https://www.zhihu.com/question/1890546618509538123)|
[function call vs MCP](https://www.dailydoseofds.com/p/function-calling-mcp-for-llms/)

---

MCP (Model-Calling-Protocol) 是一种标准协议，允许大型语言模型调用外部工具。这个教程展示如何使用Langchain与MCP集成，创建一个简单的数学计算服务。



#### 在Langchain中使用MCP的极简教程

参考：

[在Langchain中使用MCP的极简教程](https://zhuanlan.zhihu.com/p/1899053057435739384)

---

项目包含两个主要文件：
- `math_server.py`: MCP服务器端，提供数学工具
- `client.py`: 使用Langchain与MCP通信的客户端

1.  步骤1: 创建MCP服务器

首先，创建一个包含数学工具的MCP服务器：

```python
# math_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

这个服务器定义了两个数学工具：
- `add`: 将两个数字相加
- `multiply`: 将两个数字相乘

服务器使用stdio通信，这允许客户端通过标准输入/输出与服务器交互。

2.  步骤2: 创建Langchain客户端

接下来，创建一个使用Langchain调用MCP工具的客户端：

```python
# client.py
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import asyncio

# 设置LLM，这里使用Qwen-Plus
model = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus",
)

# 配置与MCP服务器的连接
server_params = StdioServerParameters(
    command="python",
    args=["math_server.py"],
)

async def run_agent():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化连接
            await session.initialize()
            
            # 获取MCP工具
            tools = await load_mcp_tools(session)
            
            # 创建并运行agent
            agent = create_react_agent(model, tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            return agent_response

if __name__ == "__main__":
    result = asyncio.run(run_agent())
    print(result)
```

3. 运行流程

    1. **启动MCP客户端**：客户端创建一个与math_server的连接
    2. **初始化会话**：与MCP服务器建立连接
    3. **加载工具**：通过`load_mcp_tools`将MCP工具加载到Langchain中
    4. **创建Agent**：使用LLM和工具创建一个ReAct风格的agent
    5. **执行查询**：Agent接收问题并使用MCP工具解决它
    6. **返回结果**：返回计算结果

4.  实现细节

    - **通信方式**：使用stdio (标准输入/输出) 在客户端和服务器之间通信
    - **工具定义**：使用装饰器(`@mcp.tool()`)和类型注解定义工具接口
    - **Langchain集成**：使用`langchain_mcp_adapters`将MCP工具转换为Langchain工具
    - **Agent实现**：使用`langgraph`创建reactive agent，能够理解问题并正确选择工具

5.  如何扩展

    您可以通过以下方式扩展这个例子：

    1. 添加更多数学工具 (如除法、平方根等)
    2. 使用其他通信方式 (如HTTP而不是stdio)
    3. 实现更复杂的工具 (如金融计算器、文本处理等)
    4. 改进Agent提示，使其更智能地使用工具

6. 运行项目

    1. 安装依赖:
    ```
    pip install mcp langchain_mcp_adapters langgraph langchain_openai
    ```

    2. 设置环境变量:
    ```
    export DASHSCOPE_API_KEY=your_api_key
    ```

    3. 运行客户端:
    ```
    python client.py
    ```

    客户端将启动math_server.py，提出问题 "what's (3 + 5) x 12?"，并输出结果。

#### MCP和Function Call
![](images/index/image.png)


## 模块九：实战项目

在前面的模块中，我们学习了 LangChain 的核心概念、组件以及如何构建链和 Agent。现在，是时候将这些知识付诸实践了。本模块将通过几个实战项目，带你一步步构建有用的 LLM 应用。

### 第十九章：项目一：构建一个基于文档的问答机器人

本项目旨在构建一个能够根据用户提供的私有文档集（例如，公司内部知识库、产品手册、法律文件、研究论文等）来回答问题的机器人。这是一种典型的检索增强生成 (Retrieval Augmented Generation, RAG) 应用。

#### 19.1 项目需求分析与设计

在开始编码之前，清晰地定义项目需求和进行初步设计至关重要。

* **需求分析**:
    1.  **核心功能**: 用户上传或指定一组文档，然后可以针对这些文档的内容提出问题，机器人应基于文档内容给出答案。
    2.  **文档类型**: 需要支持哪些文档格式？（例如，`.txt`, `.pdf`, `.docx`, `.md`, 网页内容等）
    3.  **问题类型**: 用户可能会问哪些类型的问题？（事实型、解释型、比较型等）
    4.  **答案质量**: 对答案的准确性、完整性、简洁性有何要求？是否需要引用来源？
    5.  **用户交互方式**:
        * 是通过命令行界面、Web 界面还是 API？
        * 是否需要支持多轮对话（即机器人能记住之前的问答上下文）？
    6.  **性能要求**:
        * 文档处理（加载、嵌入）的速度要求？
        * 问答响应的延迟要求？
    7.  **数据安全与隐私**: 如果处理敏感文档，如何确保数据安全和用户隐私？
    8.  **可扩展性**: 未来是否需要支持更多的文档、更高的并发用户量？
    9.  **成本预算**: LLM API 调用、向量数据库存储、计算资源等成本考虑。

* **系统设计 (初步)**:
    1.  **数据处理流程 (Indexing Pipeline)**:
        * **文档加载 (Loading)**: 选择合适的文档加载器。
        * **文档分割 (Splitting)**: 将长文档分割成较小的文本块 (chunks)。
        * **文本嵌入 (Embedding)**: 使用嵌入模型将文本块转换为向量。
        * **向量存储 (Storing)**: 将文本块及其向量存储到向量数据库中。
    2.  **问答流程 (Querying Pipeline)**:
        * **问题接收**: 获取用户输入的问题。
        * **问题嵌入**: 将用户问题转换为向量。
        * **文档检索 (Retrieval)**: 从向量数据库中检索与问题向量最相似（相关）的文档块。
        * **上下文构建**: 将检索到的文档块与用户问题组合成提示 (prompt)。
        * **答案生成 (Generation)**: 将构建好的提示发送给 LLM 生成答案。
        * **(可选) 答案后处理**: 格式化答案，添加来源引用等。
    3.  **技术选型 (初步考虑)**:
        * **LLM**: OpenAI GPT 系列 (e.g., `gpt-3.5-turbo`, `gpt-4-turbo`), Anthropic Claude 系列, Google Gemini, 或其他开源/私有模型。
        * **嵌入模型**: OpenAI `text-embedding-ada-002` / `text-embedding-3-small`, Sentence Transformers, 或其他。
        * **文档加载器**: LangChain 内置的加载器 (`PyPDFLoader`, `TextLoader`, `WebBaseLoader` 等)。
        * **文本分割器**: `RecursiveCharacterTextSplitter`, `CharacterTextSplitter` 等。
        * **向量数据库**: FAISS (本地), Chroma (本地/服务器), Pinecone (云), Weaviate (云/自托管), Qdrant, PostgreSQL (with pgvector) 等。
        * **核心 LangChain 组件**: `RetrievalQA` 链, `load_qa_chain`, 或自定义 Agent。
        * **用户界面 (可选)**: Streamlit, Gradio, Flask/Django。

#### 19.2 数据准备与处理 (加载、分割、嵌入、存储)

这是构建 RAG 应用的基础，也称为“索引 (Indexing)”过程。

1.  **文档加载 (Document Loading)**:
    * 根据需要支持的文档类型，选择合适的 LangChain 文档加载器。
    * **示例**:
        ```python
        from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader

        # 加载单个 PDF
        # pdf_loader = PyPDFLoader("./docs/my_document.pdf")
        # documents_pdf = pdf_loader.load()

        # 加载单个文本文件
        # txt_loader = TextLoader("./docs/my_notes.txt")
        # documents_txt = txt_loader.load()

        # 加载一个目录下的所有 .txt 文件
        # dir_loader = DirectoryLoader('./docs_folder/', glob="**/*.txt", loader_cls=TextLoader)
        # documents_all_txt = dir_loader.load()

        # all_documents = documents_pdf + documents_txt + documents_all_txt # 合并文档列表
        ```
    * **考虑**: 处理不同编码、错误文件、提取元数据（如文件名、页码）。

2.  **文档分割 (Text Splitting)**:
    * LLM 有上下文窗口限制，且嵌入模型通常对较短文本效果更好。因此，需要将加载的文档分割成更小的、有意义的文本块。
    * 选择合适的分割策略和参数 (`chunk_size`, `chunk_overlap`) 很重要。
        * `chunk_size`: 每个文本块的目标大小（通常以字符数衡量）。
        * `chunk_overlap`: 相邻文本块之间的重叠字符数，有助于保持语义连续性。
    * **示例**:
        ```python
        from langchain.text_splitter import RecursiveCharacterTextSplitter

        # text_splitter = RecursiveCharacterTextSplitter(
        #     chunk_size=1000,  # 每个块约1000个字符
        #     chunk_overlap=200, # 相邻块重叠200个字符
        #     length_function=len
        # )
        # chunks = text_splitter.split_documents(all_documents) # all_documents 是加载后的文档列表
        ```
    * **考虑**: 分割符的选择 (`RecursiveCharacterTextSplitter` 会尝试按常见分隔符如 `\n\n`, `\n`, ` ` 等分割)、保持句子完整性、不同语言的特点。

3.  **文本嵌入 (Text Embedding)**:
    * 选择一个嵌入模型，将每个文本块转换为高维向量，捕捉其语义信息。
    * **示例**:
        ```python
        from langchain_openai import OpenAIEmbeddings

        # embeddings_model = OpenAIEmbeddings(model="text-embedding-3-small") # 或其他模型

        # # 嵌入单个文本 (示例，实际是嵌入 Document 对象的 page_content)
        # example_chunk_text = chunks[0].page_content
        # vector = embeddings_model.embed_query(example_chunk_text)
        # print(f"Vector dimension: {len(vector)}")
        ```
    * **考虑**: 嵌入模型的性能、成本、维度大小、是否支持所需语言。

4.  **向量存储 (Vector Storing)**:
    * 将文本块（通常是其内容和元数据）及其对应的向量存储到向量数据库中，以便后续进行高效的相似性搜索。
    * **示例 (使用 FAISS，一个本地内存/磁盘向量库)**:
        ```python
        from langchain_community.vectorstores import FAISS

        # 假设 chunks 和 embeddings_model 已定义
        # vector_store = FAISS.from_documents(chunks, embeddings_model)

        # 保存到本地磁盘 (可选)
        # vector_store.save_local("faiss_index_project1")

        # 从本地磁盘加载 (如果之前已保存)
        # loaded_vector_store = FAISS.load_local("faiss_index_project1", embeddings_model, allow_dangerous_deserialization=True)
        ```
    * **考虑**:
        * **持久化**: 选择内存型（如 FAISS 默认）还是持久化型数据库。
        * **可扩展性**: 对于大量文档，需要考虑数据库的写入和查询性能。
        * **成本**: 云向量数据库通常有费用。
        * **元数据过滤**: 某些向量数据库支持基于元数据进行过滤检索。
        * **更新策略**: 如何处理文档的新增、修改或删除。

#### 19.3 构建问答链或 Agent

一旦文档被索引到向量数据库中，就可以构建问答逻辑了。

1.  **创建检索器 (Retriever)**:
    * 检索器负责从向量数据库中根据用户问题提取相关的文档块。
    * **示例**:
        ```python
        # 假设 vector_store 已创建或加载
        # retriever = vector_store.as_retriever(
        #     search_type="similarity", # "similarity_score_threshold", "mmr" (Maximal Marginal Relevance)
        #     search_kwargs={"k": 5} # 检索最相关的5个文档块
        # )

        # # 测试检索器
        # query = "项目中提到的数据处理流程是什么？"
        # relevant_docs = retriever.invoke(query)
        # for doc in relevant_docs:
        #     print(f"Source: {doc.metadata.get('source', 'N/A')}, Content: {doc.page_content[:100]}...")
        ```
    * **考虑**: `search_type` (相似度、带阈值的相似度、MMR 以增加多样性)、`k` 值的选择。

2.  **选择问答链类型 (`chain_type` in `RetrievalQA`)**:
    * LangChain 提供了 `RetrievalQA` 链，它封装了检索和问答的整个流程。你需要为其指定一个 `chain_type`，这决定了如何处理检索到的文档并与 LLM 交互（详见 11.3 节）。
        * **`stuff`**: 将所有检索到的文档块“塞”进一个提示中。简单高效，但受上下文窗口限制。
        * **`map_reduce`**: 分别处理每个文档块（map），然后合并结果（reduce）。适合大量文档，但调用次数多。
        * **`refine`**: 迭代地优化答案，逐个处理文档块。
        * **`map_rerank`**: 分别处理并让 LLM 对每个答案打分，选择最高分的。
    * **示例 (使用 `stuff` 类型)**:
        ```python
        from langchain.chains import RetrievalQA
        from langchain_openai import ChatOpenAI

        # llm_qa = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

        # qa_chain = RetrievalQA.from_chain_type(
        #     llm=llm_qa,
        #     chain_type="stuff", # 或 "map_reduce", "refine"
        #     retriever=retriever,
        #     return_source_documents=True, # 可选，返回源文档
        #     # chain_type_kwargs={"prompt": my_custom_stuff_prompt} # 可选，自定义提示
        #     verbose=True
        # )
        ```

3.  **自定义提示 (Optional)**:
    * 对于 `stuff`、`map_reduce` 等链类型，你可以提供自定义的提示模板来更好地控制 LLM 的行为。
    * 例如，指示 LLM "请仅根据以下提供的上下文回答问题。如果上下文中没有答案，请说你不知道。"

4.  **使用 Agent (更高级的场景)**:
    * 如果问答过程需要更复杂的逻辑、多步推理、或动态选择是否需要检索以及如何使用检索结果，可以考虑使用 Agent。
    * 你可以创建一个自定义工具，该工具封装了从向量数据库检索文档的逻辑。然后，Agent 可以决定何时调用此检索工具。
    * Agent 还可以结合其他工具（如计算器、搜索工具）来回答更复杂的问题。

5.  **处理对话历史 (如果需要多轮对话)**:
    * 如果希望机器人能记住之前的对话上下文，需要集成记忆模块。
    * 可以将 `RetrievalQA` 链或 Agent 与 `ConversationBufferMemory` 等记忆类型结合使用。
    * 可能需要设计更复杂的提示，将对话历史和检索到的文档同时作为上下文提供给 LLM。`ConversationalRetrievalChain` 是专门为此设计的。
        ```python
        # from langchain.chains import ConversationalRetrievalChain
        # from langchain.memory import ConversationBufferMemory

        # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key='answer')
        # conversational_qa_chain = ConversationalRetrievalChain.from_llm(
        #     llm=llm_qa,
        #     retriever=retriever,
        #     memory=memory,
        #     return_source_documents=True,
        #     verbose=True
        # )
        # # 调用方式略有不同，需要传入 question
        # # result = conversational_qa_chain.invoke({"question": "我之前提到的主要技术是什么？"})
        ```

#### 19.4 用户界面集成 (可选，如 Streamlit 或 Gradio)

为了方便用户使用，可以为问答机器人创建一个简单的 Web 界面。Streamlit 和 Gradio 是两个流行的 Python 库，可以快速构建数据应用和机器学习模型的 UI。

* **Streamlit**:
    * 更侧重于构建数据仪表盘和交互式应用。
    * 使用简单的 Python 脚本即可创建 UI 组件。
    * **示例概念**:
        ```python
        # import streamlit as st
        # # (假设 qa_chain 或 conversational_qa_chain 已定义)

        # st.title("📚 基于文档的问答机器人")

        # uploaded_file = st.file_uploader("上传你的文档 (PDF, TXT)", type=["pdf", "txt"])
        # if uploaded_file:
        #     # 这里需要实现文档处理和索引的逻辑
        #     # 例如，保存文件，然后调用 19.2 中的数据处理流程
        #     # 这部分逻辑在实际应用中可能比较耗时，需要异步处理或状态管理
        #     st.success(f"文档 '{uploaded_file.name}' 处理完成！(模拟)")
        #     # 实际应用中，索引构建完成后，qa_chain 才能基于新文档工作

        # query = st.text_input("请输入你的问题：")

        # if query:
        #     with st.spinner("思考中..."):
        #         # result = qa_chain.invoke({"query": query}) # 对于 RetrievalQA
        #         # response_text = result.get("result")
        #         # source_docs = result.get("source_documents")

        #         # 对于 ConversationalRetrievalChain (通常在会话状态中管理)
        #         # if "chat_history" not in st.session_state:
        #         #     st.session_state.chat_history = []
        #         # result = conversational_qa_chain.invoke({"question": query, "chat_history": st.session_state.chat_history})
        #         # response_text = result.get("answer")
        #         # source_docs = result.get("source_documents")
        #         # st.session_state.chat_history.extend([HumanMessage(content=query), AIMessage(content=response_text)])


        #         # 模拟回复
        #         response_text = f"关于 '{query}' 的答案是... (模拟)"
        #         source_docs = [{"page_content": "这是相关的源文档片段...", "metadata": {"source": "doc1.pdf"}}]


        #         st.write("### 答案：")
        #         st.markdown(response_text)

        #         if source_docs:
        #             st.write("### 参考来源：")
        #             for doc in source_docs:
        #                 st.caption(f"来源: {doc.metadata.get('source', 'N/A')}")
        #                 st.text(doc.page_content[:200] + "...")
        ```

* **Gradio**:
    * 更侧重于快速为机器学习模型创建演示界面。
    * API 非常简洁。
    * **示例概念**:
        ```python
        # import gradio as gr
        # # (假设 qa_chain 或处理函数已定义)

        # def answer_question(query_text, history): # history 用于聊天模式
        #     # result = qa_chain.invoke({"query": query_text})
        #     # response = result.get("result", "抱歉，无法回答。")
        #     # sources_text = ""
        #     # if result.get("source_documents"):
        #     #     sources_text = "\n\n参考来源:\n" + "\n".join([
        #     #         f"- {doc.metadata.get('source', 'N/A')}: {doc.page_content[:100]}..."
        #     #         for doc in result["source_documents"]
        #     #     ])
        #     # return response + sources_text
        #     return f"模拟回复：'{query_text}' 的答案是... \n参考来源：doc1.pdf"


        # iface = gr.ChatInterface( # Gradio 提供了 ChatInterface 用于聊天机器人
        #     fn=answer_question,
        #     title="💬 文档问答机器人",
        #     description="上传文档（功能待实现），然后针对文档内容提问。"
        # )
        # # iface.launch()
        ```

* **考虑**:
    * **状态管理**: 对于多轮对话或需要记住上传文件状态的应用，需要仔细处理会话状态。
    * **异步处理**: 文档处理和 LLM 调用可能是耗时操作，在 Web 应用中应考虑异步执行以避免阻塞 UI。
    * **部署**: Streamlit 和 Gradio 应用可以方便地部署到各种平台。

#### 19.5 测试与评估

构建完成后，对问答机器人进行彻底的测试和评估非常重要。

* **测试方面**:
    1.  **单元测试**: 测试各个组件（文档加载器、分割器、嵌入逻辑、工具等）的正确性。
    2.  **集成测试**: 测试数据处理流程和问答流程的协同工作。
    3.  **功能测试**:
        * **准确性**: 对于已知答案的问题，机器人能否给出正确答案？
        * **相关性**: 检索到的文档块是否与问题相关？
        * **完整性**: 答案是否覆盖了问题的主要方面？
        * **鲁棒性**:
            * 对于模糊或略有错误的问题，机器人表现如何？
            * 如果文档中没有答案，机器人是否会诚实地回答“不知道”而不是编造答案？
        * **处理不同文档类型**: 是否能正确处理所有声称支持的文档格式？
    4.  **性能测试**:
        * 索引大量文档所需的时间。
        * 不同类型问题的平均响应时间。
    5.  **用户体验测试 (UAT)**: 让真实用户使用并收集反馈。

* **评估指标 (定量与定性)**:
    1.  **基于答案的指标**:
        * **精确匹配 (Exact Match, EM)**: 机器人答案与标准答案完全一致的比例。
        * **F1 分数**: 综合考虑答案的精确率和召回率（通常用于抽取式问答）。
        * **BLEU, ROUGE, METEOR**: 用于评估生成文本与参考答案的相似度（更适用于开放式生成）。
        * **语义相似度**: 使用嵌入模型计算机器人答案与标准答案的语义相似度。
    2.  **基于检索的指标**:
        * **命中率 (Hit Rate)**: 检索到的文档中包含正确答案的比例。
        * **MRR (Mean Reciprocal Rank)**: 正确答案在检索结果中排名的倒数的平均值。
        * **Precision@k, Recall@k, nDCG@k**: 评估检索结果列表的质量。
    3.  **人工评估**:
        * 邀请人工评估员对答案的准确性、流畅性、相关性、完整性、是否有害性等进行打分。
        * 这是评估 RAG 系统质量的黄金标准，尤其是对于复杂或主观的问题。
    4.  **使用 LLM 作为评估器 (LLM-as-a-judge)**:
        * 利用另一个强大的 LLM（如 GPT-4）来评估问答机器人生成的答案。
        * 可以设计提示，让评估 LLM 从不同维度（如准确性、相关性、是否有害）对答案进行打分或比较。

* **评估框架与工具**:
    * **LangSmith**: 提供了数据集管理、运行评估、比较结果、人工反馈标注等功能，非常适合评估 LLM 应用。
    * **Ragas**: 一个专门用于评估 RAG 应用的开源框架，提供了多种基于检索和生成的评估指标。
    * 自定义评估脚本。

通过系统性的测试和评估，可以发现机器人的不足之处，并有针对性地进行迭代优化（例如，调整分割策略、更换嵌入模型、优化提示、改进检索逻辑等）。



* 第二十章：项目二：开发一个能执行多步骤任务的个人助理 Agent
    * 20.1 项目构思与功能定义
    * 20.2 设计并实现所需的 Tools (如日历查询、邮件发送、信息检索等)
    * 20.3 选择并配置合适的 Agent 类型
    * 20.4 实现 Agent 的逻辑与交互
    * 20.5 优化与迭代
* 第二十一章：项目三：（可选，根据热门或特定领域选择）
    * 例如：构建一个代码生成助手、一个故事创作工具、一个基于知识图谱的问答系统等。
模块九：LangChain 进阶与生态
* 第二十二章：LangChain Expression Language (LCEL)
    * 22.1 LCEL 的基本语法和优势
    * 22.2 使用 LCEL 组合组件 (Runnables)
    * 22.3 LCEL 的流式处理、批处理和异步支持
    * 22.4 将现有链转换为 LCEL 形式
* 第二十三章：部署 LangChain 应用
    * 23.1 常见的部署方式 (Serverless, Docker, PaaS 平台)
    * 23.2 LangServe：快速部署 LangChain 应用的工具
    * 23.3 API 设计与安全性考虑
* 第二十四章：LangGraph：构建具有循环和状态的复杂应用
    * 24.1 LangGraph 的核心概念 (Nodes, Edges, State)
    * 24.2 构建简单的图应用
    * 24.3 实现多 Agent 协作
* 第二十五章：LangSmith：调试、测试、评估和监控 LLM 应用
    * 25.1 LangSmith 的核心功能
    * 25.2 如何在项目中使用 LangSmith
    * 25.3 评估 LLM 应用的性能和质量
* 第二十六章：LangChain 的未来发展与社区资源
    * 26.1 LangChain 的最新进展和发展方向
    * 26.2 如何参与 LangChain 社区 (GitHub, Discord, 论坛)
    * 26.3 持续学习和探索的建议
附录
* A. 常见问题解答 (FAQ)
* B. 术语表
* C. 推荐阅读和资源链接
教程制作建议：
* 代码示例驱动： 每个概念都应伴随清晰、可运行的代码示例。
* 实践性强： 鼓励学习者动手实践，并提供练习题或小挑战。
* 循序渐进： 确保内容的难度逐步提升，避免一开始就引入过多复杂概念。
* 清晰的图示： 对于抽象概念（如链、Agent 的工作流程），使用图示辅助解释。
* 版本控制： 注意 LangChain 版本更新较快，教程内容应基于一个相对稳定的版本，并提示学习者注意版本差异。
* 互动性： 如果是视频教程或在线课程，可以设计一些互动环节。
