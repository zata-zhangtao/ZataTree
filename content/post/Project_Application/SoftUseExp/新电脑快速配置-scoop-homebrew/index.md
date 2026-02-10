---
title: 新电脑快速配置-scoop
description: ""
date: 2026-02-10T11:59:09+08:00
image: images/index/index.png
categories:
    - Project_Application
tags:
    - SoftUseExp
---





# windows (注意要最好打开clash的TUN模式)

1. 必备开发工具安装：

    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    irm get.scoop.sh | iex
    scoop bucket add extras
    scoop install git uv just nvm autohotkey
    ```

2. 额外插件安装

- 智能桌面助手--主要功能是查看当前输入法是中/英文
    [ImTip 智能桌面助手](https://github.com/aardio/ImTip) 