---
title: gemini教程_langchain_v0.3
description: ""
date: 2025-03-08T23:08:17+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---


Langchain综合教程：从入门到精通前言：Langchain教程学习路径指南本教程旨在为希望学习和掌握Langchain框架的开发者提供一个全面、系统且深入的学习路径。Langchain作为一个强大的开源框架，旨在简化基于大型语言模型（LLM）的应用程序开发。它通过提供模块化的组件、灵活的编排能力以及与众多外部工具和数据源的集成，极大地加速了从概念到生产的开发周期。本教程将从Langchain的核心价值与基本概念入手，逐步引导学习者完成环境搭建，深入剖析其核心组件（如模型、提示、索引、链、记忆、工具、智能体和回调机制），并通过构建实际应用案例（如文档问答、聊天机器人、文本摘要、数据生成和代码理解）来巩固所学知识。随后，教程将探讨Langchain的高级概念，包括LangChain表达式语言（LCEL）的进阶应用、复杂链的构建（路由与分支）、以及使用LangGraph设计状态化多智能体系统。最后，教程将聚焦于Langchain应用的生产化与部署，涵盖调试、追踪、评估、API部署以及生产环境中的最佳实践和安全注意事项。教程还将展望Langchain的未来发展，并提供丰富的学习资源，帮助学习者持续提升。通过本教程的学习，开发者不仅能够理解Langchain的“是什么”和“为什么”，更能掌握“怎么做”，从而有能力构建出强大、智能且实用的LLM应用程序。核心观点 1.1.1: Langchain的真正价值在于它不仅仅是一个库，而是一个全面的框架，它通过提供模块化的构建块和强大的编排能力，标准化并极大地简化了构建复杂LLM应用程序的过程。大型语言模型本身虽然强大，但在实际应用中，开发者往往需要将其与各种数据源连接，进行复杂的提示工程，并管理多轮对话的上下文 1。Langchain通过其精心设计的组件（如模型I/O、数据连接、链、智能体、记忆模块等）解决了这些挑战 2。它使得开发者可以像搭积木一样组合这些组件，快速构建出如问答系统、聊天机器人、内容生成工具等多样化的应用，而无需从头处理与LLM交互的底层复杂性，从而更专注于应用逻辑本身 1。这种框架化的方法论，使得原本需要大量定制开发的工作变得更加高效和规范。模块一：Langchain入门本模块旨在为初学者介绍Langchain的基本概念、核心价值、安装步骤以及学习所需的预备知识，为后续深入学习打下坚实的基础。第一章：Langchain简介1.1 Langchain是什么？Langchain是一个开源框架，专为简化基于大型语言模型（LLM）的应用程序开发而设计 1。LLM是经过海量数据预训练的深度学习模型，能够对用户查询生成响应，例如回答问题或根据文本提示创作内容 1。Langchain通过提供一系列工具和抽象，使得开发者能够更轻松地定制、部署和管理这些LLM应用。1.2 Langchain的核心价值Langchain的核心价值在于其能够增强LLM生成信息的定制化、准确性和相关性 1。它提供了一套标准化的接口和可组合的构建块，允许开发者：
快速集成与定制：轻松集成多种LLM，并根据特定需求定制提示模板和输出解析器 1。
连接外部数据：使LLM能够访问和利用外部数据源，如数据库、API、文档库等，从而生成更具上下文感知和事实依据的响应，这对于解决LLM自身知识库的局限性至关重要 1。
构建复杂应用：通过“链”（Chains）和“智能体”（Agents）的概念，将多个LLM调用或与其他工具的交互串联起来，实现更复杂的逻辑和工作流 1。
状态管理：提供记忆（Memory）组件，使应用程序能够记住先前的交互，从而进行连贯的多轮对话 1。
1.3 Langchain解决的问题LLM本身虽然强大，但在应用于特定领域或解决复杂问题时，往往面临以下挑战：
领域知识缺乏：LLM的训练数据可能不包含特定行业或组织的专有知识 1。
上下文理解局限：LLM的上下文窗口有限，难以处理长篇文档或进行需要长期记忆的对话。
缺乏行动能力：LLM本身无法直接与外部世界交互，如查询数据库、调用API或执行代码。
开发效率低下：直接与LLM API交互需要处理繁琐的细节，如API认证、请求格式化、错误处理等 2。
Langchain通过提供标准化的组件和接口，有效地解决了这些问题。例如，它通过文档加载器（Document Loaders）、文本分割器（Text Splitters）、嵌入模型（Embedding Models）和向量存储（Vector Stores）等组件，实现了检索增强生成（RAG），使LLM能够基于外部知识回答问题 1。它还通过智能体和工具的结合，赋予LLM执行具体任务的能力 1。1.4 Langchain在AI应用开发中的角色Langchain在AI应用开发中扮演着“粘合剂”和“加速器”的角色 1。它使得开发者能够：
更便捷地开发多样化的LLM驱动应用，包括聊天机器人、问答系统、内容生成、文本摘要等 1。
将LLM应用于特定领域，而无需对模型本身进行重新训练或微调 1。
通过实现如RAG这样的上下文感知工作流，减少模型幻觉，提高响应的准确性 1。
简化了提示工程和与数据源集成的中间步骤，使开发更加高效 1。
总之，Langchain通过抽象LLM交互的复杂性，并提供一套丰富的工具集，让开发者可以更专注于应用逻辑的构建，从而加速AI应用的创新和落地 1。第二章：学习Langchain的准备工作2.1 环境要求与安装在开始学习Langchain之前，确保您的开发环境满足基本要求。Langchain主要支持Python和JavaScript/TypeScript。

Python环境：

建议使用Python 3.7或更高版本 5。
可以通过pip进行安装。核心langchain包的安装命令为：
Bashpip install langchain

6
Langchain拥有庞大的集成生态系统。许多特定的LLM提供商、数据存储或工具可能需要安装额外的包。例如，与OpenAI模型交互通常需要安装langchain-openai 6。社区贡献的集成通常在langchain-community包中 8。
Bashpip install langchain-openai langchain-community





JavaScript/TypeScript环境：

支持Node.js (18.x, 19.x, 20.x), Cloudflare Workers, Vercel/Next.js, Supabase Edge Functions, 浏览器, Deno, 和 Bun 等多种环境 8。
可以通过npm, Yarn, 或 pnpm进行安装。例如，使用npm安装：
Bashnpm install -S langchain

8
与Python类似，JS版本也有核心包（@langchain/core）和各种集成包（如@langchain/openai, @langchain/community） 8。为了确保所有集成之间的类型兼容性，建议在项目的package.json中通过overrides (npm/pnpm) 或 resolutions (Yarn) 字段统一@langchain/core的版本 8。



LangSmith (可选但推荐)：

LangSmith是一个用于调试、追踪、监控和评估LLM应用的平台，与Langchain无缝集成 3。
要使用LangSmith，您需要创建一个LangSmith开发者账户并获取API密钥 6。
然后设置环境变量以启用追踪：
Bashexport LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=ls__... # 替换为您的API密钥

6


核心观点 2.1.1: Langchain的安装过程并不仅仅是执行一个简单的pip install langchain命令。开发者需要关注其Python或Node.js的版本兼容性，并根据项目需求有选择地安装众多集成包（如langchain-openai, langchain-community等），同时，为了充分利用其生态系统，还需考虑如LangSmith这样的辅助工具的环境配置。这种安装上的细致要求，源于Langchain作为一个高度可扩展的框架，其核心功能依赖于与大量第三方模型、服务和工具的集成 6。例如，使用特定的LLM（如OpenAI的GPT模型）或向量数据库（如Chroma、FAISS）都需要安装相应的集成包 6。同样，在JavaScript环境中，管理@langchain/core的版本对于确保不同集成模块间的兼容性至关重要 8。因此，一个成功的Langchain项目始于对这些依赖和环境配置的正确理解和设置。2.2 必备知识：Python编程与LLM基础虽然Langchain致力于简化LLM应用的开发，但具备一定的预备知识将极大地帮助您理解和运用该框架。

Python编程基础：

由于Langchain的Python库是其主要实现，并且拥有最广泛的社区支持和文档资源，因此熟悉Python编程至关重要 6。
应掌握Python的基本语法、数据结构（列表、字典、元组、集合）、函数、类和对象、模块和包的使用。
理解异步编程（async/await）的概念会对使用Langchain的异步功能有所帮助，尤其是在构建需要高并发处理的应用时 9。



大型语言模型 (LLM) 基础概念：

了解LLM是什么，它们是如何工作的（基于Transformer架构、预训练和微调等），以及它们的主要能力（文本生成、理解、摘要、翻译等）和局限性（知识截止、幻觉、偏见等）11。
熟悉核心术语，如：

提示 (Prompt)：向LLM发出的指令或问题。
上下文窗口 (Context Window)：LLM在一次交互中能够处理的最大文本长度（token数量）9。
Token: LLM处理文本的基本单位 9。
嵌入 (Embeddings)：将文本转换为密集向量表示，用于捕捉语义信息 9。
温度 (Temperature)：控制LLM输出随机性的参数。
微调 (Fine-tuning)：在特定任务或数据集上进一步训练预训练模型。


对常见的LLM应用场景（如聊天机器人、问答系统、文本生成）有所了解，将有助于理解Langchain中各种组件和链的设计目的。


Langchain的官方文档、教程和概念指南是学习这些基础知识的良好起点 11。虽然Langchain抽象了许多底层细节，但对这些核心概念的理解将使您能够更有效地设计、调试和优化您的Langchain应用。模块二：Langchain核心组件详解本模块将深入剖析Langchain框架的各个核心组件。理解这些组件的功能和用法是构建复杂LLM应用的基础。Langchain的设计哲学是模块化和可组合性，允许开发者根据需求灵活地选用和连接这些组件。第三章：Langchain组件概览3.1 模型 (Models): LLM、聊天模型、文本嵌入模型模型是Langchain应用的核心，负责处理语言理解和生成任务。Langchain本身不提供模型，而是提供一个标准接口，用于与各种语言模型进行交互 13。Langchain主要支持三种类型的模型：大型语言模型（LLMs）、聊天模型（Chat Models）和文本嵌入模型（Text Embedding Models）。

大型语言模型 (LLMs)：

这类模型通常指那些接受文本字符串作为输入并输出文本字符串的传统语言模型 3。
Langchain为LLMs提供了标准接口，如invoke（用于单次调用）和stream（用于流式输出）3。
支持的功能包括缓存模型响应、创建自定义LLM类、流式传输响应、跟踪token使用情况以及使用本地模型 3。
在LangChain Go的实现中，LLM接口包含Call（处理单个提示）和Generate（处理多个提示）方法 13。



聊天模型 (Chat Models)：

聊天模型专门为对话场景优化，它们以一系列消息（Messages）作为输入，并输出一个消息作为响应 3。
消息通常包含内容（content）和角色（role，如system, user, assistant）3。
Langchain支持对消息进行修剪、过滤和合并等操作 3。
聊天模型API相对较新，Langchain仍在探索最佳的抽象方式 13。
在LangChain Go中，ChatLLM接口包含Call（处理单轮对话消息）和Generate（处理多轮对话消息）方法 13。
许多聊天模型支持多模态输入，例如图像 14。Langchain允许通过特定格式（如内容块或OpenAI的聊天完成格式）传递这些多模态输入 14。一些模型甚至支持多模态输出，如生成图像或音频 14。



文本嵌入模型 (Text Embedding Models)：

嵌入模型负责将文本数据转换为数值向量（即嵌入），这些向量能够捕捉文本的语义信息 3。
这些嵌入广泛应用于语义搜索、相似性比较、聚类和检索增强生成（RAG）等任务 3。
Langchain支持多种嵌入模型提供商，并允许缓存嵌入结果或创建自定义嵌入类 3。
目前Langchain中的嵌入接口主要针对文本数据优化，未来有望扩展以支持图像、音频和视频等多模态数据的嵌入 14。


