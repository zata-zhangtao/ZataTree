---
title: 1panel使用教程｜云服务器使用教程
description: ""
date: 2025-03-09T16:14:31+08:00
# image: images/index/index.png
categories:
    - Knowledge
tags:
    - others
---


### 1panel安装

官网：   
https://1panel.cn/docs/installation/online_installation/


```bash
# ubuntu
curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh
```



### 问题和解决方案


#### 我自己使用1panel和云服务器的一些感悟

**在云服务器部署碰到的麻烦事：**

1. 1panel 的运行环境模式，会自动执行脚本，虽然它创建了一个docker容器，但是如果你进去想要把它的脚本关掉，它会自启动，而如果你把它的这个环境停掉，docker容器就消失了，所以不要用它的环境容器做什么事情
2. 1panel的docker连接之后要先执行一下su，不然的话命令是不好操作的，比如就没有补全功能
3. 要去/ect/hosts去设置一下github的ip地址解析，不然会很慢
4. 云服务器如果是国内厂商的，最好设置一下镜像源，不然的话会下载非常慢，比如pip install的时候
