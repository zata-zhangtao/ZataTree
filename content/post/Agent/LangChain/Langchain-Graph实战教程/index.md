---
title: Langchain-Graph实战教程
description: ""
date: 2025-05-06T11:07:13+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---


**什么是 Langchain GRAPH？**

Langchain GRAPH 是 Langchain 框架中用于处理和操作知识图谱（Knowledge Graphs）的模块。知识图谱是一种用节点（entities）和边（relationships）来表示知识的结构化方式。Langchain GRAPH 可以帮助你：

* **构建知识图谱：** 从文本、数据库或其他来源提取信息并构建知识图谱。
* **查询知识图谱：** 使用自然语言或结构化查询来检索知识图谱中的信息。
* **知识图谱增强的问答：** 将知识图谱与大型语言模型（LLM）结合，以提供更准确、更具上下文的答案。
* **推理：** 在知识图谱上进行推理，发现新的关系或知识。

**核心概念**

* **Graph Store (图存储):** 用于存储和管理知识图谱数据的后端。常见的有 Neo4j, NebulaGraph, Kùzu 等。Langchain 也支持内存中的 `NetworkXEntityGraph` 用于快速原型设计。
* **Graph Document Loader (图文档加载器):** 用于从不同来源（如文本文件、网页、数据库）加载数据并转换为图结构。
* **Graph Transformer (图转换器):** 用于将加载的文档转换为图谱中的节点和关系。通常会利用 LLM 来识别实体和关系。
* **Graph Cypher QA Chain (图 Cypher 问答链):** 允许你使用自然语言提问，该链会将问题转换为 Cypher (一种图查询语言，常用于 Neo4j 等图数据库)，然后在图上执行查询并返回结果。
* **Knowledge Graph Index (知识图谱索引):** 用于将知识图谱集成到检索增强生成 (RAG) 流程中，使 LLM 能够利用图谱中的信息。

**与阿里云百炼平台的模型结合**

阿里云百炼平台提供了多种强大的大语言模型，我们可以将这些模型用于 Langchain GRAPH 中的以下任务：

* **实体提取 (Entity Extraction):** 从文本中识别出关键的实体（如人名、地名、组织机构名等）。
* **关系提取 (Relationship Extraction):** 识别实体之间的关系。
* **自然语言理解 (NLU):** 理解用户用自然语言提出的关于图谱的问题。
* **答案生成 (Answer Generation):** 基于从图谱中检索到的信息生成自然的答案。

**代码实战：使用阿里云百炼模型构建和查询知识图谱**

在这个实战教程中，我们将演示如何：

1.  **设置环境：** 安装必要的库。
2.  **连接阿里云百炼模型：** 使用 Langchain 提供的接口连接百炼平台的 LLM。
3.  **准备数据：** 使用一些示例文本数据。
4.  **构建知识图谱：** 从文本中提取实体和关系，并构建一个内存中的知识图谱 (使用 `NetworkXEntityGraph` 作为示例，实际生产中推荐使用更专业的图数据库)。
5.  **查询知识图谱：** 使用自然语言进行提问。

**步骤 1: 设置环境**

首先，你需要安装 Langchain 和其他必要的库。

```bash
pip install langchain langchain-community langchain-experimental aiohttp neo4j networkx beautifulsoup4 tiktoken dashscope
```

* `langchain`, `langchain-community`, `langchain-experimental`: Langchain 核心库。
* `aiohttp`: 异步 HTTP 请求库，某些 Langchain 组件可能需要。
* `neo4j`: 如果你要使用 Neo4j 作为图存储，则需要安装。
* `networkx`: 用于在内存中创建和操作图。
* `beautifulsoup4`: 用于解析 HTML/XML，常用于从网页加载数据。
* `tiktoken`: OpenAI 的 tokenizer，Langchain 中常用。
* `dashscope`: 阿里云百炼 SDK。

**步骤 2: 连接阿里云百炼模型**

你需要拥有阿里云账号并开通百炼大模型服务，获取 API Key (DASHSCOPE_API_KEY)。

