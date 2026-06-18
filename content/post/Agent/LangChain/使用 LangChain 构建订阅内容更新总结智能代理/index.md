---
title: 使用 LangChain 构建订阅内容更新总结智能代理
description: ""
date: 2025-03-13T17:55:31+08:00
image: images/index/index.png
# image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---



# 教程：使用 LangChain 构建订阅内容更新总结智能代理

在这个教程中，我们将使用 **LangChain** 框架和一个语言模型（例如 xAI 的 Grok 3 或阿里的 Qwen-7b-chat）创建一个智能代理，用于根据内容差异（contentdiff）生成订阅内容的更新总结。输出将是一个固定格式的 JSON，包含概要、关键点、字数和生成时间。我们将深入探讨 LangChain 的核心组件（如 PromptTemplate、Chains 和 Output Parsers）在代码中的应用。

## 目标
- 掌握 LangChain 的基本概念和组件。
- 理解如何使用 LangChain 与 LLM 集成。
- 学会处理 LLM 的输出并生成结构化结果。
- 结合实际代码，探索 LangChain 的应用场景。

---

## 前置条件
1. **Python 环境**：需要 Python 3.8+。
2. **依赖安装**：
   - 安装 LangChain：
     ```bash
     pip install langchain
     ```
   - （可选）安装特定 LLM 的 SDK，例如 xAI 的 Grok 或阿里云的 Qwen。
3. **LLM 访问**：确保有一个可用的语言模型实例（例如通过 `get_ali_llm` 或直接使用 Grok 3）。
4. **代码文件**：将代码保存为 `subscription_agent.py`，并确保导入路径正确。

---

## LangChain 核心知识点

LangChain 是一个强大的框架，用于构建与语言模型交互的应用程序。以下是本教程涉及的核心组件：

1. **PromptTemplate**：
   - 用于定义 LLM 的输入提示，支持动态变量替换。
   - 通过模板化提示，确保输入结构化且一致。

2. **Chains**：
   - 将多个步骤（如提示生成、模型调用、输出处理）组合成一个可执行的工作流。
   - 支持管道操作符 `|`，简化链的定义。

3. **Output Parsers**（可选）：
   - 用于解析 LLM 的输出，确保结果符合预期格式（如 JSON）。
   - 在本例中未直接使用，但可以优化代码。

4. **RunnableSequence**：
   - LangChain 的核心执行单元，表示一系列可运行的步骤。
   - 通过 `|` 操作符隐式创建。

---

## 代码结构与 LangChain 应用讲解

### 1. 导入 LangChain 相关模块
```python
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.chains import LLMChain
from langchain_core.output_parsers.json import SimpleJsonOutputParser
import json
from src.agent.llm import get_ali_llm
```
- **LangChain 知识点**：
  - `PromptTemplate`：用于创建提示模板。
  - `RunnableSequence`：支持链式操作的核心类。
  - `SimpleJsonOutputParser`：可选的输出解析器（本例中未直接使用）。
- **注意**：确保导入的 LLM（例如 `get_ali_llm`）返回一个兼容 LangChain 的模型实例。

### 2. 定义 JSON 输出模板
```python
SUMMARY_TEMPLATE = {
    "summary": {
        "content": "",
        "key_points": [],
        "word_count": 0,
        "generated_at": ""
    },
    "status": "success",
    "error_message": None
}
```
- **作用**：定义一个固定的 JSON 结构，作为代理的输出目标。
- **LangChain 相关性**：虽然这不是 LangChain 的直接组件，但它与后续的提示模板和输出处理紧密相关。

### 3. 创建 SubscriptionAgent 类
```python
class SubscriptionAgent:
    def __init__(self, llm_model=None):
        # 初始化 LLM
        self.llm = llm_model if llm_model else get_ali_llm("qwen-7b-chat")

        # 测试 LLM
        print("----")
        print(self.llm.invoke("你好"))
        print("----")
```
- **LangChain 知识点**：
  - `self.llm` 是一个 LLM 实例，LangChain 的链需要依赖它。
  - `.invoke()` 是 LangChain 提供的一个通用方法，用于直接调用 LLM。
- **注意**：确保 LLM 实例支持 LangChain 的接口（例如具有 `invoke` 或 `ainvoke` 方法）。

#### 使用 PromptTemplate 定义提示
```python
self.prompt_template = PromptTemplate(
    input_variables=["contentdiff"],
    template="""
    你是一个订阅号运营专家，可以根据差异内容总结出订阅内容的更新情况，请对以下内容差异进行总结：
    {contentdiff}
    
    要求：
    1. 提供简洁的内容更新概要
    2. 提取关键点
    3. 计算总字数
    返回结果使用中文

    返回格式json（请严格按照以下格式返回）：
    {{
        "summary": {{
            "content": "",
            "key_points": [],
            "word_count": 0,
            "generated_at": ""
        }},
    }}
    """
)
```
- **LangChain 知识点**：
  - **PromptTemplate**：通过 `input_variables` 指定动态变量（`contentdiff`），在 `template` 中使用 `{contentdiff}` 占位符。
  - 提示明确指定了任务（总结内容差异）和输出格式（JSON），这是 LangChain 中确保 LLM 输出可控的关键。
- **关键点**：
  - 模板化的提示提高了复用性和一致性。
  - LangChain 会将 `contentdiff` 的值注入模板，生成最终的输入。
- **注意**：LLM 不一定严格遵循 JSON 格式，可能需要后续解析。

