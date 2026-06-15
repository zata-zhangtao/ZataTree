---
title: RAGFlow 深度解析：为什么它是最值得关注的 RAG 开源项目
description: RAGFlow 不只是另一个 RAG 框架，它的核心价值在于 DeepDoc 文档理解引擎和开箱即用的企业级设计。
date: 2026-03-25T16:00:00+08:00
image: images/index.png
categories:
    - Agent
tags:
    - RAG
    - RAGFlow
    - OpenSource
---

过去两年，RAG 领域涌现了无数框架：LangChain、LlamaIndex、Haystack……它们各有侧重，但解决的核心问题相似——如何让 LLM 接地气。

但如果你实际做过企业级 RAG 项目，会发现一个被忽视的问题：**文档解析**。

大部分框架默认你已经有干净、结构化的文本。现实却是：PDF 扫描件、嵌套表格、数学公式、多栏排版……这些"脏活累活"往往占据项目 60% 以上的时间。

RAGFlow 的定位很明确：**从文档到答案的全流程解决方案**，而不是又一个"需要你自己处理文档"的检索框架。

这篇文章会深入分析 RAGFlow 的设计思路、核心技术和适用场景。

## 一、RAGFlow 的差异化定位

### 现有框架的盲区

LangChain 和 LlamaIndex 的设计假设是：

```
输入：干净的文本 / 简单的 PDF
处理：Chunk → Embed → Retrieve → Generate
输出：答案
```

但企业真实场景是：

```
输入：扫描件 PDF、带表格的年报、技术手册、合同......
预处理：OCR、布局分析、表格识别、公式识别......
处理：Chunk → Embed → Retrieve → Generate
输出：答案 + 引用
```

**预处理阶段的复杂度，往往被框架忽略。**

### RAGFlow 的思路

RAGFlow 的核心定位：

```
不只是 RAG 框架，而是"文档理解 + RAG"的一体化方案
```

它的技术栈覆盖：

| 阶段 | 能力 | 技术方案 |
|------|------|----------|
| 文档解析 | OCR、布局分析、表格识别 | DeepDoc（自研） |
| 文档切分 | 8 种切分策略 | 按文档类型选择 |
| 检索 | 向量 + 关键词 + Rerank | 混合检索 + RRF 融合 |
| 生成 | 多模型支持 | OpenAI、Qwen、Ollama 等 |
| 运维 | 可视化 UI、API、监控 | 企业级特性 |

**一句话总结**：RAGFlow 解决的是"从 PDF 到答案"的完整链路，而不是"从文本到答案"。

## 二、DeepDoc：RAGFlow 的核心护城河

DeepDoc 是 RAGFlow 自研的文档理解引擎，也是它区别于其他框架的核心竞争力。

### 为什么需要 DeepDoc

传统 PDF 解析的问题：

**问题 1：OCR 质量差**

```
原文：错误码 E0028
OCR 结果：错误码 E002B（8 被识别成 B）

用户问：错误码 E0028 是什么意思
检索：找不到（因为文档里是 E002B）
```

**问题 2：布局信息丢失**

```
原文（两栏排版）：
┌──────────────┬──────────────┐
│ 左栏内容      │ 右栏内容      │
│ 跨多行...    │ 跨多行...    │
└──────────────┴──────────────┘

普通解析结果：
左栏内容
右栏内容  ← 两栏混在一起，语义被打断
```

**问题 3：表格结构破坏**

```
原文表格：
┌────────┬────────┬────────┐
│ 参数    │ 类型    │ 说明    │
├────────┼────────┼────────┤
│ timeout│ int    │ 超时时间│
│ retry  │ bool   │ 是否重试│
└────────┴────────┴────────┘

普通解析结果：
参数 类型 说明 timeout int 超时时间 retry bool 是否重试
← 变成一行，结构全丢了
```

### DeepDoc 的技术方案

```
DeepDoc Pipeline：

┌──────────┐    ┌──────────┐    ┌──────────────┐
│  Input   │───▶│  Layout  │───▶│   OCR Engine │
│  File    │    │  Analysis│    │  (PaddleOCR) │
└──────────┘    └──────────┘    └──────┬───────┘
                                       │
                ┌──────────────────────┘
                ▼
┌──────────────────────────────────────────────┐
│           Structure Recognition               │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐  │
│  │  Table   │ │  Figure  │ │   Formula    │  │
│  │  Parser  │ │  Parser  │ │   Parser     │  │
│  └──────────┘ └──────────┘ └──────────────┘  │
└──────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│           Semantic Understanding              │
│  • 标题识别                                   │
│  • 章节分割                                   │
│  • 关系提取                                   │
└──────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│           Markdown / Structured Output        │
└──────────────────────────────────────────────┘
```

