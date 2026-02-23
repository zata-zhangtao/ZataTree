---
title: Docker 私有镜像仓库
description: ""
date: 2026-02-23T00:20:36+08:00
image: images/index/index.png
categories:
    - Platforms_Tools
tags:
    - Docker
---


# 实战指南：使用 Docker 和 Traefik 搭建私有镜像仓库（及踩坑记录）

在 DevOps 流程中，拥有一个私有的 Docker Registry（镜像仓库）是必不可少的。虽然 Docker Hub 很好用，但出于隐私、速度和成本的考虑，自建仓库往往是更好的选择。本文将手把手教你如何使用 Docker Compose 和 Traefik 反向代理搭建一个带 HTTPS 和基础认证的轻量级私有仓库，并重点分析部署过程中最容易遇到的 “Gateway Timeout” 和 “Connection Refused” 等网络问题。

**为什么选择这个方案？**

*   **轻量级**：基于官方 `registry:2` 镜像，资源占用极小。
*   **安全**：通过 Traefik 自动管理 SSL 证书（Let's Encrypt），并配置 `htpasswd` 基础认证。
*   **易维护**：所有配置通过一个 `docker-compose.yml` 文件管理。

**准备工作**

1.  一台安装了 Docker 和 Docker Compose 的 Linux 服务器。
2.  一个域名并解析到服务器 IP（例如：`registry.example.com`）。
3.  **Traefik 已经在运行中**（如果你使用的是 Dokploy、Coolify 等面板，Traefik 通常是内置好的）。

**核心配置：docker-compose.yml**

为了方便演示，我们使用一个技巧：利用临时容器自动生成密码文件，避免手动安装 `htpasswd` 工具的麻烦。请创建一个目录 `my-registry`，并在其中新建 `docker-compose.yml`，内容如下：

```yaml
version: '3.8'

# 定义数据卷，持久化存储镜像和认证信息
volumes:
  registry-data:
  registry-auth-data:

# 【重点】定义网络
# 这里必须使用 external: true，表示使用外部已经存在的 Traefik 网络
# 如果你用的是 Dokploy，网络名通常是 dokploy-network
# 如果你是自己部署的 Traefik，通常叫 traefik_public 或 proxy
networks:
  dokploy-network:
    external: true

services:
  # 1. 辅助服务：自动生成账号密码
  # 启动后会生成密码文件并存入卷中，然后自动退出
  auto-setup-auth:
    image: httpd:alpine
    # 账号: admin, 密码: 123456 (生产环境请修改！)
    command: /bin/sh -c "htpasswd -Bbn admin 123456 > /auth/htpasswd"
    volumes:
      - registry-auth-data:/auth

  # 2. 核心仓库服务
  registry:
    image: registry:2
    container_name: my-private-registry
    restart: always

    # 【关键点 1】加入 Traefik 所在的网络
    networks:
      - dokploy-network
  
    # 端口映射（可选，仅用于本地调试，生产环境可注释掉）
    ports:
      - "5000:5000"
  
    environment:
      # 启用认证
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: "Registry Realm"
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
      # 告诉 Registry 它运行在 HTTPS 反向代理后面
      REGISTRY_HTTP_HEADERS_X_FORWARDED_FOR: true
      REGISTRY_HTTP_HEADERS_X_FORWARDED_PROTO: https
  
    volumes:
      - registry-data:/var/lib/registry
      - registry-auth-data:/auth
  
    depends_on:
      auto-setup-auth:
        condition: service_completed_successfully

    # 【关键点 2】Traefik 标签配置
    labels:
      - "traefik.enable=true"
      # 修改为你的实际域名
      - "traefik.http.routers.registry.rule=Host(`registry.example.com`)"
      # 指定入口点为 HTTPS
      - "traefik.http.routers.registry.entrypoints=websecure"
      # 启用 TLS (自动申请证书)
      - "traefik.http.routers.registry.tls.certresolver=letsencrypt"
      # 【至关重要】告诉 Traefik 容器内部端口是 5000
      - "traefik.http.services.registry.loadbalancer.server.port=5000"
      # 取消请求体大小限制（防止 docker push 大镜像失败）
      - "traefik.http.middlewares.limit.buffering.maxRequestBodyBytes=0"
```

配置完成后，使用 `docker-compose up -d` 命令启动服务。

**常见问题排查（Troubleshooting）**

在部署过程中，你可能会遇到以下几种错误，请根据现象进行排查：

**1. 504 Gateway Timeout (网关超时)**

![网关超时](images/index/image.png)

*   **现象**：浏览器访问域名/v2/，加载很久后显示 `504 Gateway Timeout`。
*   **原因**：这说明 Traefik 接到了请求，但是**无法连接到后端的 Registry 容器**。这通常是因为 Traefik 和 Registry **不在同一个 Docker 网络** 中。Traefik 就像大楼的前台，它想转接电话给 Registry，但发现线路不通。
*   **解决方案**：检查 `docker-compose.yml` 中的 `networks` 部分。必须确保 Registry 加入了 Traefik 所在的那个网络（通过 `docker network ls` 查看网络名称）。

**2. Context Deadline Exceeded (连接超时)**

*   **现象**：在使用 Dokploy 或命令行登录时，提示 `Client.Timeout exceeded while awaiting headers`。
*   **原因**：这通常是**网络层面的物理隔绝**。你的请求根本没有到达服务器，被防火墙拦在了外面。
*   **解决方案**：
    1.  检查云服务商（AWS/阿里云/腾讯云）的安全组，**必须开放 TCP 443 和 80 端口**。
    2.  检查服务器内部防火墙（如 `ufw` 或 `iptables`）。

**3. 登录失败或 404 Not Found**

*   **现象**：访问域名能通，但是 docker login 总是失败，或者页面显示 404。
*   **原因**：可能是 Traefik 把流量转发到了错误的端口。Registry 默认监听 **5000**，而 Traefik 默认转发到 80。
*   **解决方案**：确保 `labels` 中包含指定端口的配置：`- "traefik.http.services.registry.loadbalancer.server.port=5000"`。

**4. 推送镜像失败 (Blob Upload Unknown)**

*   **现象**：登录成功，但在 `docker push` 大文件时失败并重试。
*   **原因**：Traefik 或 Nginx 默认会限制上传文件的大小。
*   **解决方案**：添加中间件配置取消限制：`- "traefik.http.middlewares.limit.buffering.maxRequestBodyBytes=0"`。

**验证与使用**

部署成功后，建议按以下步骤进行测试：

1.  **浏览器访问**：打开 `https://registry.example.com/v2/`，应该弹出登录框，输入 `admin` / `123456`，页面显示 `{}` 即为成功。
2.  **Docker 登录**：在终端执行 `docker login registry.example.com`，输入配置的用户名和密码。
3.  **推送镜像**：
    *   给本地镜像打标签：`docker tag my-image:latest registry.example.com/my-image:latest`
    *   推送至仓库：`docker push registry.example.com/my-image:latest`

**总结**

搭建私有仓库并不难，难点通常在于**网络配置**。记住一句话：**“Traefik 是网关，防火墙是门卫，网络是内部通道。”** 只有这三者都配置正确，你的镜像仓库才能顺畅运行。希望这篇指南能帮你避开常见的陷阱。