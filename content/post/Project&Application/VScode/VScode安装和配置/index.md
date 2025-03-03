---
title: VScode安装和配置
description: 
date: 2025-03-03T00:00:00+08:00
# slug: 文件夹名/index.md ## 必填，文件夹名/index.md
# image: helena-hertz-wWZzXlDpMog-unsplash.jpg
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
    - VScode

---


参考：
https://blog.csdn.net/weixin_46474921/article/details/132841711
# 安装
## 1. 下载安装
[VScode官网](https://code.visualstudio.com/)
注意，这一步最好全部打勾

![alt text](image/index/index.png)


## 2. 设置默认terminal为cmd
![设置terminal](image/index/index-1.png)

## 3. 修改Code Runner 的配置（右键运行）
`首先你要安装好Code Runner 插件`
- 修改点击右键运行时的运行环境，改为终端运行

![让runconde默认在terminal](image/index/index-2.png)

- 修改右键运行时工作路径

![修改run code默认的路径](image/index/index-3.png)

4. 设置文件自动保存

![设置文件自动保存](image/index/index-4.png)




# 其他相关设置
## vscode右侧的预览窗口设置
![预览窗口](image/index/index-5.png)

设置方法，在设置里面搜索minimap  

![设置显示预览窗口](image/index/index-6.png)


## vscode写markdown插入图片时放在指定目录

参考 https://juejin.cn/post/7244809769794289721

![vscode写markdown插入图片时放在指定目录](image/index/index-7.png)

```bash
**/*.md      assets/${documentDirName}/${fileName}   # 以原始文件名放到 ./assets/<md文件名>/<图片文件名>
**/*.md      assets/${documentBaseName}/${documentBaseName}.${fileExtName}   # 重新以md文件名命名图片名
```

## vscode折叠代码

![alt text](image/index/index-8.png)





---
---
---


# 遇到的问题
## vscode 一直 reactivatiing terminals

这个是由于python扩展找不到虚拟环境的问题，具体可以看    
https://stackoverflow.com/questions/78886125/vscode-python-extension-loading-forever-saying-reactivating-terminals/78886126#78886126

![图片显示reactivatiing terminals](image/index/index-9.png)

我的解决方法是把python Locator换成js

![把python Locator换成js](image/index/index-10.png)