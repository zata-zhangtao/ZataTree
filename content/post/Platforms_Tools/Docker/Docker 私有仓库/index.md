---
title: Docker 私有仓库
description: ""
date: 2026-02-23T00:20:36+08:00
image: images/index/index.png
categories:
    - Platforms_Tools
tags:
    - Docker
---

# 【实战】5 分钟搭建带密码验证的 Docker 私有仓库（附 HTTP 报错完美解决方案）

在内网或个人服务器上搭建 Docker 私有仓库（Registry）时，我们通常有两个痛点：

1. **不想裸奔**：需要账号密码保护，但手动生成 `htpasswd` 文件太麻烦。
2. **连接报错**：没有域名和 SSL 证书，Docker 默认不让连 HTTP 仓库。

本文提供一个**“懒人版”**解决方案：使用 Docker Compose 自动生成密码，并解决 `server gave HTTP response to HTTPS client` 报错。

---

**一、部署：自动生成密码的 Docker Compose**

不需要在宿主机手动执行命令生成密码文件，我们利用一个临时的 Alpine 容器在启动时自动完成这项工作。

注意：请修改下方 `command` 中的 `admin` 和 `123456` 为你想要的账号密码。

新建或在 Dokploy 中填入以下 `docker-compose.yml`：

```yaml
version: '3.8'

volumes:
  registry-data:  
  registry-auth-data: 

services:
  auto-setup-auth:
    image: httpd:alpine
    command: /bin/sh -c "htpasswd -Bbn admin 123456 > /auth/htpasswd"
    volumes:
      - registry-auth-data:/auth

  registry:
    image: registry:2
    container_name: my-private-registry
    restart: always
    ports:
      - "5000:5000"
    environment:
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: "Registry Realm"
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
    volumes:
      - registry-data:/var/lib/registry
      - registry-auth-data:/auth
    depends_on:
      auto-setup-auth:
        condition: service_completed_successfully
```

点击部署后，你的 5000 端口就已经开启了带密码保护的镜像服务。

---

**二、避坑：解决 HTTP 连接报错**

当你尝试登录或在 Dokploy 添加这个仓库时，极大概率会遇到这个报错：

> `Error response from daemon: Get "https://...": http: server gave HTTP response to HTTPS client`

**原因**：Docker 客户端默认只信任 HTTPS，而我们部署的是 HTTP。

**解决方法**（在**客户端**机器或 Dokploy 所在服务器执行）：

1. 编辑 Docker 配置文件：
   ```bash
   sudo nano /etc/docker/daemon.json
   ```

2. 加入 `insecure-registries` 配置（注意 JSON 格式，如果已有内容记得加逗号）：
   ```json
   {
     "insecure-registries": ["你的服务器 IP:5000"]
   }
   ```

3. 重启 Docker 生效：
   ```bash
   sudo systemctl restart docker
   ```

---

**三、连接与使用**

配置完成后，就可以愉快地使用了。

**方式 1：在 Dokploy 面板添加**

*   **Registry URL**: `你的服务器 IP:5000` (不要加 http://)
*   **Username**: `admin` (或你修改的账号)
*   **Password**: `123456` (或你修改的密码)

**方式 2：终端命令行使用**

步骤 1：登录仓库。

```bash
docker login 你的服务器 IP:5000
```

步骤 2：推送镜像。

```bash
docker tag my-image:latest 你的服务器 IP:5000/my-image:latest
docker push 你的服务器 IP:5000/my-image:latest
```

搞定！现在你拥有了一个既安全又无需 SSL 证书的私有镜像仓库。