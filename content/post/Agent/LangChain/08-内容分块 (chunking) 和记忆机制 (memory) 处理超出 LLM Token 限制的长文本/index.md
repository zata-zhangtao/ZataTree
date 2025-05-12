---
title: 08-内容分块 (chunking) 和记忆机制 (memory) 处理超出 LLM Token 限制的长文本
description: ""
date: 2025-05-12T16:07:10+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---



[可执行py文件](./解决上下文过长.py)


---


# Python 订阅内容差异分析与摘要生成教程

本教程将引导您了解一个 Python 脚本，该脚本使用大型语言模型 (LLM) 来分析和总结内容差异，特别适用于订阅服务或任何需要跟踪文本更新的场景。它能将内容变更（如新增、修改、删除）转化为结构化的 JSON 摘要，包含关键点和相关 URL。

**核心功能:**

* **内容差异总结:** 识别并总结文本内容的变化。
* **LLM 集成:** 利用阿里云 Dashscope 上的 `qwen-plus` 模型进行智能分析。
* **结构化输出:** 使用 Pydantic 模型确保输出为统一的 JSON 格式。
* **长文本处理:** 通过内容分块 (chunking) 和记忆机制 (memory) 处理超出 LLM Token 限制的長文本。
* **错误处理与重试:** 内置重试逻辑以增加 robustness。
* **定制化提示:** 通过精心设计的 Prompt 指导 LLM 的输出。

## 准备工作

在运行此脚本之前，请确保您已满足以下条件：

1.  **Python 环境:** Python 3.7 或更高版本。
2.  **必要的库:**
    * `langchain-core`
    * `langchain-openai` (用于 `ChatOpenAI`)
    * `pydantic` (用于数据校验和模型定义)
    * `openai` (通常作为 `ChatOpenAI` 的依赖，或需要其兼容的 SDK)
    您可以使用 pip 安装它们：
    ```bash
    pip install langchain-core langchain-openai pydantic openai
    ```
3.  **API 密钥:**
    * 您需要一个阿里云 Dashscope 的 API 密钥。脚本中通过 `os.getenv("DASHSCOPE_API_KEY")` 读取此密钥。请确保您已设置此环境变量。

## 代码结构概览

脚本主要包含以下几个部分：

1.  **`MockLogger`:** 一个简单的日志记录器，用于在教程中打印调试和信息。
2.  **`SummaryResponse` (Pydantic 模型):** 定义了 LLM 最终输出的 JSON 结构。
3.  **`SubscriptionAgent` (核心类):** 封装了所有处理逻辑。

### 1. `SummaryResponse` Pydantic 模型

这个模型定义了代理 (Agent) 生成摘要的预期输出格式。

```python
class SummaryResponse(BaseModel):
    content: List[str] = Field(default_factory=list, description="内容更新摘要")
    key_points: List[str] = Field(default_factory=list, description="关键点列表")
    url_list: List[List[str]] = Field(default_factory=list, description="每个关键点对应的URL列表")
    word_count: int = Field(default=0, description="内容的总字数")
    generated_at: str = Field(default="", description="生成时间戳")
    status: str = Field(default="success", description="处理状态")
    error_message: Optional[str] = Field(default=None, description="错误信息（如有）")
    raw_response: Optional[str] = Field(default=None, description="LLM原始响应")
```

主要字段说明：

* `content`: 包含内容更新摘要的字符串列表。
* `key_points`: 对应每个 `content` 条目的关键点列表。
* `url_list`: 一个二维列表，每个子列表包含对应关键点的 URL。
* `word_count`: `content` 中中文/英文字符的总数（不含标点和空格）。
* `generated_at`: ISO 格式的生成时间。
* `status`: "success" 或 "error"。
* `error_message`: 如果状态为 "error"，则包含错误信息。
* `raw_response`: LLM 返回的原始文本。

### 2. `SubscriptionAgent` 核心类

这是实现所有功能的中心类。

#### `__init__(self, max_retries=3, retry_delay=2, max_token_limit=30000)`

* **参数:**
    * `max_retries`: LLM 调用失败时的最大重试次数。
    * `retry_delay`: 重试前的等待时间（秒）。
    * `max_token_limit`: LLM 能处理的最大 Token 数。这用于判断是否需要分块处理。
* **LLM 初始化:**
    ```python
    self.llm = ChatOpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="[https://dashscope.aliyuncs.com/compatible-mode/v1](https://dashscope.aliyuncs.com/compatible-mode/v1)",
        model="qwen-plus",
        # other params...
    )
    ```
    这里配置了使用阿里云 Dashscope 的 `qwen-plus` 模型。