**核心技术点**：

| 模块 | 技术方案 | 解决的问题 |
|------|----------|-----------|
| **OCR** | PaddleOCR | 高精度文字识别 |
| **布局分析** | YOLO/LayoutLM | 检测文本、表格、图片区域 |
| **表格识别** | Table-Transformer | 还原表格结构 |
| **公式识别** | LaTeX-OCR | 数学公式转 LaTeX |
| **图片描述** | VLM | 生成图片文字描述 |

### 表格识别的原理

表格是最难处理的文档元素之一。DeepDoc 的表格识别流程：

```
Step 1: 表格检测
用目标检测模型定位表格区域

Step 2: 结构识别
Table-Transformer 识别：
- 行边界
- 列边界
- 单元格合并关系

Step 3: 内容识别
对每个单元格做 OCR

Step 4: 结构化输出
┌────────┬────────┐
│ A1     │ A2     │   →   [{"row":1,"col":1,"text":"A1"}, ...]
├────────┼────────┤
│ B1     │ B2     │
└────────┴────────┘
```

**为什么这件事重要**？

如果表格结构丢了，用户问"参数 timeout 的类型是什么"，系统找不到答案——因为表格已经变成一团乱码。

### 与其他解析方案的对比

| 方案 | OCR | 布局分析 | 表格识别 | 公式识别 |
|------|-----|----------|----------|----------|
| PyPDF2 | ❌ | ❌ | ❌ | ❌ |
| pdfplumber | ❌ | ⚠️ 基础 | ⚠️ 基础 | ❌ |
| Unstructured | ⚠️ 外部 | ✅ | ⚠️ 基础 | ❌ |
| **DeepDoc** | ✅ | ✅ | ✅ | ✅ |

DeepDoc 是目前开源方案中对复杂文档支持最完整的。

## 三、Chunking 策略：一种文档一种切法

RAGFlow 提供了 8 种 Chunking 策略，针对不同文档类型：

### 为什么需要多种策略

不同类型文档的结构差异很大：

```
FAQ 文档：
Q: 问题
A: 答案
─────────
每个 QA 对是独立的语义单元

技术手册：
## 安装
步骤 1...
步骤 2...
## 配置
参数 1...
参数 2...
─────────
按章节切分，保留标题上下文

法律文档：
第一条 ...
第二条 ...
第三条 ...
─────────
按条款切分，每条有独立法律意义
```

用同一种"固定长度切分"处理所有文档，效果必然不好。

### RAGFlow 的 8 种策略

| 策略 | 适用文档 | 切分依据 |
|------|----------|----------|
| **Naive** | 简单文本 | 固定字符数 |
| **Q&A** | FAQ 文档 | 问题-答案对 |
| **Book** | 书籍、长文档 | 章节层级 |
| **Manual** | 技术手册 | 小节 |
| **Law** | 法律、合同 | 条款 |
| **Paper** | 学术论文 | 摘要、章节 |
| **Table** | 表格数据 | 行/单元格 |
| **Picture** | 图片 | VLM 描述 |

### 核心思路：保留语义完整性

无论哪种策略，核心原则相同：**一个 chunk 应该能独立回答一个问题**。

以 Book Chunking 为例：

```
原始文档：
# 第一章 概述
## 1.1 背景
文本内容...
## 1.2 目标
文本内容...
# 第二章 设计
## 2.1 架构
文本内容...

切分结果：
Chunk 1: 【第一章 概述 > 1.1 背景】文本内容...
Chunk 2: 【第一章 概述 > 1.2 目标】文本内容...
Chunk 3: 【第二章 设计 > 2.1 架构】文本内容...
```

关键设计：**把父级标题拼到 chunk 前面**。

这样做的原因我在 RAG 进阶篇详细讲过：Embedding 只能看到 chunk 内部的文字。如果 chunk 里没有"第一章"、"概述"、"背景"这些关键词，用户问"第一章的背景是什么"时就召不回。

### Table Chunking 的特殊性

表格数据的切分需要特殊处理：

```
方案 1：行级切分
每行一个 chunk，保留表头

方案 2：单元格级切分
每个单元格一个 chunk，附带行列信息

RAGFlow 的做法：
- 检测表格结构
- 保留表头作为上下文
- 行级切分
- 每个 chunk 包含：表头 + 该行内容

示例：
原始表格：
| 参数 | 类型 | 说明 |
|------|------|------|
| timeout | int | 超时时间 |

切分后的 chunk：
【表：API 参数配置】
参数: timeout | 类型: int | 说明: 超时时间
```

