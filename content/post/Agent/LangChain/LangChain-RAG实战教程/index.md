---
title: Langchain-RAG实战教程
description: ""
date: 2025-05-06T11:05:13+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---


## 基础概念

### **Langchain RAG 简介**

RAG (Retrieval Augmented Generation) 是一种结合了检索（Retrieval）和生成（Generation）模型的技术，旨在通过从外部知识库中检索相关信息来增强大型语言模型（LLM）的回答能力。简单来说，当用户提出一个问题时，RAG 系统首先会从一个文档集合（知识库）中找到与问题最相关的几段文本，然后将这些文本连同原始问题一起输入到 LLM 中，让 LLM 基于这些信息生成更准确、更全面的回答。

### **Langchain RAG 的优势**

* **减少幻觉 (Hallucination)**：通过提供相关的上下文信息，LLM 更倾向于基于事实进行回答，而不是编造信息。
* **知识实时更新**：可以将知识库与最新的信息同步，而无需重新训练整个 LLM。
* **提高答案的相关性和准确性**：检索到的信息为 LLM 提供了针对性的知识，从而生成更精准的答案。
* **可解释性**：可以追溯答案的来源，了解 LLM 是基于哪些信息生成的回答。

### **Langchain RAG 的核心组件**

一个典型的 Langchain RAG 应用通常包含以下几个核心组件：

1.  **文档加载器 (Document Loaders)**：用于从各种来源（如文本文件、PDF、网页、数据库等）加载文档数据。
2.  **文本分割器 (Text Splitters)**：将加载的文档分割成更小的、语义相关的文本块 (chunks)，以便于后续的检索。
3.  **文本嵌入模型 (Text Embedding Models)**：将文本块转换成向量表示 (embeddings)，使得计算机可以理解文本的语义相似度。
4.  **向量存储 (Vector Stores)**：用于存储文本块的向量表示，并提供高效的相似性搜索功能。
5.  **检索器 (Retrievers)**：根据用户问题（Query）的向量表示，从向量存储中检索出最相关的文本块。
6.  **语言模型 (Language Models - LLMs)**：接收用户问题和检索到的上下文信息，生成最终的回答。
7.  **链 (Chains)**：将上述所有组件串联起来，形成一个完整的 RAG 工作流。


### RAG和微调如何选择

1. RAG适合知识动态更新、数据分散、资源有限的场景，强调外部知识的灵活引入。
2. 微调适合任务特定、数据稳定、资源充足的场景，强调模型的定制化性能。
3. 根据任务需求、数据、资源和更新频率权衡选择，或考虑结合两者以达到最佳效果。


##  **代码实战：构建一个简单的 RAG 应用**

|源文件|
|---|
|[example_doc.txt](./02-Langchain-Rag实战/example_doc.txt)|
|[main.py](./02-Langchain-Rag实战/main.py)|



下面我们将通过一个实际的例子来演示如何使用 Langchain 构建一个简单的 RAG 应用。

**前提条件**

在开始之前，请确保您已经安装了必要的 Python 库：

```bash
pip install langchain openai chromadb tiktoken pypdf unstructured
```

* `langchain`: Langchain 核心库。
* `openai`: 用于与 OpenAI 的 LLM 和嵌入模型交互（您也可以选择其他 LLM 和嵌入模型提供商）。
* `chromadb`: 一个开源的向量数据库，用于存储文本嵌入。
* `tiktoken`: OpenAI 用于计算 token 数量的库。
* `pypdf`: 用于加载 PDF 文件。
* `unstructured`: 用于加载多种格式的文档。

**步骤 1：设置 API 密钥 (可选)**

如果您使用 OpenAI 的模型，需要设置您的 API 密钥。

```python
import os

os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
```

请将 `"YOUR_OPENAI_API_KEY"` 替换为您自己的 OpenAI API 密钥。

**步骤 2：加载文档**

我们将使用一个简单的文本文件作为我们的知识库。您也可以使用 PDF 加载器加载 PDF 文件。

```python
from langchain_community.document_loaders import TextLoader, PyPDFLoader

# 加载文本文件
# loader = TextLoader("./your_document.txt", encoding="utf-8") # 替换为您的文本文件路径

# 或者加载 PDF 文件
loader = PyPDFLoader("./sample.pdf") # 替换为您的 PDF 文件路径
documents = loader.load()

# 打印加载的文档数量和第一个文档的内容（部分）
print(f"加载了 {len(documents)} 个文档")
if documents:
    print(f"第一个文档的内容预览: {documents[0].page_content[:200]}")
```