所有LLM和聊天模型都实现了BaseLanguageModel接口（在LangChain Go中为LanguageModel接口），这使得在链中轻松替换不同类型的模型成为可能，而无需更改其余代码 13。核心观点 3.1.1: Langchain通过为不同类型的语言模型（传统LLM、聊天模型、嵌入模型）提供统一的抽象接口（如BaseLanguageModel），极大地增强了应用开发的灵活性和可移植性。这种设计允许开发者在不修改应用核心逻辑的情况下，轻松切换或试验不同的底层模型提供商（如OpenAI, Anthropic, Hugging Face等）或模型类型。例如，一个为文本补全设计的链，最初可能使用一个通用的LLM接口；如果后续需要更强的对话能力，开发者可以将模型切换为一个聊天模型接口的实现，而链的其余部分（如提示模板、输出解析器）可能只需微调甚至无需改动 3。同样，对于需要语义理解的任务，嵌入模型的抽象也使得更换不同的嵌入算法或服务变得简单 3。这种模型无关性是Langchain框架的核心优势之一，它将开发者从特定模型的API细节中解放出来，更专注于应用逻辑的构建和优化。3.2 提示 (Prompts): 模板、选择器、解析器提示工程是与LLM有效交互的关键。Langchain提供了一系列组件来帮助开发者构建、管理和优化提示。

提示模板 (Prompt Templates)：

提示模板负责将用户输入和参数格式化为LLM可以理解的指令 3。它们帮助指导模型的响应，确保输出的相关性和连贯性。
字符串提示模板 (PromptTemplate): 用于格式化单个字符串，通常用于简单的输入。它们接受一个字典作为输入，其中键对应模板中的变量，并输出一个PromptValue 16。

示例：PromptTemplate.from_template("告诉我一个关于{topic}的笑话") 16。


聊天提示模板 (ChatPromptTemplate): 用于格式化一系列消息，适用于聊天模型。它们由一个消息模板列表组成，每个模板可以定义消息的角色（如system, user, ai）和内容 16。

示例：ChatPromptTemplate.from_messages([("system", "你是一个乐于助人的助手。"), ("user", "{input}")]) 16。


MessagesPlaceholder: 这是一个特殊的提示模板组件，用于在聊天提示模板的特定位置插入一个消息列表。这对于动态地将聊天历史或其他消息序列注入到提示中非常有用 16。
少样本提示 (Few-shot Prompts): 允许在提示中包含一些示例，以指导LLM生成特定格式或风格的输出 3。Langchain支持在字符串提示和聊天提示中使用少样本示例。
提示组合 (Prompt Composition): Langchain允许将多个提示片段组合起来，创建更复杂或可复用的提示结构 3。
多模态提示 (Multimodal Prompts): Langchain支持创建包含多种数据类型（如文本和图像）的提示，以供多模态模型使用 3。



示例选择器 (Example Selectors)：

当有大量少样本示例可用时，示例选择器负责根据当前输入选择最相关的示例包含在提示中 3。这比静态地包含所有示例更为高效和有效。
Langchain提供了多种示例选择策略 3：

按长度选择 (LengthBasedExampleSelector): 根据示例的长度进行选择，以适应上下文窗口限制。
按语义相似性选择 (SemanticSimilarityExampleSelector): 使用嵌入模型找到与当前输入语义最相似的示例。
按最大边际相关性选择 (MaxMarginalRelevanceExampleSelector - MMR): 选择与输入相似但彼此之间又具有多样性的示例，避免示例过于同质化。
按N元语法重叠选择 (NGramOverlapExampleSelector): 基于输入和示例之间N元语法的重叠程度进行选择。
从LangSmith少样本数据集中选择示例。





输出解析器 (Output Parsers)：

输出解析器负责将LLM的原始文本输出转换为更结构化、更易于下游任务使用的格式 3。虽然越来越多的模型支持函数调用（function/tool calling）来直接生成结构化输出，但在某些情况下，输出解析器仍然非常有用 18。
Langchain提供了多种内置的输出解析器，并且支持自定义解析器。
常见类型包括 18：

字符串解析器 (StrOutputParser): 简单地将输出作为字符串返回。
列表解析器 (CommaSeparatedListOutputParser, NumberedListOutputParser): 将LLM生成的列表（如逗号分隔或数字编号）解析为Python列表。
JSON解析器 (JsonOutputParser, PydanticOutputParser): 将LLM的输出解析为JSON对象或Pydantic模型实例。PydanticOutputParser特别强大，因为它允许你定义一个Pydantic模型作为期望的输出模式，并自动生成格式化指令供LLM遵循，同时验证输出是否符合模式。
XML解析器 (XMLOutputParser): 解析XML格式的输出。
CSV解析器 (OutputFixingParser + CSV prompt): 解析CSV格式的输出。
日期时间解析器 (DatetimeOutputParser): 将LLM生成的日期时间文本解析为datetime对象。
枚举解析器 (EnumOutputParser): 确保LLM的输出是预定义枚举类型中的一个值。
结构化输出解析器 (StructuredOutputParser): 一个相对简单的解析器，用于从文本中提取具有预定义字段的结构化信息（字段值为字符串）。
修复错误的解析器 (OutputFixingParser, RetryWithErrorOutputParser): 这些解析器可以包装另一个解析器。如果被包装的解析器解析失败，它们会调用LLM尝试修复格式错误的输出。RetryWithErrorOutputParser在重试时会提供原始指令和错误信息，以获得更好的修复效果。


许多输出解析器都包含get_format_instructions()方法，该方法可以生成一段文本，指导LLM如何格式化其输出以符合解析器的期望 18。


核心观点 3.2.1: Langchain中的提示模板和示例选择器并不仅仅是简单的文本格式化工具，它们是实现高效、精准的提示工程的核心机制，使得开发者能够构建结构化、上下文丰富且能根据输入动态调整的与LLM的交互方式。LLM的行为在很大程度上取决于接收到的提示质量 17。提示模板通过预定义结构和变量占位符，确保了提示的一致性和可复用性，同时允许动态插入特定于每次请求的信息 3。而示例选择器则通过智能地从大量候选项中挑选最相关的少样本示例，进一步提升了LLM在特定任务上的表现，尤其是在需要模型理解复杂指令或特定输出格式时 3。这两者的结合，使得开发者可以更精细地控制LLM的输入，从而引导其产生更符合预期的输出，这对于构建可靠的LLM应用至关重要。核心观点 3.3.1: 输出解析器在Langchain中扮演着至关重要的角色，它们负责将大型语言模型（LLM）通常非结构化的文本输出转化为应用程序可以直接使用的、规范化的结构化数据，从而有效弥合了LLM的生成能力与下游程序化处理需求之间的鸿沟，尤其是在不使用或模型本身不支持工具/函数调用功能时。LLM本质上是文本生成器，即使通过精心设计的提示引导，其输出也可能在格式上存在细微变化或不完全符合预期 18。输出解析器通过定义清晰的解析逻辑（例如，期望得到JSON、列表、Pydantic模型等），不仅能够从LLM的输出中提取所需信息，还能进行格式验证，甚至在某些情况下（如使用OutputFixingParser）调用LLM来修复格式错误 18。这种能力对于确保数据在应用流程中的可靠传递和处理至关重要，使得LLM的强大生成能力能够被更广泛的软件系统所集成和利用。3.3 索引 (Indexes): 文档加载器、文本分割器、向量存储、检索器索引组件负责组织和准备数据，以便LLM能够有效地访问和利用这些数据，尤其是在构建检索增强生成（RAG）等应用时。

文档加载器 (Document Loaders)：

文档加载器负责从各种来源加载文档数据，并将其转换为Langchain统一的Document对象格式 3。Document对象通常包含page_content（文本内容）和metadata（元数据，如来源、页码等）20。
Langchain支持从多种数据源加载文档，包括 3：

文件系统：PDF, CSV, JSON, HTML, Markdown, 文本文件等。
网页内容。
数据库。
API。
Google Drive, Notion, Slack等协作平台。


开发者也可以创建自定义的文档加载器来处理特定的数据源。



文本分割器 (Text Splitters)：

由于LLM的上下文窗口大小有限，以及为了更精确地进行语义检索，通常需要将加载的长文档分割成较小的、语义相关的文本块（chunks）3。
文本分割器负责执行这个分割任务。选择合适的分割策略对于后续的检索效果至关重要。
Langchain提供了多种文本分割器 3：

按字符分割 (CharacterTextSplitter): 基于固定数量的字符进行分割，是最简单的方法。
递归字符分割 (RecursiveCharacterTextSplitter): 尝试按一系列分隔符（如换行符、句子结束符等）递归地分割文本，直到块大小符合要求。这是推荐的通用分割器 15。
按Token分割 (TokenTextSplitter): 基于LLM的tokenizer将文本分割成特定数量的token。
特定语言分割器 (如 PythonCodeTextSplitter, MarkdownHeaderTextSplitter): 针对特定格式（如Python代码、Markdown文档的标题结构）进行优化分割。
语义块分割 (SemanticChunker): 尝试根据语义相似性将文本分割成连贯的块。


分割时通常会设置块之间的重叠（chunk_overlap），以避免丢失跨越块边界的上下文信息 15。



向量存储 (Vector Stores)：

向量存储是专门设计用于存储和高效查询文本嵌入（embeddings）的数据库 3。文本嵌入是将文本转换为数值向量，使得语义相似的文本在向量空间中距离相近。
在RAG流程中，文档块首先被转换为嵌入，然后存储在向量存储中。当用户提问时，问题也被转换为嵌入，然后在向量存储中搜索最相似的文档块嵌入，从而找到相关的上下文。
Langchain集成了多种向量存储解决方案，包括 3：

本地/内存中: Chroma, FAISS, InMemoryVectorStore。
云托管: Pinecone, Weaviate, Milvus, Redis, Elasticsearch等。
自托管数据库: PostgreSQL (with pgvector), OpenSearch等。


向量存储通常提供基于不同相似性度量（如余弦相似度、欧氏距离）的查询方法，以及更高级的检索策略如最大边际相关性（MMR）15。



检索器 (Retrievers)：

检索器是一个更通用的接口，负责根据查询（通常是字符串）返回相关的Document对象列表 3。
向量存储本身可以通过as_retriever()方法轻松地用作检索器 15。
Langchain的检索器接口非常简单，只需要实现_get_relevant_documents方法 21。
除了基于向量存储的检索器，Langchain还支持其他类型的检索器，例如：

上下文压缩检索器 (ContextualCompressionRetriever): 在检索后进一步处理文档，例如过滤掉不相关的部分或使用LLM总结相关信息。
多查询检索器 (MultiQueryRetriever): 使用LLM从用户原始查询生成多个不同角度的查询，分别执行检索，然后合并结果，以提高召回率。
父文档检索器 (ParentDocumentRetriever): 索引较小的子文档块，但在检索到相关的子块时，返回其原始的、较大的父文档，以提供更完整的上下文 21。
自查询检索器 (SelfQueryRetriever): 使用LLM将自然语言查询转换为结构化查询，该查询可以包含对文档元数据的过滤条件，从而实现更精确的检索。
集成检索器 (EnsembleRetriever): 组合多个不同检索器（如BM25稀疏检索器和向量存储稠密检索器）的结果，并根据权重进行排序，以结合不同检索方法的优势 21。


检索器是Langchain可运行对象（Runnable），可以轻松地集成到LCEL链中 21。


