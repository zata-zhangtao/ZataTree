---
title: 包管理工具uv使用教程
date: 2025-05-11
image: images/index/index.png
categories:
    - Platforms&Tools
tags:
    - uv

---



uv常用命令
```bash
# 初始化一个新的 Python 项目
uv init <project-name>

# 创建虚拟环境
uv venv

# 激活虚拟环境（Unix/macOS）
source .venv/bin/activate
# 激活虚拟环境（Windows）
.venv\Scripts\activate

# 安装依赖
uv pip install <package-name>

# 安装项目依赖（从 pyproject.toml 或 requirements.txt）
uv pip install -r requirements.txt
# 或
uv pip install .

# 升级包
uv pip install --upgrade <package-name>

# 卸载包
uv pip uninstall <package-name>

# 列出已安装的包
uv pip list

# 导出依赖到 requirements.txt
uv pip freeze > requirements.txt

# 运行 Python 脚本或命令
uv run <script.py>
# 或
uv run python <script.py>

# 添加依赖到 pyproject.toml
uv add <package-name>

# 移除依赖从 pyproject.toml
uv remove <package-name>

# 同步项目依赖（确保虚拟环境与 pyproject.toml 一致）
uv sync

# 查看依赖树
uv tree

# 清理缓存
uv cache clean

# 检查 uv 版本
uv --version
```


UV 是一个由 Astral (Ruff 的开发者) 开发的、用 Rust 编写的极速 Python 包安装器和解析器。它的目标是成为 `pip` 和 `venv` 的直接替代品，提供更快、更友好的用户体验。


**教程大纲:**

1.  **UV 是什么？为什么选择 UV？**
2.  **安装 UV**
3.  **核心概念**
    * 虚拟环境管理
    * 包管理 (作为 `pip` 的替代)
    * 依赖解析
    * 全局缓存
4.  **基本命令详解**
    * 创建和管理虚拟环境 (`uv venv`)
    * 安装包 (`uv pip install`)
    * 卸载包 (`uv pip uninstall`)
    * 列出已安装的包 (`uv pip list`)
    * 生成依赖文件 (`uv pip freeze`)
    * 从依赖文件安装 (`uv pip install -r`, `uv pip sync`)
    * 编译依赖 (`uv pip compile`)
5.  **高级用法和特性**
    * 使用 `pyproject.toml`
    * 临时执行包 (`uvx`)
    * 缓存管理 (`uv cache`)
6.  **与 pip 的主要区别和优势**
7.  **总结与展望**

---

### 1. UV 是什么？为什么选择 UV？

* **UV 是什么？**
    UV 是一个实验性的 Python 包管理工具，旨在提供一个非常快速的、统一的包安装和虚拟环境管理体验。它被设计为 `pip`, `pip-tools` (特别是 `pip-compile`) 和 `venv` 的替代品。

* **为什么选择 UV？**
    * **速度极快:** UV 使用 Rust 编写，并在依赖解析和包安装方面进行了大量优化，通常比 `pip` 快几个数量级，尤其是在复杂的依赖关系或冷缓存启动时。
    * **统一体验:** 将虚拟环境创建 (`venv`) 和包安装/管理 (`pip`) 功能整合到单个命令行工具 `uv` 中。
    * **更好的依赖解析器:** UV 内置了一个高性能的依赖解析器，可以更快、更准确地解决复杂的依赖冲突。
    * **现代化的设计:** 遵循最新的 Python 打包标准 (如 PEP 517, PEP 621)。
    * **全局缓存:** UV 使用一个共享的全局缓存来存储下载的包和构建的轮子 (wheels)，这使得在不同项目中重用依赖时速度更快，并节省磁盘空间。
    * **`pip-compile` 功能内置:** `uv pip compile` 命令提供了类似于 `pip-tools` 的依赖锁定功能。
    * **`uvx`**: 类似于 `npx` (Node.js) 或 `pipx run`，允许你临时执行来自 PyPI 的包，而无需将其安装到你的项目中或全局环境中。

---

### 2. 安装 UV

你可以通过多种方式安装 UV：

* **使用 `curl` (Linux & macOS):**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
* **使用 `pip` (不推荐用于全局安装，除非在隔离环境中):**
    ```bash
    pip install uv
    ```