请创建一个名为 `sample.pdf` 的 PDF 文件，或者将 `./sample.pdf` 替换为您自己的文件路径。

**步骤 3：分割文档**

将加载的文档分割成更小的块，以便嵌入和检索。

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(documents)

# 打印分割后的文本块数量和第一个文本块的内容（部分）
print(f"文档被分割成 {len(texts)} 个文本块")
if texts:
    print(f"第一个文本块的内容预览: {texts[0].page_content[:200]}")
```

* `chunk_size`: 每个文本块的最大字符数。
* `chunk_overlap`: 相邻文本块之间的重叠字符数，有助于保持上下文的连续性。

**步骤 4：创建文本嵌入**

使用 OpenAI 的嵌入模型将文本块转换为向量。

```python
from langchain_openai import OpenAIEmbeddings

embeddings_model = OpenAIEmbeddings()

# 嵌入示例文本 (可选，仅为演示)
# example_text = "这是一个示例文本，用于测试嵌入模型。"
# example_embedding = embeddings_model.embed_query(example_text)
# print(f"示例文本的嵌入向量 (部分): {example_embedding[:5]}")
```

**步骤 5：创建向量存储**

使用 ChromaDB 将文本块的嵌入向量存储起来。

```python
from langchain_community.vectorstores import Chroma

# 创建向量存储，并将文本块及其嵌入存储进去
# persist_directory 参数指定了向量数据库在磁盘上持久化存储的路径
vectorstore = Chroma.from_documents(documents=texts,
                                    embedding=embeddings_model,
                                    persist_directory="./chroma_db")

# 持久化向量存储到磁盘 (Chroma 在创建时会自动持久化，但显式调用 ensure_persisted() 是个好习惯)
vectorstore.persist()

print("向量存储创建并持久化成功！")
```

如果您之前已经创建并持久化了向量数据库，可以这样加载它：

```python
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings

# embeddings_model = OpenAIEmbeddings()
# vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings_model)
# print("从磁盘加载向量存储成功！")
```

**步骤 6：创建检索器**

从向量存储创建一个检索器，用于根据查询检索相关的文本块。

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 3}) # k 表示检索最相关的 k 个文本块

# 测试检索器 (可选)
# query = "什么是 Langchain?"
# relevant_docs = retriever.get_relevant_documents(query)
# print(f"\n对于查询 '{query}', 检索到的相关文档数量: {len(relevant_docs)}")
# for i, doc in enumerate(relevant_docs):
#     print(f"相关文档 {i+1}:\n{doc.page_content[:150]}...\n")
```

**步骤 7：创建语言模型**

初始化一个语言模型，我们将使用 OpenAI 的 GPT-3.5-turbo 模型。

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7) # temperature 控制生成文本的随机性
```

**步骤 8：创建 RAG 链 (Chain)**

Langchain 提供了几种创建 RAG 链的方式。这里我们使用 `RetrievalQA` 链，这是一个方便的封装。

```python
from langchain.chains import RetrievalQA

# 创建 RetrievalQA 链
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff", # "stuff" 是最简单的链类型，将所有检索到的文本直接放入提示中
    retriever=retriever,
    return_source_documents=True # 是否返回源文档
)

# 其他 chain_type 选项包括:
# "map_reduce": 分别处理每个文档，然后合并结果
# "refine": 依次处理每个文档，逐步优化答案
# "map_rerank": 分别处理每个文档，并根据置信度对结果进行排序
```

**步骤 9：进行提问和获取答案**

现在，我们可以向 RAG 链提问了。

```python
query = "请介绍一下 Langchain 的主要功能。" # 替换为您想问的问题
result = qa_chain.invoke({"query": query})

print("\n模型生成的回答:")
print(result["result"])

print("\n引用的源文档:")
for i, source_doc in enumerate(result["source_documents"]):
    print(f"源文档 {i+1} (来自: {source_doc.metadata.get('source', '未知来源')}, 页码: {source_doc.metadata.get('page', 'N/A')}):") # 假设元数据中有 'source' 和 'page'
    print(f"{source_doc.page_content[:200]}...\n")
