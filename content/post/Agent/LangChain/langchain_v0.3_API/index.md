---
title: langchain_v0.3_API
description: ""
date: 2025-05-09T00:58:06+08:00
image: images/index/index.png
categories:
    - Agent
tags:
    - LangChain
---


## langchain_core


### prompts

`langchain_core.prompts` 是 LangChain 框架中用于处理和管理提示（Prompt）的核心模块，提供了一系列类来构建、格式化和传递提示给语言模型。这些类支持从简单的字符串模板到复杂的多消息对话结构，适用于多种场景，如问答、聊天机器人和动态提示生成。以下是对 `langchain_core.prompts` 中主要类的详细介绍，包括功能、用法和代码示例。

---

#### 1. `PromptTemplate`
##### 介绍
`PromptTemplate` 是最基础的提示模板类，用于创建格式化的字符串提示。它通过占位符（`{variable}`）支持动态输入，生成的提示可以传递给语言模型。支持 `f-string`（默认）或 `jinja2` 模板格式。

- **功能**：
  - 定义带有占位符的字符串模板。
  - 通过传入变量值动态生成提示。
  - 支持简单的单字符串提示场景。
- **适用场景**：
  - 需要生成固定格式但内容动态变化的提示。
  - 适合与传统语言模型（LLM）配合使用。

##### 使用代码
```python
from langchain_core.prompts import PromptTemplate

# 定义模板
template = "Tell me a {adjective} story about {topic}."
prompt_template = PromptTemplate.from_template(template)

# 动态填充模板
prompt = prompt_template.invoke({"adjective": "funny", "topic": "cats"})
print(prompt.text)
# 输出: Tell me a funny story about cats.

# 结合语言模型
from langchain_openai import OpenAI
llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key="YOUR_API_KEY")
result = llm.invoke(prompt.text)
print(result)
```

##### 注意事项
- 默认使用 `f-string` 格式，推荐避免 `jinja2` 以防安全风险（如未受信任的模板导致代码执行）。
- 适用于简单任务，若需要多消息或对话结构，建议使用 `ChatPromptTemplate`。

---

#### 2. `ChatPromptTemplate`
##### 介绍
`ChatPromptTemplate` 用于构建对话模型的提示，生成结构化的消息列表（`List[BaseMessage]`）。它支持多种消息角色（如 `system`、`human`、`ai`），适合与聊天模型（如 GPT-4）交互。

- **功能**：
  - 定义多条消息的模板（如系统指令、用户输入、AI 回复）。
  - 支持动态变量替换。
  - 提供灵活的消息结构，适配对话场景。
- **适用场景**：
  - 聊天机器人、对话系统。
  - 需要系统指令或多轮对话上下文的场景。

##### 使用代码
```python
from langchain_core.prompts import ChatPromptTemplate

# 定义对话模板
template = [
    ("system", "You are a helpful AI assistant named {name}."),
    ("human", "Tell me a joke about {topic}."),
]
prompt_template = ChatPromptTemplate.from_messages(template)

# 动态填充
prompt = prompt_template.invoke({"name": "Grok", "topic": "dogs"})
print(prompt.messages)
# 输出: [SystemMessage(content='You are a helpful AI assistant named Grok.'), HumanMessage(content='Tell me a joke about dogs.')]

# 结合聊天模型
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="YOUR_API_KEY")
result = model.invoke(prompt)
print(result.content)
```

##### 注意事项
- 消息列表可以包含任意数量和类型的消息。
- 使用 `from_messages` 方法创建模板，支持元组或消息对象。

---

#### 3. `FewShotPromptTemplate`
##### 介绍
`FewShotPromptTemplate` 用于创建少样本提示（Few-Shot Prompting），通过提供示例帮助模型理解任务模式。它将示例与用户输入组合成最终提示。

- **功能**：
  - 提供一组示例（`examples`）和模板（`example_prompt`）。
  - 支持动态选择示例（通过 `example_selector`）。
  - 自动将示例和用户输入格式化为提示。
- **适用场景**：
  - 模型需要通过示例学习特定任务（如分类、翻译）。
  - 适合任务模式复杂或需要上下文引导的场景。

