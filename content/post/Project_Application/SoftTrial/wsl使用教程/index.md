---
title: wsl使用教程
description: ""
date: 2025-06-30T15:04:11+08:00
image: images/index/index.png
categories:
    - Project_Application
tags:
    - SoftTrial
---




## 基础知识

### 安装

相关教程：

[windows官方](https://learn.microsoft.com/zh-cn/windows/wsl/install)



### 问题解决


#### wsl和docker冲突  表现为wsl无法联网

![docker打开一会wsl断开连接](images/index/image.png)
![docker报错](images/index/image-1.png)

使用下面命令之后重启可以恢复，但是当再次打开docker又会出现问题,主要就是关了docker就行
```bash
wsl --shutdown
netsh winsock reset
```