这样用户问"timeout 参数的类型是什么"，就能精确召回这一行。

## 四、检索架构：混合检索 + RRF 融合

RAGFlow 的检索架构是标准的混合检索方案：

### 整体架构

```
Query
  │
  ├─── 向量检索（Dense）───┐
  │                       │
  ├─── 关键词检索（BM25）──┤──→ RRF 融合 ──→ Rerank ──→ Top-K
  │                       │
  └─── Metadata 过滤 ─────┘
```

### RRF 融合算法

RRF（Reciprocal Rank Fusion）的核心思想：**不依赖分数，只依赖排名**。

```
RRF 公式：
score(d) = Σ 1 / (k + rank_i(d))

其中：
- d：文档
- rank_i(d)：文档 d 在第 i 路检索中的排名
- k：平滑参数（通常 60）
```

**为什么有效**？

```
问题：向量分数（0.82）和 BM25 分数（5.2）不在同一尺度

传统方案：
- 分数归一化：复杂，不稳定
- 加权融合：权重难调

RRF 的做法：
- 不管分数多少
- 只看排名
- 排名第 1 → 得分 1/61
- 排名第 2 → 得分 1/62
- 两路都召回的文档，得分更高
```

**示例**：

```
Query："错误码 401"

向量检索：
#1 Doc_A
#2 Doc_B
#3 Doc_C

BM25 检索：
#1 Doc_D
#2 Doc_C  ← 两路都有
#3 Doc_A  ← 两路都有

RRF 融合：
Doc_C: 1/(60+3) + 1/(60+2) = 0.032  ← 最高
Doc_A: 1/(60+1) + 1/(60+3) = 0.032
Doc_B: 1/(60+2) + 0 = 0.016
Doc_D: 0 + 1/(60+1) = 0.016
```

两路都召回的文档，得分更高，自然排在前面。

### Rerank 实现

RAGFlow 内置 Cross-Encoder Rerank：

```
原理：
Query + Document → Transformer → Relevance Score

为什么比向量检索更准：
- 向量检索：Query 和 Document 各自编码，交互少
- Cross-Encoder：Query 和 Document 拼在一起编码，充分交互
```

支持的 Rerank 模型：

| 模型 | 特点 | 延迟（100 候选） |
|------|------|-----------------|
| bge-reranker-v2-m3 | 多语言，效果好 | ~180ms |
| bge-reranker-large | 效果好 | ~150ms |
| ms-marco-MiniLM | 轻量，快速 | ~45ms |

Rerank 的成本很高，只能对小规模候选做精排。RAGFlow 的默认配置：

```
召回：top-50（向量 + BM25）
Rerank：top-50 全部重排
输出：top-5
```

## 五、与其他框架的对比

### 功能对比

| 维度 | RAGFlow | LangChain | LlamaIndex |
|------|---------|-----------|------------|
| **文档解析** | ⭐⭐⭐⭐⭐ DeepDoc | ⭐⭐⭐ 基础 | ⭐⭐⭐ 基础 |
| **Chunking** | ⭐⭐⭐⭐⭐ 8 种策略 | ⭐⭐⭐ 需自己实现 | ⭐⭐⭐⭐ 较丰富 |
| **检索** | ⭐⭐⭐⭐⭐ 混合 + RRF | ⭐⭐⭐ 需组合 | ⭐⭐⭐⭐ 较完整 |
| **可视化 UI** | ⭐⭐⭐⭐⭐ 完整 | ⭐⭐ LangSmith | ⭐⭐⭐ LlamaCloud |
| **开箱即用** | ⭐⭐⭐⭐⭐ 高 | ⭐⭐⭐ 需组装 | ⭐⭐⭐⭐ 较高 |
| **自定义扩展** | ⭐⭐⭐ 中等 | ⭐⭐⭐⭐⭐ 高 | ⭐⭐⭐⭐⭐ 高 |

### 架构理念对比

```
RAGFlow：应用导向
"我要做一个企业知识库" → RAGFlow 提供完整方案
特点：一站式，开箱即用

LangChain：组件导向
"我要组装一个 Agent" → LangChain 提供各种组件
特点：灵活，但需要自己组装

LlamaIndex：数据导向
"我要索引和查询数据" → LlamaIndex 提供数据框架
特点：数据处理能力强，适合研究
```

### 代码风格对比