核心观点 3.4.1: 文档加载器和文本分割器是任何依赖外部知识的Langchain应用（尤其是RAG系统）中数据预处理流程的基石，它们共同确保了异构的外部数据能够被有效地 ingest（摄入）并转化为适合LLM高效处理和精确检索的标准化、小块化格式。现实世界中的知识往往以多种格式（PDF、网页、数据库记录等）和不同长度存在 3。文档加载器通过提供统一的接口来读取这些多样化的数据源，并将其转换为Langchain内部标准的Document对象 3。然而，原始文档（尤其是长文档）往往超出LLM的上下文窗口限制，且直接对其进行嵌入和检索效率低下且效果不佳。因此，文本分割器接踵而至，通过智能地将长文档切分为语义连贯且大小适中的文本块，为后续的嵌入和向量检索步骤奠定了关键基础，直接影响最终应用的性能和准确性 3。核心观点 3.5.1: 文本嵌入模型在Langchain中扮演着语义桥梁的角色，它们通过将文本信息转化为高维向量空间中的点，使得机器能够以数值化的方式理解和比较文本的深层含义，这是实现高级功能如语义搜索、内容推荐和检索增强生成的关键技术支撑。传统的关键词匹配方法难以捕捉同义词、近义词或更复杂的语义关系。嵌入模型，如Langchain集成的OpenAIEmbeddings或HuggingFaceEmbeddings等 3，通过在大量文本数据上训练，学习到了词语和句子之间的复杂语义关联。当文本被转换为嵌入向量后，语义上相似的文本在向量空间中会更加接近 15。这使得Langchain应用能够超越字面匹配，执行基于“意义”的检索，例如，用户查询“关于猫的有趣故事”时，系统能够找到包含“小猫的奇妙冒险”的文档，即使它们没有共享完全相同的词语。这种语义理解能力是构建更智能、更自然的语言应用程序的基础。核心观点 3.6.1: 向量存储在Langchain生态中并非仅仅是传统意义上的数据存储库，它们是专门为高效管理和查询海量文本嵌入而优化的引擎，构成了大多数检索增强生成（RAG）应用的检索核心，通过快速定位与用户查询语义最相关的上下文信息，为LLM提供高质量的“燃料”。当文档被加载、分割并转换为嵌入向量后，这些高维向量需要一个能够支持快速相似性搜索的存储系统 3。向量存储（如Chroma, FAISS, Pinecone等）正是为此而生，它们使用特殊的索引结构（如ANN近似最近邻算法）来加速在高维空间中的搜索过程 21。当用户提出查询时，查询本身也被转换为嵌入向量，向量存储则迅速返回与之最相似的文档块嵌入及其对应的原始文本块 15。这个过程的效率和准确性直接决定了RAG系统能否及时提供相关、准确的上下文信息给LLM，从而生成高质量的、基于事实的回答，而不是依赖模型自身的参数化知识（这可能过时或不准确）1。因此，选择和配置合适的向量存储是构建高性能RAG应用的关键一步。3.4 链 (Chains): LCEL, 顺序链, 自定义链链（Chains）是Langchain的核心概念之一，代表了一系列对组件（如LLM、工具、提示模板等）的调用，这些调用以特定的顺序组织起来，以完成一个更复杂的任务 1。链使得将多个步骤组合成一个连贯的工作流变得简单。

LangChain表达式语言 (LCEL - LangChain Expression Language)：

LCEL是Langchain推荐的用于构建链的声明式方式 22。它允许开发者通过组合现有的可运行对象（Runnables）来创建新的链。
核心思想：描述“想要发生什么”，而不是“如何发生”，Langchain会优化运行时的执行 22。
可运行对象 (Runnable)：LCEL中的所有组件（模型、提示、解析器、检索器等）都实现了Runnable接口，该接口定义了标准的方法，如invoke, batch, stream, ainvoke等 9。这使得它们可以被无缝地组合。
组合原语：

管道操作符 (|) 或 .pipe()方法: 将一个Runnable的输出作为下一个Runnable的输入，形成顺序序列 22。
Python# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# prompt = ChatPromptTemplate.from_template("告诉我一个关于{topic}的笑话")
# model = ChatOpenAI()
# output_parser = StrOutputParser()
# chain = prompt | model | output_parser


RunnableSequence: 显式地定义一个顺序执行的Runnable序列 22。
RunnableParallel: 并行地执行多个Runnable，并将它们的输出收集到一个字典中。输入会同时传递给所有并行的Runnable 22。
Python# from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# chain = RunnableParallel(
#     passed_through_input=RunnablePassthrough(),
#     processed_text=prompt | model | output_parser
# )


RunnableLambda: 将任意Python函数包装成一个Runnable 22。


LCEL的优势 9：

优化的并行执行: 可以使用RunnableParallel并行运行Runnable，或使用Runnable Batch API并行处理多个输入，显著减少延迟。
异步支持: 任何用LCEL构建的链都可以通过Runnable Async API异步运行。
流式处理: LCEL链支持流式输出，允许逐步返回结果，优化首个token的响应时间。
可配置性: 可以通过RunnableConfig传递运行时信息（如标签、回调、最大并发数）。
可观测性: 与LangSmith等工具集成良好，便于追踪和调试。
组件化: 易于组合和重用。


虽然LCEL可以构建包含数百个步骤的链，但对于具有分支、循环、多智能体等更复杂的编排任务，推荐使用LangGraph 23。LCEL仍然可以在LangGraph的单个节点内使用。



顺序链 (Sequential Chains - Legacy)：

在LCEL广泛应用之前，Langchain提供了如SequentialChain这样的类来按顺序连接多个链 24。
SequentialChain将一个链的输出直接作为下一个链的输入 25。
它需要明确定义输入变量、输出变量以及包含的链列表 25。
虽然仍然可用，但对于新的开发，推荐使用LCEL，因为它提供了更灵活和强大的组合方式，并且与Langchain的现代特性（如流式处理、异步）结合得更好。



自定义链 (Custom Chains - Legacy)：

开发者可以通过继承Langchain的Chain基类并实现其_call（同步）或_acall（异步）方法来创建自定义链 24。
这允许实现更复杂的、LCEL可能不易直接表达的逻辑。
在自定义链中，需要手动管理输入和输出键。
同样，对于新项目，应优先考虑是否能用LCEL或LangGraph实现，因为它们提供了更好的可维护性和与生态系统的集成。


核心观点 3.7.1: LCEL不仅仅是一种更简洁的链构建语法糖；它是一种强大的声明式编程范式，它使得Langchain能够对链的执行进行深度优化，并为所有Langchain组件提供了一个一致且可组合的接口。这种范式从根本上改变了链的构建和运行方式，使得复杂的工作流编排变得更加易于管理和高效。传统的链构建方式（如继承Chain类）是命令式的，开发者需要详细指定每一步如何执行 24。相比之下，LCEL允许开发者通过组合Runnable对象来描述期望的计算流程，而将具体的执行细节（如并行化、异步处理、流式传输、批处理等）交给Langchain框架去优化 22。由于Langchain中几乎所有核心组件（模型、提示模板、输出解析器、检索器等）都实现了Runnable接口，它们可以像积木一样无缝地拼接在一起，形成强大的处理流水线。这种从命令式到声明式的转变，不仅使代码更简洁、更易读，更重要的是它解锁了Langchain内部的执行优化能力，从而提升了应用的性能和响应速度。3.5 记忆 (Memory): 记住对话记忆（Memory）组件使Langchain应用（尤其是链和智能体）能够记住先前的交互信息，从而在多轮对话中保持上下文连贯性，并做出更相关的响应 1。LLM本身是无状态的，每次调用都是独立的，因此必须通过外部机制显式地管理和提供记忆 4。

记忆的目的：

在聊天机器人中保持对话的上下文。
为智能体提供先前步骤的信息，以便做出后续决策。
个性化用户体验。



Langchain提供的记忆类型：

ConversationBufferMemory: 将所有先前的消息存储在一个缓冲区中，并在每次调用时将整个缓冲区（或其一部分）传递给提示 7。这是最简单的记忆类型。
ConversationBufferWindowMemory: 只保留最近N轮对话的消息，形成一个滑动窗口，以防止上下文过长超出LLM的限制 3。
ConversationSummaryMemory: 使用一个LLM来动态地将对话历史总结成一个简短的摘要，并将此摘要包含在提示中。适用于非常长的对话 3。
ConversationSummaryBufferMemory: 结合了ConversationBufferMemory和ConversationSummaryMemory的优点。它在内存中保留最近的一些消息，同时对更早的消息进行总结。当缓冲区的消息长度超过一定限制时，会将旧消息转换为摘要。
VectorStoreRetrieverMemory: 将对话历史（或其嵌入）存储在向量存储中。在生成响应时，检索与当前输入最相关的历史片段作为上下文。
知识图谱记忆 (Knowledge Graph Memory): 例如，FalkorDBChatMessageHistory可以将聊天消息历史存储在像FalkorDB这样的图数据库中，从而能够利用图的结构来理解和检索复杂的对话关系 4。
还有其他特定用途的记忆类型，如ChatMessageHistory的各种后端实现（文件、Redis等）。



在链和智能体中集成记忆：

通常，记忆组件会暴露特定的输入/输出键（例如，history或chat_history），这些键需要在提示模板中通过MessagesPlaceholder或相应的变量占位符来引用 7。
当链或智能体执行时，它会从记忆组件中加载相关历史，将其注入提示，然后将当前的交互结果保存回记忆组件。
LCEL使得将记忆集成到链中更为灵活。



智能体记忆 (Agentic Memory) 26：

过程记忆 (Procedural Memory): 指智能体如何执行任务的核心逻辑，可以看作是LLM的权重和智能体代码的组合。在实践中，这可能表现为智能体更新其系统提示的能力。
语义记忆 (Semantic Memory): 指智能体关于世界的长期知识存储。在实践中，这通常通过LLM从对话或交互中提取信息，然后将这些信息存储起来（例如，在向量数据库或知识图谱中），以便在未来的交互中检索并用于个性化响应或改进决策。



示例：在LCEL链中添加ConversationBufferMemory：
Python# from langchain_openai import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.runnables import RunnablePassthrough

# llm = ChatOpenAI()
# memory = ConversationBufferMemory(return_messages=True, memory_key="chat_history")
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你是一个乐于助人的聊天机器人。"),
#     MessagesPlaceholder(variable_name="chat_history"),
#     ("user", "{input}")
# ])

# def load_memory(inputs):
#     return memory.load_memory_variables({})["chat_history"]

# conversational_chain = (
#     RunnablePassthrough.assign(chat_history=load_memory) # 加载记忆
# | prompt
# | llm
# )

# def invoke_chain(input_text):
#     response = conversational_chain.invoke({"input": input_text})
#     memory.save_context({"input": input_text}, {"output": response.content}) # 保存记忆
#     return response.content

# print(invoke_chain("你好，我叫小明。"))
# print(invoke_chain("我叫什么名字？"))


核心观点 3.8.1: Langchain提供了一个从简单到复杂的记忆解决方案谱系，从基础的对话缓冲区到由LLM驱动的智能摘要，再到与外部知识库（如图数据库）的深度集成，这充分反映了现代会话式AI应用在管理短期和长期上下文方面的多样化需求。简单的聊天应用可能只需要记住最近几轮对话，此时ConversationBufferMemory或ConversationBufferWindowMemory就能胜任 7。然而，当对话变得冗长，超出了LLM的上下文窗口限制时，就需要更智能的策略，如ConversationSummaryMemory，它利用LLM自身的能力来提炼对话精髓 3。对于需要智能体在多次、跨会话的交互中回忆特定事实、用户偏好或过往经验的复杂场景，则需要更持久化、结构化的记忆存储方案，例如将记忆嵌入向量数据库进行语义检索，或利用图数据库（如FalkorDB 4）来捕捉和利用对话中更深层次的关系和背景。Langchain对过程记忆和语义记忆的区分 26，进一步指明了构建更接近人类学习和适应能力的智能体的方向。Langchain多样化的记忆组件正是为了满足这一完整谱系的需求而设计的。3.6 工具 (Tools): 扩展LLM能力工具（Tools）是Langchain中赋予LLM与外部世界交互、执行具体操作或获取模型自身知识库之外信息的功能性组件 3。LLM本身是基于其训练数据生成文本，无法直接执行如网络搜索、数据库查询、代码运行等任务。工具弥补了这一缺陷，使智能体能够调用这些功能。

工具的构成：

名称 (Name): 工具的唯一标识符。
描述 (Description): 对工具功能的自然语言描述。这对于LLM（尤其是智能体中的LLM）理解何时以及如何使用该工具至关重要。描述需要清晰、准确地说明工具的作用、输入和输出。
参数模式 (Argument Schema): 定义工具接受的输入参数的结构和类型，通常使用Pydantic模型或JSON Schema来指定。
执行逻辑 (Implementation): 工具实际执行其功能的代码。



使用预构建工具：

Langchain提供了一个包含数百个预构建工具的庞大库，涵盖了各种常见任务 3。这些工具可以直接在智能体或链中使用。
常见类别包括 27：