```python
import os
from langchain_community.llms import Tongyi
from langchain_community.graphs import NetworkXEntityGraph
from langchain.chains import GraphQAChain # 旧版本可能是 GraphCypherQAChain
from langchain.prompts import PromptTemplate
from langchain.indexes.graph import GraphIndexCreator # 旧版本可能是 GraphQAChain
from langchain.document_loaders import TextLoader # 示例使用文本加载器
from langchain_core.documents import Document

# 设置你的阿里云百炼 API Key
# 建议使用环境变量来管理 API Key
os.environ["DASHSCOPE_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx" # 替换为你的真实 API Key

# 初始化阿里云百炼模型
# 你可以选择不同的模型，例如 qwen-turbo, qwen-plus, qwen-max 等
# llm = Tongyi(model_name="qwen-turbo")
# 对于图构建中更复杂的实体和关系抽取，可能需要更高能力的模型
llm_for_graph_extraction = Tongyi(model_name="qwen-plus")
llm_for_qa = Tongyi(model_name="qwen-turbo") # 问答可以使用稍轻量的模型

print("阿里云百炼模型已初始化。")
```

**步骤 3: 准备数据**

我们使用一些简单的文本数据作为示例。你可以将其替换为更复杂的文档或从其他来源加载。

```python
# 示例文本数据
document_content = """
张三是北京大学的教授，他研究人工智能领域。
李四是张三的学生，他就读于清华大学，学习计算机科学。
北京大学和清华大学是中国顶尖的大学。
人工智能是计算机科学的一个重要分支。
王五是百度的工程师，百度是一家位于北京的科技公司，专注于人工智能。
张三和王五在一次人工智能会议上认识。
"""

# 将文本内容包装成 Langchain Document 对象
docs = [Document(page_content=document_content)]

print("示例文本数据已准备。")
```

**步骤 4: 构建知识图谱 (使用 NetworkXEntityGraph)**

我们将使用 `GraphIndexCreator` (或者旧版本中的直接使用 LLM 进行提取并手动添加到 Graph) 从文本中提取实体和关系，并构建一个内存中的知识图谱。