* **使用 `pipx` (推荐，用于将 UV 安装到隔离环境中):**
    ```bash
    pipx install uv
    ```
    如果你没有 `pipx`, 可以先安装它: `pip install pipx` 

![安装pipx](images/index/image.png)


* **使用 `cargo` (如果你是 Rust 开发者):**
    ```bash
    cargo install uv
    ```
* **从 GitHub Releases 下载预编译的二进制文件。**

安装完成后，验证安装：
```bash
uv --version
```

*注意：如果你发现安装好之后，vscode/cursor中的terminal并没有生效，那么需要完全重启vscode/cursor*



---

### 3. 核心概念

* **虚拟环境管理:**
    UV 可以像 `python -m venv` 或 `virtualenv` 一样创建和管理虚拟环境。它会将环境创建在 `.venv` 目录（默认）或你指定的目录。

* **包管理 (作为 `pip` 的替代):**
    `uv pip` 子命令旨在成为 `pip` 命令的直接替代品。大多数你熟悉的 `pip` 命令都可以用 `uv pip` 替代，例如 `uv pip install <package>`, `uv pip uninstall <package>`。

* **依赖解析:**
    UV 的核心优势之一是其快速且健壮的依赖解析器。当你安装包或编译需求文件时，它会分析所有直接和间接的依赖关系，找到一组兼容的版本。

* **全局缓存:**
    UV 会在用户缓存目录（例如 `~/.cache/uv` 或 `%LOCALAPPDATA%\uv\cache`）中维护一个全局缓存。这包括下载的包索引、sdist、wheel 文件等。这意味着如果你在项目 A 中安装了 `requests==2.30.0`，在项目 B 中再次安装相同版本的 `requests` 时，UV 可以直接从缓存中获取，无需重新下载或构建。

---

### 4. 基本命令详解

#### 创建和管理虚拟环境 (`uv venv`)

* **创建虚拟环境:**
    默认情况下，会在当前目录下创建一个名为 `.venv` 的虚拟环境。
    ```bash
    uv venv
    ```
    ![uv venv](images/index/image-1.png)
    你也可以指定环境名称和 Python解释器：
    ```bash
    uv venv myenv --python 3.11 # 使用 python3.11 创建名为 myenv 的环境
    uv venv .env -p 3.9       # 使用 python3.9 创建名为 .env 的环境
    ```

* **激活虚拟环境:**
    UV 创建的虚拟环境与标准 `venv` 模块创建的环境结构相同，激活方式也一样：
    * Linux/macOS:
        ```bash
        source .venv/bin/activate
        # 或 source myenv/bin/activate
        ```
    * Windows (CMD):
        ```bash
        .venv\Scripts\activate.bat
        ```
    * Windows (PowerShell):
        ```bash
        .venv\Scripts\Activate.ps1
        ```
    激活后，命令行提示符通常会显示虚拟环境的名称。

* **停用虚拟环境:**
    ```bash
    deactivate
    ```

#### 安装包 (`uv pip install`)

* **从 PyPI 安装最新版本:**
    (确保你已激活虚拟环境，或者 UV 会尝试安装到全局环境，除非配置了 `UV_SYSTEM_PYTHON=true` 来明确允许)
    ```bash
    uv pip install requests
    uv pip install flask sqlalchemy
    ```

* **安装特定版本:**
    ```bash
    uv pip install "requests==2.28.1"
    uv pip install "django>=3.2,<4.0"
    ```

* **从 `requirements.txt` 文件安装:**
    ```bash
    uv pip install -r requirements.txt
    ```

* **从本地项目安装 (使用 `pyproject.toml` 或 `setup.py`):**
    ```bash
    uv pip install .  # 安装当前目录下的项目
    uv pip install -e . # 以可编辑模式安装
    ```

* **从 Git 仓库安装:**
    ```bash
    uv pip install git+https://github.com/pallets/flask.git
    ```

* **指定索引 URL:**
    ```bash
    uv pip install --index-url https://my-private-index/simple requests
    ```

#### 卸载包 (`uv pip uninstall`)