搜索工具: GoogleSearchRun, DuckDuckGoSearchRun, ArxivQueryRun, BingSearchRun, TavilySearchResults等，用于从网络获取信息。
数据库工具: SQLDatabaseTool (或 QuerySQLDataBaseTool, InfoSQLDatabaseTool, ListSQLDatabaseTool, QuerySQLCheckerTool 组合)，用于与SQL数据库交互。
代码执行工具: PythonREPLTool (用于执行Python代码), ShellTool (用于执行shell命令，需谨慎使用)。
API交互工具: 用于调用各种第三方API，如Gmail, GitHub, Jira, Office365, 天气API等。
文件系统工具: 用于读写本地文件。
计算工具: 如计算器。
“Human-in-the-loop”工具: 允许智能体在需要时请求人类输入或批准。


示例：使用DuckDuckGoSearchRun工具进行网络搜索。
Python# from langchain_community.tools import DuckDuckGoSearchRun
# search = DuckDuckGoSearchRun()
# result = search.run("Langchain是什么？")
# print(result)





创建自定义工具：

当预构建工具不满足特定需求时，可以轻松创建自定义工具。
使用@tool装饰器: 这是创建自定义工具最简单的方法。只需用@tool装饰一个Python函数，Langchain会自动将其转换为一个工具。函数的docstring将用作工具的描述，类型注解将用于推断参数模式 9。
Python# from langchain_core.tools import tool

# @tool
# def multiply(a: int, b: int) -> int:
#     """计算两个整数的乘积。"""
#     return a * b

# print(multiply.name)
# print(multiply.description)
# print(multiply.args)
# print(multiply.invoke({"a": 4, "b": 5}))


继承BaseTool类: 对于更复杂的工具，可以继承BaseTool类并实现其_run（同步）和_arun（异步）方法，同时定义name, description, 和 args_schema (Pydantic模型)。



表3.6.1: Langchain常用工具选介

工具名称 (Langchain Class/Function)类别简要描述DuckDuckGoSearchRun搜索执行DuckDuckGo搜索并返回结果摘要。TavilySearchResults搜索使用Tavily搜索引擎进行高级搜索，可返回结构化结果。ArxivAPIWrapper / ArxivQueryRun学术搜索从arXiv.org检索学术论文。PythonREPLTool代码执行在Python REPL环境中执行Python代码片段。SQLDatabaseTool (or toolkit)数据库连接到SQL数据库并执行查询或获取模式信息。RequestsTools (e.g., RequestsGetTool)API交互发送HTTP请求 (GET, POST等) 到指定URL。FileSystemTool (or toolkit)文件操作读、写、列出本地文件系统中的文件和目录。LLMMathChain (as a tool)计算使用LLM进行数学计算。HumanInputRun人机交互允许智能体在执行过程中请求人类输入。*选择这些工具是为了展示Langchain工具的多样性和覆盖范围，从信息获取到代码执行再到与外部系统交互。实际可用的工具远不止这些，开发者应查阅官方文档以获取完整列表和具体用法。*
核心观点 3.9.1: 工具是Langchain智能体克服大型语言模型固有局限性（如知识截止日期、无法执行实时操作或与外部环境交互）的核心机制，它们将LLM从被动的文本生成器转变为能够主动解决问题、获取新信息并执行任务的“行动者”。LLM本身被其训练数据所限制，无法感知当前世界状态或直接操作外部系统 1。工具通过提供明确定义的接口（如网络搜索、数据库查询、代码执行、API调用等），使得LLM能够“委托”这些超出其自身能力范围的任务给专门的外部函数或服务 3。智能体中的LLM根据当前任务需求和工具的描述来决定调用哪个工具以及如何调用 28。这种将LLM的推理能力与外部工具的执行能力相结合的模式，极大地扩展了LLM应用的潜能和实用性。Langchain庞大的预构建工具生态系统以及创建自定义工具的便捷性，是其赋能强大智能体开发的关键所在。3.7 智能体 (Agents): 自主决策者智能体（Agents）是Langchain中一种更高级的抽象，它们利用LLM作为“大脑”或“推理引擎”，来决定采取一系列操作以达成目标 3。与链（Chains）通常执行预定义好的步骤序列不同，智能体可以动态地选择下一步操作，通常涉及到调用一个或多个工具。

智能体的工作原理：

接收输入: 智能体接收用户输入（查询或指令）。
思考与规划 (Thought/Reasoning): LLM分析输入、可用的工具集（及其描述）、以及之前的操作历史（如果适用）。
决策 (Action Decision): LLM决定下一步是：

调用一个特定的工具，并提供该工具所需的参数。
还是直接给出最终答案。


执行操作 (Action Execution): 如果LLM决定调用工具，智能体框架会执行该工具。
获取观察结果 (Observation): 工具执行后返回一个结果（观察）。
迭代: 观察结果会连同之前的步骤一起反馈给LLM，LLM再次进行思考、规划和决策。这个“思考-行动-观察”的循环会一直持续，直到LLM认为任务已完成并给出最终答案，或者达到某个停止条件（如最大迭代次数）。



智能体的关键组成：

LLM/Chat Model: 作为智能体的核心推理引擎。
工具 (Tools): 智能体可以调用的外部功能。
提示模板 (Prompt Template): 用于指导LLM如何思考、如何选择工具、如何格式化其输出（行动或最终答案）的特定提示。
智能体执行器 (Agent Executor): 负责实际运行智能体循环的运行时环境，它管理LLM的调用、工具的执行以及状态的传递。



常见的智能体类型/架构 (简述)：

ReAct (Reasoning and Acting): 这是一种流行的智能体框架，LLM通过生成“思考”（Thought）步骤来阐述其推理过程，然后决定采取“行动”（Action）调用工具，或给出“最终答案”（Final Answer）28。提示中会包含如何进行思考和行动的指令。
OpenAI Functions/Tools Agents: 利用支持函数调用或工具调用的LLM（如OpenAI的GPT模型）。LLM可以直接在其响应中指定要调用的函数及其参数，而不是通过解析文本输出来确定行动 3。这通常更可靠。Langchain提供了如create_openai_tools_agent这样的构造器来简化这类智能体的创建。
Plan-and-Execute Agents: 这类智能体首先由LLM制定一个详细的计划（一系列步骤），然后逐个执行这些步骤，可能每个步骤都由一个子智能体或工具完成 28。
Self-Ask with Search: 智能体通过迭代地向自己提问（并使用搜索工具寻找答案）来分解复杂问题。



构建一个简单的智能体：

定义工具集: 创建或选择一组智能体可以使用的工具。
选择LLM: 选择一个适合用作智能体推理引擎的LLM（例如，支持工具调用的ChatOpenAI模型）。
创建智能体逻辑: 使用Langchain提供的构造函数（如create_openai_tools_agent）或更底层的组件来定义智能体的核心逻辑（通常是一个提示模板和LLM的组合）。
实例化智能体执行器 (AgentExecutor): 将智能体逻辑和工具集传递给AgentExecutor。
运行智能体: 调用AgentExecutor的invoke方法并传入用户输入。



示例：一个使用搜索工具和计算器工具的智能体
Python# from langchain_openai import ChatOpenAI
# from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun
# from langchain.agents import AgentExecutor, create_openai_tools_agent
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# tools =

# # 智能体的核心提示，告诉它如何行为，以及如何使用工具
# prompt = ChatPromptTemplate.from_messages()

# agent = create_openai_tools_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = agent_executor.invoke({
#     "input": "Langchain的创始人是谁？他还在哪些知名项目中工作过？"
# })
# print(response["output"])


核心观点 3.10.1: 智能体代表了Langchain应用开发中的一个重要范式转变，即从开发者预先定义固定的执行流程（如链）转向由LLM自身在运行时动态编排其工作流，通过战略性地选择和使用工具来达成目标，从而展现出更强的自主性和适应性。传统的链，即使是使用LCEL构建的复杂链，其操作顺序和逻辑分支通常也是由开发者在设计阶段确定的 23。而智能体则将LLM置于“驾驶位” 3，LLM基于当前的用户输入、可用的工具集以及（可能的）过往交互历史，来决定下一步应该调用哪个工具、传递什么参数，或者是否已经可以给出最终答案。这种动态决策过程，通常伴随着LLM内部的“思考”或“推理”步骤（例如ReAct框架中的“Thought”），使得智能体能够处理那些解决方案路径并非事先已知的、更为复杂和开放式的多步骤问题 28。LangGraph的出现进一步扩展了这种能力，允许开发者构建和管理更为复杂、包含循环和持久状态的智能体架构 28，标志着向更高级自主AI系统的迈进。3.8 回调 (Callbacks): 监控内部工作回调（Callbacks）机制为Langchain应用提供了一个强大的钩子系统，允许开发者在LLM应用执行的各个阶段注入自定义代码，以实现日志记录、监控、流式处理、调试以及其他自定义行为 3。

回调的目的 30：

日志记录与调试: 追踪链、智能体、LLM和工具的执行流程，记录输入、输出和中间步骤，帮助诊断问题。
性能监控: 测量各组件的执行时间、token使用量、API调用成本等，以优化应用性能和成本。
流式处理: 例如，在LLM生成新token时立即将其流式传输到用户界面。
事件驱动的触发器: 根据特定事件（如工具调用失败、链执行结束）触发自定义操作（如发送通知、保存数据）。
与外部系统集成: 将Langchain应用的执行事件发送到外部监控平台（如LangSmith）。



回调处理器 (Callback Handlers)：

回调逻辑封装在回调处理器中。Langchain提供了同步（BaseCallbackHandler）和异步（AsyncCallbackHandler）两种处理器基类 31。
开发者通过继承这些基类并重写特定的事件方法来创建自定义处理器。
关键事件方法包括 31（详见下表）：

on_llm_start, on_llm_new_token, on_llm_end, on_llm_error
on_chat_model_start
on_chain_start, on_chain_end, on_chain_error
on_tool_start, on_tool_end, on_tool_error
on_agent_action, on_agent_finish
on_retriever_start, on_retriever_end, on_retriever_error
on_text (用于任意文本处理)
on_retry (用于重试事件)





内置回调处理器：

StdOutCallbackHandler: 将所有事件的详细信息打印到标准输出（控制台），非常适合快速调试和观察执行流程 30。
LangSmith的追踪功能在底层严重依赖回调机制来捕获执行数据。



创建自定义回调处理器 30：
Python# from langchain_core.callbacks.base import BaseCallbackHandler
# from typing import Any, Dict, List, Union
# from langchain_core.messages import BaseMessage
# from langchain_core.outputs import LLMResult

# class MyCustomHandler(BaseCallbackHandler):
#     def on_llm_start(self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any) -> None:
#         print(f"LLM 开始执行，输入提示: {prompts}")

#     def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
#         print(f"LLM 生成新 Token: {token}")

#     def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
#         print(f"LLM 执行结束，输出: {response.generations.text[:50]}...")

#     def on_chain_start(self, serialized: Dict[str, Any], inputs: Dict[str, Any], **kwargs: Any) -> None:
#         print(f"链 {serialized.get('name', serialized.get('id', ['<unknown>']))} 开始执行，输入: {inputs}")

#     def on_chain_end(self, outputs: Dict[str, Any], **kwargs: Any) -> None:
#         print(f"链执行结束，输出: {outputs}")

#     def on_tool_start(self, serialized: Dict[str, Any], input_str: str, **kwargs: Any) -> None:
#         print(f"工具 {serialized.get('name')} 开始执行，输入: {input_str}")

#     def on_tool_end(self, output: str, **kwargs: Any) -> None:
#         print(f"工具执行结束，输出: {output}")



传递回调 31：

构造器回调 (Constructor Callbacks): 在创建Langchain对象（如LLM、链、工具）时，通过callbacks参数传入回调处理器列表。这些回调仅作用于该对象本身，不被其子对象继承。

llm = ChatOpenAI(callbacks=[MyCustomHandler()])


请求时回调 (Request-time Callbacks): 在调用Runnable对象的invoke, stream, batch等方法时，通过config参数中的"callbacks"键传入。这些回调会被传递给被调用对象及其所有子对象。

chain.invoke({"input": "你好"}, config={"callbacks": [MyCustomHandler()]})


注意: 在Python 3.10及更早版本中，如果自定义的RunnableLambda, RunnableGenerator或Tool异步调用其他Runnable，需要手动将请求时回调传播给子对象 31。