##### 使用代码
```python
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# 定义示例
examples = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
]

# 定义示例模板
example_template = PromptTemplate(
    input_variables=["question", "answer"],
    template="Question: {question}\nAnswer: {answer}\n"
)

# 创建少样本提示
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_template,
    suffix="Question: {input}\nAnswer:",
    input_variables=["input"]
)

# 生成提示
prompt = few_shot_prompt.invoke({"input": "What is the capital of Brazil?"})
print(prompt.text)
# 输出:
# Question: What is the capital of France?
# Answer: Paris
#
# Question: What is the capital of Japan?
# Answer: Tokyo
#
# Question: What is the capital of Brazil?
# Answer:

# 结合模型
llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key="YOUR_API_KEY")
result = llm.invoke(prompt.text)
print(result)
```


此外有个高级技巧， 结合RAG的
![将相近对话使用RAG获取并传入](images/index/image.png)
![具体代码](images/index/image-1.png)


##### 注意事项
- 示例数量需适中，过多可能超出模型上下文窗口。
- 可结合 `ExampleSelector`（如 `SemanticSimilarityExampleSelector`）动态选择相关示例。

---

#### 4. `FewShotChatMessagePromptTemplate`
##### 介绍
`FewShotChatMessagePromptTemplate` 是 `FewShotPromptTemplate` 的对话版本，生成消息列表而非单一字符串。适合与聊天模型配合使用。

- **功能**：
  - 将少样本示例格式化为对话消息。
  - 支持动态变量和复杂对话结构。
- **适用场景**：
  - 对话场景中需要通过示例引导模型。
  - 任务需要多轮对话上下文。

##### 使用代码
```python
from langchain_core.prompts import FewShotChatMessagePromptTemplate, ChatPromptTemplate

# 定义示例
examples = [
    {"question": "What is 2+2?", "answer": "4"},
    {"question": "What is 3+3?", "answer": "6"},
]

# 定义示例消息模板
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{question}"),
    ("ai", "{answer}")
])

# 创建少样本对话提示
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt
)

# 组合最终提示
final_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a math expert."),
    few_shot_prompt,
    ("human", "{input}")
])

# 生成提示
prompt = final_prompt.invoke({"input": "What is 4+4?"})
print(prompt.messages)
# 输出: [SystemMessage(...), HumanMessage(content='What is 2+2?'), AIMessage(content='4'), ...]

# 结合模型
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="YOUR_API_KEY")
result = model.invoke(prompt)
print(result.content)
```

##### 注意事项
- 确保示例与任务相关，提升模型理解能力。
- 可与 `MessagesPlaceholder` 结合支持动态对话历史。

---

#### 5. `SystemMessagePromptTemplate`
##### 介绍
`SystemMessagePromptTemplate` 用于定义系统消息模板，通常作为对话的元指令，指导模型行为。生成 `SystemMessage` 对象。

- **功能**：
  - 创建系统级指令，支持动态变量。
  - 常用于设置模型角色或行为规则。
- **适用场景**：
  - 需要为对话设置全局指令。
  - 结合 `ChatPromptTemplate` 使用。

##### 使用代码
```python
from langchain_core.prompts import SystemMessagePromptTemplate, ChatPromptTemplate

# 定义系统消息模板
system_template = SystemMessagePromptTemplate.from_template(
    "You are a {role} assistant who speaks in a {tone} tone."
)

# 组合对话模板
chat_prompt = ChatPromptTemplate.from_messages([
    system_template,
    ("human", "{input}")
])

# 生成提示
prompt = chat_prompt.invoke({"role": "friendly", "tone": "casual", "input": "Tell me about AI."})
print(prompt.messages)
# 输出: [SystemMessage(content='You are a friendly assistant who speaks in a casual tone.'), HumanMessage(content='Tell me about AI.')]

# 结合模型
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="YOUR_API_KEY")
result = model.invoke(prompt)
print(result.content)
```

##### 注意事项
- 系统消息通常放在对话开头，影响模型整体行为。
- 保持指令简洁明确，避免歧义。

---

#### 6. `HumanMessagePromptTemplate`
##### 介绍
`HumanMessagePromptTemplate` 用于定义用户消息模板，生成 `HumanMessage` 对象，表示用户输入。

