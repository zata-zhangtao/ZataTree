---
title: Docker 和 Traefik 一键安装脚本
description: "适合 Ubuntu/Debian VPS 的 Docker Engine、Compose 插件和 Traefik 网关初始化脚本。"
date: 2026-06-08T00:30:00+08:00
image: images/index/index.png
slug: docker-traefik-install-script
categories:
    - Engineering
tags:
    - DevOps
    - Docker
    - Traefik
    - Linux
    - CI/CD
---

在单台 VPS 上部署多个 Web 服务时，我现在更倾向于先准备一个公共入口层：Docker 负责跑应用，Traefik 负责根据域名把请求转发到不同容器，并自动接入 HTTPS。

这篇文章放一个可直接运行的脚本，用来在 Ubuntu/Debian 服务器上安装 Docker Engine、Docker Compose 插件，并启动一个基础 Traefik 网关。

脚本文件和这篇文章放在同一个目录里，可以直接查看或下载：[install-docker-traefik.sh](install-docker-traefik.sh)。

## 适用场景

适合这些情况：

- 一台新的 Ubuntu/Debian 云服务器。
- 准备用 Docker Compose 部署多个站点或服务。
- 想用 Traefik 统一管理 `80`、`443` 入口。
- 不想再为每个应用单独写 Nginx 配置。

不适合这些情况：

- 已经使用 Kubernetes Ingress。
- 已经由 1Panel、Coolify、Dokploy 等平台完整接管反向代理。
- 需要复杂的企业级网关策略，比如多租户权限、统一认证、灰度发布等。

## 快速运行

如果只是安装 Docker 和 Traefik，不需要立即配置 HTTPS：

```bash
chmod +x install-docker-traefik.sh
./install-docker-traefik.sh
```

如果要给真实网站签发 Let's Encrypt 证书，建议填写 `ACME_EMAIL`：

```bash
ACME_EMAIL=you@example.com ./install-docker-traefik.sh
```

脚本会把 Traefik 配置写到：

```text
/opt/traefik
```

Dashboard 默认只监听服务器本机：

```text
http://127.0.0.1:8080/dashboard/
```

远程查看可以用 SSH 端口转发：

```bash
ssh -L 8080:127.0.0.1:8080 user@server
```

## 参数说明

常用环境变量如下：

| 变量 | 默认值 | 说明 |
| --- | --- | --- |
| `TRAEFIK_DIR` | `/opt/traefik` | Traefik 配置目录 |
| `TRAEFIK_NETWORK` | `traefik` | 公共 Docker 网络名 |
| `TRAEFIK_IMAGE` | `traefik:v3.7` | Traefik 镜像版本 |
| `ACME_EMAIL` | 空 | Let's Encrypt 邮箱，不填则不启用自动 HTTPS |
| `ENABLE_HTTPS_REDIRECT` | 自动判断 | 填了 `ACME_EMAIL` 时默认开启 HTTP 到 HTTPS 跳转 |
| `INSTALL_SAMPLE` | `false` | 是否启动 `whoami` 测试服务 |
| `WHOAMI_HOST` | `whoami.localhost` | 只给测试服务使用，不是你的真实网站域名 |

`ACME_EMAIL` 可以不填。不填时，脚本仍然会安装 Docker 和 Traefik，但不会配置 Let's Encrypt 证书解析器。

`WHOAMI_HOST` 也可以不填。它只在 `INSTALL_SAMPLE=true` 时用于测试服务，真实网站应该在自己的 `docker-compose.yml` 里配置 Traefik labels。

## 真实网站接入方式

真实网站容器需要加入同一个 Traefik 网络：

```yaml
networks:
  traefik:
    external: true
```

然后给 Web 服务加 labels：

```yaml
services:
  site:
    image: your-site-image
    restart: unless-stopped
    networks:
      - traefik
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.site.rule=Host(`example.com`)"
      - "traefik.http.routers.site.entrypoints=websecure"
      - "traefik.http.routers.site.tls=true"
      - "traefik.http.routers.site.tls.certresolver=letsencrypt"
      - "traefik.http.services.site.loadbalancer.server.port=80"

networks:
  traefik:
    external: true
```

