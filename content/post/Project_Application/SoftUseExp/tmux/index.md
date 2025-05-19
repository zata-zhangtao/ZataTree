---
title: tmux
description: ""
date: 2025-05-19T11:32:28+08:00
image: images/index/index.png
categories:
    - Project_Application
tags:
    - SoftUseExp
---

```bash

# 创建新会话，无名称
tmux

# 创建新会话（带名称）
tmux new -s mysession

# 列出所有会话
tmux ls

# 附加到已有会话
tmux attach -t mysession

# 常用快捷键（默认前缀是 Ctrl-b）
Ctrl-b d        # 退出会话（不关闭）
Ctrl-b c        # 新建窗口
Ctrl-b ,        # 重命名当前窗口
Ctrl-b n        # 切换到下一窗口
Ctrl-b p        # 切换到上一窗口
Ctrl-b %        # 垂直分割窗格
Ctrl-b "        # 水平分割窗格
Ctrl-b o        # 切换到下一个窗格
Ctrl-b x        # 关闭当前窗格
Ctrl-b &        # 关闭当前窗口

# 杀死指定会话
tmux kill-session -t mysession

# 杀死所有 tmux 服务
tmux kill-server

# 提示：
# 1. 前缀键后松开再按功能键
# 2. 可修改 ~/.tmux.conf 自定义配置，例如：
#    set -g mouse on  # 启用鼠标支持
#    bind r source-file ~/.tmux.conf  # 重新加载配置
```