```python
from langchain.graphs.graph_document import GraphDocument, Node, Relationship
from langchain.chains.graph_qa.extract_triple import GraphTripleExtractionChain # 用于提取三元组

# 方法一：使用 GraphIndexCreator (较新的推荐方式)
# GraphIndexCreator 在内部会调用 LLM 进行实体和关系的提取
# 注意：GraphIndexCreator 的实现可能依赖于特定的 LLM 能力和提示工程

# graph_index_creator = GraphIndexCreator(llm=llm_for_graph_extraction) # 使用能力更强的模型进行抽取
# graph = graph_index_creator.graph_from_documents(docs)

# print("知识图谱 (使用 GraphIndexCreator) 构建完成。")
# print("节点数:", len(graph.get_schema()['nodes']))
# print("关系数:", len(graph.get_schema()['relationships']))
# print("图谱概要 (Schema):", graph.get_schema())


# 方法二：手动提取三元组并构建图 (更灵活，但更复杂)
# 这种方法可以让你更好地控制提取过程和自定义提示

# 定义节点和关系的类型 (可选，但有助于结构化)
# 这部分通常需要根据你的领域知识进行设计
allowed_nodes = ["Person", "Organization", "Location", "Field", "Concept", "Event"]
allowed_relationships = ["IS_A", "WORKS_AT", "STUDIES_AT", "LOCATED_IN", "FOCUSES_ON", "PART_OF", "MEETS_AT"]

# 创建一个空的 NetworkX 图
knowledge_graph = NetworkXEntityGraph()

# 使用 GraphTripleExtractionChain 提取三元组
# 你可能需要根据百炼模型的特点调整提示 (prompt)
# Langchain 默认的提示可能不是最优的
# 以下是一个简化的示例，实际中提示工程非常重要

# prompt_template_str = """
# 从以下文本中提取实体及其之间的关系。
# 仅提取文本中明确提到的实体和关系。
# 实体类型应尽可能具体，例如：Person, Organization, Location, Field, Concept, Event。
# 关系类型应描述实体间的联系，例如：IS_A, WORKS_AT, STUDIES_AT, LOCATED_IN, FOCUSES_ON, PART_OF, MEETS_AT。
# 以 (Head Entity, Relation, Tail Entity) 的格式输出三元组，每个三元组占一行。
# 如果没有找到三元组，则不输出任何内容。

# 示例：
# 文本: "爱因斯坦出生在德国。"
# 输出:
# (爱因斯坦, BORN_IN, 德国)

# 文本: "{text}"
# 输出:
# """
# extraction_prompt = PromptTemplate.from_template(prompt_template_str)

# triple_extractor = GraphTripleExtractionChain.from_llm(
# llm=llm_for_graph_extraction,
#     prompt=extraction_prompt
# )

# # 或者使用更通用的方式，让LLM直接生成图结构
# # 这通常需要更复杂的提示和后处理

# print("开始从文本中提取三元组...")
# extracted_knowledge = []
# for doc in docs:
# # 这种方式直接让LLM生成图谱结构，对于百炼模型可能需要特定的 Prompt
#     try:
# # 尝试让LLM直接生成 GraphDocument 格式
# # 这需要非常精巧的 Prompt Engineering，让模型理解输出的JSON结构
# # 这里我们简化处理，假设有一个函数能调用LLM并解析其输出为 GraphDocument
# # 实际中，你可能需要一个专门的 chain 来做这件事，该 chain 内部调用 LLM
# # 并将 LLM 的文本输出解析成 Node 和 Relationship 对象。

# # 简化的概念性代码：
#         response = llm_for_graph_extraction.invoke(
# f"""
# 分析以下文本，并将其转换为知识图谱。
# 节点应该包含 'id' (实体名称) 和 'type' (实体类型，例如：Person, Organization, Location, Field, Concept, Event)。
# 关系应该包含 'source' (源节点 id), 'target' (目标节点 id), 和 'type' (关系类型，例如：IS_A, WORKS_AT, STUDIES_AT, LOCATED_IN, FOCUSES_ON, PART_OF, MEETS_AT)。
# 请以JSON格式输出，包含一个 'nodes' 列表和一个 'relationships' 列表。

# 文本：
# {doc.page_content}

# JSON输出：
# """
# )
# # print("LLM原始输出:", response) # 调试用

# # 解析 LLM 的输出 (这里需要根据 LLM 的实际输出来编写解析逻辑)
# # 这是一个非常理想化的情况，通常LLM不会直接完美输出这个结构
# # 你可能需要使用 PydanticOutputParser 或类似的工具来确保输出格式
# # 这里我们手动构造一些示例 GraphDocument，模拟提取过程

# # 模拟提取结果：
#         nodes_data = [
#             Node(id="张三", type="Person"),
# Node(id="北京大学", type="Organization"),
# Node(id="人工智能", type="Field"),
# Node(id="李四", type="Person"),
# Node(id="清华大学", type="Organization"),
# Node(id="计算机科学", type="Field"),
# Node(id="中国", type="Location"),
# Node(id="王五", type="Person"),
# Node(id="百度", type="Organization"),
# Node(id="北京", type="Location"),
# Node(id="人工智能会议", type="Event")
# ]
#         rels_data = [
# Relationship(source=Node(id="张三", type="Person"), target=Node(id="北京大学", type="Organization"), type="WORKS_AT"),
# Relationship(source=Node(id="张三", type="Person"), target=Node(id="人工智能", type="Field"), type="STUDIES_FIELD"), # 或者 RESEARCHES
# Relationship(source=Node(id="李四", type="Person"), target=Node(id="张三", type="Person"), type="IS_STUDENT_OF"),
# Relationship(source=Node(id="李四", type="Person"), target=Node(id="清华大学", type="Organization"), type="STUDIES_AT"),
# Relationship(source=Node(id="李四", type="Person"), target=Node(id="计算机科学", type="Field"), type="STUDIES_FIELD"),
# Relationship(source=Node(id="北京大学", type="Organization"), target=Node(id="中国", type="Location"), type="LOCATED_IN"), # 假设关系
# Relationship(source=Node(id="清华大学", type="Organization"), target=Node(id="中国", type="Location"), type="LOCATED_IN"), # 假设关系
# Relationship(source=Node(id="人工智能", type="Field"), target=Node(id="计算机科学", type="Field"), type="IS_BRANCH_OF"),
# Relationship(source=Node(id="王五", type="Person"), target=Node(id="百度", type="Organization"), type="WORKS_AT"),
# Relationship(source=Node(id="百度", type="Organization"), target=Node(id="北京", type="Location"), type="LOCATED_IN"),
# Relationship(source=Node(id="百度", type="Organization"), target=Node(id="人工智能", type="Field"), type="FOCUSES_ON"),
# Relationship(source=Node(id="张三", type="Person"), target=Node(id="王五", type="Person"), type="MET_AT", properties={"event": "人工智能会议"}),
# ]
#         graph_doc = GraphDocument(nodes=nodes_data, relationships=rels_data, source=doc)
#         extracted_knowledge.append(graph_doc)
#         print(f"从文档中模拟提取了 {len(nodes_data)} 个节点和 {len(rels_data)} 个关系。")

#     except Exception as e:
# print(f"从文档提取三元组失败: {e}")
#         continue

# # 将提取的知识添加到图中
# for gd in extracted_knowledge:
#     knowledge_graph.add_graph_documents([gd])

# print("\n知识图谱 (手动提取并构建) 构建完成。")
# print("图谱 Schema:", knowledge_graph.schema)
# print("所有三元组 (Triples):")
# for triple in knowledge_graph.get_triples():
#     print(triple)

# --- 切换到更简单和推荐的 LLMGraphTransformer 方法 ---
from langchain_experimental.graph_transformers.llm import LLMGraphTransformer

# 使用 LLMGraphTransformer 进行图构建
# 这通常是更推荐的方式，因为它封装了复杂的提示工程
# 你可以传入 allowed_nodes 和 allowed_relationships 来指导提取过程
# 如果不传入，它会尝试自动识别

llm_transformer = LLMGraphTransformer(
    llm=llm_for_graph_extraction,
    allowed_nodes=allowed_nodes, # 可选
    allowed_relationships=allowed_relationships # 可选
    # prompt= # 你也可以自定义提示，但这通常比较复杂
)

print("开始使用 LLMGraphTransformer 从文档构建图谱...")
graph_documents = llm_transformer.convert_to_graph_documents(docs)
print(f"\n成功从文档转换了 {len(graph_documents)} 个 GraphDocument。")

# 将转换后的 GraphDocument 添加到 NetworkX 图中
# 创建一个新的 NetworkXEntityGraph 实例来存储最终的图
final_graph = NetworkXEntityGraph()
final_graph.add_graph_documents(graph_documents)

print("\n知识图谱 (使用 LLMGraphTransformer) 构建完成。")
print("图谱 Schema:", final_graph.schema) # final_graph.schema 可能不直接显示所有节点和关系，取决于其内部实现
print("所有提取的三元组 (Triples):")
for triple in final_graph.get_triples():
    print(triple)

# 你也可以直接查看 NetworkX 图的节点和边
print(f"\nNetworkX 图中的节点数: {final_graph.graph.number_of_nodes()}")
print(f"NetworkX 图中的边数: {final_graph.graph.number_of_edges()}")
# print("节点:", list(final_graph.graph.nodes(data=True))) # 打印节点及其属性
# print("边:", list(final_graph.graph.edges(data=True)))   # 打印边及其属性
```

