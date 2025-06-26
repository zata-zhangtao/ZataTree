---
title: conda使用教程|pip使用教程|依赖安装_使用教程
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


<!-- #  ☆ conda基本使用教程 -->
## conda安装

```bash
# linux
 wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh 
cd ~   # 如果按照路径不是~/miniconda，需要执行   安装路径/miniconda/bin/conda init bash,然后在cd ~
source .bashrc   
```







|标题|内容|
|--|--|
|windwos安装miniconda|[CSDN](https://blog.csdn.net/ming12131342/article/details/140233867)|
|ubtuntu安装miniconda|[CSDN](https://blog.csdn.net/qq_41685627/article/details/139057628)|
---
##  conda 创建/删除 一个环境

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




## **pip 使用指南**
`pip` 是 Python 的默认包管理工具，用于安装、升级和卸载 Python 包。它通常与 Python 一起安装，适用于大多数 Python 项目。

### **基本用法**
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

### **实用建议**
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



## 配置镜像源


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





## 一些问题和解决方案



### 配置


### 希望 pip 忽略版本冲突并继续安装其他包/忽略报错

```bash 

# 忽略依赖检查
pip install -r requirements.txt --no-dependencies

# 强制安装，即使版本冲突
pip install -r requirements.txt --force-reinstall

# 跳过失败的包
while read requirement; do
    pip install "$requirement" || echo "Failed to install $requirement, continuing..."
done < requirements.txt

```





###  安装完成后，在执行`source.bashrc`后，输入命令`conda --version`并没有弹出conda，显示没有此命令

一般来说，miniconda会默认安装在`~/miniconda3`目录下，执行上面的cd ~  和 source .bashrc后，会将conda添加到环境变量中，但是有时候，默认安装位置也会发生变化，在本次事件中，我发现conda的默认安装位置变成了opt目录下（在1panel平台上的容器中使用），所以需要手动添加环境变量，

验证 Conda 是否正常工作：
```bash
/opt/miniconda3/bin/conda --version
```
- 如果输出类似 `conda 24.1.2` 的版本号，说明 Conda 已正确安装，只是未添加到 Shell 环境中。
- 如果报错（例如文件不存在），检查 `/opt/miniconda3/bin/conda` 是否存在，可能需要重新安装。


如果conda能正常使用，那么
执行下面的命令


```bash
# 这会在你的 ~/.bashrc 文件中添加 Conda 的初始化脚本，指向 /opt/miniconda3 目录。
/opt/miniconda3/bin/conda init  

# 添加环境变量到 Shell 会话
source ~/.bashrc
```
上面操作后就成功了，可以
检查 `conda` 命令是否全局可用：
```bash
conda --version
```
- 如果成功输出版本号，说明配置完成。


![配置过程](images/index/image.png)






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


### pip问题  get_installed_distributions 出错

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





### 如何生成依赖

```py
pip freeze > requirements.txt


pipreqs ./
```