这里的 `example.com` 要替换成真实域名，并且 DNS 需要提前解析到这台服务器 IP。服务器安全组或防火墙也要放行 `80` 和 `443`。

## 后续如何做 CD

这个脚本只解决服务器入口层：安装 Docker、启动 Traefik、准备公共网络。它不会负责“代码变了以后怎么自动发布”。真正的 CD 需要额外建立一条发布链路：

```text
push 代码
  -> CI/CD 平台构建 Docker 镜像
  -> 推送镜像到镜像仓库
  -> SSH 到服务器
  -> 更新应用 compose 的镜像 tag
  -> docker compose pull && docker compose up -d
  -> Traefik 根据 labels 接管流量
```

这里用 GitHub Actions 举例，但思路对 GitLab CI、Woodpecker CI、Gitea Actions 也一样。Traefik 不关心你用哪个 CI/CD 平台，它只关心最终跑起来的容器是否在同一个 Docker 网络里，并且有没有正确的 labels。

### 一、每个项目准备自己的镜像

每个要部署的项目都应该能被构建成一个 Docker 镜像。不同技术栈的 `Dockerfile` 不一样，但对 Traefik 来说只需要满足两点：

1. 容器内部有一个 HTTP 服务端口，比如 `80`、`3000`、`8080`。
2. 不要直接把业务容器的端口暴露到公网，公网入口交给 Traefik。

如果是静态站点，可以用 Nginx 承载构建产物：

```dockerfile
FROM nginx:alpine
COPY public /usr/share/nginx/html
```

如果是 Node、Python、Go、Java 后端，则按对应技术栈构建镜像，只要最后服务监听一个明确端口即可。

### 二、服务器上每个项目一个目录

建议每个应用单独放到 `/opt/apps/<app-name>`：

```bash
sudo mkdir -p /opt/apps/my-app
cd /opt/apps/my-app
```

目录里放两个文件：

```text
/opt/apps/my-app
├── .env
└── docker-compose.yml
```

`.env` 只放部署层变量：

```bash
APP_IMAGE=ghcr.io/your-org/my-app:initial
APP_HOST=app.example.com
APP_PORT=3000
```

`docker-compose.yml` 写成通用模板：

```yaml
services:
  app:
    image: ${APP_IMAGE}
    restart: unless-stopped
    networks:
      - traefik
    expose:
      - "${APP_PORT}"
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.my-app.rule=Host(`${APP_HOST}`)"
      - "traefik.http.routers.my-app.entrypoints=websecure"
      - "traefik.http.routers.my-app.tls=true"
      - "traefik.http.routers.my-app.tls.certresolver=letsencrypt"
      - "traefik.http.services.my-app.loadbalancer.server.port=${APP_PORT}"

networks:
  traefik:
    external: true
```

这里没有写 `ports`。业务容器不需要直接占用宿主机端口，Traefik 会通过 `traefik` 网络访问容器内部端口。

如果你的 Traefik 没有启用 Let's Encrypt，可以先用 HTTP：

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.my-app.rule=Host(`${APP_HOST}`)"
  - "traefik.http.routers.my-app.entrypoints=web"
  - "traefik.http.services.my-app.loadbalancer.server.port=${APP_PORT}"
```

真实项目的数据库密码、API key 等运行时环境变量，建议放在另一个只存在服务器上的文件，例如 `app.env`，然后在 compose 里引用：

```yaml
env_file:
  - app.env