```

**更高级的 RAG：使用 LCEL (LangChain Expression Language)**

LCEL 提供了更灵活和可组合的方式来构建链。下面是使用 LCEL 构建 RAG 链的示例：

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. 定义提示模板
template = """请根据以下上下文信息来回答问题。如果你不知道答案，就说你不知道，不要试图编造答案。
用最多三句话来回答，并保持答案简洁。

上下文:
{context}

问题: {question}

有用的回答:"""
prompt = ChatPromptTemplate.from_template(template)

# 2. 定义如何格式化检索到的文档
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 3. 构建 RAG 链
rag_chain_lcel = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 4. 进行提问
query_lcel = "Langchain 的核心组件有哪些？"
answer_lcel = rag_chain_lcel.invoke(query_lcel)

print(f"\n使用 LCEL 构建的 RAG 链，对于查询 '{query_lcel}' 的回答:")
print(answer_lcel)

# 如果你想同时获取源文档，可以这样构建：
from operator import itemgetter

rag_chain_with_source = RunnablePassthrough.assign(
    context=itemgetter("question") | retriever | format_docs
).assign(
    answer= (
        {"context": itemgetter("context"), "question": itemgetter("question")}
        | prompt
        | llm
        | StrOutputParser()
    )
)

result_lcel_with_source = rag_chain_with_source.invoke({"question": query_lcel})

print("\n使用 LCEL (包含源文档) 的回答:")
print(result_lcel_with_source["answer"])
# print("\n引用的上下文 (LCEL):") # context 实际上是格式化后的检索文档字符串
# print(result_lcel_with_source["context"][:500] + "...")
```






## 代码实战：构建一个简单的RAG应用 阿里云百炼模型

**阿里云百炼平台**

阿里云百炼是一个企业级的大模型服务平台，提供了一系列预置的或可定制的大模型，包括通义千问（Qwen）系列等。我们可以通过其提供的 API 或 SDK 来调用这些模型，并将其集成到 Langchain 中。百炼平台通常会使用阿里云的 `DashScope` SDK 来进行模型调用。

**教程目标**

1.  了解 RAG 的基本原理和 Langchain 中的核心组件。
2.  学会在 Langchain 中配置和使用阿里云百炼提供的 Embedding 模型（用于文本向量化）。
3.  学会在 Langchain 中配置和使用阿里云百炼提供的大语言模型（用于生成答案）。
4.  构建一个完整的 RAG 应用，能够基于本地知识库回答问题。

**前提条件**

1.  **Python 环境**: 确保你安装了 Python 3.8 或更高版本。
2.  **阿里云账户**: 并开通百炼大模型服务。
3.  **API Key**: 从阿里云百炼平台获取 `DASHSCOPE_API_KEY`。这通常在阿里云的 RAM 访问控制中创建 AccessKey，并确保该 AccessKey 有权限访问 DashScope 服务。
4.  **安装必要的库**:
    ```bash
    pip install langchain langchain-community langchain-core python-dotenv
    pip install faiss-cpu  # 或者 faiss-gpu 如果你有GPU环境
    pip install dashscope  # 阿里云百炼模型调用的SDK
    pip install unstructured # 用于加载多种文档格式 (可选，但推荐)
    pip install "unstructured[pdf]" # 如果需要处理PDF
    pip install "unstructured[docx]" # 如果需要处理Word文档
    # 如果遇到 tiktoken 相关问题，可以尝试指定版本
    # pip install tiktoken
    ```

**教程步骤**

**第1步：设置环境变量**

创建一个 `.env` 文件（与你的 Python 脚本在同一目录下），并填入你的 API Key：

```env
DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

然后在你的 Python 脚本中加载它：

```python
import os
from dotenv import load_dotenv

load_dotenv() # 加载 .env 文件中的环境变量

