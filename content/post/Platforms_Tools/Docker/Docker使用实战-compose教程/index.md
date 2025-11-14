---
title: Docker使用实战-compose教程
description: ""
date: 2025-03-18T15:48:18+08:00
image: images/index/index.png
categories:
    - Platforms&Tools
tags:
    - Docker
---



```bash
#--------------------------------------
# 1. 通用/推荐的关闭方式 (任何系统)
#--------------------------------------

# 向 Redis 服务器发送关闭信号 (会安全保存数据)
# 这是最推荐的关闭方式
redis-cli shutdown

#--------------------------------------
# 直接运行 / Docker 容器内 (你当前的环境)
#--------------------------------------

# 启动 (前台运行，日志会占满终端)
redis-server

# 启动 (使用配置文件，推荐)
redis-server /path/to/redis.conf

# 启动 (后台运行，就像你之前用的)
redis-server &

# 关闭 (在 Docker 或直接运行时，用 cli 关闭)
redis-cli shutdown

# 强行关闭 (如果上面的命令无效)
# 1. 找到进程 PID
ps aux | grep redis-server
# 2. 杀死进程 (用 PID 替换 12345)
kill 12345



#--------------------------------------
# Linux (使用 systemd, 如 Ubuntu, CentOS)
#--------------------------------------

# 启动服务
sudo systemctl start redis-server
# (服务名也可能是 redis)
# sudo systemctl start redis

# 停止服务
sudo systemctl stop redis-server

# 重启服务
sudo systemctl restart redis-server

# 查看服务状态
sudo systemctl status redis-server

# 设置开机自启
sudo systemctl enable redis-server


```


下面是一个详细的 Docker Compose 教程，涵盖了从基础概念到实际操作的全面内容。教程将逐步讲解 Docker Compose 的用途、安装、配置文件编写以及常见使用场景，帮助你快速上手。

---

## Docker Compose 教程

### 什么是 Docker Compose？
Docker Compose 是一个用于定义和运行多容器 Docker 应用的工具。它通过一个 YAML 文件（通常是 `docker-compose.yml`）来配置多个服务、网络和卷，然后使用单一命令启动和管理这些容器。相比手动运行 `docker run`，它更适合需要协调多个容器的复杂应用。

#### 适用场景
- 开发环境：快速搭建包含前端、后端、数据库等的本地开发环境。
- 测试：运行集成测试或模拟生产环境。
- 小型部署：单机多容器应用的部署。

---

### 安装 Docker Compose
Docker Compose 有两种形式：
1. **旧版（docker-compose）**：一个独立的 Python 工具。
2. **新版（docker compose）**：集成在 Docker CLI 中的插件，从 Docker 20.10 开始默认包含。

#### 检查是否已安装
运行以下命令：
```bash
docker compose version
```
- 如果输出类似 `Docker Compose version v2.x.x`，说明已安装新版。
- 如果提示未找到命令，尝试 `docker-compose --version` 检查旧版。

#### 安装（如果需要）
- **Linux / macOS / Windows（新版）**：
  如果你的 Docker 是最新版（20.10+），无需额外安装，直接用 `docker compose`。
- **旧版安装（可选）**：
  ```bash
  sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
  ```

#### 前提条件
- 已安装 Docker Engine（运行 `docker --version` 确认）。

---

### 基本概念
- **服务（Services）**：一个服务对应一个容器，可以基于镜像启动，定义端口、卷等。
- **网络（Networks）**：Compose 默认创建网络，所有服务可以互相通信。
- **卷（Volumes）**：用于持久化数据，防止容器删除后数据丢失。
- **`docker-compose.yml`**：核心配置文件，描述整个应用。

---

### 创建第一个 Docker Compose 文件
假设我们要搭建一个简单的 Web 应用，包括：
- 一个 Nginx Web 服务器。
- 一个 Redis 数据库。

#### 1. 创建项目目录
```bash
mkdir my-compose-app
cd my-compose-app
```

#### 2. 编写 `docker-compose.yml`
创建一个名为 `docker-compose.yml` 的文件，内容如下：
```yaml
version: '3.8'  # 使用最新稳定的版本
services:
  web:
    image: nginx:latest  # 使用官方 Nginx 镜像
    ports:
      - "8080:80"        # 主机端口 8080 映射到容器端口 80
    volumes:
      - ./html:/usr/share/nginx/html  # 挂载本地 html 文件夹
  redis:
    image: redis:latest  # 使用官方 Redis 镜像
    ports:
      - "6379:6379"      # 映射 Redis 默认端口
    volumes:
      - redis-data:/data # 使用命名卷存储数据

volumes:
  redis-data:          # 定义一个命名卷
```