**重要提示关于图构建：**

* **提示工程 (Prompt Engineering):** 使用 LLM 进行实体和关系提取时，提示的设计至关重要。你需要仔细设计提示，以便模型能够准确地识别出你感兴趣的实体类型和关系类型。对于百炼模型，你可能需要根据其特性进行特定的优化。
* **LLMGraphTransformer：** 这是目前 Langchain 中推荐的用于从文档构建图谱的方式。它内部处理了与 LLM 的交互和提示。你可以通过 `allowed_nodes` 和 `allowed_relationships` 参数来指导提取过程，使其更符合你的需求。如果不提供这些参数，Transformer 会尝试自动推断。
* **迭代和评估：** 图构建通常是一个迭代的过程。你需要不断评估提取的质量，并根据需要调整提示或使用的模型。
* **PydanticOutputParser:** 对于更复杂的提取任务，并希望LLM输出结构化的JSON，可以考虑使用 `PydanticOutputParser` 来定义期望的输出模式，并解析LLM的输出。
* **错误处理和鲁棒性：** 在实际应用中，LLM的输出可能并不总是完美的。你需要添加错误处理逻辑来处理不符合预期格式或不准确的提取结果。

**步骤 5: 查询知识图谱**

现在我们已经有了一个知识图谱，可以使用 `GraphQAChain` (或旧版本的 `GraphCypherQAChain`，但对于内存中的 `NetworkXEntityGraph`，通常是前者或直接的图遍历/查询) 来用自然语言提问。