```bash
uv pip uninstall requests
uv pip uninstall requests flask
```
可以配合 `-r requirements.txt` 使用，卸载文件中列出的所有包。

#### 列出已安装的包 (`uv pip list`)

```bash
uv pip list
uv pip list --format freeze # 输出格式与 requirements.txt 相同
uv pip list --format json   # 输出为 JSON 格式
```

#### 生成依赖文件 (`uv pip freeze`)

这会将当前环境中所有已安装的包及其版本输出到标准输出，通常用于生成 `requirements.txt` 文件。
```bash
uv pip freeze > requirements.txt
```

#### 从依赖文件安装 (`uv pip install -r`, `uv pip sync`)

* `uv pip install -r requirements.txt`:
    安装 `requirements.txt` 中列出的所有包。如果某些包已安装但版本不匹配，UV 会尝试升级或降级。如果某些包已安装但不在文件中，它们不会被卸载。

* `uv pip sync requirements.txt`:
    **推荐使用 `sync` 来精确同步环境。** 此命令会确保你的虚拟环境与 `requirements.txt` 文件中的内容 *完全一致*。
    * 安装文件中列出的、但尚未安装的包。
    * 升级或降级已安装的、但版本与文件中不符的包。
    * **卸载环境中已安装的、但未在文件中列出的包。**
    这对于确保环境的纯净和可复现性非常有用。

    如果你也使用 `pyproject.toml` (见下文)，你可以同步项目的依赖：
    ```bash
    uv pip sync pyproject.toml
    # 或 uv pip sync (如果 pyproject.toml 在当前目录)
    ```

#### 编译依赖 (`uv pip compile`)

类似于 `pip-compile` (来自 `pip-tools`)，此命令用于将高层级的依赖需求（例如 `requirements.in` 或 `pyproject.toml`）解析并锁定为具体的版本，输出到一个完全固定的依赖文件（例如 `requirements.txt`）。

* **从 `requirements.in` 编译到 `requirements.txt`:**
    `requirements.in` (示例):
    ```
    flask
    requests>=2.20
    ```
    编译命令:
    ```bash
    uv pip compile requirements.in -o requirements.txt
    ```
    这会生成一个 `requirements.txt` 文件，其中包含 Flask、Requests 以及它们所有子依赖的精确版本。

* **从 `pyproject.toml` 编译:**
    如果你的项目使用 `pyproject.toml` 定义依赖：
    `pyproject.toml` (部分示例):
    ```toml
    [project]
    name = "my-app"
    version = "0.1.0"
    dependencies = [
        "flask",
        "requests>=2.20",
    ]

    [project.optional-dependencies]
    dev = [
        "pytest",
        "black",
    ]
    ```
    编译命令:
    ```bash
    # 编译核心依赖
    uv pip compile pyproject.toml -o requirements.txt

    # 编译核心依赖和 'dev' 附加依赖
    uv pip compile pyproject.toml --extra dev -o requirements-dev.txt
    ```

---

### 与 Jupyter Notebook / JupyterLab 集成




#### 4.2 设置步骤 


```bash 
# 4.2.1 创建并激活项目的 uv 虚拟环境 
uv venv .venv && source .venv/bin/activate

# 4.2.2 在 uv 环境中安装 Jupyter 和 ipykernel
uv pip install jupyterlab ipykernel (或 notebook ipykernel)
#建议将这些作为开发依赖添加到 pyproject.toml

# 4.2.3 (推荐) 将 uv 环境注册为 Jupyter 内核 (Kernel) 
uv run python -m ipykernel install --user --name=my-project-venv --display-name="Python (my-project-venv)"


# 4.2.4 启动 JupyterLab 或 Jupyter Notebook 
从已激活 uv 环境的终端启动：uv run jupyter lab 或 uv run jupyter notebook
或者全局安装的 Jupyter 自动检测到注册的内核

# 4.2.5 在 Jupyter 中选择和使用 uv 环境的内核

```
#### 4.3 管理项目依赖 

在 Notebook 中通过 !uv pip install <new_package> (不推荐长期做法)

正确做法：在终端中激活 uv 环境，使用 uv pip install，然后重启 Jupyter 内核

