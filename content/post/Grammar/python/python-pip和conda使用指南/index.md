---
title: python-pip和conda使用指南
description: ""
date: 2025-03-18T18:11:09+08:00
image: images/index/index.png
categories:
    - Grammar
tags:
    - python
---

<!-- ![alt text](images/index/index.png) -->


以下是一些常用的 `pip` 和 `conda` 的镜像源，特别是在国内网络环境下可以显著提升下载速度。这些源由高校或机构提供，通常比默认源更快更稳定。

---

### **pip 镜像源**
`pip` 默认使用 PyPI（https://pypi.org/）作为包的来源，以下是常用的国内镜像源：

1. **清华大学镜像**  
   ```
   https://pypi.tuna.tsinghua.edu.cn/simple
   ```
   使用方法：
   ```bash
   pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple
   ```

2. **阿里云镜像**  
   ```
   https://mirrors.aliyun.com/pypi/simple/
   ```
   使用方法：
   ```bash
   pip install 包名 -i https://mirrors.aliyun.com/pypi/simple/
   ```

3. **中国科技大学镜像**  
   ```
   https://pypi.mirrors.ustc.edu.cn/simple/
   ```
   使用方法：
   ```bash
   pip install 包名 -i https://pypi.mirrors.ustc.edu.cn/simple/
   ```

4. **豆瓣镜像**  
   ```
   http://pypi.douban.com/simple/
   ```
   使用方法：
   ```bash
   pip install 包名 -i http://pypi.douban.com/simple/
   ```

5. **华为云镜像**  
   ```
   https://repo.huaweicloud.com/pypi/simple/
   ```
   使用方法：
   ```bash
   pip install 包名 -i https://repo.huaweicloud.com/pypi/simple/
   ```

#### **永久配置 pip 源**
为了避免每次手动指定，可以全局配置：
- **Linux/Mac**：编辑 `~/.pip/pip.conf`（没有就创建）
  ```ini
  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  ```
- **Windows**：编辑 `%USERPROFILE%\pip\pip.ini`
  同上内容。

---

### **conda 镜像源**
`conda` 默认使用 Anaconda 官方仓库，以下是常用的国内镜像源：

1. **清华大学镜像**  
   ```
   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
   https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
   ```
   配置方法：
   ```bash
   conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
   conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
   conda config --set show_channel_urls yes
   ```

2. **中国科技大学镜像**  
   ```
   https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
   https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
   ```
   配置方法：
   ```bash
   conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main
   conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free
   conda config --set show_channel_urls yes
   ```

3. **中科院镜像**  
   ```
   https://mirror.sjtu.edu.cn/anaconda/pkgs/main/
   https://mirror.sjtu.edu.cn/anaconda/pkgs/free/
   ```
   配置方法：
   ```bash
   conda config --add channels https://mirror.sjtu.edu.cn/anaconda/pkgs/main
   conda config --add channels https://mirror.sjtu.edu.cn/anaconda/pkgs/free
   conda config --set show_channel_urls yes
   ```

4. **阿里云镜像**  
   ```
   https://mirrors.aliyun.com/anaconda/pkgs/main/
   https://mirrors.aliyun.com/anaconda/pkgs/free/
   ```
   配置方法：
   ```bash
   conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/main
   conda config --add channels https://mirrors.aliyun.com/anaconda/pkgs/free
   conda config --set show_channel_urls yes
   ```

#### **conda-forge 源**
`conda-forge` 是一个社区维护的广泛使用的附加源，可以与上述源一起使用：
```bash
conda config --add channels conda-forge
```

#### **查看和清除配置**
- 查看当前配置：
  ```bash
  conda config --show channels
  ```
- 恢复默认源（清除自定义源）：
  ```bash
  conda config --remove-key channels
  ```






---

### **pip 使用指南**
`pip` 是 Python 的默认包管理工具，用于安装、升级和卸载 Python 包。它通常与 Python 一起安装，适用于大多数 Python 项目。

#### **基本用法**
1. **检查 pip 版本**  
   ```bash
   pip --version
   ```
   确保你使用的是最新版本，可以通过以下命令升级：
   ```bash
   pip install --upgrade pip
   ```

2. **安装包**  
   ```bash
   pip install 包名
   ```
   示例：安装 `requests` 库
   ```bash
   pip install requests
   ```
   指定版本：
   ```bash
   pip install requests==2.28.1
   ```

