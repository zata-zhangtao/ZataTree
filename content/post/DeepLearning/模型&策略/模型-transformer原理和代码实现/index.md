---
title: 模型-transformer原理和代码实现
description: ""
date: 2025-03-31T14:35:25+08:00
image: images/index/index.png
categories:
    - DeepLearning
tags:
    - 模型&策略
---


参考：

https://zhuanlan.zhihu.com/p/338817680




### 生成的图片描述

#### `[图片标记1]`：Transformer 整体架构图
- **内容**：展示 Transformer 的完整结构。
- **设计**：
  - 左侧为编码器（Encoder），右侧为解码器（Decoder）。
  - 编码器由 6 个相同的层堆叠组成，每层包含多头自注意力（Multi-Head Attention）和前馈神经网络（Feed-Forward）。
  - 解码器同样由 6 个层堆叠，每层包含掩码多头自注意力（Masked Multi-Head Attention）、多头注意力（与编码器交互）和前馈神经网络。
  - 用箭头表示数据流：输入序列 → 编码器 → 解码器 → 输出序列。
  - 添加简单的输入示例（如“Input: I am happy” → “Output: 我很开心”）。
- **风格**：简洁的流程图，使用蓝色（编码器）、橙色（解码器）区分模块，文字标注清晰。

#### `[图片标记2]`：编码器和解码器内部结构图
- **内容**：详细展示单个编码器层和解码器层的内部结构。
- **设计**：
  - **编码器层**（左半部分）：
    - 一个矩形框内包含“Multi-Head Self-Attention”和“Feed-Forward”两个子模块。
    - 每个子模块后有“Add & Norm”（残差连接和层归一化），用虚线箭头连接。
  - **解码器层**（右半部分）：
    - 一个矩形框内包含“Masked Multi-Head Attention”、“Multi-Head Attention”（与编码器连接）、“Feed-Forward”三个子模块。
    - 同样每个子模块后有“Add & Norm”。
  - 用绿色虚线表示编码器输出到解码器的信息流。
- **风格**：模块化设计，颜色区分不同部分（自注意力蓝色、前馈网络紫色、归一化灰色）。

#### `[图片标记3]`：自注意力机制计算流程图
- **内容**：展示自注意力（Self-Attention）的计算步骤。
- **设计**：
  - 从输入向量 \(X\) 开始，用箭头指向三个线性变换：\(Q\)（查询）、\(K\)（键）、\(V\)（值）。
  - 显示矩阵乘法 \(QK^T\)，并标注缩放因子 \(\sqrt{d_k}\)。
  - 用一个矩形框表示 Softmax 操作，输出注意力权重。
  - 最后通过 \(V\) 加权求和，输出注意力结果。
  - 标注公式：\(\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V\)。
- **风格**：流程图形式，箭头引导计算顺序，关键公式用红色高亮。

---



## Transformer 模型原理和代码实现教程

### 一、Transformer 模型简介
Transformer 是一种基于注意力机制的深度学习模型，由 Vaswani 等人在 2017 年的论文《Attention is All You Need》中提出。它抛弃了传统 RNN 的循环结构，完全依赖自注意力机制实现序列建模，广泛应用于 NLP 和其他领域。

---

### 二、Transformer 模型结构

#### 1. 整体架构
Transformer 由编码器和解码器组成，通常堆叠 6 层，用于序 列到序列任务。  
![Transformer 整体架构图](images/index/index-1.png)

*上图展示了编码器和解码器的堆叠结构及数据流向。*

#### 2. 编码器（Encoder）
每个编码器层包含：
1. 多头自注意力机制  
2. 前馈神经网络  
加上残差连接和层归一化。

#### 3. 解码器（Decoder）
解码器多了掩码自注意力，用于防止未来信息泄露。  
![编码器和解码器内部结构图]([图片标记2已生成])  
*上图详细展示了编码器和解码器层的子模块及连接方式。*

#### 4. 输入嵌入与位置编码
位置编码通过正弦和余弦函数加入序列位置信息：
\[
PE_{(pos, 2i)} = \sin(pos / 10000^{2i/d_{model}})
\]
\[
PE_{(pos, 2i+1)} = \cos(pos / 10000^{2i/d_{model}})
\]

---

### 三、自注意力机制（Self-Attention）详解

#### 1. 计算过程
自注意力通过查询 \(Q\)、键 \(K\)、值 \(V\) 计算相关性：  
\[
\text{Attention}(Q, K, V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V
\]  
![自注意力机制计算流程图]([图片标记3已生成])  
*上图展示了自注意力的计算步骤。*

#### 2. 多头机制
将注意力分成多个子空间并行计算，最后拼接结果。

---

### 四、代码实现（基于 PyTorch）
以下是简化的编码器实现：

```python
import torch
import torch.nn as nn
import math

# 位置编码
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return x + self.pe[:, :x.size(1), :]

# 多头自注意力
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()
        assert d_model % num_heads == 0
        self.d_k = d_model // num_heads
        self.num_heads = num_heads
        self.q_linear = nn.Linear(d_model, d_model)
        self.k_linear = nn.Linear(d_model, d_model)
        self.v_linear = nn.Linear(d_model, d_model)
        self.out_linear = nn.Linear(d_model, d_model)

    def forward(self, q, k, v, mask=None):
        batch_size = q.size(0)
        q = self.q_linear(q).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        k = self.k_linear(k).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        v = self.v_linear(v).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        attn = torch.softmax(scores, dim=-1)
        context = torch.matmul(attn, v)
        context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.num_heads * self.d_k)
        return self.out_linear(context)

# Transformer 编码器层
class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
        super(EncoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model)
        )
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        attn_output = self.self_attn(x, x, x, mask)
        x = self.norm1(x + self.dropout(attn_output))
        ffn_output = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_output))
        return x

# 测试
d_model, num_heads, d_ff, seq_len, batch_size = 512, 8, 2048, 10, 2
encoder_layer = EncoderLayer(d_model, num_heads, d_ff)
x = torch.randn(batch_size, seq_len, d_model)
output = encoder_layer(x)
print(output.shape)  # torch.Size([2, 10, 512])
```

---