使用 pyproject.toml 和 uv pip compile / uv pip sync 管理 Jupyter 项目的依赖

#### 4.4 移除 Jupyter 内核 (如果已注册) 

jupyter kernelspec list

jupyter kernelspec uninstall my-project-venv



### 5. 高级用法和特性

#### 使用 `pyproject.toml`

UV 对 PEP 621 (`pyproject.toml` 中的 `[project]` 表) 有良好支持。
* `uv pip install .`: 会读取 `pyproject.toml` 中的 `dependencies`。
* `uv pip install .[extra]`: 会安装核心依赖和指定的 `optional-dependencies`。
* `uv pip sync pyproject.toml`: 会同步环境以匹配 `pyproject.toml` 中定义的核心依赖。
* `uv pip sync pyproject.toml --extra dev`: 同步核心依赖和 `dev` 附加依赖。
* `uv pip compile pyproject.toml`: 将 `pyproject.toml` 中的依赖编译成锁文件。

#### 临时执行包 (`uvx`)

`uvx` 允许你执行来自 PyPI 的命令行工具，而无需将其永久安装到你的项目虚拟环境或全局 Python 环境中。UV 会在后台创建一个临时的隔离环境来运行该工具。

这对于代码格式化器、linter 或一次性脚本非常有用。

```bash
uvx black .             # 临时下载 black 并用它格式化当前目录代码
uvx cowsay "Hello UV"
uvx python -m http.server # 临时运行一个 http 服务器
```
`uvx` 会缓存下载的包，所以后续执行会更快。

#### 缓存管理 (`uv cache`)

* **查看缓存目录:**
    ```bash
    uv cache dir
    ```
* **清理缓存:**
    ```bash
    uv cache clean
    # 或者 uv cache prune (更推荐，会保留最近使用的条目)
    ```
    清理缓存可以释放磁盘空间，但下次安装包时可能需要重新下载。

---

### 6. 与 pip 的主要区别和优势

| 特性         | UV                                     | pip + venv + pip-tools                 |
| :----------- | :------------------------------------- | :------------------------------------- |
| **核心语言** | Rust                                   | Python                                 |
| **速度** | 极快 (通常快几个数量级)                   | 较慢                                   |
| **工具集** | 单一工具 `uv` (包含 venv, pip, compile) | 多个工具 (`python -m venv`, `pip`, `pip-compile`) |
| **依赖解析** | 内置高性能解析器                        | 依赖外部解析器 (有时较慢或不够健壮)         |
| **缓存** | 智能全局缓存                            | 每个虚拟环境或用户级缓存 (pip >= 20.1)     |
| **`sync`** | `uv pip sync` 精确同步环境               | 无直接对应命令 (需手动组合)             |
| **`uvx`** | `uvx <cmd>` 临时执行包                   | `pipx run <cmd>` (需要额外安装 `pipx`) |
| **`compile`**| `uv pip compile` 内置依赖锁定            | `pip-compile` (需要额外安装 `pip-tools`) |
| **错误信息** | 通常更清晰                              | 有时冗长                               |

**主要优势总结:**

1.  **性能:** 最显著的优势，尤其在大型项目或 CI/CD 环境中。
2.  **易用性:** 单个工具简化了工作流程。
3.  **强大的依赖管理:** 内置的编译和同步功能使得依赖管理更稳健。

---

### 7. 总结与展望

UV 是一个非常有前途的 Python 打包工具，它通过 Rust 实现带来了显著的性能提升和现代化的用户体验。它旨在简化 Python 开发者的日常工作，从创建环境到安装、管理和锁定依赖。

虽然 UV 仍在积极开发中（截至2025年初），但它已经足够稳定和强大，可以在许多项目中使用，特别是对于那些对性能有较高要求的场景。

**建议:**

* **尝试一下！** 特别是如果你对当前 `pip` 和 `venv` 的速度或工作流程感到不满。
* **关注 Astral 的官方博客和 UV 的 GitHub 仓库** ([https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)) 以获取最新的更新和功能。
* 可以考虑在你的项目中逐步引入 UV，例如先用它来创建虚拟环境和安装包，然后再尝试 `uv pip compile` 和 `uv pip sync`。
