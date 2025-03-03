---
title: 4-自定义Python函数创建博客：告别繁琐的文件头输入
description: ""
date: 2025-03-03T16:32:39+08:00
image: images/index/index.png
categories:
    # - DeepLearning
    # - Chart
    # - Python
    # - LLM
    - Project&Application
    # - Library
    # - PaperReading
    # - Study
    # - Other
    # - Knowledge points
tags:
    - hugo
    - Blog
---



![alt text](images/index/index.jpg)


以下是基于最新的需求重新撰写的博客文章，主题仍是“使用自定义Python函数创建博客，避免繁琐的文件头标准内容输入”。这次博客将反映新的功能：通过 `categories`、`tags` 和 `title` 三个参数生成文件夹和文件，并将路径组合为 `categories/tags/title`。

---

# 使用自定义Python函数创建博客：告别繁琐的文件头输入

在维护技术博客时，每次创建新文章都需要手动设置文件夹结构和标准化的Markdown文件头，例如标题、分类、标签和日期等。这种重复劳动不仅耗时，还容易出错。想象一下，如果能通过一个简单的命令，比如 `zata create -c Python -t github -b MyProject`，自动生成带有标准头部的博客文件，并按分类和标签组织目录结构，会不会让写作更高效？

在这篇博客中，我将展示如何用Python实现这一自动化工具，并将其打包成一个命令行可执行文件。通过自定义函数，我们可以轻松创建博客文件，避免手动输入繁琐的文件头内容。

---

## 背景与目标

假设你正在用静态网站生成器（如Jekyll或Hugo）写博客，每次新建文章时需要：
1. 创建一个文件夹结构，比如 `Python/github/MyProject`。
2. 在最内层文件夹中生成一个 `index.md` 文件。
3. 为 `index.md` 添加标准头部，例如：
   ```
   ---
   title: MyProject
   description: "空"
   date: 2025-03-03T15:20:45+08:00
   image: images/index.png
   categories:
       - Python
   tags:
       - github
   ---
   ```

手动完成这些步骤虽然可行，但效率低下。我的目标是：
- 编写一个Python脚本，接受 `categories`、`tags` 和 `title` 三个参数。
- 根据输入生成路径 `categories/tags/title`，并创建对应的文件夹和 `index.md` 文件。
- 自动填充标准头部信息，日期使用当前时间。
- 将脚本打包成命令行工具，支持 `zata create -c [分类] -t [标签] -b [标题]` 的调用方式。

---

## 实现步骤

### 步骤 1：设计基本功能

我们需要一个函数，根据输入的 `categories`、`tags` 和 `title` 创建文件夹和文件。以下是最小化的实现：

```python
import os
from datetime import datetime

def create_folder_and_md(categories, tags, title):
    current_dir = os.getcwd()
    target_path = os.path.join(current_dir, categories, tags, title)
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    os.makedirs(target_path, exist_ok=True)
    md_file_path = os.path.join(target_path, "index.md")
    header_content = f"""---
title: {title}
description: "空"
date: {current_time}
image: images/index.png
categories:
    - {categories}
tags:
    - {tags}
---
"""
    with open(md_file_path, 'w', encoding='utf-8') as f:
        f.write(header_content)
    print(f"文件夹 '{target_path}' 和 'index.md' 创建成功！")

create_folder_and_md("Python", "github", "MyProject")
```

这个脚本会在当前目录下创建 `Python/github/MyProject` 文件夹，并在其中生成带有标准头部的 `index.md`。

### 步骤 2：添加命令行支持

为了让脚本更实用，我们引入 `argparse` 模块，支持命令行参数输入：

```python
import os
from datetime import datetime
import argparse

def create_folder_and_md(categories, tags, title):
    current_dir = os.getcwd()
    target_path = os.path.join(current_dir, categories, tags, title)
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    try:
        os.makedirs(target_path, exist_ok=True)
        md_file_path = os.path.join(target_path, "index.md")
        header_content = f"""---
title: {title}
description: "空"
date: {current_time}
image: images/index.png
categories:
    - {categories}
tags:
    - {tags}
---
"""
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(header_content)
        print(f"文件夹 '{target_path}' 和 'index.md' 创建成功！")
    except Exception as e:
        print(f"发生错误: {str(e)}")

def main():
    parser = argparse.ArgumentParser(prog="zata", description="根据categories、tags和title创建一个文件夹和index.md文件")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")
    create_parser = subparsers.add_parser("create", help="创建文件夹和index.md")
    create_parser.add_argument("-c", "--categories", required=True, help="博客分类")
    create_parser.add_argument("-t", "--tags", required=True, help="博客标签")
    create_parser.add_argument("-b", "--title", required=True, help="博客标题")
    args = parser.parse_args()
    
    if args.command == "create":
        create_folder_and_md(args.categories, args.tags, args.title)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
```

保存为 `zata.py`，运行以下命令测试：
```bash
python zata.py create -c Python -t github -b MyProject
```

### 步骤 3：打包成可执行文件

为了方便使用，我们用 `PyInstaller` 将脚本打包成单一的 `.exe` 文件：

1. 安装 PyInstaller：
   ```bash
   pip install pyinstaller
   ```
2. 打包脚本：
   ```bash
   pyinstaller --onefile zata.py
   ```
3. 打包完成后，在 `dist` 文件夹中找到 `zata.exe`，运行：
   ```bash
   zata.exe create -c Python -t github -b MyProject
   ```

### 步骤 4：配置全局访问（可选）

若想在任意目录下直接运行 `zata`，可以将其添加到系统环境变量：
1. 将 `zata.exe` 移动到固定目录（如 `C:\Tools`）。
2. 在 Windows 的“环境变量”设置中，将该目录添加到 `Path`。
3. 重启命令行，输入 `zata create -c Python -t github -b MyProject` 测试。

---

## 成果展示

运行以下命令：
```bash
zata create -c Python -t github -b MyProject
```

结果：
- 生成目录结构：`Python/github/MyProject`。
- 在 `MyProject` 文件夹中创建 `index.md`，内容如下：
  ```
  ---
  title: MyProject
  description: "空"
  date: 2025-03-03T15:20:45+08:00
  image: images/index.png
  categories:
      - Python
  tags:
      - github
  ---
  ```
- 控制台输出：
  ```
  文件夹 'Python/github/MyProject' 和 'index.md' 创建成功！
  ```

整个过程只需一条命令，省去了手动创建文件夹和输入文件头的麻烦。

---

## 扩展与改进

这个工具已经能满足基本需求，但还有改进空间：
- **支持多分类和多标签**：修改 `header_content`，允许输入多个 `categories` 和 `tags`，用列表形式写入。
- **参数验证**：检查输入值是否包含非法字符（如 `/`、`\`），避免路径错误。
- **配置文件支持**：通过外部文件（如 YAML）定制头部模板。
- **跨平台兼容**：为 Linux/Mac 用户生成可执行脚本。

例如，要支持多标签，可以调整命令为：
```bash
zata create -c Python -t "github tensorflow" -b MyProject
```
然后解析 `tags` 参数为列表，写入多个 `- {tag}` 条目。

---

## 总结

通过这个简单的Python工具，我们将博客创建过程从繁琐的手动操作简化为一条命令。无论你是技术博主还是文档管理者，这种自动化方法都能显著提升效率。试试这个脚本吧，用代码解放你的双手，让创作更专注内容本身！

---

