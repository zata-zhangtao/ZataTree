---
title: 教程_langchain_v0.3
description: ""
date: 2025-05-08T22:59:00+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---



参考





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
####  * 3.1 模型 I/O (Model I/O)：与语言模型的交互接口

模型 I/O 是 LangChain 框架中最核心的模块之一，负责处理与语言模型的输入输出交互。它提供了一套标准化的接口，使得开发者能够以统一的方式与各种语言模型（无论是本地模型还是云端 API，如 OpenAI、Hugging Face、Grok 等）进行通信。模型 I/O 模块主要包括以下三个核心组成部分：

1. **Prompts（提示）**  
   Prompts 是与语言模型交互的起点，用于定义输入的结构和内容。LangChain 提供了强大的提示管理工具，允许开发者创建动态、可重用的提示模板。  
   - **提示模板 (Prompt Templates)**：通过占位符和变量，开发者可以构建灵活的提示。例如，一个模板可以是：“请将以下文本翻译成{language}：{text}”。  
   - **动态提示**：支持根据上下文或用户输入动态填充提示内容，适用于需要个性化或复杂逻辑的场景。  
   - **提示优化**：LangChain 提供工具帮助优化提示，例如通过 Few-Shot Learning 或 Chain-of-Thought 提示设计，提升模型输出质量。

2. **语言模型 (Language Models)**  
   语言模型是模型 I/O 的核心执行单元，LangChain 支持多种类型的语言模型：  
   - **聊天模型 (Chat Models)**：如 OpenAI 的 GPT-4、Grok 等，擅长处理对话型任务。  
   - **嵌入模型 (Embedding Models)**：如 Hugging Face 的句嵌入模型，用于生成文本的向量表示，适用于语义搜索或相似性比较。  
   - **本地模型支持**：LangChain 允许集成本地部署的模型（如 LLaMA 或其他开源模型），适合对隐私和成本敏感的场景。  
   LangChain 的抽象层屏蔽了不同模型 API 的差异，开发者只需调用统一的接口即可切换模型。

3. **输出解析器 (Output Parsers)**  
   语言模型的输出通常是自由文本，难以直接用于结构化处理。输出解析器负责将模型的原始输出转换为开发者需要的格式。  
   - **结构化输出**：将模型输出解析为 JSON、列表或其他数据结构。例如，将模型生成的回答解析为键值对。  
   - **自定义解析**：支持正则表达式、Pydantic 模型等工具，定义复杂的解析逻辑。  
   - **错误处理**：当模型输出不符合预期时，解析器可以触发重试或提供默认值，确保系统鲁棒性。


- 这些组件可以通过 LangChain 表达式语言（LCEL）组合，例如 chain = chat_prompt | chat_model | output_parser。这允许开发者根据需要切换模型或连接外部数据源。

    * 3.2 数据连接 (Data Connection)：让语言模型与外部数据交互
        * Document Loaders
        * Document Transformers
        * Text Embedding Models (再次提及，强调其在数据连接中的作用)
        * Vector Stores
        * Retrievers
    * 3.3 链 (Chains)：构建调用序列
        * 基本链 (LLMChain)
        * 顺序链 (Sequential Chains)
        * 路由链 (Router Chains)
        * 其他常用链类型
    * 3.4 记忆 (Memory)：让链拥有记忆能力
        * 记忆的类型 (ConversationBufferMemory, ConversationSummaryMemory 等)
        * 如何在链中使用记忆
    * 3.5 代理 (Agents)：让语言模型动态决策和行动
        * Agent 的核心概念：Tools, Agent Executor, ReAct 框架等
        * 不同类型的 Agent (Zero-shot ReAct, Self-ask with search 等)
    * 3.6 回调 (Callbacks)：监控和记录 LangChain 应用的执行过程
        * 回调的作用和使用场景
        * 常用的回调处理器
模块二：模型 I/O (Model I/O) 深入
* 第四章：与语言模型 (LLMs) 交互
    * 4.1 理解 LLMs 接口
    * 4.2 使用不同的 LLM提供商 (OpenAI, Hugging Face Hub, Azure OpenAI 等)
    * 4.3 Prompt Templates：动态构建高效的提示
        * 基本 Prompt Template
        * 带有变量的 Prompt Template
        * Few-shot Prompt Template
        * Output Parsers：结构化输出处理
    * 4.4 异步操作与流式输出
    * 4.5 模型参数配置与优化 (temperature, max_tokens 等)
* 第五章：与聊天模型 (Chat Models) 交互
    * 5.1 理解 Chat Models 的消息类型 (SystemMessage, HumanMessage, AIMessage)
    * 5.2 构建聊天应用的 Prompt Templates
    * 5.3 聊天历史管理
    * 5.4 结合 Output Parsers 实现更复杂的聊天交互
* 第六章：文本嵌入模型 (Text Embedding Models)
    * 6.1 文本嵌入的原理和应用场景
    * 6.2 使用不同的文本嵌入模型 (OpenAI Embeddings, Hugging Face Embeddings 等)
    * 6.3 生成文本的向量表示
    * 6.4 比较文本相似度