- **功能**：
  - 创建用户输入的模板，支持动态变量。
  - 常用于模拟用户查询。
- **适用场景**：
  - 构建对话中的用户消息部分。
  - 结合其他消息模板使用。

##### 使用代码
```python
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

# 定义用户消息模板
human_template = HumanMessagePromptTemplate.from_template("Summarize {topic} in {word_count} words.")

# 组合对话模板
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a concise summarizer."),
    human_template
])

# 生成提示
prompt = chat_prompt.invoke({"topic": "AI", "word_count": 50})
print(prompt.messages)
# 输出: [SystemMessage(...), HumanMessage(content='Summarize AI in 50 words.')]

# 结合模型
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="YOUR_API_KEY")
result = model.invoke(prompt)
print(result.content)
```

##### 注意事项
- 用户消息应清晰表达需求。
- 可与 `MessagesPlaceholder` 结合支持动态消息列表。

---

#### 7. `AIMessagePromptTemplate`
##### 介绍
`AIMessagePromptTemplate` 用于定义 AI 回复消息模板，生成 `AIMessage` 对象。常用于模拟或预定义 AI 响应。

- **功能**：
  - 创建 AI 回复的模板，支持动态变量。
  - 适合在少样本提示中模拟模型输出。
- **适用场景**：
  - 少样本对话提示。
  - 预定义 AI 回复模式。

##### 使用代码
```python
from langchain_core.prompts import AIMessagePromptTemplate, ChatPromptTemplate

# 定义 AI 消息模板
ai_template = AIMessagePromptTemplate.from_template("I found {item} to be {opinion}.")

# 组合对话模板
chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "What do you think of {item}?"),
    ai_template
])

# 生成提示
prompt = chat_prompt.invoke({"item": "Python", "opinion": "awesome"})
print(prompt.messages)
# 输出: [HumanMessage(...), AIMessage(content='I found Python to be awesome.')]

# 结合模型
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="YOUR_API_KEY")
result = model.invoke(prompt)
print(result.content)
```

##### 注意事项
- 通常用于示例或测试场景，实际 AI 回复由模型生成。
- 确保模板与任务逻辑一致。

---

#### 8. `ChatMessagePromptTemplate`
##### 介绍
`ChatMessagePromptTemplate` 是一个通用的消息模板类，允许指定自定义角色（如 `"Jedi"`），生成 `ChatMessage` 对象。

- **功能**：
  - 支持任意角色名称的消息模板。
  - 提供灵活性，适应非标准对话场景。
- **适用场景**：
  - 自定义对话角色（如虚构角色）。
  - 特殊对话格式需求。

##### 使用代码
```python
from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate

# 定义自定义角色消息模板
custom_template = ChatMessagePromptTemplate.from_template(
    role="Jedi",
    template="May the {subject} be with you."
)

# 组合对话模板
chat_prompt = ChatPromptTemplate.from_messages([
    custom_template,
    ("human", "What's your message?")
])

# 生成提示
prompt = chat_prompt.invoke({"subject": "Force"})
print(prompt.messages)
# 输出: [ChatMessage(role='Jedi', content='May the Force be with you.'), HumanMessage(...)]

# 结合模型
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="YOUR_API_KEY")
result = model.invoke(prompt)
print(result.content)
```

##### 注意事项
- 自定义角色需与模型支持的格式兼容。
- 适合创意或非标准对话场景。

---

#### 9. `MessagesPlaceholder`
##### 介绍
`MessagesPlaceholder` 是一个占位符类，用于在提示模板中插入动态消息列表（如对话历史）。它允许在运行时注入一组消息。

- **功能**：
  - 支持插入任意数量的消息（`List[BaseMessage]`）。
  - 提供灵活性，适配动态对话历史。
- **适用场景**：
  - 需要插入对话历史或外部消息。
  - 多轮对话或上下文管理。

