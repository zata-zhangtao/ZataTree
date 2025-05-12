---
title: conda使用教程
description: ""
date: 2025-03-10T14:00:34+08:00
# image: images/index/index.png
categories:
    - Knowledge
tags:
    - others
    - 教程
---



## conda常用命令


```bash
# 1. 创建新的环境（指定Python版本）
conda create -n env_name python=3.8

# 2. 激活环境
conda activate env_name

# 3. 安装包（在当前环境）
conda install package_name

# 4. 列出当前环境的已安装包
conda list

# 5. 退出当前环境
conda deactivate

# 6. 列出所有环境
conda env list

# 7. 更新所有包
conda update --all

# 8. 删除指定环境
conda env remove -n env_name

# 9. 搜索可用包
conda search package_name

# 10. 卸载包
conda remove package_name

# 11. 查看Conda版本
conda --version

# 12. 更新Conda
conda update conda

# 13. 导出当前环境到文件
conda env export > environment.yml

# 14. 从文件创建环境
conda env create -f environment.yml

# 15. 创建环境并指定多个包
conda create -n env_name python=3.8 numpy pandas

# 16. 批量安装requirements.txt中的包
conda install --file requirements.txt

# 17. 导出当前环境的包列表到requirements.txt
conda list --export > requirements.txt

# 18. 安装特定版本的包
conda install package_name=1.2.3

# 19. 指定通道安装包
conda install -c channel_name package_name

# 20. 查看当前配置的通道
conda config --show channels

# 21. 添加新的通道
conda config --add channels channel_name

# 22. 清理未使用的包和缓存
conda clean --all

# 23. 克隆现有环境
conda create --name new_env_name --clone env_name

# 24. 在特定环境中运行命令
conda run -n env_name command

# 25. 临时使用某个环境运行命令（不激活）
conda run -n env_name python script.py

# 26. 查看环境的历史修订版本
conda list --revisions

# 27. 回滚到特定版本的包
conda install package_name --revision N

# 28. 设置通道优先级（优先使用指定通道）
conda config --set channel_priority strict

# 29. 启用/禁用自动激活base环境
conda config --set auto_activate_base false

# 30. 查看Conda配置信息
conda config --show

# 31. 设置环境变量
conda env config vars set VARIABLE_NAME=value

# 32. 查看环境变量
conda env config vars list

# 33. 取消环境变量
conda env config vars unset VARIABLE_NAME

# 34. 列出包的依赖关系
conda info --dependencies package_name

# 35. 列出环境的安装历史
conda list --show-channel-urls

# 36. 移除指定通道
conda config --remove channels channel_name

# 37. 检查Conda环境的完整性
conda doctor

# 38. 在离线模式下安装包
conda install --offline package_name

# 39. 安装本地下载的Conda包
conda install /path/to/package_file.tar.bz2

# 40. 查看Conda的缓存位置
conda info --cache
```


## 一些问题和解决方案

### 如何修改当前环境的名称

```bash
# 克隆 myenv 到 newenv
conda create --name newenv --clone myenv

# 删除 myenv
conda env remove --name myenv
```


### conda install 和pip install区别

[参考-csdn](https://blog.csdn.net/whc18858/article/details/127135973)

`conda install` 和 `pip install` 都是用于安装 Python 包的工具，但它们有以下主要区别：

1. **包管理范围**：
   - `conda install`：管理 Python 包和非 Python 依赖（如 C 库、编译器等），适用于科学计算和数据科学环境。
   - `pip install`：主要管理 Python 包，依赖系统级库或预编译轮子（wheels）。

2. **环境管理**：
   - `conda install`：与 Conda 环境紧密集成，安装的包默认进入当前激活的 Conda 环境，隔离性强。
   - `pip install`：默认安装到全局 Python 环境或虚拟环境（如 venv），需要额外配置隔离。

3. **包来源**：
   - `conda install`：从 Conda 仓库（默认或自定义通道，如 conda-forge）获取包，包通常预编译，兼容性好。
   - `pip install`：从 PyPI 仓库获取包，可能需要编译源码，兼容性依赖系统环境。

4. **依赖解决**：
   - `conda install`：使用更严格的依赖解析器，优先考虑整个环境的兼容性，可能安装较旧版本以确保稳定性。
   - `pip install`：依赖解析较宽松，可能导致版本冲突，需手动处理。

5. **使用场景**：
   - `conda install`：适合需要复杂依赖（如 NumPy、TensorFlow）或跨平台环境的场景，常见于数据科学和机器学习。
   - `pip install`：适合轻量级 Python 项目或 Conda 仓库中不可用的包。

**注意**：两者可结合使用，但在 Conda 环境中优先用 `conda install`，仅在包缺失时用 `pip install`，以避免环境冲突。




<!-- #  ☆ conda基本使用教程 -->
## 安装

|标题|内容|
|--|--|
|windwos安装miniconda|[CSDN](https://blog.csdn.net/ming12131342/article/details/140233867)|
|ubtuntu安装miniconda|[CSDN](https://blog.csdn.net/qq_41685627/article/details/139057628)|
---
##  创建/删除 一个环境

`创建`
```bash
conda create --name your_env_name numpy scipy
或者
conda create -n your_env_name python=3.5 numpy scipy
```

`删除`

```cpp
# 如果环境正在使用
conda deactivate
# 删除环境
conda remove --name ENV_NAME --all
或
conda remove -n ENV_NAME --all

```

> ENV_NAME表示要移除/删除的环境名称。在删除环境之前，请确保通过运行conda deactivate命令来停用该环境。
> 使用--all标志会删除安装在该环境中的所有软件包

---


## 把自己的代码安装到conda环境中
step1： 安装setuptools库

```cpp
pip install setuptools
```

step2：创建一个如下的setup.py程序

比如我的代码包的文件夹名是 nirapi,`setup.py文件必须放在和nirapi文件同一级的目录`

```cpp
|----nirapi
|		|------utils.py
|       |------test.py
|
|----setup.py
```


```cpp
# coding=utf-8
from setuptools import setup

setup(
    author="zata",
    description="This is a nir analyse api, writen by zata",   ### 一句话概括一下
    name="nirapi",   ### 给你的包取一个名字
    version="1.0",   ### 你的包的版本号
    packages=["nirapi", "nirapi/AnalysisClass"],# 这里写的是需要从哪个文件夹下导入python包，如果找不到会报错，默认你下载下来解压之后的文件夹名就是nirapi，如果文件夹里面还有子文件夹也要输入进去
    package_data={
        'nirapi': ['*'],  # 特定子文件夹中的所有文件，这行代码和上面那行好像只要一个就是，不过不管了，都写吧
    },
	exclude_package_date={'':['.gitignore'], '':['dist'], '':'build', '':'utility.egg.info'},    ### 这是需要排除的文件，也就是只把有用的python文件导入到环境变量中

)

```

step3：安装
(到setup.py的路径下面)

```cpp
 pip install . 
```