3. **列出已安装的包**  
   ```bash
   pip list
   ```

4. **升级包**  
   ```bash
   pip install --upgrade 包名
   ```

5. **卸载包**  
   ```bash
   pip uninstall 包名
   ```

6. **安装 requirements.txt 文件中的依赖**  
   如果项目有 `requirements.txt`，可以通过以下命令批量安装：
   ```bash
   pip install -r requirements.txt
   ```
   生成 `requirements.txt`：
   ```bash
   pip freeze > requirements.txt
   ```

#### **实用建议**
- **使用虚拟环境**：避免全局安装冲突，推荐使用 `venv`：
  ```bash
  python -m venv myenv
  source myenv/bin/activate  # Linux/Mac
  myenv\Scripts\activate     # Windows
  ```
- **代理设置**：如果网络受限，可通过代理安装：
  ```bash
  pip install 包名 --proxy=http://代理地址:端口
  ```
- **换源加速**：国内用户可使用镜像源（如清华源）：
  ```bash
  pip install 包名 -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

---

### **conda 使用指南**
`conda` 是一个跨平台的包和环境管理工具，适用于 Python 和其他语言，尤其在数据科学领域广受欢迎。它不仅管理包，还能管理整个环境（包括 Python 版本）。

#### **基本用法**
1. **检查 conda 版本**  
   ```bash
   conda --version
   ```
   更新 conda：
   ```bash
   conda update conda
   ```

2. **创建新环境**  
   ```bash
   conda create -n 环境名 python=版本号
   ```
   示例：创建名为 `myenv` 的 Python 3.9 环境
   ```bash
   conda create -n myenv python=3.9
   ```

3. **激活环境**  
   ```bash
   conda activate 环境名
   ```
   退出环境：
   ```bash
   conda deactivate
   ```

4. **安装包**  
   ```bash
   conda install 包名
   ```
   示例：
   ```bash
   conda install numpy
   ```
   指定版本：
   ```bash
   conda install numpy=1.21
   ```

5. **列出已安装的包**  
   ```bash
   conda list
   ```

6. **删除环境**  
   ```bash
   conda env remove -n 环境名
   ```

7. **导出和导入环境**  
   导出当前环境到 `environment.yml`：
   ```bash
   conda env export > environment.yml
   ```
   从文件创建环境：
   ```bash
   conda env create -f environment.yml
   ```

#### **实用建议**
- **conda 与 pip 混用**：conda 环境支持 pip，可以在激活环境后使用 pip 安装包。
- **换源加速**：国内用户可配置清华镜像：
  ```bash
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  conda config --set show_channel_urls yes
  ```
- **解决依赖冲突**：如果安装失败，尝试：
  ```bash
  conda install 包名 --channel conda-forge
  ```

---

### **pip vs conda 对比**
| 特性            | pip                          | conda                       |
|-----------------|------------------------------|-----------------------------|
| **主要用途**    | Python 包管理                | 包 + 环境管理              |
| **依赖管理**    | 仅 Python 包                 | 支持多种语言和工具          |
| **环境隔离**    | 需要配合 venv 或 virtualenv  | 内置环境管理功能           |
| **安装源**      | PyPI                         | Anaconda 仓库 + conda-forge |
| **适用场景**    | 轻量级项目                   | 数据科学、复杂依赖项目     |

---

### **问题解答**
####  **pip 和 conda 可以一起用吗？**  
   可以，但建议优先使用 conda 安装依赖，若 conda 源中没有，再用 pip。

####  **如何选择？**  
   - 小型项目或纯 Python 开发：用 pip + venv。
   - 数据科学、机器学习或需要管理多种依赖：用 conda。
   - 20250508，现在又出来一个uv

#### get_installed_distributions 出错

项目场景：开源项目 graph-tiger

在跑这个项目的时候，有一行代码一直报错

> from pip._internal.utils.misc import get_installed_distributions


这一行代码一直有问题，一开始我以为是环境的问题，后来才发现是pip版本的问题，好像在pip21.3版本之后就不支持这样写了

解决方案：

降级pip版本，可以降级到21.2版本

```
pip install -u pip==21.2
或者
pip intall pip==21.2
或者其他降级方法
```