表3.8.1: Langchain关键回调事件

事件名称 (Event Name)触发描述 (Trigger Description)处理器中对应的方法 (Associated Method)llm_startLLM（或聊天模型）开始处理提示。on_llm_startchat_model_start聊天模型开始处理消息。on_chat_model_startllm_new_tokenLLM（或聊天模型）生成一个新的token（用于流式处理）。on_llm_new_tokenllm_endLLM（或聊天模型）完成响应生成。on_llm_endllm_errorLLM（或聊天模型）执行过程中发生错误。on_llm_errorchain_start链开始执行。on_chain_startchain_end链执行结束。on_chain_endchain_error链执行过程中发生错误。on_chain_errortool_start工具开始执行。on_tool_starttool_end工具执行结束。on_tool_endtool_error工具执行过程中发生错误。on_tool_erroragent_action智能体决定执行一个动作（通常是调用工具）。on_agent_actionagent_finish智能体完成执行并返回最终答案。on_agent_finishretriever_start检索器开始检索文档。on_retriever_startretriever_end检索器完成文档检索。on_retriever_endretriever_error检索器执行过程中发生错误。on_retriever_error*此表总结了Langchain中最常用和关键的回调事件，帮助开发者理解何时以及如何通过实现相应的处理器方法来介入应用的执行流程。*
核心观点 3.11.1: Langchain的回调系统为开发者提供了对应用执行生命周期的细粒度观测能力和控制点，这对于构建健壮的监控、深入的调试以及实时的交互功能至关重要，并且是LangSmith等可观测性平台实现其强大追踪功能的基础。LLM应用，尤其是那些包含多个链、工具调用和复杂逻辑的智能体应用，其内部运作往往像一个“黑箱”，难以追踪问题或理解其行为 30。回调机制通过在几乎每一个关键执行节点（如LLM调用、链的开始与结束、工具的使用等）设置“钩子”，允许开发者精确地捕获中间数据、记录性能指标（如on_llm_start和on_llm_end可用于计时）、实现逐字流式输出（通过on_llm_new_token事件 31），甚至在运行时动态调整行为。这种深度的内省能力不仅是调试复杂错误的必要条件（正如LangSmith严重依赖回调来收集追踪数据所证明的那样 3），也是创建如实时聊天界面、进度更新等丰富用户体验的关键。模块三：Langchain应用实战本模块将通过构建几个常见的端到端应用案例，展示如何综合运用Langchain的各项核心组件来解决实际问题。这些案例将帮助学习者巩固理论知识，并掌握将Langchain应用于不同场景的实践技能。第四章：构建实际应用4.1 文档问答 (RAG - 检索增强生成)检索增强生成（RAG）是一种强大的技术，它将LLM的生成能力与外部知识库的检索能力相结合，以生成更准确、更具上下文、且基于特定文档内容的回答。Langchain为构建RAG应用提供了完整的组件支持。完整的RAG流程：

加载文档 (Load Documents)：

首先，需要从各种来源（如PDF文件、网页、数据库等）加载目标文档。Langchain的DocumentLoader组件负责此任务 3。
常用的加载器包括PyPDFLoader (用于PDF), WebBaseLoader (用于网页), CSVLoader (用于CSV文件)等 3。
加载后，文档内容通常被转换为Langchain标准的Document对象，其中包含page_content和metadata 20。
示例：
Python# from langchain_community.document_loaders import PyPDFLoader
# loader = PyPDFLoader("example.pdf")
# documents = loader.load()





分割文本 (Split Text)：

由于LLM的上下文窗口有限，且为了提高检索效率和精度，长文档需要被分割成较小的文本块（chunks）3。
使用TextSplitter组件，如RecursiveCharacterTextSplitter，它会尝试按语义上有意义的边界（如段落、句子）进行分割，并可以设置块之间的重叠（chunk_overlap）以保留上下文 3。
示例：
Python# from langchain_text_splitters import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# splits = text_splitter.split_documents(documents)





创建嵌入 (Create Embeddings)：

将分割后的文本块转换为数值向量（嵌入），以便进行语义相似性比较。使用EmbeddingModel完成此任务 3。
常用的嵌入模型包括OpenAI的OpenAIEmbeddings，或Hugging Face提供的各种开源模型。
示例：
Python# from langchain_openai import OpenAIEmbeddings
# embeddings = OpenAIEmbeddings()





存入向量存储 (Store in Vector Store)：

将生成的文本块嵌入存储到向量数据库中。向量存储支持高效的相似性搜索 3。
Langchain集成了多种向量存储，如Chroma, FAISS, Pinecone等 15。
示例：
Python# from langchain_community.vectorstores import Chroma
# vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)





创建检索器 (Create Retriever)：

从向量存储创建一个检索器对象，该对象负责根据用户查询检索相关的文档块 3。
通常通过调用向量存储的as_retriever()方法来创建 15。可以配置检索参数，如返回的文档数量（k）或检索类型（如similarity或mmr）。
示例：
Python# retriever = vectorstore.as_retriever(search_kwargs={"k": 3})





创建提示模板 (Create Prompt Template)：

设计一个提示模板，该模板将包含两个关键的输入变量：context（由检索器提供的相关文档内容）和question（用户的原始问题）。
提示应指导LLM基于提供的上下文来回答问题。
示例：
Python# from langchain_core.prompts import ChatPromptTemplate
# prompt_template = """根据以下上下文信息回答问题：
# 上下文：{context}
# 问题：{question}
# 回答："""
# prompt = ChatPromptTemplate.from_template(prompt_template)





创建并执行链 (Create and Execute Chain)：

使用LangChain表达式语言（LCEL）将检索器、提示模板、LLM和输出解析器组合成一个RAG链 32。
RunnableParallel用于并行获取上下文和传递问题。
示例：
Python# from langchain_openai import ChatOpenAI
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser

# llm = ChatOpenAI(model_name="gpt-3.5-turbo")
# output_parser = StrOutputParser()

# # 定义如何从检索结果格式化上下文
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# rag_chain_from_docs = (
#     RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
# | prompt
# | llm
# | output_parser
# )

# rag_chain_with_source = RunnableParallel(
#     {"context": retriever, "question": RunnablePassthrough()}
# ).assign(answer=rag_chain_from_docs)

# # 调用链
# question = "Langchain中的Agent是什么？"
# result = rag_chain_with_source.invoke(question)
# print(f"问题: {question}")
# print(f"答案: {result['answer']}")
# print(f"来源文档数量: {len(result['context'])}")





变体：对话式RAG (Conversational RAG)：

为了支持多轮问答，可以将聊天历史（Memory）集成到RAG链中 3。
这通常涉及到修改提示模板以包含聊天历史（例如，使用MessagesPlaceholder），并创建一个能够感知历史的检索器（create_history_aware_retriever），该检索器会根据当前问题和聊天历史生成一个更适合检索的独立查询 32。
然后，将检索到的上下文、原始问题和聊天历史一起传递给LLM以生成答案。


Langchain的RAG实现示例还包括针对代码库的问答（RAG over code）和结合聊天历史的RAG 2。核心观点 4.1.1: RAG是Langchain框架的一个基石级应用，它完美地展示了如何通过将LLM的强大生成能力与外部的、可控的知识源相结合，来构建出既能理解复杂查询又能提供准确、有据可查答案的智能系统。LLM本身虽然知识渊博，但其知识库存在截止日期，且有时会产生不准确或完全虚构的信息（即“幻觉”）1。RAG通过在LLM生成答案之前，先从指定的文档集合（如公司内部文档、特定领域的知识库等）中检索出与用户问题最相关的片段，并将这些片段作为上下文信息提供给LLM，从而有效地缓解了这些问题 2。Langchain提供了一整套模块化的组件——文档加载器、文本分割器、嵌入模型、向量存储和检索器——它们恰好构成了实现RAG流程中“检索”部分所需的所有关键部件 3。随后，通过LCEL，开发者可以轻松地将这些检索组件与提示模板、LLM以及输出解析器串联起来，形成一个高效的端到端RAG流水线。Langchain文档和社区中RAG应用的普遍性（如2中的例子）也从侧面印证了其在LLM应用开发中的核心地位和巨大价值。4.2 构建对话式聊天机器人对话式聊天机器人是LLM最广泛的应用之一。Langchain提供了构建功能丰富、能够进行上下文感知对话的聊天机器人的工具和模式。

核心组件：

LLM/聊天模型 (Chat Model): 负责理解用户输入并生成回复。如ChatOpenAI。
提示模板 (Prompt Template): 结构化与模型的交互，通常包含系统消息、聊天历史占位符和当前用户输入。ChatPromptTemplate和MessagesPlaceholder是关键 16。
记忆 (Memory): 存储和管理对话历史，使机器人能够“记住”之前的对话内容，从而进行连贯的多轮交流 3。如ConversationBufferMemory。
（可选）检索器 (Retriever): 如果机器人需要基于特定文档或知识库回答问题（即RAG功能），则需要集成检索器 33。



管理聊天历史：

使用MessagesPlaceholder(variable_name="chat_history")在ChatPromptTemplate中为聊天历史指定一个位置。
将一个Memory对象（如ConversationBufferMemory，设置return_messages=True）集成到链中。该记忆对象负责在每次交互后保存新的用户输入和模型回复，并在下次交互前加载历史记录。
对于非常长的对话，可以考虑使用ConversationSummaryMemory或ConversationSummaryBufferMemory来避免超出LLM的上下文窗口限制 3。



上下文感知的响应：

通过将聊天历史注入提示，LLM能够理解当前用户输入的上下文，并生成更相关、更自然的回复 33。
如果集成了RAG，机器人不仅能利用对话历史，还能利用从外部文档检索到的信息来回答问题，使其知识更丰富、回答更准确。



示例：一个带记忆的简单聊天机器人
Python# from langchain_openai import ChatOpenAI
# from langchain.memory import ConversationBufferMemory
# from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser

# # 1. 初始化LLM和记忆组件
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# # 2. 创建提示模板，包含聊天历史和当前输入
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你是一个友好且乐于助人的聊天机器人。"),
#     MessagesPlaceholder(variable_name="chat_history"),
#     ("user", "{input}")
# ])

# # 3. 创建LCEL链
# #    - RunnablePassthrough.assign将记忆加载的聊天历史添加到链的输入中
# #    - 然后传递给提示模板，再到LLM，最后通过输出解析器
# chain = (
#     RunnablePassthrough.assign(
#         chat_history=lambda x: memory.load_memory_variables(x)["chat_history"]
#     )
# | prompt
# | llm
# | StrOutputParser()
# )

# # 4. 定义交互函数
# def chat(user_input):
#     # 调用链获取回复
#     response = chain.invoke({"input": user_input})
#     # 将当前的用户输入和模型回复保存到记忆中
#     memory.save_context({"input": user_input}, {"output": response})
#     return response

# # 5. 进行对话
# print("机器人: 你好！有什么可以帮你的吗？")
# while True:
#     user_message = input("你: ")
#     if user_message.lower() in ["再见", "退出"]:
#         print("机器人: 再见！")
#         break
#     bot_response = chat(user_message)
#     print(f"机器人: {bot_response}")

在这个例子中，ConversationBufferMemory存储了对话的完整历史。每次调用chain.invoke时，通过RunnablePassthrough.assign和lambda函数从memory中加载历史记录，并将其与当前用户输入一起传递给提示模板。LLM根据这些信息生成回复。然后，memory.save_context将新的交互（用户输入和机器人回复）保存起来，供后续轮次使用。


结合RAG的聊天机器人：

可以进一步扩展上述机器人，使其能够从文档中检索信息来回答问题。这通常需要构建一个更复杂的链，其中包含一个历史感知检索器（history-aware retriever）和一个结合了检索上下文、聊天历史和用户问题的提示。Langchain的create_conversational_retrieval_chain是一个高级别的构造器，可以简化此类机器人的创建。