```python
# 对于 NetworkXEntityGraph，我们通常不直接使用 Cypher 查询。
# GraphQAChain 会尝试理解问题，并在图上查找相关信息，然后用LLM生成答案。

# 创建 GraphQAChain
# 注意：对于 NetworkXEntityGraph，GraphQAChain 的行为可能与基于 Cypher 的图数据库不同。
# 它更多的是利用图的结构进行上下文检索，然后让 LLM 回答。

graph_qa_chain = GraphQAChain.from_llm(
    llm=llm_for_qa,  # 用于生成答案的 LLM
    graph=final_graph, # 我们构建的图
    verbose=True  # 打印中间步骤，便于调试
)

# 提出问题
questions = [
    "张三是做什么工作的？",
    "谁是张三的学生？",
    "李四在哪里学习？",
    "百度公司专注于哪个领域？",
    "张三和王五是在哪里认识的？",
    "列出所有的人物和他们的职业或研究领域。",
    "北京大学和清华大学位于哪个国家？"
]

for question in questions:
    print(f"\n问题: {question}")
    try:
        answer = graph_qa_chain.run(question) # 或者使用 .invoke({"query": question})
        print(f"答案: {answer}")
    except Exception as e:
        print(f"回答问题时出错: {e}")
        # 对于 NetworkXEntityGraph，如果 GraphQAChain 内部尝试生成 Cypher，可能会出错。
        # 可以尝试直接从图中提取信息并让LLM总结。

# 如果 GraphQAChain 对于 NetworkXEntityGraph 支持不佳，或你想更直接地控制：
# 可以先从图中检索相关三元组，然后将这些信息作为上下文喂给 LLM 进行问答。

print("\n--- 使用检索到的上下文进行问答 (备选方案) ---")

def get_relevant_triples(graph, entity_name):
    """一个简单的函数，用于检索与某个实体相关的三元组"""
    relevant_triples_str = []
    for s, p, o in graph.get_triples():
        if entity_name in str(s) or entity_name in str(o):
            relevant_triples_str.append(f"({s}, {p}, {o})")
    return "\n".join(relevant_triples_str)

qa_prompt_template = """根据下面提供的知识图谱信息回答问题。
如果信息不足，请回答“根据已知信息无法回答”。

知识图谱信息：
{context}

问题：{question}
答案："""
qa_prompt = PromptTemplate(template=qa_prompt_template, input_variables=["context", "question"])
qa_chain_with_context = qa_prompt | llm_for_qa

for question in questions:
    print(f"\n问题: {question}")
    # 尝试从问题中提取关键实体 (这本身也可以用LLM完成)
    # 简化的实体提取：
    main_entity = ""
    if "张三" in question: main_entity = "张三"
    elif "李四" in question: main_entity = "李四"
    elif "百度" in question: main_entity = "百度"
    # ... 可以扩展这个逻辑

    if main_entity:
        context_triples = get_relevant_triples(final_graph, main_entity)
        if not context_triples:
            context_triples = "没有找到与该实体直接相关的明确信息。"
    else: # 如果没有明显实体，可以尝试提供所有三元组或一个子集
        context_triples = "\n".join([f"({s}, {p}, {o})" for s, p, o in final_graph.get_triples()[:20]]) # 限制上下文长度

    print(f"提供的上下文: \n{context_triples[:500]}...") # 打印部分上下文
    try:
        answer = qa_chain_with_context.invoke({"context": context_triples, "question": question})
        print(f"答案 (使用上下文): {answer}")
    except Exception as e:
        print(f"回答问题时出错 (使用上下文): {e}")
```

**关于查询的说明:**

* `GraphQAChain`: 当与支持 Cypher 的图数据库（如 Neo4j）一起使用时，`GraphQAChain` (特别是 `GraphCypherQAChain`) 会将自然语言问题转换为 Cypher 查询，在图数据库上执行，然后将结果传递给 LLM 以生成最终答案。对于内存中的 `NetworkXEntityGraph`，其行为可能更多是基于关键词匹配或简单的图遍历来提取上下文，然后由 LLM 回答。
* **上下文检索:** 对于复杂的查询或 `NetworkXEntityGraph`，一种更可靠的方法是先设计一个检索步骤：识别问题中的核心实体，从图中检索与这些实体相关的子图或三元组，然后将这些信息作为上下文提供给 LLM 来回答问题。
* **LLM 的角色:** 在查询阶段，LLM 不仅用于理解问题，也用于根据检索到的图信息生成流畅、自然的答案。

**使用专业的图数据库 (例如 Neo4j)**

虽然上面的示例使用了内存中的 `NetworkXEntityGraph`，但在生产环境中，你通常会使用更强大、持久化的图数据库，如 Neo4j。

**使用 Neo4j 的大致流程：**