#### 使用 Chain 组合提示和 LLM
```python
self.chain = self.prompt_template | self.llm
```
- **LangChain 知识点**：
  - **RunnableSequence**：使用 `|` 操作符将 `PromptTemplate` 和 `self.llm` 组合成一个链。
  - 工作原理：
    1. `PromptTemplate` 接收输入并生成格式化的提示。
    2. `self.llm` 接收提示并生成输出。
  - 这是一个简化的链，替代了传统的 `LLMChain`。
- **优势**：管道语法简洁，易于扩展（例如添加输出解析器）。
- **注意**：确保 LangChain 版本支持 `|` 操作符（0.1.0+）。

### 4. 生成总结的函数
```python
def generate_summary(self, contentdiff: str) -> dict:
    try:
        # 执行链
        result = self.chain.invoke({"contentdiff": contentdiff}).content
        print("result: ", result)
        
        # 解析 LLM 输出
        parsed_result = json.loads(result)
        summary_content = parsed_result["summary"]["content"]
        key_points = parsed_result["summary"]["key_points"]
        word_count = parsed_result["summary"]["word_count"]
        generated_at = parsed_result["summary"]["generated_at"]

        # 填充模板
        response = SUMMARY_TEMPLATE.copy()
        response["summary"]["content"] = summary_content
        response["summary"]["key_points"] = key_points
        response["summary"]["word_count"] = word_count
        response["summary"]["generated_at"] = generated_at

        return response

    except Exception as e:
        error_response = SUMMARY_TEMPLATE.copy()
        error_response["status"] = "error"
        error_response["error_message"] = f"Error on line {e.__traceback__.tb_lineno}: {str(e)}"
        return error_response
```
- **LangChain 知识点**：
  - **invoke 方法**：`self.chain.invoke` 执行整个链，输入是一个字典（`{"contentdiff": contentdiff}`）。
  - **输出处理**：LangChain 返回的对象通常有 `.content` 属性，表示 LLM 的原始输出。
- **关键点**：
  - LangChain 的链将提示生成和模型调用无缝连接。
  - 手动使用 `json.loads` 解析输出，因为未使用 LangChain 的输出解析器。
- **注意**：
  - 如果 LLM 返回非 JSON 格式，`json.loads` 会失败。
  - 建议使用 `SimpleJsonOutputParser` 增强鲁棒性（见优化建议）。

### 5. 测试代码
```python
def main():
    sample_contentdiff = """
    Original: The quick brown fox jumps over the lazy dog.
    Updated: The swift brown fox leaps over the idle dog quickly.
    """
    agent = SubscriptionAgent()
    summary_result = agent.generate_summary(sample_contentdiff)
    print(summary_result)

if __name__ == "__main__":
    main()
```
- **LangChain 相关性**：展示了如何使用 LangChain 构建的代理处理实际输入。

---

## LangChain 的关键应用与注意事项

### 关键应用
1. **提示工程**：
   - 使用 `PromptTemplate` 规范化输入，确保 LLM 理解任务。
   - 示例中的提示明确了总结要求和 JSON 格式。

2. **链式工作流**：
   - 通过 `|` 操作符创建的链，展示了 LangChain 的模块化设计。
   - 可以轻松扩展，例如添加解析器或多个 LLM 步骤。

3. **与 LLM 集成**：
   - LangChain 抽象了 LLM 的调用细节，使代码更简洁。

### 注意事项
1. **LLM 输出不一致**：
   - LLM 可能不严格遵循提示中的 JSON 格式。
   - 解决方法：使用 `SimpleJsonOutputParser`：
     ```python
     from langchain_core.output_parsers.json import SimpleJsonOutputParser
     self.chain = self.prompt_template | self.llm | SimpleJsonOutputParser()
     result = self.chain.invoke({"contentdiff": contentdiff})
     ```

2. **输入格式**：
   - `invoke` 需要字典输入，确保变量名与 `PromptTemplate` 的 `input_variables` 匹配。

3. **性能问题**：
   - 同步调用可能在高并发场景下较慢，考虑异步：
     ```python
     async def generate_summary(self, contentdiff: str) -> dict:
         result = await self.chain.ainvoke({"contentdiff": contentdiff})
     ```

---

## 优化建议：增强 LangChain 使用
1. **添加输出解析器**：
   - 使用 `SimpleJsonOutputParser` 自动解析 JSON：
     ```python
     self.chain = self.prompt_template | self.llm | SimpleJsonOutputParser()
     ```

2. **动态提示**：
   - 支持多语言或自定义要求：
     ```python
     self.prompt_template = PromptTemplate(
         input_variables=["contentdiff", "language"],
         template="Summarize in {language}: {contentdiff} ..."
     )
     ```

3. **错误重试**：
   - 使用 LangChain 的重试机制：
     ```python
     from langchain_core.retry import retry
     result = retry(self.chain.invoke, max_attempts=3)({"contentdiff": contentdiff})
     ```

---

## 示例运行结果
假设 LLM 和 LangChain 正常工作，输出可能是：
```json
{
  "summary": {
    "content": "内容从‘quick’改为‘swift’，‘jumps’改为‘leaps’，新增‘quickly’。",
    "key_points": ["quick -> swift", "jumps -> leaps", "新增 quickly"],
    "word_count": 18,
    "generated_at": "2025-03-13T10:00:00"
  },
  "status": "success",
  "error_message": null
}
```

---

## 总结
通过这个教程，你掌握了 LangChain 的核心组件（PromptTemplate、Chains）和它们在构建智能代理中的应用。LangChain 的强大之处在于其模块化和灵活性，能够将复杂的 LLM 交互简化为几行代码。关键是设计清晰的提示、利用链式工作流，并根据需要添加输出解析或错误处理。

如果你想进一步探索 LangChain 的高级功能（如记忆上下文、工具调用），请告诉我！