##### 使用代码
```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# 定义对话模板
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# 动态消息历史
history = [
    HumanMessage(content="What's the weather like?"),
    AIMessage(content="It's sunny!")
]

# 生成提示
prompt = chat_prompt.invoke({"history": history, "input": "What's the forecast tomorrow?"})
print(prompt.messages)
# 输出: [SystemMessage(...), HumanMessage(content="What's the weather like?"), AIMessage(...), HumanMessage(...)]

# 结合模型
model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="YOUR_API_KEY")
result = model.invoke(prompt)
print(result.content)
```

##### 注意事项
- 确保 `variable_name` 与输入字典的键匹配。
- 适合与记忆模块（如 `ConversationBufferMemory`）结合使用。

---

#### 10. `PipelinePromptTemplate`
##### 介绍
`PipelinePromptTemplate` 用于组合多个提示模板，生成复杂的提示结构。它允许将子模板嵌套在主模板中，支持模块化设计。

- **功能**：
  - 将多个提示模板组合成单一提示。
  - 支持嵌套和动态变量传递。
- **适用场景**：
  - 复杂提示需要分模块设计。
  - 提示包含多个独立部分（如上下文、指令、查询）。

##### 使用代码
```python
from langchain_core.prompts import PipelinePromptTemplate, PromptTemplate

# 定义子模板
intro_template = PromptTemplate.from_template("You are a {role}.")
task_template = PromptTemplate.from_template("Your task is to {task}.")
input_template = PromptTemplate.from_template("Input: {input}")

# 定义主模板
main_template = """
{intro}
{task}
{input}
"""
main_prompt = PromptTemplate.from_template(main_template)

# 组合管道
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=main_prompt,
    pipeline_prompts=[
        ("intro", intro_template),
        ("task", task_template),
        ("input", input_template)
    ]
)

# 生成提示
prompt = pipeline_prompt.invoke({
    "role": "teacher",
    "task": "explain AI",
    "input": "What is AI?"
})
print(prompt.text)
# 输出:
# You are a teacher.
# Your task is to explain AI.
# Input: What is AI?

# 结合模型
llm = OpenAI(model="gpt-3.5-turbo-instruct", openai_api_key="YOUR_API_KEY")
result = llm.invoke(prompt.text)
print(result)
```

##### 注意事项
- 确保子模板的变量与主模板匹配。
- 适合大型项目中提示的模块化管理。

---

#### 总结
以下是 `langchain_core.prompts` 中主要类的功能和适用场景概览：

| 类名                          | 功能                                              | 适用场景                              |
|-------------------------------|--------------------------------------------------|---------------------------------------|
| `PromptTemplate`             | 格式化字符串提示，支持动态变量                    | 简单任务、传统 LLM                  |
| `ChatPromptTemplate`         | 构建对话消息列表，支持多角色                      | 聊天机器人、多轮对话                |
| `FewShotPromptTemplate`      | 提供少样本示例，生成字符串提示                    | 任务需要示例引导、传统 LLM          |
| `FewShotChatMessagePromptTemplate` | 提供少样本示例，生成对话消息                  | 对话任务需要示例引导                |
| `SystemMessagePromptTemplate` | 定义系统消息模板                                 | 设置对话全局指令                    |
| `HumanMessagePromptTemplate` | 定义用户消息模板                                 | 模拟用户输入                        |
| `AIMessagePromptTemplate`    | 定义 AI 回复模板                                 | 少样本对话、预定义 AI 输出          |
| `ChatMessagePromptTemplate`  | 定义自定义角色消息模板                           | 创意对话、非标准角色                |
| `MessagesPlaceholder`        | 插入动态消息列表                                 | 对话历史、动态上下文                |
| `PipelinePromptTemplate`     | 组合多个子模板，生成复杂提示                     | 模块化提示设计、复杂任务            |

---

#### 附加说明
- **安全性**：避免使用 `jinja2` 模板从不受信任的来源加载，推荐 `f-string` 格式。
- **模型兼容性**：`PromptTemplate` 适合传统 LLM（如 `text-davinci-003`），`ChatPromptTemplate` 适合聊天模型（如 `gpt-3.5-turbo`）。
- **扩展性**：可结合 `ExampleSelector`、`OutputParser` 等增强提示功能。
- **调试**：使用 `print(prompt)` 或 `prompt.messages` 检查生成的提示结构。

