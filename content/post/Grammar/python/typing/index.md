---
title: typing-提高代码可读性
description: ""
date: 2025-03-15T20:34:43+08:00
# image: images/index/index.png
categories:
    - Grammar
tags:
    - python
---


## 首先掌握


### typedDict

```python
from typing import TypedDict

# 定义一个 TypedDict
class Person(TypedDict):
    name: str
    age: int
    email: NotRequired[str]  # 可选字段

# 使用这个类型
person: Person = {"name": "Alice", "age": 25}  # 合法
# person = {"name": "Alice"}  # 非法：缺少 'age' 键
# person = {"name": "Alice", "age": "25"}  # 非法：'age' 应该是 int 类型
```
**特点**
1. **固定键**：`TypedDict` 定义的键是固定的，不能随意添加或删除未定义的键。
2. **类型检查**：类型检查工具（如 `mypy`）会验证字典是否符合定义的结构。
3. **继承性**：可以通过继承扩展 `TypedDict`。


### 基本类型注解
```python
from typing import List, Dict, Tuple, Set, Optional, Union

# 基本类型
name: str = "Alice"
age: int = 25
height: float = 1.75
is_student: bool = True

# 容器类型
numbers: List[int] = [1, 2, 3]
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
point: Tuple[int, int, str] = (10, 20, "origin")
unique_numbers: Set[int] = {1, 2, 3}

# 可选类型和联合类型
middle_name: Optional[str] = None  # 可以是字符串或 None
id: Union[int, str] = 123  # 可以是整数或字符串


# 函数注解
def greet(name: str) -> str:
    return f"Hello, {name}!"

# 类注解
class Point:
    x: int
    y: int
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

# 泛型
from typing import TypeVar
T = TypeVar('T') # 表示任何类型
def identity(item: T) -> T:
    return item
T = TypeVar('T', int, float)
def add(a: T, b: T) -> T:
    return a + b

# 嵌套类型
from typing import List, Dict
def process_data(data: List[Dict[str, int]]) -> List[int]:
    return [item["value"] for item in data]
    
# callable类型
from typing import Callable
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)

# Any类型
from typing import Any
def print_anything(value: Any) -> None:
    print(value)

# 类型别名
Vector = List[float]
def normalize(vector: Vector) -> Vector:
    return [v / sum(vector) for v in vector]

# 自定义类型
from typing import NewType
UserId = NewType('UserId', int)
```







---


## typing




{{<bilibili BV14Q4y1n7jz>}}



`typing` 模块在 Python 3.5+ 中引入，用于支持类型注解（Type Hints），帮助开发者在代码中声明变量、函数参数和返回值的类型。它主要用于静态类型检查工具（如 mypy）和提高代码可读性，而不是运行时强制类型检查。

以下是逐步讲解：

---

### 1. **基础概念**
类型注解是 Python 中一种可选的语法，用于标注变量或函数的预期类型。它不会影响代码的运行，但可以被工具（如 IDE 或 mypy）用来检测类型错误。

```python
# 没有类型注解
x = 42

# 有类型注解
x: int = 42
```

---

### 2. **导入 `typing` 模块**
`typing` 模块提供了许多工具，用于处理复杂类型（如列表、字典、函数等）。

```python
from typing import List, Dict, Optional, Union
```

---

### 3. **基本类型注解**
Python 的内置类型（如 `int`, `str`, `float`, `bool`）可以直接使用。

```python
name: str = "Alice"
age: int = 25
height: float = 1.75
is_student: bool = True
```

---

### 4. **容器类型**
`typing` 提供了支持泛型（Generic Types）的工具，用于指定容器内的元素类型。

#### (1) `List`
表示列表及其元素类型：
```python
from typing import List

numbers: List[int] = [1, 2, 3]  # 列表中的元素是整数
names: List[str] = ["Alice", "Bob"]
```

#### (2) `Dict`
表示字典及其键值类型：
```python
from typing import Dict

scores: Dict[str, int] = {"Alice": 90, "Bob": 85}  # 键是字符串，值是整数
```