# 检查 API Key 是否加载成功 (可选)
# dashscope_api_key = os.getenv("DASHSCOPE_API_KEY")
# if not dashscope_api_key:
#     raise ValueError("DASHSCOPE_API_KEY not found in environment variables.")
# else:
#     print("DASHSCOPE_API_KEY loaded successfully.")
```

**第2步：准备知识库文档**

创建一个简单的文本文件作为我们的知识库。例如，创建一个名为 `my_knowledge.txt` 的文件，内容如下：

```txt
阿里云百炼是领先的企业级大模型服务平台。
它提供了多种高效的大语言模型，例如通义千问系列。
用户可以通过百炼平台快速构建和部署AI应用。
百炼支持文本生成、知识问答、代码生成等多种场景。
Langchain是一个用于构建基于LLM应用的框架。
通过Langchain可以方便地集成阿里云百炼模型来开发RAG应用。
```

**第3步：加载和分割文档 (Load & Split)**

我们需要加载文档，并将其分割成较小的文本块（chunks），以便进行向量化和检索。

```python
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 1. 加载文档
loader = TextLoader("./my_knowledge.txt", encoding="utf-8")
documents = loader.load()

# 2. 分割文档
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,  # 每个块的最大字符数
    chunk_overlap=20   # 相邻块之间的重叠字符数
)
docs = text_splitter.split_documents(documents)

# 打印分割后的文档块数量和第一个块的内容 (可选)
print(f"文档被分割成了 {len(docs)} 个块。")
if docs:
    print("第一个块的内容：")
    print(docs[0].page_content)
```

**第4步：选择和配置 Embedding 模型 (Embeddings)**

我们将使用阿里云百炼（通过 DashScope）提供的文本向量模型。`DashScopeEmbeddings` 是 Langchain 中用于对接 DashScope 向量模型的类。

```python
from langchain_community.embeddings import DashScopeEmbeddings

# 配置 Embedding 模型
# 你需要从阿里云百炼或DashScope文档中查找可用的文本向量模型ID
# 例如："text-embedding-v1" 或 "text-embedding-v2" (请确认最新模型)
# 更多模型请参考：https://help.aliyun.com/document_detail/2582303.html
embedding_model_name = "text-embedding-v2" # 示例模型，请替换为实际可用模型

try:
    embeddings = DashScopeEmbeddings(
        model=embedding_model_name,
        dashscope_api_key=os.getenv("DASHSCOPE_API_KEY") # API Key 会自动从环境变量加载，这里显式传递也可以
    )
    print(f"成功初始化 Embedding 模型: {embedding_model_name}")

    # 测试 Embedding 模型 (可选)
    # test_text = "你好，世界！"
    # text_embedding = embeddings.embed_query(test_text)
    # print(f"'{test_text}' 的向量 (前5个维度): {text_embedding[:5]}")
    # print(f"向量维度: {len(text_embedding)}")

except Exception as e:
    print(f"初始化 Embedding 模型失败: {e}")
    print("请检查：")
    print("1. DASHSCOPE_API_KEY 是否正确设置在环境变量或代码中。")
    print(f"2. Embedding 模型名称 '{embedding_model_name}' 是否有效且账户有权访问。")
    print("3. 网络连接是否正常。")
    exit()
```
*注意*: 请确保你使用的 `embedding_model_name` 是你账户有权限访问且当前可用的模型。模型列表和名称可能会更新，请参考阿里云官方文档。

**第5步：创建向量数据库 (Vector Store)**

我们将使用 `FAISS` 作为内存向量数据库，它非常适合快速原型开发。

```python
from langchain_community.vectorstores import FAISS

# 使用分割后的文档和 Embedding 模型创建向量数据库
try:
    print("正在创建向量数据库...")
    vector_store = FAISS.from_documents(docs, embeddings)
    print("向量数据库创建成功！")
except Exception as e:
    print(f"创建向量数据库失败: {e}")
    exit()
```

**第6步：选择和配置大语言模型 (LLM)**

我们将使用阿里云百炼（通过 DashScope）提供的聊天模型，如通义千问系列。`ChatTongyi` 或 `ChatAlibabaCloud` (如果使用更通用的接口) 是 Langchain 中用于对接的类。

```python
from langchain_community.chat_models import ChatTongyi # 或者 from langchain_alibaba.chat_models import ChatAlibabaCloud

# 配置 LLM
# 你需要从阿里云百炼或DashScope文档中查找可用的聊天模型ID
# 例如："qwen-turbo", "qwen-plus", "qwen-max", "bailian-v1" (如果百炼平台有特定模型ID)
# 更多模型请参考：https://help.aliyun.com/document_detail/2582302.html
llm_model_name = "qwen-turbo" # 示例模型，请替换为实际可用且你有权限的模型