模块三：数据连接 (Data Connection) 详解
* 第七章：文档加载 (Document Loaders)
    * 7.1 从不同数据源加载文档 (文本文件, PDF, 网页, YouTube, Notion 等)
    * 7.2 常用 Document Loaders 介绍和使用
    * 7.3 自定义 Document Loader
* 第八章：文档转换 (Document Transformers)
    * 8.1 文本分割 (Text Splitters)：按字符、Token、递归等方式分割长文本
    * 8.2 文本清洗和预处理
    * 8.3 元数据提取和添加
* 第九章：向量存储 (Vector Stores) 与检索 (Retrievers)
    * 9.1 向量数据库的基本概念 (FAISS, Chroma, Pinecone, Weaviate 等)
    * 9.2 将文档嵌入并存储到向量数据库
    * 9.3 构建不同类型的检索器 (VectorStoreRetriever, MultiQueryRetriever, SelfQueryRetriever 等)
    * 9.4 相似性搜索与语义检索的原理
    * 9.5 优化检索效果 (Top K, 过滤等)
模块四：构建强大的链 (Chains)
* 第十章：基础与顺序链 (Basic and Sequential Chains)
    * 10.1 LLMChain：最基础的链
    * 10.2 SimpleSequentialChain：单输入单输出的顺序链
    * 10.3 SequentialChain：多输入多输出的顺序链
    * 10.4 链的输入输出管理
* 第十一章：高级链应用
    * 11.1 转换链 (TransformChain)：在链中进行数据转换
    * 11.2 路由链 (RouterChain)：根据输入动态选择下一个链
    * 11.3 文档问答链 (Question Answering over Documents)
        * load_qa_chain, RetrievalQA 等
        * 不同的 chain_type (stuff, map_reduce, refine, map_rerank)
    * 11.4 摘要链 (Summarization Chains)
    * 11.5 自定义链的创建与使用
模块五：赋予应用记忆 (Memory)
* 第十二章：记忆的类型与使用
    * 12.1 ConversationBufferMemory：基础的对话缓冲区记忆
    * 12.2 ConversationBufferWindowMemory：带窗口大小的对话缓冲区记忆
    * 12.3 ConversationTokenBufferMemory：基于 Token 数量限制的记忆
    * 12.4 ConversationSummaryMemory：对话摘要记忆
    * 12.5 ConversationSummaryBufferMemory：结合摘要和缓冲区的记忆
    * 12.6 EntityMemory：实体记忆
    * 12.7 VectorStoreRetrieverMemory：基于向量存储的记忆
    * 12.8 在链和 Agent 中集成和管理记忆
* 第十三章：高级记忆策略
    * 13.1 自定义记忆类型
    * 13.2 多轮对话中的记忆管理
    * 13.3 记忆的持久化与加载
模块六：智能代理 (Agents) 的开发与应用
* 第十四章：Agent 基础
    * 14.1 Agent 的核心组件：Tools, Agent, Agent Executor
    * 14.2 理解 Agent 的思考过程 (Thought, Action, Observation)
    * 14.3 内置 Tools 的使用 (Google Search, Wikipedia, Python REPL, Shell 等)
    * 14.4 创建自定义 Tools
* 第十五章：不同类型的 Agent
    * 15.1 Zero-shot ReAct Agent
    * 15.2 Self-ask with search Agent
    * 15.3 Conversational React Agent (用于对话的 Agent)
    * 15.4 OpenAI Functions Agent (利用 OpenAI 函数调用)
    * 15.5 Plan and Execute Agent
    * 15.6 选择合适的 Agent 类型
* 第十六章：高级 Agent 应用
    * 16.1 Agent 的错误处理与调试
    * 16.2 限制 Agent 的行为和资源使用
    * 16.3 构建复杂的 Agent 来完成多步骤任务
    * 16.4 Agent 与外部 API 的交互
模块七：回调 (Callbacks) 与调试
* 第十七章：使用 Callbacks 进行监控与日志记录
    * 17.1 CallbackManager 和 CallbackHandler
    * 17.2 内置的回调处理器 (StdOutCallbackHandler, FileCallbackHandler)
    * 17.3 自定义回调处理器
    * 17.4 跟踪链和 Agent 的执行流程
    * 17.5 与 LangSmith 等监控平台集成 (可选，但推荐提及)
* 第十八章：LangChain 应用的调试技巧
    * 18.1 理解和分析 LangChain 的日志输出
    * 18.2 使用 verbose=True 进行详细输出
    * 18.3 LangChain Debugging 工具 (如果 LangChain 自身提供)
    * 18.4 常见错误及其解决方法
模块八：实战项目
* 第十九章：项目一：构建一个基于文档的问答机器人
    * 19.1 项目需求分析与设计
    * 19.2 数据准备与处理 (加载、分割、嵌入、存储)
    * 19.3 构建问答链或 Agent
    * 19.4 用户界面集成 (可选，如 Streamlit 或 Gradio)
    * 19.5 测试与评估
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
希望这个详细的教程计划能帮助您制作出优秀的 LangChain 教程！祝您一切顺利！