Langchain官方文档和社区提供了许多关于构建聊天机器人的指南和示例，包括如何处理更复杂的场景，如工具使用、多语言支持和高级对话管理策略 3。核心观点 4.2.1: 构建一个真正有效的对话式聊天机器人，其核心在于建立一个强大的记忆机制以维持对话的连贯性，并且通常需要借助检索增强生成（RAG）来使其回答基于事实、内容丰富且能响应特定知识领域的问题。仅仅依赖LLM的参数化知识进行多轮对话，很快会暴露出上下文理解不足和知识陈旧的问题 33。Langchain通过提供多样化的Memory组件（如ConversationBufferMemory, ConversationSummaryMemory等），使得开发者可以根据应用需求灵活地管理短期和长期对话历史 3。更进一步，将RAG流程集成到聊天机器人中——即在生成回复前先从外部知识库检索相关信息——能够显著提升机器人的知识水平和回答质量，使其能够就特定文档、产品或服务进行有深度的交流 33。Langchain的模块化设计使得将记忆管理和RAG功能顺畅地组合进一个统一的对话流程成为可能，从而赋能开发者构建出既能“记住”又能“查证”的智能聊天伙伴。4.3 文本摘要文本摘要是LLM的另一个重要应用场景，旨在将长篇文本精炼成简短、核心内容突出的摘要。Langchain提供了多种实现文本摘要的策略，以适应不同长度的文本和LLM的上下文窗口限制。

摘要技术：


填充 (Stuff)：

这是最简单直接的方法。它将所有待摘要的文档（或文本块）简单地连接起来，形成一个单一的、包含全部内容的上下文，然后将其传递给LLM，并要求LLM对这个完整的上下文进行摘要 3。
优点：实现简单，LLM一次性看到全部上下文，可能产生连贯性较好的摘要。
缺点：仅适用于总文本长度不超过LLM上下文窗口限制的情况。对于非常长的文档，此方法不可行。
Langchain中可以使用create_stuff_documents_chain来快速实现此方法 34。
示例提示可能类似于：“请对以下文本进行简洁的摘要：\n\n{context}” 34。



Map-Reduce：

这是一种更适合处理大量或非常长文档的策略。它分两步进行 3：

Map阶段：首先，将原始长文档分割成多个较小的文本块。然后，针对每一个文本块，独立地调用LLM生成一个该块的摘要。这个过程可以并行处理。
Reduce阶段：将Map阶段生成的所有小块摘要收集起来，然后再次调用LLM（可能使用不同的提示），对这些摘要进行合并和提炼，生成最终的、全局性的摘要。如果小块摘要的总长度仍然很长，Reduce阶段本身也可能需要迭代进行（例如，分批合并摘要，再对合并后的摘要进行摘要）。


优点：能够处理任意长度的文档，不受LLM上下文窗口的直接限制；Map阶段可以并行化，提高效率。
缺点：由于LLM在Map阶段只能看到局部信息，最终摘要的全局连贯性可能不如Stuff方法；实现相对复杂。
Langchain提供了MapReduceDocumentsChain来实现此策略，也可以使用LCEL或LangGraph构建更灵活的Map-Reduce工作流 34。
Map阶段的提示与Stuff类似，针对单个文档块。Reduce阶段的提示则类似于：“以下是一系列摘要：\n{docs}\n请将这些摘要提炼成一个最终的、统一的摘要，涵盖主要主题。” 34。



Refine (优化)：

这种策略迭代地处理文档块。首先，对第一个文档块生成一个初步摘要。然后，对于后续的每一个文档块，将其与前一个摘要一起传递给LLM，要求LLM根据新的文档块内容来优化和更新已有的摘要 3。
优点：可以处理长文档，并且每个优化步骤都能利用到之前已处理的信息。
缺点：处理过程是顺序的，无法并行化，可能比较耗时；摘要质量可能受到文档块顺序的影响。
Langchain提供了RefineDocumentsChain。





实现步骤（以Map-Reduce为例）：

加载和分割文档：使用DocumentLoader加载文档，然后使用TextSplitter（如CharacterTextSplitter.from_tiktoken_encoder）将其分割成适合LLM处理的块 34。
定义Map阶段的链: 创建一个LLMChain或LCEL链，用于对单个文档块生成摘要。
Python# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser

# llm = ChatOpenAI(temperature=0)
# map_prompt_template = "简要总结以下文本：\n\n{context}"
# map_prompt = ChatPromptTemplate.from_template(map_prompt_template)
# map_chain = map_prompt | llm | StrOutputParser()


定义Reduce阶段的链: 创建一个LLMChain或LCEL链，用于合并Map阶段生成的多个摘要。
Python# reduce_prompt_template = """以下是一系列摘要：
# {docs}
# 请将这些摘要提炼成一个最终的、统一的摘要，涵盖主要主题。
# 最终摘要："""
# reduce_prompt = ChatPromptTemplate.from_template(reduce_prompt_template)
# reduce_chain = reduce_prompt | llm | StrOutputParser()


组合Map和Reduce逻辑:

可以使用Langchain内置的MapReduceDocumentsChain。
或者使用LCEL和LangGraph构建自定义的Map-Reduce流程，这样可以更好地控制并行化、流式处理和错误处理 34。例如，在LangGraph中，可以将Map操作定义为一个节点，Reduce操作定义为另一个节点，并根据文档块的数量或摘要长度来决定是否需要迭代Reduce。





选择合适的策略：

如果文档较短，且LLM上下文窗口足够大，Stuff方法简单有效。
如果文档很长，或者需要处理大量文档，Map-Reduce是更可行的选择，尤其是在需要并行处理以提高效率时。
Refine方法提供了一种迭代构建摘要的方式，但其顺序性可能导致处理速度较慢。


Langchain通过这些不同的摘要链和构建块，为开发者提供了根据具体需求（如文本长度、LLM能力、性能要求）选择最合适摘要方案的灵活性。核心观点 4.3.1: Langchain通过提供如“Stuff”、“Map-Reduce”和“Refine”等多样化的文本摘要策略，展现了其在应对常见自然语言处理任务时，能够灵活适应不同文档长度和大型语言模型（LLM）上下文窗口限制的实用性与工程考量。直接将长文本“塞”给LLM进行摘要（Stuff方法）虽然简单，但很快会遇到LLM输入长度的瓶颈 34。为了解决这个问题，Langchain借鉴了分布式计算中的经典思想，引入了Map-Reduce策略：先将长文档分解为小块并独立摘要（Map），然后再将这些局部摘要汇总并融合成最终的全局摘要（Reduce）3。这种分而治之的方法有效地绕开了上下文窗口的限制，使得处理极长的文档成为可能。同时，Refine策略则提供了一种迭代式的摘要构建方式。Langchain不仅提供了这些策略的现成实现（如create_stuff_documents_chain, MapReduceDocumentsChain），还允许开发者通过LCEL或LangGraph等工具根据具体需求定制和优化这些摘要流程，体现了框架的灵活性和强大功能。4.4 Langchain数据生成除了处理和理解现有数据外，Langchain还可以被用来生成全新的、人工的（合成的）数据。这种合成数据在多种场景下都非常有用，例如测试、训练机器学习模型（特别是当真实数据稀缺或涉及隐私问题时）、扩充数据集、模拟特定场景等 35。

合成数据的益处 35：

隐私保护：无需使用真实的、可能包含敏感个人信息的数据。
数据扩增：为小型数据集生成更多样本，以改进模型训练。
灵活性与可控性：可以根据特定需求生成具有特定特征或分布的数据，甚至模拟罕见事件。
成本效益：通常比收集和标注真实数据更便宜、更快捷。
法规遵从：有助于在严格的数据保护法规下进行开发和测试。
模型鲁棒性：通过生成多样化的数据，可以训练出泛化能力更强的模型。
快速原型验证：在没有真实数据的情况下快速测试想法。



使用Langchain生成数据的流程：


定义输出模式 (Output Schema)：

明确你希望生成的合成数据应具有的结构和字段。使用Pydantic模型是Langchain中定义这种模式的推荐方式 35。Pydantic模型可以清晰地指定每个字段的名称和数据类型。
示例（生成演员及其电影列表的合成数据）：
Python# from typing import List
# from pydantic import BaseModel, Field

# class ActorFilms(BaseModel):
#     actor_name: str = Field(description="演员的名字")
#     films: List[str] = Field(description="该演员主演的电影名称列表")





提供少样本示例 (Few-shot Examples) (可选但推荐)：

向LLM提供一些符合期望输出格式和内容的示例，可以极大地提高生成数据的质量和一致性 35。这些示例作为LLM的“参照物”。
示例：
Python# examples = [
#     {"actor_name": "汤姆·汉克斯", "films": ["阿甘正传", "拯救大兵瑞恩", "绿里奇迹"]},
#     {"actor_name": "莱昂纳多·迪卡普里奥", "films": ["泰坦尼克号", "盗梦空间", "荒野猎人"]}
# ]





构建提示模板 (Prompt Template)：

设计一个提示模板，指示LLM如何根据输入信息（如果有）和少样本示例来生成符合Pydantic模式的数据。
可以使用FewShotPromptWithTemplates（如果Pydantic模型作为模板）或结合PydanticOutputParser的get_format_instructions()来指导LLM输出特定格式。
Langchain的实验性模块langchain_experimental.synthetic_data提供了一些专门用于合成数据生成的提示（如SYNTHETIC_FEW_SHOT_PREFIX, SYNTHETIC_FEW_SHOT_SUFFIX）和工具 35。



选择LLM并创建数据生成器/链：

选择一个合适的LLM（通常是具有较强指令遵循能力的模型）。
Langchain提供了如create_openai_data_generator (来自langchain_experimental) 或更通用的create_structured_output_runnable (结合Pydantic模型和LLM) 来创建数据生成逻辑。
DatasetGenerator (来自langchain_experimental) 也可以用于基于输入列表和偏好生成文本数据集 35。
示例（使用create_structured_output_runnable）：
Python# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.pydantic_utils import pydantic_to_json_schema

# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
# prompt_template_str = """请根据以下模式生成关于一位演员及其电影的数据。
# 如果提供了主题，请围绕该主题生成。
# 模式:
# {schema}

# 主题（可选）: {subject}
# ---
# 生成的数据:
# """
# prompt = ChatPromptTemplate.from_template(prompt_template_str)

# structured_llm = create_structured_output_runnable(ActorFilms, llm, prompt)
# # 或者直接使用LLM的.with_structured_output(ActorFilms) 方法 (如果模型支持)
# # structured_llm = llm.with_structured_output(ActorFilms)


# # 生成数据
# synthetic_data_point = structured_llm.invoke({
#     "schema": pydantic_to_json_schema(ActorFilms), # 或者直接传入ActorFilms
#     "subject": "一位擅长科幻片的中国女演员"
# })
# print(synthetic_data_point)

# # 批量生成
# inputs_for_generation = [
#     {"schema": pydantic_to_json_schema(ActorFilms), "subject": "一位获得过奥斯卡奖的喜剧演员"},
#     {"schema": pydantic_to_json_schema(ActorFilms), "subject": "一位90年代著名的动作明星"}
# ]
# synthetic_dataset = structured_llm.batch(inputs_for_generation)
# for item in synthetic_dataset:
#     print(item)

在较新版本的Langchain中，许多模型提供商（如OpenAI, Anthropic, Google, Mistral, Ollama）的聊天模型都内置了.with_structured_output()方法，这使得从LLM获取结构化输出（如Pydantic模型或JSON模式）变得更加简单直接，通常不再需要手动创建复杂的提示模板来包含格式指令。



生成数据：

调用创建好的生成器或链，根据需要生成指定数量的合成数据点。





应用场景举例：

为提取任务生成基准数据集：如35所示，可以先定义一个包含“演员”和“电影列表”的Pydantic模型，然后提供一些真实数据作为输入，让LLM围绕这些输入生成包含这些信息的文本段落，并指定风格偏好（如“非正式”、“最小长度500词”）。这样生成的文本和对应的结构化标签（原始输入）就可以用来测试和评估信息提取链的性能 35。
生成多样化的用户查询：用于测试聊天机器人或搜索引擎的鲁棒性。
创建符合特定格式的假数据：用于填充数据库或API的测试环境。