try:
    llm = ChatTongyi(
        model_name=llm_model_name,
        # dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"), # API Key 会自动从环境变量加载
        streaming=False # 为了简单起见，先禁用流式输出
    )
    print(f"成功初始化 LLM: {llm_model_name}")

    # 测试 LLM (可选)
    # test_response = llm.invoke("你好，介绍一下你自己。")
    # print("LLM 测试响应：")
    # print(test_response.content)

except Exception as e:
    print(f"初始化 LLM 失败: {e}")
    print("请检查：")
    print("1. DASHSCOPE_API_KEY 是否正确设置在环境变量或代码中。")
    print(f"2. LLM 模型名称 '{llm_model_name}' 是否有效且账户有权访问。")
    print("3. 网络连接是否正常。")
    exit()
```
*注意*: 同样，请确保 `llm_model_name` 是你账户有权限访问且当前可用的模型。

**第7步：创建 RAG 链 (RAG Chain)**

Langchain 提供了 `RetrievalQA` 链，可以方便地将检索器（Retriever）和 LLM 组合起来。

```python
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# 1. 创建检索器 (Retriever)
# k=3 表示检索与问题最相关的3个文本块
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# 2. (可选) 定义 Prompt 模板
# 这个模板指导 LLM 如何利用检索到的上下文来回答问题
prompt_template = """请根据以下上下文信息来回答问题。如果你在上下文中找不到答案，就说你不知道，不要试图编造答案。

上下文:
{context}

问题: {question}

答案:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

# 3. 创建 RetrievalQA 链
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # "stuff" 会将所有检索到的文本块"塞进"一个 Prompt 中
    retriever=retriever,
    return_source_documents=True, # 同时返回源文档块，方便溯源
    chain_type_kwargs={"prompt": PROMPT} # 应用自定义的Prompt
)

print("RAG 链创建成功！")
```

**第8步：提问和获取答案**

现在可以向我们构建的 RAG 系统提问了。

```python
# 提问
query1 = "什么是阿里云百炼？"
query2 = "Langchain如何与百炼模型集成？"
query3 = "百炼支持哪些应用场景？"
query4 = "Python是什么？" # 知识库中没有的信息

queries = [query1, query2, query3, query4]

for query in queries:
    print(f"\n--- 正在提问: {query} ---")
    try:
        result = qa_chain.invoke({"query": query}) # Langchain 0.1.0+ 使用 invoke

        print("\n模型回答:")
        print(result["result"])

        print("\n相关源文档块:")
        for i, doc in enumerate(result["source_documents"]):
            print(f"  源文档 {i+1}:")
            print(f"  内容: {doc.page_content[:100]}...") # 打印前100个字符
            # print(f"  元数据: {doc.metadata}") # 可以查看源文件名等
    except Exception as e:
        print(f"处理问题 '{query}' 时出错: {e}")

```

**完整代码示例**

将以上所有步骤整合到一个 Python 文件中（例如 `rag_bailian_tutorial.py`）：

```python
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatTongyi
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def main():
    # 第1步：设置环境变量
    load_dotenv()
    dashscope_api_key = os.getenv("DASHSCOPE_API_KEY")
    if not dashscope_api_key:
        raise ValueError("DASHSCOPE_API_KEY not found in environment variables. Please set it in your .env file.")
    print("DASHSCOPE_API_KEY 加载成功。")

    # 第2步：准备知识库文档 (确保 my_knowledge.txt 文件存在且有内容)
    knowledge_file = "./my_knowledge.txt"
    if not os.path.exists(knowledge_file):
        print(f"错误: 知识库文件 {knowledge_file} 未找到。请创建它并添加内容。")
        # 为了演示，创建一个简单的知识库文件
        with open(knowledge_file, "w", encoding="utf-8") as f:
            f.write("阿里云百炼是领先的企业级大模型服务平台。\n")
            f.write("它提供了多种高效的大语言模型，例如通义千问系列。\n")
            f.write("用户可以通过百炼平台快速构建和部署AI应用。\n")
            f.write("百炼支持文本生成、知识问答、代码生成等多种场景。\n")
            f.write("Langchain是一个用于构建基于LLM应用的框架。\n")
            f.write("通过Langchain可以方便地集成阿里云百炼模型来开发RAG应用。\n")
        print(f"已创建示例知识库文件: {knowledge_file}")


    # 第3步：加载和分割文档
    print("\n--- 步骤 3: 加载和分割文档 ---")
    loader = TextLoader(knowledge_file, encoding="utf-8")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    docs = text_splitter.split_documents(documents)
    print(f"文档被分割成了 {len(docs)} 个块。")
    if docs:
        print(f"第一个块的内容：'{docs[0].page_content[:50]}...'")

    # 第4步：选择和配置 Embedding 模型
    print("\n--- 步骤 4: 配置 Embedding 模型 ---")
    embedding_model_name = "text-embedding-v2" # 确保这是你账户可用的模型
    try:
        embeddings = DashScopeEmbeddings(
            model=embedding_model_name,
            dashscope_api_key=dashscope_api_key
        )
        print(f"成功初始化 Embedding 模型: {embedding_model_name}")
    except Exception as e:
        print(f"初始化 Embedding 模型失败: {e}")
        print(f"请检查模型名称 '{embedding_model_name}' 和 API Key。")
        return

    # 第5步：创建向量数据库
    print("\n--- 步骤 5: 创建向量数据库 ---")
    try:
        vector_store = FAISS.from_documents(docs, embeddings)
        print("向量数据库创建成功！")
    except Exception as e:
        print(f"创建向量数据库失败: {e}")
        return

    # 第6步：选择和配置大语言模型 (LLM)
    print("\n--- 步骤 6: 配置 LLM ---")
    llm_model_name = "qwen-turbo" # 确保这是你账户可用的模型
    try:
        llm = ChatTongyi(
            model_name=llm_model_name,
            # dashscope_api_key=dashscope_api_key, # 已通过环境变量或DashScope SDK内部机制加载
            streaming=False
        )
        print(f"成功初始化 LLM: {llm_model_name}")
    except Exception as e:
        print(f"初始化 LLM 失败: {e}")
        print(f"请检查模型名称 '{llm_model_name}' 和 API Key。")
        return

    # 第7步：创建 RAG 链
    print("\n--- 步骤 7: 创建 RAG 链 ---")
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    prompt_template = """请根据以下上下文信息来回答问题。如果你在上下文中找不到答案，就说你不知道，不要试图编造答案。