#### (3) `Tuple`
表示元组及其元素类型：
```python
from typing import Tuple

point: Tuple[int, int, str] = (10, 20, "origin")  # 元组有 3 个元素，类型分别是 int, int, str
```

#### (4) `Set`
表示集合及其元素类型：
```python
from typing import Set

unique_numbers: Set[int] = {1, 2, 3}
```

---

### 5. **可选类型和联合类型**
#### (1) `Optional`
表示一个值可以是某种类型或 `None`：
```python
from typing import Optional

middle_name: Optional[str] = None  # 可以是字符串或 None
middle_name = "Marie"  # 合法
```

#### (2) `Union`
表示一个值可以是多种类型之一：
```python
from typing import Union

id: Union[int, str] = 123  # 可以是整数或字符串
id = "ABC123"  # 也合法
```

> **注意**：从 Python 3.10 开始，可以直接使用 `|` 运算符替代 `Union`，例如 `int | str`。

```python
id: int | str = 123  # Python 3.10+
```

---

### 6. **函数类型注解**
函数的参数和返回值也可以添加类型注解。

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}"
```

- `a: int` 表示参数 `a` 应为整数。
- `-> int` 表示函数返回值的类型是整数。

#### 可选参数
```python
from typing import Optional

def get_full_name(first: str, last: str, middle: Optional[str] = None) -> str:
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"
```

---

### 7. **复杂类型**
#### (1) 嵌套类型
```python
from typing import List, Dict

# 列表中的元素是字典
students: List[Dict[str, int]] = [
    {"Alice": 90},
    {"Bob": 85}
]
```

#### (2) `Callable`
表示可调用对象（如函数）的类型：
```python
from typing import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# 示例用法
def multiply(x: int, y: int) -> int:
    return x * y

result = apply(multiply, 3, 4)  # 返回 12
```

- `Callable[[int, int], int]` 表示一个函数，接受两个 `int` 参数，返回 `int`。

---

### 8. **自定义类型**
可以使用 `TypeAlias` 定义类型别名（Python 3.6+）：
```python
from typing import TypeAlias

Vector: TypeAlias = List[float]

def magnitude(v: Vector) -> float:
    return sum(x * x for x in v) ** 0.5
```

在 Python 3.12+ 中，可以直接用 `type` 关键字：
```python
type Vector = List[float]  # Python 3.12+
```

---

### 9. **Any 类型**
`Any` 表示任意类型，相当于禁用类型检查：
```python
from typing import Any

data: Any = 42  # 可以是任何类型
data = "hello"  # 合法
```

---

### 10. **使用类型检查工具**
类型注解不会在运行时强制执行。要检查类型错误，可以使用 `mypy`：
1. 安装 mypy：
   ```bash
   pip install mypy
   ```
2. 运行检查：
   ```bash
   mypy your_script.py
   ```

示例：
```python
# test.py
def add(a: int, b: int) -> int:
    return a + b

print(add("1", "2"))  # 类型错误
```
运行 `mypy test.py` 会提示参数类型不匹配。

---

### 11. **常见问题**
- **类型注解会影响性能吗？**
  不会，类型注解仅用于静态检查，运行时会被忽略。
- **Python 版本差异？**
  - Python 3.9+ 支持内置类型（如 `list[int]`）代替 `List[int]`。
  - Python 3.10+ 支持 `|` 替代 `Union`。
  - Python 3.12+ 支持 `type` 关键字定义类型别名。

---

### 12. **完整示例**
```python
from typing import List, Dict, Optional, Union

def process_data(
    numbers: List[int],
    info: Dict[str, str],
    flag: Optional[bool] = None
) -> Union[str, int]:
    if flag:
        return sum(numbers)
    return info.get("name", "Unknown")

result = process_data([1, 2, 3], {"name": "Alice"}, True)
print(result)  # 输出 6
```

---

希望这个教程对你有帮助！如果有具体问题或需要更深入的示例，请告诉我。