---
title: linux服务器初始化配置教程
description: ""
date: 2025-03-16T17:16:02+08:00
# image: images/index/index.png
categories:
    - Knowledge
tags:
    - Linux
---


### Ubuntu 初始化配置



```bash

## 1.设置密码并更新软件包
sudo passwd 
sudo apt update && sudo apt upgrade -y

## 2. 安装ssh-server
sudo apt install  openssh-server

## 3.配置ssh
vim /etc/ssh/sshd_config

# 常见配置项示例
Port 22                    # SSH 端口
PermitRootLogin no        # 禁止 root 登录
PasswordAuthentication yes # 允许密码认证
AllowUsers myuser # 允许特顶用户登录
Port 2222  #修改端口，减少扫描攻击

## 4.重启ssh服务
sudo systemctl restart ssh

## 5.创建用户(避免直接使用root账号)
adduser myuser
usermod -aG sudo myuser


## 6. 连接服务器
ssh root@服务器IP地址 -p [你自己设置的端口]