#### 文件解析
- `version: '3.8'`：指定 Compose 文件格式版本。
- `services`：定义两个服务：
  - `web`：运行 Nginx，映射端口 8080:80，挂载本地 `./html` 文件夹。
  - `redis`：运行 Redis，映射端口 6379，数据存储在命名卷 `redis-data`。
- `volumes`：定义一个命名卷 `redis-data`，用于持久化 Redis 数据。

#### 3. 创建 HTML 文件（可选）
在项目目录下创建 `html` 文件夹，并添加一个简单的 `index.html`：
```bash
mkdir html
echo "<h1>Hello, Docker Compose!</h1>" > html/index.html
```

#### 4. 启动应用
运行以下命令启动所有服务：
```bash
docker compose up -d
```
- `-d` 表示后台运行。

#### 5. 验证
- 检查运行中的容器：
  ```bash
  docker compose ps
  ```
  输出应显示 `web` 和 `redis` 服务状态为 `Up`。
- 访问 Nginx：打开浏览器，输入 `http://localhost:8080`，应看到 "Hello, Docker Compose!"。
- 检查 Redis：用 Redis 客户端连接 `localhost:6379`。

#### 6. 停止和清理
停止服务并删除容器：
```bash
docker compose down
```
如果要删除卷数据：
```bash
docker compose down -v
```

---

### 常用配置字段
以下是 `docker-compose.yml` 中常用的字段：

#### 服务配置
- `image`：指定镜像（如 `nginx:latest`）。
- `build`：构建镜像（替代 `image`），指定 Dockerfile 路径：
  ```yaml
  build:
    context: .       # 构建上下文路径
    dockerfile: Dockerfile  # Dockerfile 文件名
  ```
- `ports`：端口映射，格式 `"主机端口:容器端口"`。
- `volumes`：卷挂载，支持本地路径或命名卷：
  ```yaml
  volumes:
    - ./data:/app/data  # 本地路径
    - my-volume:/data   # 命名卷
  ```
- `environment`：环境变量：
  ```yaml
  environment:
    - DEBUG=true
    - PORT=8080
  ```
- `depends_on`：定义服务启动依赖：
  ```yaml
  depends_on:
    - redis
  ```

#### 全局配置
- `networks`：自定义网络：
  ```yaml
  networks:
    my-network:
      driver: bridge
  ```
- `volumes`：定义命名卷：
  ```yaml
  volumes:
    my-volume:
  ```

---

### 进阶示例：WordPress + MySQL
以下是一个更复杂的例子，搭建 WordPress 和 MySQL：

#### `docker-compose.yml`
```yaml
version: '3.8'
services:
  db:
    image: mysql:8.0
    volumes:
      - db-data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: somewordpress
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    restart: unless-stopped

  wordpress:
    image: wordpress:latest
    ports:
      - "8080:80"
    volumes:
      - wp-data:/var/www/html
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: wordpress
      WORDPRESS_DB_NAME: wordpress
    depends_on:
      - db
    restart: unless-stopped

volumes:
  db-data:
  wp-data:
```

#### 启动
```bash
docker compose up -d
```
访问 `http://localhost:8080`，即可看到 WordPress 安装页面。

---

### 常用命令
- 启动服务：`docker compose up -d`
- 停止服务：`docker compose stop`
- 删除服务（保留卷）：`docker compose down`
- 查看日志：`docker compose logs [服务名]`
- 重启服务：`docker compose restart`
- 构建镜像：`docker compose build`
- 查看服务状态：`docker compose ps`

---

### 保存和迁移
#### 保存镜像
1. 提交容器为镜像：
   ```bash
   docker commit my-compose-app_web_1 mywebimage:latest
   ```
2. 导出镜像：
   ```bash
   docker save -o myimages.tar mywebimage:latest
   ```

#### 备份卷
```bash
docker run --rm -v my-compose-app_db-data:/data -v $(pwd):/backup busybox tar cvf /backup/db-backup.tar /data
```

#### 恢复
1. 加载镜像：
   ```bash
   docker load -i myimages.tar
   ```
2. 恢复卷：
   ```bash
   docker run --rm -v my-compose-app_db-data:/data -v $(pwd):/backup busybox tar xvf /backup/db-backup.tar -C /data
   ```
3. 启动：`docker compose up -d`

---

### 注意事项
- **版本选择**：根据 Docker Engine 版本选择合适的 `version`（推荐 `3.8` 或更高）。
- **命名冲突**：多个 Compose 项目运行时，卷和网络名称可能冲突，可用 `docker compose -p 项目名` 指定项目名。
- **最佳实践**：尽量通过 `build` 和 Dockerfile 定义镜像，而不是手动修改容器。

---