```

CD 流水线只更新 `.env` 里的 `APP_IMAGE`，不要覆盖服务器上的业务密钥文件。

### 三、准备部署用户和 SSH key

生产环境建议创建专门的部署用户，不要长期用 `root` 跑 CD：

```bash
sudo adduser --disabled-password --gecos "" deploy
sudo usermod -aG docker deploy
```

加入 `docker` 组后，需要重新登录这个用户，组权限才会生效。

生成一把专门给 CD 用的 SSH key：

```bash
ssh-keygen -t ed25519 -C "cd-my-app" -f ./cd-my-app -N ""
```

公钥放到服务器：

```bash
sudo install -d -m 700 -o deploy -g deploy /home/deploy/.ssh
cat ./cd-my-app.pub | sudo tee -a /home/deploy/.ssh/authorized_keys
sudo chmod 600 /home/deploy/.ssh/authorized_keys
sudo chown -R deploy:deploy /home/deploy/.ssh
```

私钥内容放到 CI/CD 平台的 Secret 里。以 GitHub Actions 为例，进入：

```text
Repository -> Settings -> Secrets and variables -> Actions
```

添加：

```text
SERVER_HOST      服务器 IP 或域名
SERVER_USER      deploy
SERVER_SSH_KEY   cd-my-app 私钥完整内容
```

注意：私钥不要提交到 Git 仓库。公钥留在服务器的 `authorized_keys`，私钥只放 CI/CD Secret。

### 四、准备镜像仓库

镜像仓库可以用 GitHub Container Registry、Docker Hub、Harbor、阿里云/腾讯云镜像仓库等。通用原则是：

- CI/CD 需要有 `push` 权限，用来推送新镜像。
- 服务器需要有 `pull` 权限，用来拉取新镜像。
- CD 部署时尽量使用不可变 tag，例如 Git commit SHA。
- `latest` 可以保留给人工查看，但不要只依赖 `latest` 做生产发布。

如果使用私有镜像，先在服务器上用部署用户登录一次：

```bash
sudo -iu deploy
echo "你的镜像仓库 token" | docker login ghcr.io -u your-user --password-stdin
```

登录信息会保存在部署用户自己的 Docker 配置里。之后 CD 执行 `docker compose pull` 时，就能拉取私有镜像。

### 五、GitHub Actions 通用 CD 模板

下面这个模板做三件事：

1. 构建镜像。
2. 推送 `latest` 和当前 commit SHA 两个 tag。
3. SSH 到服务器，把 `.env` 里的 `APP_IMAGE` 改成当前 commit SHA 对应的镜像，然后重启应用。

保存为：

```text
.github/workflows/cd.yml
```

```yaml
name: CD

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  packages: write

env:
  REGISTRY_HOST: ghcr.io
  IMAGE_NAME: ghcr.io/your-org/my-app
  APP_DIR: /opt/apps/my-app

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4

      - name: Login to registry
        uses: docker/login-action@v4
        with:
          registry: ${{ env.REGISTRY_HOST }}
          username: ${{ secrets.REGISTRY_USERNAME }}
          password: ${{ secrets.REGISTRY_TOKEN }}

      - name: Build and push image
        uses: docker/build-push-action@v7
        with:
          context: .
          push: true
          tags: |
            ${{ env.IMAGE_NAME }}:${{ github.sha }}
            ${{ env.IMAGE_NAME }}:latest

      - name: Deploy on server
        env:
          SERVER_HOST: ${{ secrets.SERVER_HOST }}
          SERVER_USER: ${{ secrets.SERVER_USER }}
          SERVER_SSH_KEY: ${{ secrets.SERVER_SSH_KEY }}
          IMAGE: ${{ env.IMAGE_NAME }}:${{ github.sha }}
        run: |
          mkdir -p ~/.ssh
          printf '%s\n' "$SERVER_SSH_KEY" > ~/.ssh/deploy_key
          chmod 600 ~/.ssh/deploy_key
          ssh-keyscan -H "$SERVER_HOST" >> ~/.ssh/known_hosts

          ssh -i ~/.ssh/deploy_key "$SERVER_USER@$SERVER_HOST" \
            "cd '${APP_DIR}' && \
             sed -i 's#^APP_IMAGE=.*#APP_IMAGE=${IMAGE}#' .env && \
             docker compose pull && \
             docker compose up -d --remove-orphans && \
             docker image prune -f"