上下文:
{context}

问题: {question}

答案:"""
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    print("RAG 链创建成功！")

    # 第8步：提问和获取答案
    print("\n--- 步骤 8: 提问和获取答案 ---")
    queries = [
        "什么是阿里云百炼？",
        "Langchain如何与百炼模型集成？",
        "百炼支持哪些应用场景？",
        "Python是什么？"
    ]

    for query in queries:
        print(f"\n--- 正在提问: {query} ---")
        try:
            result = qa_chain.invoke({"query": query})
            print("\n模型回答:")
            print(result["result"])
            print("\n相关源文档块:")
            for i, doc in enumerate(result["source_documents"]):
                print(f"  源文档 {i+1}: {doc.page_content[:100]}...")
        except Exception as e:
            print(f"处理问题 '{query}' 时出错: {e}")

if __name__ == "__main__":
    main()
```

**运行教程**

1.  确保你的 `.env` 文件配置正确。
2.  确保 `my_knowledge.txt` 文件存在于脚本同级目录（如果不存在，代码会自动创建一个示例文件）。
3.  在终端运行脚本：`python rag_bailian_tutorial.py`

**预期输出**

你会看到每个步骤的打印信息，最后是针对每个问题的回答和相关的源文档片段。对于知识库中没有的信息（如“Python是什么？”），模型应该回答它不知道或者基于通用知识回答（如果Prompt允许）。

**使用 LangChain Expression Language (LCEL) 构建更灵活的 RAG 链**

LCEL 提供了更灵活和声明式的方式来构建链。下面是如何用 LCEL 实现相似的 RAG 逻辑：

```python
# ... (前面的步骤：加载文档、分割、初始化 embeddings, vector_store, llm, retriever 保持不变) ...

# 确保执行了前面的步骤以创建 retriever 和 llm

# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate

# # 定义 LCEL RAG 链
# print("\n--- 使用 LCEL 构建 RAG 链 ---")

# # 1. 定义 Prompt 模板 (与之前类似，但更适合 Chat Models)
# template = """基于以下上下文信息回答问题:
# {context}

# 问题: {question}
# """
# prompt = ChatPromptTemplate.from_template(template)

# # 2. 定义 RAG 链
# # RunnablePassthrough.assign 会将 retriever 的输出 (文档列表) 赋值给 context 变量
# # StrOutputParser 用于解析 LLM 的输出为字符串

# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)

# rag_chain_lcel = (
#     {"context": retriever | format_docs, "question": RunnablePassthrough()}
#     | prompt
#     | llm
#     | StrOutputParser()
# )

# print("LCEL RAG 链创建成功！")

# # 使用 LCEL RAG 链提问
# query_lcel = "阿里云百炼有哪些特点？" # 可以用知识库中的问题测试
# print(f"\n--- 正在使用 LCEL RAG 链提问: {query_lcel} ---")
# try:
#     answer = rag_chain_lcel.invoke(query_lcel)
#     print("\n模型回答 (LCEL):")
#     print(answer)

#     # 如果需要源文档，可以单独调用 retriever
#     # relevant_docs = retriever.invoke(query_lcel)
#     # print("\n相关源文档块 (LCEL):")
#     # for i, doc in enumerate(relevant_docs):
#     #     print(f"  源文档 {i+1}: {doc.page_content[:100]}...")

# except Exception as e:
#     print(f"处理 LCEL RAG 问题时出错: {e}")

```
你可以将这段 LCEL 代码添加到 `main` 函数的末尾（在 `RetrievalQA` 示例之后）来体验。注意，`RunnablePassthrough()` 会将原始输入（这里是问题字符串）传递下去。`retriever | format_docs` 表示先用 `retriever` 获取文档，然后用 `format_docs` 函数处理文档列表。

**重要注意事项和进阶**

* **模型选择**: `embedding_model_name` 和 `llm_model_name` 的选择对效果至关重要。请参考阿里云百炼和 DashScope 的最新文档，选择适合你场景和预算的模型。
* **错误处理**: 实际应用中需要更健壮的错误处理，例如 API 调用失败、模型限流等。
* **Prompt 工程**: `prompt_template` 的设计对 RAG 的性能影响很大。可以尝试不同的表述方式、指令、或者加入 few-shot示例。
* **文档处理**: 对于复杂的文档（如 PDF、Word、HTML），`TextLoader` 可能不够。可以使用 `UnstructuredFileLoader`、`PyPDFLoader` 等更专业的加载器。
* **文本分割策略**: `chunk_size` 和 `chunk_overlap` 的设置会影响检索效果。需要根据文档特性进行调整。
* **向量数据库**: `FAISS` 适合快速开始。对于生产环境，可以考虑更持久化、可扩展的向量数据库，如 Milvus, PGVector, ChromaDB, Weaviate 等，Langchain 对它们都有集成。
* **检索策略**: `as_retriever(search_kwargs={"k": 3})` 中的 `k` 值表示检索最相关的多少个文档块。可以调整此参数。还有其他检索策略，如 MMR (Maximal Marginal Relevance) 等。
* **异步和流式处理**: 对于需要高并发或实时响应的应用，可以研究 Langchain 和 DashScope SDK 的异步调用和流式输出功能。
* **成本**: 调用 Embedding 模型和 LLM 模型都会产生费用。请关注阿里云百炼的计费策略。

希望这个详细的教程能帮助你成功使用 Langchain 和阿里云百炼模型构建 RAG 应用！







## **总结与进一步学习**

本教程涵盖了使用 Langchain 构建 RAG 应用的基本步骤和核心组件。您可以基于此进行扩展和优化，例如：

* **尝试不同的文档加载器**：加载网页、数据库、Notion 等。
* **优化文本分割策略**：根据文档特性调整 `chunk_size` 和 `chunk_overlap`，或使用更高级的分割器。
* **使用不同的嵌入模型和向量存储**：例如 Hugging Face 的嵌入模型，FAISS 或 Pinecone 向量数据库。
* **探索更高级的检索策略**：例如使用 ParentDocumentRetriever, SelfQueryRetriever, EnsembleRetriever 等。
* **优化提示工程 (Prompt Engineering)**：精心设计的提示可以显著提高 LLM 的回答质量。
* **实现聊天历史记录**：构建一个可以进行多轮对话的 RAG 应用。
* **评估 RAG 系统**：使用评估指标来衡量 RAG 系统的性能。

Langchain 的文档非常丰富，是进一步学习的好资源：[https://python.langchain.com/](https://python.langchain.com/)

希望这个详细的教程对您有所帮助！如果您有任何问题，欢迎随时提出。