虽然合成数据非常有用，但也需要注意其局限性：它可能无法完全捕捉真实世界数据的复杂性和细微差别，过度依赖合成数据可能导致模型在真实场景中表现不佳 35。因此，在使用时应谨慎评估其适用性。核心观点 4.4.1: Langchain不仅能够帮助开发者理解和处理已有的数据，更进一步地，它能够被有效地用于程序化地生成全新的、结构化的合成数据，这一能力为数据扩增、场景模拟、隐私保护下的模型测试与训练等开辟了广阔的应用前景。大型语言模型的核心是其强大的生成能力 36。通过结合Langchain中的Pydantic模型（用于定义期望的数据结构）35、精心设计的提示模板（用于指导LLM的生成行为）以及可能的少样本示例（用于提供具体的格式和内容参考），开发者可以引导LLM产出符合特定模式的、多样化的合成数据点。Langchain提供的工具，如create_openai_data_generator或更现代的create_structured_output_runnable（或模型自带的.with_structured_output()方法），极大地简化了这一过程，使得批量生成用于测试信息提取算法的文本、创建用于训练的特定领域对话、或模拟各种用户输入等任务变得更加高效和可控。这标志着LLM应用从单纯的“信息消费者”向“信息创造者”的延伸。4.5 代码理解与生成Langchain及其集成的LLM（尤其是那些针对代码进行过优化的模型，如CodeLlama）在代码理解和生成方面展现出强大的潜力。开发者可以利用Langchain构建工具来辅助编码、分析代码库、生成文档等。

主要应用场景 32：

代码库问答 (Q&A over codebase): 允许开发者用自然语言提问关于代码库结构、特定函数功能、类继承关系等问题。
代码重构与改进建议: LLM可以分析现有代码，并提出重构建议、性能优化点或潜在的bug。
代码文档生成: 自动为函数、类或整个模块生成文档字符串或更详细的解释性文档。
代码生成 (Code Generation): 根据自然语言描述生成代码片段，或补全不完整的代码块 37。
代码解释 (Code Explanation): 详细解释一段代码的逻辑和功能。



Langchain在代码处理中的应用：


特定语言的文本分割器: 对于代码这种结构化文本，使用针对特定编程语言优化的文本分割器至关重要。例如，RecursiveCharacterTextSplitter.from_language(Language.PYTHON)能够更好地根据Python的语法结构（如类、函数定义）来分割代码，而不是简单地按字符数或通用分隔符 32。这有助于在后续的RAG流程中检索到更完整和相关的代码上下文。


构建代码库RAG系统:

克隆代码库: 使用GitPython等库将目标代码仓库克隆到本地 32。
加载代码文件: 使用DirectoryLoader配合特定文件类型的加载器（如TextLoader处理.py文件）加载代码库中的所有相关文件。
分割代码: 使用如上所述的特定语言文本分割器进行分割。
创建嵌入并存入向量存储: 与标准RAG流程类似，使用嵌入模型（如OpenAIEmbeddings）和向量存储（如Chroma）来索引代码块 32。
创建检索器: 从向量存储创建检索器，可能使用MMR（Maximal Marginal Relevance）等搜索类型以平衡相关性和多样性 32。
构建问答链: 创建一个包含检索器、提示模板（针对代码提问设计）、LLM和输出解析器的链。提示模板可能需要引导LLM基于提供的代码上下文回答问题，或者解释代码片段。


32中展示了一个完整的示例，通过加载Langchain自身的Python代码库，并构建RAG系统来回答诸如“RunnableBinding是什么？”或“从Runnable类派生了哪些类？”等问题。



使用代码专用LLM:

许多LLM提供商（如OpenAI, Anthropic, Google）的模型本身就具有很强的代码能力。
此外，还有专门为代码任务微调的模型，如Meta的CodeLlama系列 32。Langchain可以通过ChatOllama等集成轻松调用这些本地或托管的代码LLM。
32的示例中，使用了通过Ollama运行的codellama模型来回答一个通用的Bash命令问题：“如何在bash中列出当前目录下过去一个月内修改过的所有文本文件？”模型成功生成了正确的find命令。



直接代码生成/解释的提示:

除了RAG，也可以直接向代码LLM发送提示，要求其生成代码、解释代码或进行转换。
例如，提示LLM：“用Python写一个函数，计算斐波那契数列的第n项。”





示例：代码库问答 32
Python# # 假设已完成代码库克隆、加载、分割、嵌入和存储到Chroma的步骤，并创建了retriever
# # from langchain_openai import ChatOpenAI, OpenAIEmbeddings
# # from langchain_community.vectorstores import Chroma
# # from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
# # from langchain_community.document_loaders import GitLoader # 或者 DirectoryLoader
# # from langchain.chains import create_retrieval_chain
# # from langchain.chains.combine_documents import create_stuff_documents_chain
# # from langchain_core.prompts import ChatPromptTemplate

# # llm = ChatOpenAI(model="gpt-3.5-turbo")
# # # retriever = db.as_retriever(...) # 假设db是已填充的Chroma实例

# # # 提示模板，用于结合检索到的代码上下文和问题
# code_qa_template = """根据以下代码上下文回答问题。如果上下文中没有答案，请说明你不知道。
# 代码上下文:
# {context}

# 问题: {input}
# 回答:"""
# code_qa_prompt = ChatPromptTemplate.from_template(code_qa_template)

# # 创建一个链来组合文档并传递给LLM
# question_answer_chain = create_stuff_documents_chain(llm, code_qa_prompt)
# # 创建包含检索步骤的完整RAG链
# rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# # 提问
# question = "Langchain中的RunnableSequence是如何工作的？"
# response = rag_chain.invoke({"input": question})
# print(f"问题: {question}")
# print(f"答案: {response['answer']}")


通过结合Langchain的模块化组件和强大的代码LLM，开发者可以构建出显著提升编程效率和代码库可维护性的智能工具。核心观点 4.5.1: Langchain的通用组件（如RAG流程、提示模板、模型集成）可以被有效地特化并应用于代码领域，从而赋能开发者构建强大的代码辅助应用，如代码库智能问答、自动化文档生成和自然语言驱动的代码生成，特别是当与那些在代码理解和生成方面表现出色的LLM（如CodeLlama）相结合时。代码本质上是一种结构化的文本，LLM在处理自然语言方面的进展也越来越多地体现在其处理编程语言的能力上 32。Langchain的RAG流水线（加载、分割、嵌入、检索、生成）可以无缝地应用于源代码文件，就像应用于普通文本文档一样，32中克隆Git仓库并对其进行问答的示例充分证明了这一点。通过使用针对特定编程语言设计的文本分割器（如RecursiveCharacterTextSplitter.from_language(Language.PYTHON) 32），可以显著提高代码块切分的质量，确保检索到的上下文更具相关性和完整性。更进一步，集成那些专门在海量代码数据上训练过的LLM（如37中提到的CodeLlama，并在32中实际使用），能够大幅提升在代码理解、代码生成、代码解释等任务上的表现。Langchain作为一个灵活的框架，为整合这些专门化的模型和处理流程提供了便利。模块四：Langchain高级概念在掌握了Langchain的核心组件和基本应用构建之后，本模块将深入探讨一些更高级的概念和技术。这些内容将帮助开发者构建更复杂、更高效、更具动态性的LLM应用。我们将重点关注LangChain表达式语言（LCEL）的进阶用法、如何构建包含路由和分支的复杂链条，以及如何利用LangGraph设计和实现状态化的多智能体系统。第五章：深入Langchain5.1 LangChain表达式语言 (LCEL) 进阶LangChain表达式语言（LCEL）是Langchain中构建链（Chains）的推荐方式，它采用声明式的方法，通过组合可运行对象（Runnables）来创建新的链 22。LCEL不仅仅是语法糖，它使得Langchain能够优化链的运行时执行，并提供了一致的接口。

LCEL核心回顾：

声明式: 描述“做什么”而非“怎么做”，Langchain负责优化执行 22。
可组合性: 所有LCEL组件都实现了Runnable接口，可以通过管道操作符|或.pipe()方法轻松组合 22。
优化执行: Langchain利用LCEL的结构进行并行执行、异步支持、流式处理和批处理等优化 22。



高级组合技巧：

RunnableParallel进行复杂输入映射: 当一个链的后续步骤需要多个独立处理的输入时，RunnableParallel非常有用。它可以并行执行多个Runnable，并将它们的输出收集到一个字典中，作为下一步的输入。
Python# from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser

# prompt1 = ChatPromptTemplate.from_template("生成一个关于{topic}的笑话。")
# prompt2 = ChatPromptTemplate.from_template("写一句关于{topic}的诗。")
# model = ChatOpenAI()
# parser = StrOutputParser()

# map_chain = RunnableParallel(
#     joke=prompt1 | model | parser,
#     poem=prompt2 | model | parser
# )
# # 输入 {"topic": "猫"} 将会并行生成关于猫的笑话和诗
# # 输出将会是 {"joke": "...", "poem": "..."}
# result = map_chain.invoke({"topic": "猫"})
# print(result)


RunnablePassthrough.assign()添加键: RunnablePassthrough()通常用于将输入原样传递。结合.assign()方法，可以在传递输入的同时，计算并添加新的键值对到传递的字典中。
Python# from langchain_core.runnables import RunnablePassthrough
# chain = RunnablePassthrough.assign(
#     modified_input=lambda x: x["input"].upper()
# )
# # 输入 {"input": "hello"} 会输出 {"input": "hello", "modified_input": "HELLO"}
# print(chain.invoke({"input": "hello"}))


从RunnableParallel的输出中提取特定项 (Itemgetting): 如果RunnableParallel的输出是一个字典，而后续步骤只需要该字典中的某一项，可以使用RunnableLambda或直接在LCEL中通过字典键来提取。更规范的方式是使用operator.itemgetter或Langchain提供的RunnablePick。
Python# from operator import itemgetter
# # 假设 map_chain 如上定义
# # final_chain = map_chain | itemgetter("joke") # 或者 RunnableLambda(lambda x: x["joke"])
# # result_joke = final_chain.invoke({"topic": "狗"})
# # print(result_joke) # 只输出笑话





流式处理 (Streaming)：

LCEL原生支持流式处理，这意味着你可以逐步获取链的输出，而不是等待整个链执行完毕 22。这对于提高用户体验（如聊天机器人的实时响应）至关重要。
Runnable接口提供了.stream()（同步）和.astream()（异步）方法。
当链中的LLM或聊天模型支持流式输出时，LCEL会自动处理并将token流式传递。
astream_events (Beta): 除了流式传输最终输出外，还可以流式传输链执行过程中的详细事件，如哪个Runnable开始/结束，输入/输出是什么等，这对于调试和构建更复杂的UI非常有用 9。
示例：
Python# # chain = prompt1 | model | parser (如上定义)
# # for chunk in chain.stream({"topic": "编程"}):
# #     print(chunk, end="", flush=True)





异步操作 (Asynchronous Operations)：

LCEL中的所有Runnable都支持异步执行，通过.ainvoke(), .abatch(), 和 .astream() 方法 23。
这对于构建可扩展的、能够处理高并发请求的Web服务或应用至关重要。
当链中包含I/O密集型操作（如调用外部API、数据库查询）时，异步执行可以显著提高吞吐量。
RunnableParallel在异步模式下使用asyncio.gather来并发执行其包含的Runnable 23。



配置可运行对象 (Configuring Runnables)：

在调用Runnable的方法（如invoke, stream）时，可以传递一个RunnableConfig对象（通常作为config参数）。
RunnableConfig允许你指定运行时的参数，例如 9：

tags: 为运行添加标签，便于在LangSmith中过滤和分组。
metadata: 添加自定义元数据到运行中。
callbacks: 传递请求时回调处理器。
max_concurrency: 控制批处理或并行操作的最大并发数。
recursion_limit: 控制链的最大递归深度。
configurable: 用于传递可配置字段的值，允许在运行时动态改变链的行为（例如，改变LLM的temperature参数）。


示例：
Python# # chain.invoke(
# #     {"topic": "太空"},
# #     config={"tags": ["science", "jokes"], "max_concurrency": 5}
# # )





LCEL Cookbook 示例：

