import os
from typing import List, Dict, Any, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
# from langchain_core.pydantic_v1 import BaseModel, Field
from pydantic import BaseModel, Field
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.utils.function_calling import convert_to_openai_function
# 设置阿里云DashScope模型
model = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-max",  # 可按需更换模型
)

# 使用@tool装饰器定义工具函数
@tool
def get_weather(location: str, unit: str = "celsius") -> str:
    """获取指定位置的当前天气。
    
    Args:
        location: 城市名称，例如 北京、上海
        unit: 温度单位，可选 'celsius' 或 'fahrenheit'
    
    Returns:
        当前天气预报
    """
    # 实际应用中应调用天气API
    return f"{location}当前天气晴朗，温度25{unit}"

@tool
def search_database(query: str) -> List[Dict[str, Any]]:
    """搜索数据库获取信息。
    
    Args:
        query: 搜索查询字符串
    
    Returns:
        匹配查询的结果列表
    """
    # 模拟数据库搜索
    return [{"id": 1, "name": "产品A", "price": 99.99}]

@tool
def create_user(name: str, email: str, age: Optional[int] = None) -> Dict[str, Any]:
    """在系统中创建新用户。
    
    Args:
        name: 用户全名
        email: 用户邮箱
        age: 用户年龄（可选）
    
    Returns:
        创建的用户对象
    """
    user = {"id": 123, "name": name, "email": email}
    if age:
        user["age"] = age
    return user

# 创建代理所需的提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有用的AI助手。使用提供的工具来回答用户问题。"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# 从工具函数创建OpenAI函数格式
tools = [get_weather, search_database, create_user]

# 创建代理
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

# 添加必要的prompt参数
agent = create_openai_functions_agent(model, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,  # 使用上面创建的agent
    tools=tools,  # 提供工具列表供agent使用
    verbose=True,  # 启用详细输出，显示agent的思考过程
    handle_parsing_errors=True  # 添加错误处理，当agent返回的输出无法解析时自动处理
)  # 创建执行器，负责协调agent与tools之间的交互

result = agent_executor.invoke({
    "input": "帮我查询上海的天气，并创建一个名为张三的用户，邮箱为zhangsan@example.com",
    "chat_history": []
})
print(result["output"])



# 简单函数调用示例（不使用代理）


functions = [convert_to_openai_function(t) for t in tools]
message = HumanMessage(content="北京今天天气怎么样？")
response = model.invoke([message], functions=functions)
print(response)

# 手动处理函数调用
import json
from langchain_core.messages import AIMessage, FunctionMessage

# 创建原始函数的副本（不是工具）
def get_weather_func(location: str, unit: str = "celsius") -> str:
    return f"{location}当前天气晴朗，温度25{unit}"

def search_database_func(query: str) -> List[Dict[str, Any]]:
    return [{"id": 1, "name": "产品A", "price": 99.99}]

def create_user_func(name: str, email: str, age: Optional[int] = None) -> Dict[str, Any]:
    user = {"id": 123, "name": name, "email": email}
    if age:
        user["age"] = age
    return user

available_functions = {
    "get_weather": get_weather_func,
    "search_database": search_database_func,
    "create_user": create_user_func
}

messages = [
    HumanMessage(content="创建一个名为李四的用户，邮箱为lisi@example.com"),
]

ai_response = model.invoke(messages, functions=functions)

if ai_response.additional_kwargs.get("function_call"):
    function_name = ai_response.additional_kwargs["function_call"]["name"]
    function_args = json.loads(ai_response.additional_kwargs["function_call"]["arguments"])
    
    function_to_call = available_functions[function_name]
    function_response = function_to_call(**function_args)
    
    messages.append(AIMessage(content="", additional_kwargs={"function_call": {
        "name": function_name,
        "arguments": json.dumps(function_args)
    }}))
    messages.append(FunctionMessage(content=str(function_response), name=function_name))
    
    final_response = model.invoke(messages)
    print(final_response.content)