```

对应需要在 GitHub Secrets 里添加：

```text
REGISTRY_USERNAME  镜像仓库用户名
REGISTRY_TOKEN     镜像仓库 token
SERVER_HOST        服务器 IP 或域名
SERVER_USER        SSH 部署用户
SERVER_SSH_KEY     SSH 私钥
```

如果使用 GitHub Container Registry，并且镜像属于当前仓库，构建推送阶段也可以用 `${{ github.actor }}` 和 `${{ secrets.GITHUB_TOKEN }}`。但服务器拉取私有镜像时，仍然需要能 `pull` 该镜像的凭据，最清晰的做法是给服务器配置一份只读或低权限的 registry token。

### 六、发布后检查和回滚

部署完成后，至少检查三处：

```bash
cd /opt/apps/my-app
docker compose ps
docker compose logs -f
curl -I https://app.example.com
```

如果应用提供健康检查接口，可以在 workflow 里加一步：

```bash
curl -fsS https://app.example.com/health
```

回滚的本质是把 `APP_IMAGE` 改回旧镜像 tag：

```bash
cd /opt/apps/my-app
sed -i 's#^APP_IMAGE=.*#APP_IMAGE=ghcr.io/your-org/my-app:old-commit-sha#' .env
docker compose pull
docker compose up -d --remove-orphans
```

所以每次发布都用 commit SHA 做镜像 tag 很重要。它让你能明确知道当前服务器运行的是哪一次代码，也能快速回到上一个可用版本。

### 七、多项目部署约定

单台服务器跑多个项目时，建议保持这些约定：

- 每个项目一个目录：`/opt/apps/<app-name>`。
- 每个项目一个 compose：只管理自己的业务容器。
- 所有需要公网 HTTP/HTTPS 的服务都加入同一个 `traefik` 网络。
- 每个项目使用不同的 router/service 名称，例如 `blog`、`api`、`admin`。
- 每个项目只在 labels 里声明自己的域名和内部端口。
- CD 流水线只更新项目目录，不要改 `/opt/traefik`。

这样 Traefik 是稳定的公共入口，业务项目各自独立发布。新增项目时，只需要新建项目目录、写自己的 compose、配置 DNS、接入一条 CD workflow。

## 完整脚本

完整脚本不再内嵌在正文里，避免博客内容和实际可执行文件不同步。脚本文件放在这篇文章同目录：[install-docker-traefik.sh](install-docker-traefik.sh)。

## 运行后检查

查看 Traefik 容器：

```bash
sudo docker compose --env-file /opt/traefik/.env -f /opt/traefik/docker-compose.yml ps
```

查看日志：

```bash
sudo docker compose --env-file /opt/traefik/.env -f /opt/traefik/docker-compose.yml logs -f
```

测试服务可以这样启动：

```bash
ACME_EMAIL=you@example.com INSTALL_SAMPLE=true WHOAMI_HOST=whoami.example.com ./install-docker-traefik.sh
```

如果 `whoami.example.com` 能访问，说明 DNS、80/443、防火墙、Traefik 路由和证书申请基本都通了。

## 注意事项

1. 脚本会按 Docker 官方安装方式添加 apt 仓库，并安装 `docker-ce`、`docker-ce-cli`、`containerd.io`、`docker-buildx-plugin`、`docker-compose-plugin`。
2. 脚本会移除可能冲突的旧包，例如 `docker.io`、旧版 `docker-compose`、`podman-docker`、`containerd`、`runc`。
3. Traefik dashboard 使用 `api.insecure: true`，但端口只绑定到 `127.0.0.1:8080`，不要改成公网监听，除非你额外加认证。
4. Traefik 通过只读方式挂载 `/var/run/docker.sock`。这依然是高权限入口，生产环境要限制谁能创建带 Traefik labels 的容器。
5. Let's Encrypt HTTP challenge 需要 `80` 端口能从公网访问，否则证书申请会失败。

## 参考

- [Docker Engine Ubuntu 安装文档](https://docs.docker.com/engine/install/ubuntu/)
- [Docker Engine Debian 安装文档](https://docs.docker.com/engine/install/debian/)
- [Traefik Docker provider 文档](https://doc.traefik.io/traefik/providers/docker/)
- [Traefik Docker 官方镜像](https://hub.docker.com/_/traefik)
- [GitHub Actions 发布 Docker 镜像](https://docs.github.com/en/actions/tutorials/publish-packages/publish-docker-images)
- [GitHub Actions Secrets](https://docs.github.com/en/actions/concepts/security/secrets)
- [Docker 的 GitHub Actions 指南](https://docs.docker.com/guides/gha/)
