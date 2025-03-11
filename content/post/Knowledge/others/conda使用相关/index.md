---
title: conda使用相关
description: ""
date: 2025-03-10T14:00:34+08:00
# image: images/index/index.png
categories:
    - Knowledge
tags:
    - others
---



#  ☆ conda基本使用教程
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