* **解析器 (Parser) 初始化:**
    ```python
    self.parser = PydanticOutputParser(pydantic_object=SummaryResponse)
    ```
    用于将 LLM 的 JSON 字符串输出解析为 `SummaryResponse` 对象。
* **Prompt 模板 (`self.prompt_template`):**
    这是指导 LLM 如何处理输入 `contentdiff` 并生成所需 JSON 输出的核心指令。
    关键指令包括：
    * 忽略仅时间或日期的更改。
    * 确保 `content` 和 `key_points` 一一对应。
    * `url_list` 是二维数组。
    * 如果存在更新，则以中文返回结果。
    * 遵循指定的 JSON 格式 (`format_instructions` 由 `PydanticOutputParser` 自动生成)。
* **对话记忆 (`self.memory`):**
    ```python
    self.memory = ConversationSummaryBufferMemory(
        llm=self.llm,
        max_token_limit=self.max_token_limit,
        return_messages=True
    )
    ```
    此记忆模块在 `__init__` 中初始化，但在此脚本的当前实现中，主要用于 `generate_summary_with_memory` 方法内部重新创建的局部记忆实例。`generate_summary` 方法本身不直接使用这个 `self.memory` 实例进行摘要链调用。

#### `extract_json(self, raw_content: str) -> str`

一个辅助函数，用于从 LLM 可能返回的包含额外文本的原始响应中提取 JSON 部分。

#### `generate_summary(self, contentdiff: str) -> SummaryResponse`

这是生成摘要的主要入口点。

1.  **Token 估算:** 估算输入 `contentdiff` 的 Token 大小。
2.  **决策:**
    * 如果估算的 Token 超过 `self.max_token_limit`，则调用 `generate_summary_with_memory` 处理长文本。
    * 否则，直接处理。
3.  **直接处理流程:**
    * 构建 LangChain 表达式链 (LCEL): `chain = self.prompt_template | self.llm`。
    * 调用链: `raw_response = chain.invoke({"contentdiff": contentdiff})`。
    * 提取并解析 JSON: 使用 `self.extract_json` 和 `self.parser.parse`。
    * 填充额外字段: `generated_at`, `word_count`, `raw_response`。
    * **重试逻辑:** 如果在调用 LLM 或解析响应时发生异常，会进行重试，最多 `self.max_retries` 次。
    * 返回 `SummaryResponse` 对象。如果所有重试都失败，则返回包含错误信息的 `SummaryResponse`。

#### `chunking_content(self, contentdiff: str) -> List[str]`

当输入内容过长时，此方法将其分割成更小的块。

1.  **判断是否需要分块:** 如果估算的 Token 未超限，则返回包含整个内容的单元素列表。
2.  **分块策略:**
    * **优先按变更单元分割:** 尝试使用正则表达式 `r'""(?:Changed|Added|Deleted):.*?"",'` 查找独立的变更单元。如果找到，则将这些单元组合成不超过 `max_token_limit` 的块。
    * **按字符数分割:** 如果未找到明确的变更单元，则按大致等同于 `max_token_limit` 的字符数进行硬性分割。

#### `generate_summary_with_memory(self, contentdiff: str) -> SummaryResponse`

此方法专门用于处理因过长而需要分块的内容。

1.  **内容分块:** 调用 `self.chunking_content(contentdiff)` 获取内容块列表。
2.  **初始化局部记忆:**
    ```python
    memory = ConversationSummaryBufferMemory(
        llm=self.llm,
        max_token_limit=self.max_token_limit // 2, # 为每个块的摘要留出空间
        return_messages=True
    )
    memory.chat_memory.add_message(SystemMessage(content="...")) # 添加系统消息指导后续块处理
    ```
    注意：这里创建了一个新的、局部的 `memory` 实例，专门用于此次分块处理会话，其 `max_token_limit` 通常设置为较小值，以适应摘要历史。
3.  **逐块处理:**
    * 为每个块定义一个简单的 `chunk_prompt`，指示 LLM 从该块中提取 `content`, `key_points`, `urls`。
    * 调用 LLM 处理每个块。
    * 从每个块的 LLM 响应 (JSON) 中收集提取的信息 (`collected_content`, `collected_key_points`, `collected_urls`)。
    * 将当前块的输入和输出摘要存入局部 `memory` 中 (`memory.save_context(...)`)。这有助于在理论上为后续块的处理提供上下文，尽管当前脚本中每个块的处理相对独立。
