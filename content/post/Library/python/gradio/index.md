---
title: gradio
description: ""
date: 2025-03-05T21:52:18+08:00
image: images/index/index.png
categories:
    - Library
tags:
    - python
---



### 快速入门

```py
import gradio as gr
#输入文本处理程序
def greet(name):
    return "Hello " + name + "!"
#接口创建函数
#fn设置处理函数，inputs设置输入接口组件，outputs设置输出接口组件
#fn,inputs,outputs都是必填函数
demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
```


![alt text](images/index/image.png)