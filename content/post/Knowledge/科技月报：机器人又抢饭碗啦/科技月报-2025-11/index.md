---
title: 科技月报-2025-11
description: ""
date: 2025-11-26T15:22:18+08:00
image: images/index/index.png
categories:
    - Knowledge
tags:
    - 科技月报：机器人又抢饭碗啦
---




# Google Gemini API File Search / Long Context 

[ RAG被判死刑：Google用一行API架空工程师！](https://mp.weixin.qq.com/s/6A4Dk14MejdvXdPSnBVfbA)

## 1. 核心架构思维转变

Google 的方案并不是传统的 RAG（检索），而是基于 **Long Context (长上下文)** 的全量处理。

| 特性 | 传统 RAG (LangChain + VectorDB) | Google Gemini File API |
| :--- | :--- | :--- |
| **处理逻辑** | 文档切片 -> 向量化 -> 相似度检索 -> 只有片段进 LLM | 全文档上传 -> Token化 -> **整个文档进 Context** -> LLM 原生注意力机制 |
| **优势** | 成本低，适合海量非结构化数据 (TB级) | **精度极高**，具备跨段落推理能力，支持复杂图表/表格理解 |
| **劣势** | 丢失上下文，图表/表格处理困难 | Token 消耗大 (需配合 Context Caching)，受限于 Context Window (目前 1M/2M) |

---

## 2. 环境准备

需要安装 Google 官方 Python SDK：

```bash
pip install -U google-generativeai
````

获取 API Key: [Google AI Studio](https://aistudio.google.com/)

-----

## 3\. Python 实战代码 (MVP)

这是一个最小可行性脚本，包含了**文件上传**、**状态轮询**和**生成回答**的全流程。

```python
import os
import time
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# ================= 配置区域 =================
# 建议将 API Key 放入环境变量: export GEMINI_API_KEY="your_key"
API_KEY = os.getenv("GEMINI_API_KEY")
FILE_PATH = "technical_spec.pdf"  # 替换为你的测试文件路径 (支持 PDF, CSV, TXT, MD 等)
MODEL_NAME = "gemini-1.5-flash-002" # 推荐: flash-002 (快/便宜) 或 pro-002 (强)
# ===========================================

genai.configure(api_key=API_KEY)

def upload_and_wait(path, mime_type=None):
    """
    上传文件并阻塞直到处理完成。
    Google 需要时间对大文件进行预处理（Token化/索引）。
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"文件未找到: {path}")

    print(f"🚀 正在上传: {path} ...")
    file = genai.upload_file(path, mime_type=mime_type)
    print(f"✅ 上传成功. URI: {file.uri}")
    print(f"⏳ 等待文件处理 (状态: {file.state.name})...")

    # 轮询状态直到 ACTIVE
    while file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(2)
        file = genai.get_file(file.name)
    
    if file.state.name != "ACTIVE":
        raise Exception(f"❌ 文件处理失败: {file.state.name}")
    
    print("\n🎉 文件就绪!")
    return file

def main():
    try:
        # 1. 上传文件
        # 如果是纯文本，mime_type 可不填，PDF 建议显式指定 application/pdf
        your_file = upload_and_wait(FILE_PATH)

        # 2. 初始化模型
        # 关闭安全过滤以避免误杀技术文档内容
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }

        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            safety_settings=safety_settings,
            system_instruction="你是一个资深技术专家。请基于提供的文件内容回答问题。引用原文时请尽量精确。"
        )

        # 3. 发起提问 (Long Context 模式)
        # 提示：你可以在列表中传入多个 file 对象
        prompt = "请总结这份文档的核心架构，并提取出所有的数据库 Schema 定义（如果有）。"
        
        print(f"\n🤖 正在思考 ({MODEL_NAME})...")
        start_time = time.time()
        
        response = model.generate_content(
            [your_file, prompt],
            request_options={"timeout": 600} # 大文件处理可能较慢
        )
        
        print(f"⏱️ 耗时: {time.time() - start_time:.2f}s")
        print("-" * 30)
        print(response.text)
        print("-" * 30)

        # 4. (可选) 查看引用元数据
        if response.candidates[0].citation_metadata:
            print(f"📚 引用来源: {response.candidates[0].citation_metadata}")

    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
    
    # 5. 清理资源 (根据需求决定是否保留文件)
    # print("正在删除云端文件...")
    # genai.delete_file(your_file.name)

if __name__ == "__main__":
    main()
```

-----

## 4\. 关键测试点 (PoC 验证清单)

在验证此方案是否能替代现有 RAG 时，请着重测试以下三点：

1.  **多模态理解能力 (Multimodal RAG)**

      * **测试素材：** 包含系统架构图、流程图或复杂数据表格的 PDF。
      * **Prompt：** "根据图 3 的架构图，解释数据是如何流转的？"
      * **预期：** 传统 RAG 通常做不到这一点（OCR 丢失结构），Gemini 应该能准确识别。

2.  **跨段落/全局信息整合**

      * **测试素材：** 长篇技术白皮书或小说。
      * **Prompt：** "总结文档中提到的所有关于‘安全性’的约束，并按优先级排序。"
      * **预期：** 传统 RAG 容易漏掉没检索到的切片，Gemini 拥有全量上下文，召回率应接近 100%。

3.  **延迟与成本 (Latency & Cost)**

      * **观察：** 首次请求的延迟（Cold Start）。
      * **注意：** 如果文件非常大且需要频繁提问，必须使用 **Context Caching**（见下文）。

-----

## 5\. 进阶：Context Caching (降本增效)

如果你的场景是“**一个大文档，被反复提问**”（例如：员工手册 bot、API 文档助手），直接每次上传或传入 Token 会非常贵。

请使用 Google 的 **Context Caching** 功能：

  * **原理：** 支付低廉的存储费，将处理好的 Context 缓存在 Google 端。
  * **效果：** 后续提问无需再次计算 Input Token，大幅降低延迟和推理成本。

*文档参考：[Google AI Studio - Context Caching](https://ai.google.dev/gemini-api/docs/caching)*


