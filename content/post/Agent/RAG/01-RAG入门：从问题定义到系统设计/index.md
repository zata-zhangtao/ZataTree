---
title: RAG入门：从问题定义到系统设计
description: 从0到1理解 RAG 的目标、核心组件、数据流，以及第一版系统应该如何落地。
date: 2026-03-25T15:40:00+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - RAG
    - LLM
---

RAG，全称 Retrieval-Augmented Generation，核心思想其实很朴素：不要把所有知识都塞进模型参数里，而是在回答问题前，先从外部知识库里把最相关的信息找出来，再交给模型生成答案。

这套方法之所以重要，是因为纯大模型回答经常会遇到三类问题：

1. 知识过期，模型不知道最新信息。
2. 专有知识太细，训练时根本没覆盖。
3. 回答看起来很像对的，但实际上是幻觉。

RAG 的目标不是让模型“更聪明”，而是让系统“更可控”。你把知识更新、答案依据、召回范围、调试手段都从模型参数里解耦了出来。

## 一、一个最小可用 RAG 系统长什么样

最小版本通常包含 5 个部分：

1. 文档接入：把 PDF、Markdown、网页、数据库记录等内容收集进来。
2. 文本切分：把长文档拆成适合检索的小块。
3. 向量化与索引：为 chunk 生成 embedding，写入向量库。
4. 查询检索：用户提问后，检索最相关的若干 chunk。
5. 答案生成：把问题和检索结果一起交给 LLM 生成答案。

可以用一句伪代码概括：

```python
query = user_question
retrieved_chunks = retrieve(query)
prompt = build_prompt(query, retrieved_chunks)
answer = llm.generate(prompt)
```

这只是开始。真正决定 RAG 好不好用的，往往不是“有没有向量库”，而是下面这些设计细节：

- chunk 怎么切
- metadata 怎么建
- 检索是 dense、sparse 还是 hybrid
- 是否需要 rerank
- 上下文预算怎么控制
- 如何评测和排查问题

## 二、RAG 的系统视角

做 RAG 时，最好把系统拆成三条链路来看。

### 1. Ingestion 链路

负责让知识真正进入系统。

典型步骤：

1. 文档抽取文本
2. 清洗脏数据
3. 分块
4. 给每个 chunk 补充 metadata
5. 生成 embedding
6. 写入向量库和原文存储

建议至少保存这些字段：

- `document_id`
- `chunk_id`
- `source`
- `title`
- `section`
- `chunk_index`
- `content`
- `embedding_model`
- `created_at`
- `updated_at`

如果你一开始就把 metadata 设计好，后面做过滤检索、权限隔离、来源展示、增量更新会轻松很多。

### 2. Retrieval 链路

负责把“用户问的问题”变成“系统能找到的证据”。

这一层最重要的问题不是“能不能搜到”，而是：

- 能不能稳定搜到
- 能不能在噪声少的前提下搜到
- 能不能解释为什么搜到或没搜到

### 3. Generation 链路

负责把证据组织成模型真正能用的 prompt。

很多系统的问题不在检索，而在生成：

- 检索到了，但 prompt 组装混乱
- chunk 太多，模型忽略中间内容
- 没有引用约束，模型继续自由发挥

所以 RAG 从来不只是检索系统，它是“检索 + prompt 组装 + 答案约束”的组合工程。

## 三、第一版系统应该怎么做

如果你是从零开始，不建议一上来就追求最复杂的架构。第一版更应该追求“路径可解释”。

推荐起步配置：

1. 文档清洗后做规则化 chunking。
2. 每个 chunk 保存清晰 metadata。
3. 先做 dense retrieval。
4. 召回结果保留原始分数和来源信息。
5. prompt 中强制模型优先依据检索结果回答。
6. 输出里带来源或引用。
7. 先把 debug 页面做好，再追求更复杂的召回策略。

第一版最常见的错误是：

- 上来就把所有内容丢进向量库
- chunk 规则非常随意
- 检索参数硬编码
- 没有离线测试集
- 答案错了也不知道是检索错、prompt 错，还是模型错

## 四、什么时候应该用 RAG，而不是微调

RAG 更适合这些情况：

- 知识会变，甚至每天都变
- 你希望回答能追溯来源
- 你的领域知识规模大，但结构相对稳定
- 你不想频繁重训模型

微调更适合这些情况：

- 任务格式固定
- 需要模型稳定掌握某种输出风格
- 你优化的是“行为模式”，不是“事实知识”

很多业务其实不是二选一，而是两者结合：

- 用微调解决输出格式、风格、工具使用习惯
- 用 RAG 提供最新事实和业务知识

## 五、做 RAG 时最值得优先想清楚的 5 个问题

### 1. 你的知识边界是什么

不要把所有内容都放进一个集合里。要先定义：

- 哪些内容是知识库
- 哪些内容只是日志
- 哪些内容需要权限隔离
- 哪些内容应该单独建 source

### 2. 用户问题长什么样

如果用户问题多数是关键词式查询、实体查询、编号查询，那么单纯 dense 检索通常不够，后面大概率要补 sparse 或 hybrid。

### 3. 答案是否必须可追溯

如果业务要求“必须给出依据”，那引用、chunk 元数据、prompt 约束和 inspect 工具都应该在第一版就设计进去。

### 4. 你的更新频率多高

如果知识每天变化，增量摄取、版本管理、旧向量失效、重建索引这些事情都要提前想。

### 5. 你如何判断系统变好了

没有评测集的 RAG，优化往往会变成主观感觉。你需要尽早准备一组问题和期望证据，至少能观察：

- Recall@K
- 最终答案是否正确
- 是否引用了正确来源

## 六、一个推荐的演进路线

### 阶段 1：可用

- 文档导入
- chunk
- embedding
- dense 检索
- 引用展示

### 阶段 2：可调

- metadata 过滤
- query debug
- 候选集检查
- top_k 和阈值调优

### 阶段 3：可优化

- hybrid retrieval
- rerank
- chunk contextualization
- 查询改写

### 阶段 4：可运营

- 离线评测
- 在线观测
- trace 级分析
- 版本对比

## 七、这组文章接下来会写什么

如果你准备继续深入，可以接着看后面三篇：

1. [RAG进阶：Chunking、召回、Hybrid Search 与 Rerank](../02-RAG进阶：Chunking、召回、Hybrid Search 与 Rerank/)
2. [RAG评测与 Inspect：如何知道问题出在检索、重排还是生成](../03-RAG评测与 Inspect：如何知道问题出在检索、重排还是生成/)
3. [RAG生产实践：常见坑、性能优化与迭代路线图](../04-RAG生产实践：常见坑、性能优化与迭代路线图/)

## 延伸阅读

- Anthropic: Contextual Retrieval
- OpenAI Cookbook: Doing RAG on PDFs using File Search in the Responses API
- Qdrant Docs: Hybrid Queries / Reranking Hybrid Search
