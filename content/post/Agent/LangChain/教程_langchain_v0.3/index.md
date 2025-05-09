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




好的，我们来结合 Python 代码详细介绍 LangChain 中的链 (Chains)。

为了运行这些代码示例，你需要先安装 LangChain 及相关的库，例如 `langchain`, `langchain-openai` (如果你使用 OpenAI 模型)等。

```bash
pip install langchain langchain-openai python-dotenv
```

你还需要设置你的 OpenAI API 密钥。通常，可以将其设置为环境变量 `OPENAI_API_KEY`。

```python
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量 (如果你的 API Key 在那里)
load_dotenv()

# 确保 OPENAI_API_KEY 环境变量已设置
# os.environ["OPENAI_API_KEY"] = "sk-YOUR_ACTUAL_API_KEY" # 或者直接在这里设置
```

**注意：** 以下代码中的 LLM 将主要使用 `ChatOpenAI`。为了使示例可独立运行且不实际消耗 API 配额，部分示例会使用 `FakeListLLM` from `langchain.llms.fake` (较旧的模块，新版中推荐 `from langchain_community.llms.fake import FakeListLLM` 或者 `from langchain_core.language_models.fake import FakeListLLM`) 或 `FakeChatModel` from `langchain_core.language_models.fake`。我会尽量指出。在实际应用中，你会替换为真实的 LLM 实例。

---

#### 3.3 链 (Chains)：构建调用序列

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

---

这些示例应该能帮助你理解 LangChain 中不同类型链的工作方式和如何在代码中实现它们。记住，LangChain 的生态系统非常庞大，还有许多其他特定用途的链和组件可以探索。实际应用中，你可能会组合这些链来构建更复杂的应用程序。




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