1.  **安装和启动 Neo4j 服务。**
2.  **安装 Python 的 Neo4j驱动：** `pip install neo4j`
3.  **连接到 Neo4j：**
    ```python
    from langchain_community.graphs import Neo4jGraph

    graph_db = Neo4jGraph(
        url="bolt://localhost:7687", # Neo4j 的 Bolt URL
        username="neo4j",           # 用户名
        password="your_password"    # 密码
    )
    # 可以清除现有数据（可选，用于测试）
    # graph_db.query("MATCH (n) DETACH DELETE n")
    ```
4.  **构建图谱：**
    * 你可以使用 `LLMGraphTransformer` 将文档转换为 `GraphDocument` 对象。
    * 然后使用 `graph_db.add_graph_documents(graph_documents)` 将这些结构化数据存入 Neo4j。Neo4jGraph 会自动将这些 GraphDocument 转换为 Cypher `CREATE` 语句并执行。
    * 你也可以直接构造 Cypher 语句来创建节点和关系。
5.  **查询图谱：**
    * 使用 `GraphCypherQAChain` (如果你的 Langchain 版本较旧) 或更新的 `GraphQAChain` 配置为使用 Cypher。
    * 这个链会将自然语言问题转换为 Cypher 查询。
    ```python
    from langchain.chains import GraphCypherQAChain # 或者更新的 GraphQAChain

    # qa_chain = GraphCypherQAChain.from_llm(
    #     cypher_llm=llm_for_qa, # LLM 用于生成 Cypher
    #     qa_llm=llm_for_qa,     # LLM 用于从 Cypher 结果生成答案
    #     graph=graph_db,
    #     verbose=True,
    #     # validate_cypher=True, # 验证生成的 Cypher 语句
    # )
    # 或者使用更新的 API，可能需要指定 GraphDBType
    from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain as UpdatedGraphCypherQAChain

    # 对于较新版本的 Langchain，可能会有不同的初始化方式或推荐的 Chain
    # 检查 Langchain 文档以获取最新的 GraphCypherQAChain 用法

    # 假设我们有一个可以生成 Cypher 的 LLM 和一个可以从结果回答问题的 LLM
    # (这里简化，两者都用 llm_for_qa)
    cypher_generation_llm = llm_for_qa
    qa_llm = llm_for_qa

    chain = UpdatedGraphCypherQAChain.from_llm(
        graph=graph_db,
        cypher_llm=cypher_generation_llm,
        qa_llm=qa_llm,
        validate_cypher=True, # 推荐在开发时开启
        verbose=True
    )

    # question = "张三研究什么领域？"
    # result = chain.invoke({"query": question})
    # print(result["result"])
    ```
    * **Cypher 生成的挑战：** 让 LLM 准确生成符合你的图谱 Schema 的 Cypher 查询可能具有挑战性，需要良好的提示工程和图谱 Schema 的描述。`GraphCypherQAChain` 内部包含提示来指导 LLM 根据图的 Schema 生成 Cypher。你需要确保 `graph_db.schema` (或通过 `refresh_schema=True` 更新的 schema) 对 LLM 可见且准确。

**总结与进一步探索**

* **选择合适的图存储：** 对于小型实验，`NetworkXEntityGraph` 很方便。对于生产应用，应选择专业的图数据库（Neo4j, NebulaGraph, Amazon Neptune, Kùzu 等）。
* **Prompt Engineering is Key：** 无论是实体/关系提取还是 Cypher 生成，提示的质量都直接影响结果。针对阿里云百炼模型，你可能需要进行特定的提示词优化。
* **Schema 设计：** 一个良好定义的图谱 Schema (节点标签、属性、关系类型) 对于后续的查询和分析至关重要。
* **评估与迭代：** 构建和查询知识图谱是一个迭代的过程。你需要持续评估提取的准确性、图谱的完整性以及查询的性能和结果质量。
* **高级特性：**
    * **Graph RAG (Retrieval Augmented Generation):** 将知识图谱作为上下文信息源，增强 LLM 的问答能力。`KnowledgeGraphIndex` 可以用于此目的。
    * **复杂推理：** 在图上执行更复杂的推理任务，例如路径查找、社区检测、链接预测等。
    * **多跳查询 (Multi-hop Queries):** 回答需要连接多个信息片段才能得到的复杂问题。

这个教程提供了一个基础的框架。在实际应用中，你可能需要根据你的具体需求和数据特性进行大量的定制和优化。祝你在使用 Langchain GRAPH 和阿里云百炼模型构建知识图谱的旅程中顺利！