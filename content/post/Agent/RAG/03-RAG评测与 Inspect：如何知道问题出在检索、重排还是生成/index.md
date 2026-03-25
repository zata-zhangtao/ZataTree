---
title: RAG评测与 Inspect：如何知道问题出在检索、重排还是生成
description: 很多 RAG 系统不是不能用，而是出了问题后不知道该怎么定位。本文讲清楚评测、Inspect 和可观测性该怎么做。
date: 2026-03-25T15:50:00+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - RAG
    - Evaluation
    - Observability
---

很多 RAG 项目最开始都能跑起来，但一到线上就会卡在一个非常现实的问题上：

用户说答案不对，可你根本不知道问题出在：

1. 没召回到正确内容
2. 召回到了，但排序不对
3. 排好了，但没进最终 prompt
4. 进了 prompt，但模型没用
5. 模型用了，但引用展示错了

所以 RAG 一定不能只做“生成结果观测”，还要做“阶段化 inspect”。

## 一、先把错误分层

调 RAG 时，建议固定使用下面这套分层框架。

### 1. 检索层错误

表现：

- 正确 chunk 根本不在候选里
- top_k 很低
- keyword 类查询表现差
- source 过滤不对

### 2. 重排层错误

表现：

- 正确 chunk 在原始候选里
- 但精排后位置太靠后
- 最终没进 prompt

### 3. Prompt 组装层错误

表现：

- 正确 chunk 已经进入最终结果
- 但被截断、去重或顺序处理掉了

### 4. 生成层错误

表现：

- 证据在 prompt 里
- 模型还是答错，或者无视证据自由发挥

如果不先分层，后续所有优化都容易变成盲改。

## 二、RAG 的 inspect 页面应该看到什么

很多系统的 debug 只显示一个最终答案，这远远不够。

一个真正有用的 inspect 页面，最好至少包含这些信息。

### 1. 输入侧

- 用户原始 query
- query rewrite 后的 query
- query 分类结果
- 使用了哪些过滤条件

### 2. 检索侧

- active sources
- 每个 source 的文档数和可见向量数
- 原始候选列表
- 每个候选的分数
- 候选的 document / chunk / metadata

### 3. 重排侧

- rerank 输入候选
- rerank 输出排序
- 前后位次变化
- 被丢弃的原因

### 4. Prompt 组装侧

- 哪些 chunk 最终进入 prompt
- 总长度 / token 预算
- 是否发生截断
- 去重规则是否生效
- 最终 prompt 快照

### 5. 生成侧

- 最终答案
- 使用的模型
- 引用 chunk 列表
- 答案和证据的一致性判断

## 三、离线评测应该怎么做

很多团队一开始只看“主观体验”，但主观体验很难支撑稳定迭代。

离线评测至少要准备一套数据集，里面包含：

- 用户问题
- 标准答案
- 可接受答案
- 期望命中的证据 chunk 或 document

### 检索层指标

最基础的是：

- Recall@K
- Precision@K
- MRR
- NDCG

这些指标回答的问题是：检索系统有没有把正确证据找回来，以及排得够不够靠前。

### 生成层指标

常见做法包括：

- Exact Match
- F1
- LLM-as-a-Judge
- 引用一致性
- 忠实性 / 幻觉率

### 为什么要把检索层和生成层分开

因为“答案错”这个结果可能来自完全不同的原因。

例如：

- 检索 Recall 很低，那应该优先调 chunking 和召回
- 检索 Recall 很高，但答案仍差，应该看 rerank、prompt 和模型输出约束

## 四、在线观测该怎么做

离线评测解决“系统总体质量”，在线观测解决“某次请求为什么出错”。

在线 trace 最好以一次请求为单位，拆成多个 span：

1. retrieval_query
2. retrieval_candidates
3. rerank_input
4. rerank_output
5. prompt_assembly
6. llm_generation
7. postprocess

这样做的好处是：

- 你能看见每一步输入输出
- 能定位延迟集中在哪
- 能做分阶段评分
- 能把用户反馈挂到具体 trace 上

## 五、给 trace 打分，而不是只给最终答案打分

很多团队只给最终答案打一个“好/坏”的标签，这不够。

更推荐的是多层评分：

### trace 级评分

- 整体答案质量
- 用户满意度

### observation 级评分

- retrieval relevance
- rerank quality
- citation coverage
- grounding quality

这样你后面做回归分析时，才能知道到底是哪一层退化了。

## 六、一个实用的排障流程

当你发现某个问题回答不对时，可以按下面这个顺序查：

### 第一步：看 active source 是否正确

先确认知识边界没错。

### 第二步：看原始候选里有没有正确 chunk

如果没有，优先怀疑：

- chunking
- embedding
- 检索策略
- metadata 过滤

### 第三步：看 rerank 前后位次变化

如果有正确 chunk，但被排后面了，就看重排策略。

### 第四步：看最终 prompt

如果正确 chunk 在候选里，也在重排里，但没进 prompt，问题在上下文组装。

### 第五步：看答案引用和生成结果

如果 prompt 正确，答案仍然错，就要看模型是否真正利用了证据。

## 七、一个建议落地的 inspect 数据结构

你可以给每次请求保留一个结构化记录：

```json
{
  "query": "...",
  "filters": {},
  "raw_candidates": [],
  "reranked_candidates": [],
  "prompt_chunks": [],
  "prompt_length": 0,
  "answer": "...",
  "citations": [],
  "scores": {
    "retrieval_recall": null,
    "grounding": null,
    "answer_quality": null
  }
}
```

这样无论你用 LangSmith、Langfuse，还是自己做后台页面，都会方便很多。

## 八、RAG 团队最容易忽视的 3 件事

### 1. 只做“能看 trace”，不做“可操作诊断”

真正有用的 inspect 不只是展示数据，更要直接回答：

- 为什么没召回
- 为什么被过滤
- 为什么没进 prompt

### 2. 只评测最终答案，不评测检索

这样你会很难判断优化方向。

### 3. 没有固定 benchmark

没有一组长期稳定的问题集，你很难证明系统是在进步，而不是“这次感觉好一点”。

## 九、本文小结

RAG 要想可迭代，必须同时具备三样东西：

1. 分层 inspect
2. 离线评测
3. 在线 trace

只有这样，你才能从“会用”走到“会调”。

下一篇会继续讲生产环境里最常见的坑，以及一条更稳的优化路线。