```python
# RAGFlow：高层抽象，配置驱动
from ragflow import RAGFlow

app = RAGFlow()
dataset = app.create_dataset(name="knowledge")
dataset.add_documents("./docs")
chat = app.create_chat(dataset=dataset)
response = chat.query("What is RAG?")

# LangChain：Chain 组合式
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=vectorstore.as_retriever()
)
response = qa.run("What is RAG?")

# LlamaIndex：索引为中心
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./docs").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("What is RAG?")
```

### 选型建议

| 场景 | 推荐 | 理由 |
|------|------|------|
| 企业知识库 | RAGFlow | 开箱即用，DeepDoc 解析复杂文档 |
| 复杂 Agent 应用 | LangChain | 灵活的 Chain/Tool 组合 |
| 数据分析研究 | LlamaIndex | 强大的索引策略 |
| 快速原型 | RAGFlow | 最快落地 |
| 高度定制化 | LangChain/LlamaIndex | 更底层的控制 |

## 六、生产级特性

### API 设计

RAGFlow 提供完整的 REST API：

```bash
# 创建数据集
POST /api/dataset
{"name": "my_knowledge"}

# 上传文档
POST /api/document/upload
-F "file=@document.pdf"
-F "dataset_id={id}"

# 对话
POST /api/chat/completion
{
  "question": "什么是 RAG?",
  "dataset_ids": ["{id}"],
  "stream": true
}
```

### 部署方案

```
最小部署（Docker Compose）：
├── ragflow（API 服务）
├── milvus（向量库）
├── mysql（元数据）
└── elasticsearch（可选，全文检索）

生产部署（Kubernetes）：
├── Ingress
├── ragflow deployment（多副本）
├── milvus cluster
├── mysql primary/replica
└── 监控（Prometheus + Grafana）
```

### 多租户与权限

```
租户隔离：
- 每个租户独立的数据集
- 数据集级别的访问控制
- API Key 认证

权限模型：
- 管理员：全部权限
- 编辑者：上传、解析、编辑
- 查看者：仅查询
```

### 可观测性

```
指标监控：
- 文档处理吞吐量
- 检索延迟（P50/P95/P99）
- LLM 调用耗时
- 向量库查询性能

日志追踪：
- 请求级 Trace ID
- 结构化日志
- 全链路追踪
```

## 七、RAGFlow 的优势与局限

### 优势

| 维度 | 说明 |
|------|------|
| **DeepDoc** | 业界最强的开源文档解析能力 |
| **开箱即用** | 完整 UI + API，快速落地 |
| **企业级** | 多租户、权限、监控完备 |
| **多策略 Chunking** | 针对不同文档类型优化 |
| **混合检索** | 向量 + BM25 + Rerank 完整支持 |

### 局限

| 维度 | 说明 |
|------|------|
| **灵活性** | 不如 LangChain/LlamaIndex 灵活 |
| **Agent 能力** | 不适合复杂多 Agent 场景 |
| **定制成本** | 深度定制需要理解源码 |
| **学习曲线** | 概念较多，需要时间熟悉 |

### 适用场景

**强烈推荐**：
- 企业内部知识库
- 需要处理复杂文档（PDF、表格）
- 追求快速落地
- 需要可视化管理和审计

**谨慎选择**：
- 复杂 Agent 编排
- 需要深度定制检索逻辑
- 已有 LangChain/LlamaIndex 生态

## 八、快速入门

```bash
# 克隆项目
git clone https://github.com/infiniflow/ragflow.git
cd ragflow

# Docker Compose 启动
docker compose up -d

# 访问 Web UI
open http://localhost:9380

# 创建数据集、上传文档、开始对话
```

核心概念：

```
Dataset（数据集）
├── Document（文档）
│   ├── Chunk（切片）
│   └── Embedding（向量）
└── Chat（对话）

流程：
上传文档 → DeepDoc 解析 → 切分 → 向量化 → 存储
                                         ↓
Query → 检索 → Rerank → LLM 生成 → 答案 + 引用
```

## 九、总结

RAGFlow 不是"又一个 RAG 框架"，而是**从文档到答案的全流程解决方案**。

它的核心价值：

```
1. DeepDoc：解决被忽视的文档解析问题
2. 多策略 Chunking：不同文档不同切法
3. 混合检索：向量 + BM25 + Rerank
4. 开箱即用：UI + API + 部署方案
```

如果你在做企业级 RAG 项目，尤其是需要处理复杂文档的场景，RAGFlow 是目前最值得尝试的开源方案。

它不一定是灵活性最高的，但可能是落地最快的。

---

**相关链接**：
- GitHub: https://github.com/infiniflow/ragflow
- 文档: https://ragflow.io/docs
- Demo: https://ragflow.io