4.  **最终汇总:**
    * 所有块处理完毕后，使用 `final_prompt_template` 指导 LLM 将所有收集到的信息 (`collected_content`, `collected_key_points`, `collected_urls`) 合并成一个最终的 `SummaryResponse` 格式的 JSON。
    * 这个最终的 prompt 也包含了 `format_instructions`。
    * 调用 LLM 进行最终汇总，并解析结果。
5.  **重试与错误处理:** 与 `generate_summary` 类似，最终汇总步骤也有重试逻辑。
6.  **返回结果:** 返回包含汇总信息的 `SummaryResponse`。

## 工作流程

1.  **输入:** `contentdiff` 字符串，描述了内容的变化。
2.  **`generate_summary` 调用:**
    * **Token 检查:** 估算 `contentdiff` 的 Token 数。
    * **路径选择:**
        * **短文本路径:** 如果 Token 未超限，使用 `self.prompt_template` 直接调用 LLM，解析结果，返回 `SummaryResponse`。
        * **长文本路径 (`generate_summary_with_memory`):**
            1.  `contentdiff` 被 `chunking_content` 分割成小块。
            2.  初始化一个局部的 `ConversationSummaryBufferMemory`。
            3.  LLM 逐个处理这些小块，提取初步信息。这些信息被收集起来。
            4.  使用 `final_prompt_template`，LLM 将所有收集到的初步信息整合成最终的 `SummaryResponse`。
3.  **输出:** 一个 `SummaryResponse` 对象，包含结构化的摘要信息或错误详情。

## 如何运行

脚本的末尾有一个 `if __name__ == "__main__":` 代码块，用于演示如何使用 `SubscriptionAgent`：

```python
if __name__ == "__main__":
    # 示例内容差异
    sample_contentdiff = """
    "[\"\"Changed: '1' -> '2 分钟前\\n.\\nAIbase\\nFlower Labs 颠覆AI应用模式，2360万美元打造首个全开放混合计算平台\\n人工智能正在以前所未有的速度融入我们的日常应用，而一家名为Flower Labs的初创公司正以革命性的方式改变AI模型的部署和运行方式。这家获得Y Combinator支持的新锐企业近日推出了Flower Intelligence，一个创新的分布式云平台，专为在移动设备、个人电脑和网络应用中提供AI模型服务而设计。Flower Intelligence的核心优势在于其独特的混合计算策略。该平台允许应用程序在本地设备上运行AI模型，既保证了速度，又增强了隐私保护。当需要更强大的计算能力时，系统会在获得用户同意的情况下，无\\n7'\"\", \"\"Added: '美国埃隆大学的一项调查显示，5'\"\", ...]"
    """

    # 初始化并测试代理
    logger.info("Initializing SubscriptionAgent for testing")
    # 注意：这里 max_token_limit=300 是为了演示分块功能，实际应用中应根据模型调整
    agent = SubscriptionAgent(max_retries=3, retry_delay=2, max_token_limit=300)
    logger.info("Starting summary generation test")
    summary_result = agent.generate_summary(sample_contentdiff)
    logger.info("Summary generation test completed")

    # 显示结果
    logger.info("Displaying summary result")
    print(json.dumps(summary_result.dict(), indent=2, ensure_ascii=False))
```

1.  **设置环境变量:**
    ```bash
    export DASHSCOPE_API_KEY="your_actual_api_key"
    ```
2.  **运行脚本:**
    ```bash
    python your_script_name.py
    ```
    脚本将使用 `sample_contentdiff`（由于 `max_token_limit` 设置为较低的 `300`，它可能会触发 `generate_summary_with_memory` 路径），生成摘要，并以 JSON 格式打印结果。

## 定制与扩展

* **更换 LLM 模型:** 修改 `SubscriptionAgent` 中 `ChatOpenAI` 的 `model` 参数，或使用其他兼容 LangChain 的 LLM 提供商。
* **调整 Prompts:** 根据您的具体需求修改 `self.prompt_template`、`chunk_prompt` 和 `final_prompt_template`。
* **修改分块逻辑:** 调整 `chunking_content` 中的正则表达式或字符分割逻辑。
* **增强记忆使用:** 当前脚本中，`generate_summary_with_memory` 内部的记忆主要用于保存每个块的处理上下文。可以进一步扩展，使其在处理后续块时能更智能地利用先前块的摘要信息。
* **不同的输出结构:** 修改 `SummaryResponse` Pydantic 模型并相应更新 Prompts 中的 `format_instructions` 部分（或让 PydanticOutputParser 自动处理）。

## 总结

这个 Python 脚本提供了一个强大且可扩展的框架，用于利用 LLM 分析和总结内容差异。通过其分块处理、重试机制和结构化输出，它可以有效地处理各种大小的文本输入，并为下游应用提供标准化的摘要信息。
```