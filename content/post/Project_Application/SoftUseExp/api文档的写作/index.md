---
title: 生成api文档工具的简易使用
description: ""
date: 2025-05-03T10:42:53+08:00
image: images/index/index.png
categories:
    - Project_Application
tags:
    - SoftUseExp
    - 简易使用
---


## api文档的必要性

虽然我一直在写python项目，也并没有前后端的区别，但是随着项目越变越大，越发感觉没有api文档，对于我的回顾来说是非常麻烦的，因此还是需要一个用于生成api的python插件或者说一个用于书写api文档的在线或离线工具，之前是有用过Sphinx来自动生成api文档，但是感觉存在使用太麻烦的问题，如果是小项目，可能配置都感觉很麻烦，书写格式，似乎有md格式可以使用，但是我还没有去尝试，使用了它默认的格式，头都昏了

![如图](images/index/image.png)


## 那些api文档工具可以使用

我只是做了简单的了解，太具体的深度还没有做。

1. Sphinx 也就是我上面说到了，我只使用了python版本的，感觉并不是特别好用的
2. fastopenapi 这个是专门用于生成fastapi后端的项目[项目地址](https://github.com/mr-fatalyst/fastopenapi)


## 具体工具使用

### Sphinx

以我的fainigleam项目为例
![faintgleam项目](images/index/image-1.png)

```bash 
mkdir docs && cd docs

sphinx-quickstart  # 第一个选y，后面看着填

vim source/conf.py  # 具体怎么改看下面

vim source/index.rst  # 具体怎么改看下面

sphinx-apidoc -o ./source ../src

make html

```


1. 创建docs文件夹，并cd进去
![创建文件夹](images/index/image-2.png)


2.sphinx-quickstart
![](images/index/image-3.png)

3.修改 `source/conf.py`文件

```py
# conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))  # 添加项目根目录到路径
sys.path.insert(0, os.path.abspath('../../src/'))  # 添加src目录到路径


#######################################
project = 'XXXXX'
copyright = 'XXXXXX'
author = 'XXXXX'
release = 'X.X.X'
#######################################


extensions = [
    'sphinx.ext.autodoc',      # 自动从docstrings生成文档
    'sphinx.ext.viewcode',     # 添加查看源码的链接
    'sphinx.ext.napoleon',     # 支持Google风格的文档字符串
]

# 配置autodoc扩展
autodoc_member_order = 'bysource'  # 按源码顺序记录成员
add_module_names = False  # 不在API文档中添加模块名

templates_path = ['_templates']
exclude_patterns = []

language = 'zh'


html_theme = 'sphinx_rtd_theme'  # 使用ReadTheDocs主题
html_static_path = ['_static']

```

![](images/index/image-4.png)


4. 修改 `source/index.rst`文件

```rst
########################################################
fainitgleam documentation
=============
.. toctree::
   :maxdepth: 2
   :caption: Contents:
#########################################################

# 前面都不变的，就这里增加一个modules
   modules
   
```

![](images/index/image-5.png)


5. 执行
    ```
    sphinx-apidoc -o ./source ../src
    ```
    ![](images/index/image-6.png)


6. make html

![](images/index/image-7.png)


7.就可以打开静态页面查看了

![alt text](images/index/image-8.png)
![alt text](images/index/image-9.png)
![alt text](images/index/image-10.png)