Langchain官方文档提供了LCEL Cookbook，其中包含许多常见任务的实现示例，如“提示+LLM”、“多链组合”、“RAG”、“SQL查询”、“添加记忆”、“使用工具”和“智能体”等 38。
这些Cookbook示例是学习和掌握LCEL强大功能的绝佳资源。
Langfuse等第三方工具也提供了与LCEL集成的Cookbook，展示了如何结合使用以增强可观测性，例如追踪invoke/ainvoke, batch/abatch, stream/astream等操作 39。


LCEL的这些高级特性使其成为构建复杂、高性能且易于维护的LLM应用的强大工具。通过熟练运用这些技巧，开发者可以充分发挥Langchain框架的潜力。核心观点 5.1.1: LCEL不仅仅是一种用于串联组件的简洁语法，其内置的对流式处理、异步操作和并行执行的强大支持，对于构建能够满足真实世界应用场景（如高并发服务、实时交互界面）需求的、响应迅速且可扩展的大型语言模型（LLM）应用而言，是至关重要的核心能力。简单的同步链条虽然易于理解和构建，但在面对需要即时反馈或同时处理多个请求的生产环境中，其性能和用户体验往往难以达标。流式处理（通过.stream()和.astream()实现）允许应用在LLM生成内容的同时就逐步将其展示给用户，极大地缩短了用户的感知等待时间，提升了交互的流畅性 22。异步操作（通过.ainvoke(), .abatch(), .astream()实现）则使得应用能够非阻塞地处理I/O密集型任务（如API调用、数据库访问），从而在服务器环境中高效处理大量并发用户请求 23。更进一步，LCEL通过RunnableParallel等机制支持在链内部并行执行多个计算分支，这可以有效降低复杂任务的总执行延迟 22。LCEL将这些高级执行模式作为其Runnable接口的标准特性提供出来，意味着任何使用LCEL构建的链都可以“开箱即用”地获得这些能力，这无疑是Langchain框架在工程实践方面的一大优势。5.2 构建复杂链：路由与分支虽然许多LLM应用可以通过线性的、顺序执行的链来构建，但更复杂的场景往往需要根据输入动态地选择不同的处理路径（路由），或者将一个处理流程分叉到多个并行的子流程中再合并结果（分支与合并）。Langchain提供了多种机制来实现这种非线性工作流。

路由 (Routing)：

概念: 路由是指根据输入的内容或某些条件，动态地决定接下来应该执行哪个子链或采取哪个操作。这使得应用能够根据不同的情况采取不同的策略。
RouterChain (传统方式):

RouterChain本身是一个链，它的任务是分析输入并决定应该将输入路由到哪个“目标链”以及传递给目标链的输入是什么 40。
通常包含一个LLM（用于做路由决策）和一个解析器（用于解析LLM的输出以确定目标）。


MultiRouteChain (传统方式):

MultiRouteChain使用一个RouterChain来选择多个预定义好的候选链中的一个来处理当前输入 40。它包含一个路由链和多个目标链（以及这些目标链的描述，供路由链参考）。


EmbeddingRouterChain (传统方式):

这种路由链使用文本嵌入的语义相似性来进行路由决策 40。它将输入的查询与每个候选目标链的描述（或代表性查询）的嵌入进行比较，选择最相似的目标链。


使用LCEL实现路由:

在LCEL中，路由逻辑通常可以通过RunnableLambda结合条件判断来实现。RunnableLambda可以包含一个函数，该函数根据输入决定返回哪个后续的Runnable。
RunnableBranch: 这是一个更专门用于条件执行的LCEL组件。它接受一系列(condition_runnable, true_runnable)对和一个可选的default_runnable。它会按顺序评估每个condition_runnable，如果某个条件为真，则执行对应的true_runnable并返回其结果；如果所有条件都为假，则执行default_runnable。

Python# from langchain_core.runnables import RunnableBranch, RunnableLambda
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate

# llm = ChatOpenAI()
# # 分类器链，判断问题类型
# classifier_prompt = PromptTemplate.from_template(
#     "将用户问题分类为'数学'或'语言'。问题：{question} 分类："
# )
# classifier_chain = classifier_prompt | llm

# # 数学处理链
# math_prompt = PromptTemplate.from_template("解决数学问题：{question}")
# math_chain = math_prompt | llm

# # 语言处理链
# lang_prompt = PromptTemplate.from_template("回答语言问题：{question}")
# lang_chain = lang_prompt | llm

# # 路由逻辑
# def route_logic(info):
#     if "数学" in info["topic"].content: # 假设classifier_chain的输出在info["topic"]
#         return math_chain
#     else:
#         return lang_chain

# # 使用RunnableBranch (更推荐的方式)
# branch = RunnableBranch(
#   (lambda x: "数学" in x["topic"].content, math_chain), # 条件1, 对应链1
#   (lambda x: "语言" in x["topic"].content, lang_chain), # 条件2, 对应链2
#   lang_chain  # 默认链
# )

# full_chain = {
#     "topic": classifier_chain, # 先运行分类器
#     "question": lambda x: x["question"] # 保留原始问题
# } | branch # 然后根据分类结果进行分支

# print(full_chain.invoke({"question": "2+2等于几？"}))
# print(full_chain.invoke({"question": "天空为什么是蓝色的？"}))





分支与合并 (Branching and Merging) 使用LCEL：

分支 (RunnableParallel): RunnableParallel是实现处理流程分支的关键。它可以接收一个输入，并将这个输入（或其部分）同时传递给多个并行的Runnable。每个Runnable构成一个分支，独立处理输入 42。
合并: RunnableParallel的输出是一个包含所有分支结果的字典。这个字典可以作为后续步骤的输入。

可以将这个字典直接传递给一个需要多输入的提示模板。
可以使用RunnableLambda或itemgetter来选择、组合或进一步处理这些分支的结果，然后传递给下一个组件。


42中的示例展示了如何创建一个planner分支（生成论点）和多个arguments_for分支（为论点生成支持或反驳理由），然后可能将这些结果合并以形成一个完整的报告或分析。
示例（简化自42，概念性）：
Python# from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser

# model = ChatOpenAI()
# parser = StrOutputParser()

# # 分支1：生成主要观点
# main_point_prompt = ChatPromptTemplate.from_template("针对{input}，提出一个主要观点。")
# main_point_chain = main_point_prompt | model | parser

# # 分支2：生成支持性论据
# support_prompt = ChatPromptTemplate.from_template("为观点“{main_point}”提供一个支持性论据。")
# # 注意：这里需要将main_point_chain的输出作为此分支的输入一部分
# # 这可以通过更复杂的RunnableParallel结构或后续的assign实现

# # 更简单的并行分支示例，都基于原始输入
# branch_chain = RunnableParallel(
#     main_point=main_point_chain,
#     elaboration=ChatPromptTemplate.from_template("详细阐述{input}。") | model | parser
# )

# # 合并结果到一个最终提示
# final_prompt_template = """主要观点：{main_point}
# 详细阐述：{elaboration}
# ---
# 基于以上信息，撰写一段总结。"""
# final_prompt = ChatPromptTemplate.from_template(final_prompt_template)
# final_chain = branch_chain | final_prompt | model | parser

# print(final_chain.invoke({"input": "人工智能的未来"}))





处理多个输入/输出：

LCEL链天然支持处理字典形式的输入和输出 41。
当一个Runnable需要多个输入时，通常期望其输入是一个包含所有必需键的字典。RunnableParallel常用于构建这样的输入字典，其中每个键的值由一个上游Runnable计算得到。
同样，如果一个Runnable（如RunnableParallel或一个配置为输出多项内容的LLM调用）产生多个输出项，它通常会返回一个字典。下游的Runnable可以消费整个字典，或通过itemgetter等方式选择特定的输出项。


通过这些路由和分支机制，Langchain应用不再局限于简单的线性流程，而是能够构建出能够根据具体情况做出决策、并行处理信息并综合结果的、更智能和灵活的系统。核心观点 5.2.1: Langchain通过其路由和分支机制，特别是利用LCEL的RunnableBranch和RunnableParallel等组件，使得开发者能够创建动态和条件性的工作流程，让应用程序能够根据输入数据的特性或中间结果自适应地调整其行为，从而超越了传统静态、线性的链式处理模式。许多现实世界的问题并非总能通过一个固定的步骤序列来解决；相反，它们可能需要根据具体情况选择不同的处理路径，或者同时探索多个方面的信息再进行综合。例如，一个客服应用可能需要根据用户问题的类型（技术支持、账单查询、产品建议）将其导向不同的处理逻辑 40。RouterChain及其变体（如EmbeddingRouterChain）提供了这种基于内容或语义的路由能力。在LCEL的范式下，RunnableBranch允许基于前一个Runnable的输出（条件）来选择执行哪一个后续的Runnable，实现了清晰的条件分支。同时，RunnableParallel则允许将一个输入“分发”给多个并行的处理单元（分支），每个单元可以独立地对输入进行某种操作或分析，然后这些并行的结果可以被后续的步骤“合并”和利用，以形成更全面的输出或决策 42。这种构建非线性、数据依赖的执行路径的能力，是开发更智能、更灵活、更能适应复杂场景的LLM应用的关键。5.3 使用LangGraph设计状态化多智能体系统当LCEL构建的链（通常是无环图）不足以表达更复杂的、包含循环、显式状态管理或多个协作智能体的应用逻辑时，LangGraph就派上了用场 23。LangGraph是一个基于Langchain构建的库，专门用于创建强大且可定制的智能体和多智能体系统。

何时选择LangGraph：

循环 (Cycles): 当智能体需要迭代、反思、重试或进行多轮工具调用直到满足某个条件时（例如，ReAct智能体中的思考-行动循环）。
显式状态管理 (Explicit State Management): 当需要在图的不同节点之间显式地传递和修改一个共享的状态对象时 44。这个状态可以包含聊天历史、中间结果、智能体的信念等。
多智能体协作 (Multi-Agent Collaboration): 当需要多个智能体（或角色）协同工作，每个智能体负责图中的一部分，并通过共享状态或消息传递进行交互时 28。
人类在环 (Human-in-the-loop): 当需要在工作流的特定点暂停，等待人类输入、批准或干预时 28。
构建可靠的、长时间运行的、可持久化的流程 6。



LangGraph的核心概念 28：

图 (Graph): 整个工作流被定义为一个状态图（Stateful Graph）。
节点 (Nodes): 图中的计算单元。每个节点可以是一个Python函数或一个Langchain Runnable（如LCEL链）。节点接收当前状态作为输入，执行其逻辑，并返回一个更新状态的对象（通常是字典，用于更新部分状态）。
边 (Edges): 定义了从一个节点到另一个节点的转换。

条件边 (Conditional Edges): 边的选择可以基于当前状态或前一个节点的输出来动态决定。这允许实现分支和循环逻辑。通常，一个节点执行后，会指向一个特殊的“条件节点”，该节点根据状态决定接下来应该路由到哪个实际工作节点。
普通边: 从一个节点直接指向下一个节点。


状态 (State): 一个在图的执行过程中被传递和修改的对象（通常是一个Pydantic模型或TypedDict）。每个节点都可以读取和更新这个状态。LangGraph确保状态的正确传递。
入口点 (Entry Point): 图开始执行的第一个节点。
结束点 (Finish Point / End Node): 标记图执行结束的节点。



LangGraph的优势：

对智能体运行时的精细控制: 允许开发者精确定义智能体的每一步行为和状态转换 28。
自定义智能体工作流: 可以构建标准智能体架构（如ReAct, Plan-and-Execute）的自定义版本，或全新的架构。
无缝的人类在环交互: 容易在图的任何位置插入等待人类输入的节点 28。
原生的中间步骤流式传输: 可以流式传输每个节点执行的中间结果，增强可观测性和用户体验 28。
持久化与可恢复性: LangGraph支持检查点（checkpointing），可以将图的当前状态保存下来，并在之后从该状态恢复执行，这对于构建长时间运行或需要容错的应用非常重要。



构建LangGraph应用的步骤（概念性） 44：

定义状态模式 (Define State Schema): 使用Pydantic模型或TypedDict定义图的状态对象结构。
创建节点 (Create Nodes): 实现每个节点的Python函数或LCEL链。这些函数通常接收状态对象作为输入，并返回一个包含状态更新的字典。
实例化图 (StateGraph 或 MessageGraph): 创建一个图实例，并传入状态模式


