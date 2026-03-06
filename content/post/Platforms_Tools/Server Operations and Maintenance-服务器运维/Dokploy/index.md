---
title: Dokploy
description: ""
date: 2026-02-22T15:43:30+08:00
image: images/index/index.png
categories:
    - Platforms_Tools
tags:
    - Server Operations and Maintenance-服务器运维
---




# 快速安装使用教程


[官网地址](https://dokploy.com/)
[关于swarm的安装](https://docs.dokploy.com/docs/core/manual-installation)

一键安装脚本，安装完成之后会给一个地址
```bash
export ADVERTISE_ADDR=<指定IP地址>  # 需要指定公网IP
curl -sSL https://dokploy.com/install.sh | sh

# 或者

curl -sSL https://dokploy.com/install.sh | ADVERTISE_ADDR=<你的服务器公网IP> bash
```


帮助子节点安装docker
```bash
curl -fsSL https://get.docker.com | sh

# 设置开机自启  
systemctl enable --now docker

# 作为子节点加入到 swarm 集群
docker swarm join \
  --token <TOKEN> \
  --advertise-addr <当前子节点的_公网IP> \
  --data-path-addr <当前子节点的_公网IP> \
  <Manager_公网IP>:2377
```


查看所有容器的运行状态
```bash
docker service ps 
```


## 安装卡住时的清理方法

有时候安装Dokploy可能会卡住，需要清除重来，以下是完整的清理步骤：

```bash
# 离开 swarm 并清理
docker swarm leave --force

# 删掉所有 Dokploy 相关的东西
docker service rm $(docker service ls -q)
docker container rm -f $(docker ps -aq --filter "name=dokploy")
docker volume rm $(docker volume ls -q --filter "name=dokploy")
docker network rm $(docker network ls -q --filter "name=dokploy")

# 清理残留镜像（可选）
docker system prune -a --volumes --force

# 再跑安装（加 --debug 看更详细输出）
curl -sSL https://dokploy.com/install.sh | bash -s -- --debug
# 或指定 advertise addr（如果你的公网IP不是自动检测到的）
curl -sSL https://dokploy.com/install.sh | ADVERTISE_ADDR=你的服务器公网IP bash
```



# 注意事项


1. 只要改过了domin,就一定要重新deploy
![提醒重新部署](images/index/image-6.png)

1. 可以先用自己电脑ssh-copy-id 到远程服务器，然后把自己电脑上的ssh密钥复制过来
![可以复制自己电脑上的ssh密钥](images/index/image-1.png)

2. 子节点默认可能是没有docker的,需要安装一下
![没有docker报错](images/index/image-2.png)

3. 添加docker swarm 误操作添加了管理节点，然后又下线会导致原本的管理节点脑裂,详情需要看dokploy的官方文档
重新安装请查看前面的方法

4. dokploy很多时候部署失败可能是不提示的,尤其是使用 docker stack 的时候

5. 配置了域名地址之后,有时候可能要等一会才能生效

6. 网络配置
这一步非常重要，告诉 Docker 使用 Dokploy 已经建好的网络
networks:
  dokploy-network:
    external: true




# 一些应用的部署


## FileBrowser

这份教程不仅能让你拥有一个管理 VPS 全盘文件的神器，还规避了密码无法重置、下载系统文件报错等常见问题。

---

**1. 准备工作**

*   **目标**：部署一个 Web 端的文件管理器，可以管理 VPS 上的**所有文件**（拥有 Root 权限）。
*   **工具**：Dokploy 面板（使用 Docker Compose 方式）。

**2. 部署配置 (Docker Compose)**

在 Dokploy 中创建一个新的 **Application (Compose)**，将以下代码完整复制进去。

**代码特点：**

1.  **超级权限**：使用 `user: "0:0"` 获得 Root 权限，可读写系统任何文件。
2.  **全盘挂载**：将宿主机根目录 `/` 挂载到容器内，实现全盘管理。
3.  **防止配置冲突**：修正了之前的语法错误，并配置了数据卷以确保持久化。

```yaml
version: '3.3'
services:
  filebrowser:
    image: filebrowser/filebrowser:latest
    container_name: filebrowser_root
    restart: unless-stopped
    # 核心：赋予容器 Root 权限，否则无法修改系统文件
    user: "0:0"
    networks:
      - dokploy-network
    volumes:
      # 核心：将 VPS 的根目录 (/) 挂载到容器的 /srv 目录
      - /:/srv
      # 数据库持久化卷：存储你的用户信息和设置
      # 如果忘记密码，修改冒号前的名称 (如改成 filebrowser_data_v3) 即可重置
      - filebrowser_data_v2:/database 

    # 启动命令 (合并写在一行)：
    # -d 指定数据库路径
    # -p 强制监听 80 端口
    # -r 指定根目录为挂载进来的 /srv
    command: -d /database/filebrowser.db -p 80 -r /srv

volumes:
  # 对应上面的数据卷名称
  filebrowser_data_v2:

networks:
  dokploy-network:
    external: true
```

**3. 端口设置 (Ports)**

在 Dokploy 的应用设置界面，找到 **Ports** 选项卡：

*   **Internal Port (容器端口)**: `80`
*   **External Port (外部端口)**: 填写一个未被占用的端口，例如 `8088` 或 `9999`。

点击 **Save** 并 **Deploy**。

**4. 首次登录与设置**

部署完成后，通过浏览器访问 `http://你的 IP:你的外部端口`。

1.  **默认账号**：`admin`
2.  **默认密码**：`admin`
3.  **修改密码（重要）**：
    *   登录后，点击左侧栏 **Settings** -> **Profile**。
    *   在 **Password** 区域输入新密码。
    *   点击 **Update** 保存。

**5. 避坑指南 (常见误区)**

**Q1: 为什么下载某些文件报错 `ERR_INVALID_RESPONSE`？**

*   **现象**：尝试下载 `/proc`、`/sys`、`/dev` 目录下的文件时失败。
*   **原因**：这些不是真实文件，而是系统内存和内核状态的“虚拟映射”。它们大小通常显示为 0，Web 服务器无法打包下载它们。
*   **解决**：**不要下载这些目录的文件**。请测试下载 `/etc/hosts` 或者你自己创建的 `/home/test.txt`，这些才是真实文件。

**Q2: 我忘记了密码怎么办？**

**无法通过环境变量设置密码**。如果忘记密码，最快的方法是“洗号重来”：

1.  修改 Docker Compose 中的 `volumes` 部分。
2.  将 `- filebrowser_data_v2:/database` 改为 `- filebrowser_data_v3:/database`。
3.  重新部署。这会生成全新的数据库，密码恢复为默认的 `admin`。

**Q3: 安全警告**

因为这个容器挂载了 `/` 根目录且拥有 Root 权限：

*   **不要**随意删除 `/bin`, `/boot`, `/usr` 等系统核心目录，否则 VPS 会挂掉。
*   **务必**设置强密码，不要将此服务随意暴露给不可信的人。



# 使用与配置


## dokploy 如果因为磁盘爆了而崩溃，怎么解决

```bash
# 确认磁盘状态
df -h  


# 清除陈旧的系统日志
sudo journalctl --vacuum-time=1d
sudo journalctl --vacuum-size=100M

# 清理未使用的 Docker 镜像和停止的容器
docker system prune -a -f
```


## 配置S3 Destinations

- 以b2_buckets 为例


**将 Backblaze B2 配置到 Dokploy 的 S3 存储指南**

将 Backblaze B2 配置到 Dokploy 的 S3 存储中主要分为两步：首先在 Backblaze 获取凭据，然后在 Dokploy 仪表板中完成设置。

**第一步：在 Backblaze B2 中获取信息**

1.  **创建存储桶 (Bucket)**
    *   登录 Backblaze，进入 B2 Cloud Storage > Buckets。
    *   创建一个新存储桶（例如命名为 `dokploy-backups`）。
    *   注意：在存储桶列表中找到刚才创建的桶，复制其显示的 S3 Endpoint（例如 `s3.us-west-002.backblazeb2.com`）。

2.  **创建应用程序密钥 (Application Keys)**
    *   进入 App Keys 页面。
    *   点击 Add a New Application Key。
    *   设置名称，并确保权限设置为 Read and Write。
    *   创建后，你会得到：
        *   `keyID`（即 Dokploy 中的 Access Key）
        *   `applicationKey`（即 Dokploy 中的 Secret Key）
    *   注意：`applicationKey` 仅显示一次，请务必保存。

**第二步：在 Dokploy 中进行配置**

1.  进入 Dokploy 面板，点击左侧菜单的 Settings (设置)。
2.  找到 S3 Destinations 选项卡，点击 Add S3 Destination。
3.  根据以下对应关系填写表单：

| Dokploy 字段 | 对应 Backblaze 的信息 | 示例值 |
| :--- | :--- | :--- |
| Name | 自定义名称 | Backblaze-B2 |
| Provider |  | 选择 Amazon Web Services （AWS）S3 ｜
| Endpoint | 存储桶页面的 S3 Endpoint (需带 https://) | `https://s3.us-west-002.backblazeb2.com` |
| Region | Endpoint 中的地区部分 | `us-west-002` |
| Bucket | 你创建的存储桶名称 | `dokploy-backups` |
| Access Key | 刚才生成的 keyID | `002123456789...` |
| Secret Key | 刚才生成的 applicationKey | `K001abcd...` |

4.  **保存并测试**：填写完成后，点击 Test Connection。如果显示成功，则说明配置正确。

**第三步：为数据库或应用开启备份**

配置好 S3 目的地后，你还需要将其应用到具体的备份任务中：

1.  进入你想备份的 Database (数据库) 或 Service。
2.  点击 Backups 选项卡。
3.  在 Select Destination 下拉菜单中选择刚才创建的 Backblaze-B2。
4.  设置 Cron Schedule（例如 `0 0 * * *` 表示每天午夜备份）并启用。

**常见问题排查**

*   **权限错误**：确保创建 Key 时勾选了对应存储桶的 "Read and Write" 权限。
*   **Endpoint 格式**：Dokploy 通常需要完整的 URL 格式，请确保包含 `https://`。
*   **地区 (Region)**：Backblaze 的地区代码通常就在 Endpoint URL 中（如 `us-west-002`），必须准确填写。




## Dokploy Swarm 子节点联通性测试指南

这是一份专为 Dokploy 用户准备的 **Docker Swarm 子节点（Worker Node）联通性测试教程**。在搭建好 Dokploy 多节点集群后，最关键的一步是验证 **管理节点（Manager）** 是否能通过 **Overlay 网络** 正常调度并连接到 **子节点（Worker）** 上的容器。本教程将通过部署一个跨节点的测试应用，验证网络数据平面（Data Plane）是否畅通。

**一、核心概念：为什么不能用“默认”网络？**

很多教程提到“不要使用默认网络”，这通常指两点：

1.  **禁止使用 `bridge` 网络**：这是单机网络。如果你不指定网络，Docker 默认使用 `bridge`，跨服务器的容器将无法互相访问。
2.  **必须使用 `Overlay` 网络**：Swarm 模式下，只有 Overlay 网络能建立跨物理机的虚拟隧道。
3.  **Dokploy 的做法**：Dokploy 已经预设了一个名为 `dokploy-network` 的 Overlay 网络。**我们的应用必须挂载到这个网络上**，才能被 Dokploy 的 Traefik 网关识别并实现跨节点转发。

**二、准备工作**

1.  确保在 Dokploy 的 **Servers** 菜单中，子节点显示为 `Ready`。
2.  （可选）为子节点添加标签：
    *   在管理节点终端执行：`docker node update --label-add type=worker <子节点主机名>`
    *   *这能确保我们的测试应用准确落在子节点上。*

**三、编写部署文件 (Compose)**

在 Dokploy 中新建一个 **Compose**，选择 **Stack** 模式，填入以下配置：

```yaml
version: '3.8'

services:
  # 服务 A：强制运行在管理节点 (Manager)
  test-manager:
    image: nginxdemos/hello:plain-text
    networks:
      - dokploy-network
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == manager

  # 服务 B：强制运行在子节点 (Worker)
  test-worker:
    image: nginxdemos/hello:plain-text
    networks:
      - dokploy-network
    deploy:
      replicas: 1
      placement:
        constraints:
          # 如果没打标签，可用 - node.role == worker
          - node.role == worker 

networks:
  # 使用 Dokploy 预设的 Overlay 网络
  dokploy-network:
    external: true
```

*注意：上述 YAML 中的注释行已保留，但请确保在实际编辑时不要误删关键配置。*

**四、部署步骤**

1.  **创建 Stack**：在 Dokploy 项目中点击 `Create Service` -> `Compose`。
2.  **配置**：
    *   **Name**: `swarm-test`
    *   **Source**: 直接粘贴上述 YAML 代码。
3.  **部署**：点击 **Deploy**。
4.  **确认位置**：
    *   部署完成后，在 Dokploy 的容器列表里查看。
    *   确认 `test-manager` 运行在管理节点 IP 上。
    *   确认 `test-worker` 运行在子节点 IP 上。

**五、联通性验证（手动测试）**

即使两个容器都显示 "Running"，也不代表网络是通的。我们需要执行以下两项压力测试：

**1. 容器间内网互访（验证 Overlay 网络）**

进入管理节点上的 `test-manager` 容器，尝试访问子节点上的服务名：

```bash
    # 1. 在管理节点终端找到容器 ID
docker ps | grep test-manager

    # 2. 进入容器内部
docker exec -it <容器 ID> sh

    # 3. 通过服务名访问子节点的容器（Swarm 会自动做 VIP 负载均衡）
curl http://test-worker
```

*   **成功标志**：如果返回 `Server address: 10.0.x.x` 且该 IP 是子节点的内部 IP，说明 **Overlay 网络跨机通信正常**。

**2. 外部网关转发（验证 Traefik 联通）**

在 Dokploy 中为 `test-worker` 服务配置一个域名（Domain）：

1.  在 `test-worker` 的域名设置里绑定一个测试域名。
2.  通过浏览器访问该域名。
*   **原理**：流量会先到达 **管理节点的 Traefik** -> 通过 **dokploy-network** -> 转发到 **子节点的容器**。
*   **成功标志**：浏览器正常显示网页。如果出现 `502 Bad Gateway`，说明管理节点和子节点之间的 **4789/UDP** 端口被防火墙拦截了。

**六、故障排查**

如果测试不通，请检查各节点间防火墙是否放行了以下 Swarm 必需端口：

1.  **TCP 2377**：集群管理通信。
2.  **TCP/UDP 7946**：节点发现与健康检查。
3.  **UDP 4789**：**关键！** 数据平面 Overlay 网络（UDP 封装）。如果该端口不通，容器能启动但无法互相 ping 通。

**检查指令（在任一节点查看网络详情）：**

```bash
docker network inspect dokploy-network
```

确认子节点（Worker）的容器 IP 是否出现在 `Containers` 列表中。

**总结**

在 Dokploy 中测试子节点，**核心就是利用 `dokploy-network` (External Overlay)**。只要能通过管理节点的容器 `curl` 通子节点的容器名，你的集群网络就是完美的。

## Dokploy + Docker Swarm 实战：为什么扩容后看不见容器？(多节点部署避坑指南)



![dokploy只能看见本地的容器,但是实际上是有两个容器在跑的](images/index/image-5.png)

最近在使用 **Dokploy** 配合 **Docker Swarm** 进行多节点部署时，遇到了一些非常经典的概念误区。这篇笔记旨在记录从单机迈向集群模式时，容易让人产生“自我怀疑”的几个瞬间，以及如何正确地管理你的 Swarm 集群。

**01. 现象：明明扩容了，容器去哪了？**

我在 Dokploy 的后台将一个应用（`transfileserver`）的副本数（Replicas）设置为了 **2**。

在主节点（Master/Manager）终端输入 `docker service ls`，状态看起来非常完美：

```bash
root@master:~# docker service ls
ID             NAME                             REPLICAS   IMAGE
j4pif4la2ox3   smallappforfun-test..._app       2/2        registry.../app:latest
```

`REPLICAS 2/2` 告诉我：期望跑 2 个，实际跑了 2 个。一切正常，对吧？

**但是**，当我习惯性地在主节点输入 `docker ps` 想看看这两个容器时，却发现：**只有一个容器在运行！**

```bash
root@master:~# docker ps | grep transfileserver
// 只有一行输出，显示其中一个容器 ID
```

**我的第一个反应是：** 部署失败了？还是 Dokploy UI 显示 bug 了？为什么丢了一个容器？

**02. 原理：上帝视角 vs. 本地视角**

其实，部署并没有失败。这是 **Docker Swarm** 最基本的运行逻辑，也是新手最容易混淆的地方。

**为什么 `docker ps` 看不到？**

*   **`docker ps` 是“本地视角”**：这个命令问的是当前这台物理服务器：“你的 CPU 和内存里现在跑着哪些进程？”
*   **Swarm 调度机制**：当你设置 `replicas: 2` 且拥有多个节点时，Swarm 调度器为了负载均衡，大概率会将其中一个容器分配给主节点，另一个分配给子节点（Worker Node）。

所以，你在主节点运行 `docker ps`，当然只能看到分配给主节点的那个容器。另一个容器正在子节点的肚子里跑得欢呢。

**正确的查看方式：上帝视角**

要确认所有副本的状态和位置，不能用 `docker ps`，而要用 **Service** 级别的命令：

```bash
docker service ps <你的服务名称>
```

输出结果会像这样：

| ID | NAME | NODE | DESIRED STATE | CURRENT STATE |
| :--- | :--- | :--- | :--- | :--- |
| x7... | ...app.1 | **racknerd-master** | Running | Running |
| y9... | ...app.2 | **worker-node-01** | Running | Running |

注意 **NODE** 这一列。你可以清晰地看到，Swarm 已经把任务分发到了不同的机器上。这证明你的负载均衡集群已经完美工作了。

**03. 疑问：子节点需要安装 Dokploy 吗？**

既然应用跑在子节点上，我是否需要在子节点上也跑一遍 Dokploy 的安装脚本？

**答案是：绝对不需要，千万别装！**

**为什么？**

1.  **架构逻辑**：Dokploy 是“指挥官”（Brain），它只需要存在于主节点。Worker 节点只需要安装基础的 Docker Engine。主节点通过 Swarm 协议遥控子节点干活。
2.  **端口冲突**：Dokploy 自带 Traefik（网关），占用 80/443 端口。如果在子节点再装一套，会导致端口冲突，破坏集群的统一路由网络。
3.  **资源浪费**：子节点会被迫运行一套多余的 Postgres、Redis 和监控服务。

**子节点只需要做一件事**：安装 Docker，然后运行 `docker swarm join ...` 命令加入集群即可。

**04. 关键避坑：多节点下的文件存储（Volumes）**

虽然多节点部署成功了，但如果你的应用涉及到文件上传或持久化存储（比如我的文件传输服务），这里有一个巨大的隐患。

**场景重现**

假设你的 `docker-compose.yml` 是这样写的：

```yaml
volumes:
  - ./uploads:/app/uploads
```

*   **用户 A** 上传文件，请求被分发到了 **主节点** 的容器。文件保存在主节点的硬盘里。
*   **用户 A** 再次刷新，请求被分发到了 **子节点** 的容器。
*   **结果**：子节点容器里是空的！用户发现刚传的文件“丢了”。

**解决方案**

在 Swarm 模式下，本地目录挂载（Bind Mounts）不再适用于需要数据共享的场景。你需要：

1.  **方案一（推荐）：对象存储**
    修改代码，不要把文件存本地硬盘，而是存到 AWS S3、阿里云 OSS 或自建的 MinIO 中。这是云原生应用的最佳实践。
2.  **方案二：NFS（网络文件系统）**
    搭建一个 NFS 服务器，让所有节点挂载同一个网络硬盘。
3.  **方案三：限制节点（临时方案）**
    如果是单机应用强行上 Swarm，可以通过配置 `placement constraints`，强制该服务只运行在主节点上，放弃多节点负载均衡，只利用 Swarm 的管理功能。

**总结**

1.  **信任 `docker service ls`**：如果它显示 `2/2`，那就是成功的。
2.  **用对命令**：查看集群状态用 `docker service ps`，而不是 `docker ps`。
3.  **保持子节点纯净**：不要在 Worker 节点重复安装 Dokploy。
4.  **留意存储**：多节点部署必须解决文件共享问题，否则数据会“漂移”。

希望这篇避坑指南能帮你更自信地驾驭 Dokploy 和 Docker Swarm！



## Dokploy 安全建议检查与服务器加固操作指南


![刚安装完成的dokploy](images/index/image-3.png)

这张截图显示的是 Dokploy 的 **安全建议检查（Security Suggestions）**。它并不是让你在 Dokploy 的网页界面里填个表，而是提示你需要登录到 **服务器的终端（Terminal）** 去修改系统配置文件。这是一份服务器“加固”清单。要把这些红色的叉号（❌）变成绿色的勾号（✅），你需要 SSH 登录到这台服务器，依次执行以下操作。

⚠️ **警告：在操作之前，请务必确保你已经可以通过 SSH 密钥登录服务器！如果你在没有配置好密钥的情况下禁用了密码登录，你将无法进入服务器！**

---

**第一步：修复 SSH 设置 (最重要)**

截图建议你禁用密码登录（Password Auth）和 PAM，只允许密钥登录。

1.  **SSH 登录服务器**。
2.  **编辑 SSH 配置文件**：
    ```bash
    sudo nano /etc/ssh/sshd_config
    ```
3.  **修改以下配置项**（使用键盘上下键找到这些行，修改后的样子如下）：
    *   找到 `PasswordAuthentication`，将其改为 `no`：
        ```text
        PasswordAuthentication no
        ```
    *   找到 `UsePAM`，建议改为 `no` (注意：有些系统改为 no 可能会有副作用，通常改 PasswordAuthentication 最关键，但为了满足 Dokploy 的检查，你可以改为 no)：
        ```text
        UsePAM no
        ```
    *   *确保 `PubkeyAuthentication` 是 `yes`（通常默认就是）。*
4.  **保存并退出**：按 `Ctrl + O` 回车保存，按 `Ctrl + X` 退出。
5.  **重启 SSH 服务**使配置生效：
    ```bash
    sudo systemctl restart ssh
    ```
    *操作完这一步，SSH 部分的红色叉号应该会变绿。*

---

**第二步：配置 UFW 防火墙**

截图显示 UFW 已安装但未激活，且默认策略不是“拒绝”。

1.  **设置默认拒绝进入**（安全基线）：
    ```bash
    sudo ufw default deny incoming
    ```
2.  **放行必要的端口**（**非常重要，否则你会把自己关在外面**）：
    ```bash
    # 放行 SSH (通常是 22)
    sudo ufw allow 22/tcp

    # 放行 Web 服务 (HTTP/HTTPS)
    sudo ufw allow 80/tcp
    sudo ufw allow 443/tcp

    # 放行 Dokploy 面板端口 (默认是 3000)
    sudo ufw allow 3000/tcp
    ```
3.  **启用防火墙**：
    ```bash
    sudo ufw enable
    ```
    *(系统会提示你这可能会断开 SSH 连接，输入 `y` 确认即可，只要上面 allow 22 执行了就没事)*。

---

**第三步：安装并配置 Fail2Ban**

截图显示 Fail2Ban 根本没安装，建议安装并开启 SSH 攻击保护（Aggressive 模式）。

1.  **安装 Fail2Ban**：
    ```bash
    sudo apt-get update
    sudo apt-get install fail2ban -y
    ```
2.  **创建配置文件**（不要直接改 jail.conf，新建 jail.local）：
    ```bash
    sudo nano /etc/fail2ban/jail.local
    ```
3.  **粘贴以下内容**（开启 SSH 保护并设为激进模式）：
    ```ini
    [sshd]
    enabled = true
    port    = ssh
    filter  = sshd
    logpath = /var/log/auth.log
    maxretry = 3
    # 截图建议 SSH Mode: aggressive
    mode    = aggressive
    ```
4.  **保存并退出**：`Ctrl + O` 回车，`Ctrl + X`。
5.  **启动 Fail2Ban 服务**：
    ```bash
    sudo systemctl enable fail2ban
    sudo systemctl start fail2ban
    ```

---

**最后一步：验证**

回到 Dokploy 网页界面，点击弹窗右上角的 **Refresh (刷新)** 按钮。如果操作正确，大部分或者全部的红叉 ❌ 应该都会变成绿色的 ✅。

**简单总结：**
1.  改 `/etc/ssh/sshd_config` 禁止密码。
2.  运行 `ufw` 命令开放端口并开启防火墙。
3.  运行 `apt install fail2ban` 并配置它。


![配置完成如下](images/index/image-4.png)





## Dokploy 搭配 Nginx Proxy Manager 保姆级实操教程

没问题！既然你习惯了 1Panel 的操作逻辑，那么**方案一：使用 Nginx Proxy Manager (NPM)** 绝对是你的最佳选择。

这将是一个**手把手、保姆级**的实操教程，涵盖从网络配置到最终通过域名访问的全过程。

---

**准备工作**

1.  **一台安装好 Dokploy 的服务器**。
2.  **一个域名**（假设为 `example.com`）。
3.  **确保端口未被占用**：确保服务器的 80 和 443 端口没有被其他程序占用（Dokploy 面板默认通常在 3000 端口，所以 80/443 通常是空闲的）。

---

**第一步：规划 Docker 网络（关键点）**

在 1Panel 里，系统帮你自动处理了网络。但在 Dokploy（以及原生 Docker）中，为了让“反向代理容器”能找到“应用容器”，它们必须在**同一个 Docker 网络**中。

我们先创建一个专用的网络，名字叫 `proxy-net`。

1.  登录你的服务器终端（SSH）。
2.  执行以下命令创建网络：

```bash
docker network create proxy-net
```

这一步做完，以后所有的应用和 NPM 都加入这个网络，它们就能通过“容器名”互相通信了。

---

**第二步：在 Dokploy 中部署 Nginx Proxy Manager**

1.  登录 Dokploy 面板。
2.  进入 **Project（项目）** -> 选择或新建一个项目（例如叫 `System`）。
3.  点击 **Compose** -> **Add Compose**。
    *   **Name:** `nginx-proxy-manager`
    *   **Description:** 反向代理服务
4.  在右侧的编辑器中，粘贴以下配置（注意我添加了网络配置）：

```yaml
version: '3.8'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    container_name: nginx-proxy-manager
    restart: unless-stopped
    ports:
      - '80:80'
      - '81:81'
      - '443:443'
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    networks:
      - proxy-net

networks:
  proxy-net:
    external: true
```

5.  点击 **Deploy**（部署）。
6.  等待日志显示 `Listening on port 81`，表示启动成功。

---

**第三步：初始化 Nginx Proxy Manager**

1.  在浏览器访问：`http://你的服务器 IP:81`
2.  使用默认账号登录：
    *   **Email:** `admin@example.com`
    *   **Password:** `changeme`
3.  登录后，系统会立即要求你修改**用户名**和**密码**，请务必修改并记住。

此时，你的“反向代理中心”已经搭建好了！

---

**第四步：部署一个业务应用（以 Alist 为例）**

现在我们来部署一个实际的应用，并尝试通过域名访问它。

1.  回到 Dokploy 面板。
2.  进入你的项目，点击 **Compose** -> **Add Compose**。
3.  **Name:** `alist`
4.  粘贴以下配置（**注意看 `networks` 和 `ports` 的部分**）：

```yaml
version: '3.3'
services:
  alist:
    image: 'xhofe/alist:latest'
    container_name: alist-app
    restart: always
    volumes:
      - './etc/alist:/opt/alist/data'
    networks:
      - proxy-net

networks:
  proxy-net:
    external: true
```

5.  点击 **Deploy**。

**重点理解**：此时，`alist-app` 和 `nginx-proxy-manager` 都在 `proxy-net` 这个网络里。虽然你在公网通过 IP:5244 访问不到 Alist（因为没暴露端口），但 NPM 可以通过内部网络访问到它。

---

**第五步：域名解析 (DNS)**

去你的域名服务商（阿里云、腾讯云、Cloudflare 等）：

1.  添加一条 **A 记录**。
2.  **主机记录 (Name):** 例如 `pan` (即 `pan.example.com`)。
3.  **记录值 (Value):** 填写你 **Dokploy 服务器的公网 IP**。

---

**第六步：在 NPM 中配置反向代理（最后一步！）**

1.  回到 NPM 的管理后台 (`http://你的服务器 IP:81`)。
2.  点击顶部菜单 **Hosts** -> **Proxy Hosts**。
3.  点击右上角 **Add Proxy Host**。

**A. Details 标签页 (基本信息)**
*   **Domain Names:** `pan.example.com` (你刚才解析的域名)
*   **Scheme:** `http`
*   **Forward Hostname / IP:** `alist-app`
    *   这里最关键！填写你在第四步定义的 `container_name`。不要填 IP，填容器名即可。
*   **Forward Port:** `5244`
    *   填写 Alist 的内部端口。
*   **Cache Assets / Block Common Exploits:** 推荐勾选。

**B. SSL 标签页 (HTTPS 证书)**
*   **SSL Certificate:** 选择 `Request a new SSL Certificate`。
*   **Force SSL:** 勾选 (强制跳转 HTTPS)。
*   **HTTP/2 Support:** 推荐勾选。
*   **Email Address:** 填写你的邮箱。
*   **I Agree to the Terms:** 勾选。

4.  点击 **Save**。

---

**验证成果**

现在，在浏览器输入 `https://pan.example.com`。

*   如果一切顺利，你应该能看到 Alist 的页面。
*   并且浏览器地址栏有一把**小锁**（HTTPS 已启用）。
*   整个过程你不需要手动去碰 Nginx 的配置文件，也不需要手动上传证书。

**进阶小贴士**

1.  **后续添加新应用：**
    *   在 Dokploy 部署新应用时，记得在 Compose 文件里加上 `networks: - proxy-net`。
    *   记下容器名 (`container_name`) 和内部端口。
    *   去 NPM 添加一条新的 Proxy Host 即可。

2.  **关于端口 81 的安全：**
    *   NPM 的后台（81 端口）直接暴露在公网其实不太安全。
    *   **高级玩法**：你可以在 NPM 里，把自己（`nginx-proxy-manager` 容器，端口 81）也代理一下！
    *   配置一个域名如 `npm.example.com` -> Forward Hostname: `nginx-proxy-manager` -> Port: `81`。
    *   一旦配置成功，去云服务商防火墙把 81 端口封掉，只留 80/443，以后通过 `npm.example.com` 访问管理后台，更加安全且带有 HTTPS。

通过这套流程，你在 Dokploy 上就完美复刻了 1Panel 的反向代理体验，甚至在多服务器扩展性上比 1Panel 更强（因为基于标准的 Docker 网络）。




# Dokploy介绍

Dokploy 是一个新兴的、开源的、基于 Web 的服务器管理和应用程序部署平台，旨在让开发者和中小型团队能够像使用 Heroku 或 Vercel 一样简便地部署和管理应用，但所有服务完全运行在您自己拥有或控制的服务器（如 VPS）上。简单来说，Dokploy 是“自托管/私有化部署的 Heroku”。

它通过一个直观的 Web 控制面板，将复杂的 Docker、Git、Webhook 和反向代理配置过程完全可视化，让您无需记忆冗长的命令行指令，就能完成应用部署、数据库创建、SSL 证书安装等一系列操作。

 核心特性

- **基于 Docker**：所有应用和服务都以 Docker 容器形式运行，保证环境的一致性和隔离性。支持上传标准的 `docker-compose.yml` 文件，或使用内置模板快速创建多容器应用。

- **可视化部署**：
  - **Git 集成**：连接 GitHub、GitLab 或 Bitbucket 仓库，实现持续部署。每次推送代码到指定分支，Dokploy 会自动拉取、构建并重新部署应用。
  - **Docker 镜像部署**：可直接从 Docker Hub 或私有仓库拉取镜像进行部署。
  - **环境变量管理**：在网页界面中轻松添加、编辑和管理敏感配置信息，无需手动编辑文件。

- **内置服务支持**：一键部署常用数据库（MySQL、PostgreSQL、MongoDB、Redis 等）、缓存服务和反向代理（Nginx），无需手动编写配置文件。

- **SSL 证书自动管理**：集成 Let’s Encrypt，为您的应用域名自动签发和续期免费的 HTTPS 证书，仅需点击几下即可完成配置。

- **直观的监控与管理**：
  - 实时查看容器状态（运行/停止）、CPU 与内存使用情况。
  - 查看实时日志流，支持在线启动、停止、重启容器。

- **多服务器管理**：一个 Dokploy 控制面板可同时管理多个远程服务器（节点），便于在不同机器上分布和调度应用。

- **开源与可扩展**：完全开源（采用商业源码许可证），代码透明，社区驱动，支持通过插件或模板扩展功能，便于二次开发与定制。

 典型工作流程

1. **准备一台 VPS**：在 DigitalOcean、Linode、阿里云、腾讯云等服务商购买一台安装了 Ubuntu 或 Debian 的虚拟服务器。
2. **安装 Dokploy**：使用官方提供的一键安装脚本，在服务器上部署 Dokploy（其本身也是一个 Docker 容器）。
3. **访问控制面板**：通过浏览器访问服务器 IP 和指定端口，进入 Dokploy 的 Web 界面并完成初始设置。
4. **连接 Git 账户**：在面板中授权您的 GitHub、GitLab 或 Bitbucket 账号。
5. **创建新项目**：点击“部署应用”，选择目标仓库和分支。
6. **配置部署参数**：设置端口映射、环境变量、构建命令等。Dokploy 会自动生成 `Dockerfile`（如项目未提供），或使用您上传的 `docker-compose.yml`。
7. **执行部署**：点击“部署”按钮，Dokploy 会自动拉取代码、构建镜像、启动容器，并通过内置的 Traefik 或 Nginx 配置好域名访问。
8. **持续管理**：部署完成后，通过面板监控应用状态、查看日志、添加自定义域名并启用 SSL。

 适合谁使用？

- **前端/全栈开发者**：希望快速部署 Next.js、Nuxt.js、React、Vue 或 Node.js 等项目，却不愿花时间处理服务器运维。
- **初创团队和小公司**：需要成本可控、易于维护的部署方案，同时避免被 Heroku、Railway 等 PaaS 平台绑定或高额费用困扰。
- **注重数据隐私的个人或组织**：因合规性、安全或数据主权要求，必须将应用部署在自有基础设施上，但仍希望享受现代云平台的便捷体验。
- **Docker 初学者**：想体验容器化部署的优势，但对命令行、网络配置、存储卷等概念感到困难。

 优点与缺点

**优点：**
- **成本效益高**：仅需支付 VPS 费用，Dokploy 本身免费，长期使用远低于按需付费的云 PaaS。
- **完全自主可控**：数据和基础设施由您掌控，可自由定制服务器配置和安全策略。
- **开发者体验友好**：极大降低了 Docker 和 CI/CD 的入门门槛，部署流程流畅直观。
- **活跃社区**：项目更新频繁，功能持续迭代，社区支持逐步增强。

**缺点：**
- **依赖自有服务器**：您需具备基本的服务器运维能力（如 SSH 登录、防火墙设置），并自行负责安全更新、备份和底层维护。
- **非企业级架构**：相比 Kubernetes 或商业面板（如 Plesk、cPanel），在集群管理、高可用、自动伸缩等方面功能尚不完善。
- **新兴项目**：作为较新的开源工具，其长期稳定性、大规模生产环境验证和生态成熟度仍需时间检验。

 与其他工具的对比

| 工具 | 类型 | 核心特点 | 适合场景 |
| :--- | :--- | :--- | :--- |
| **Dokploy** | 自托管 PaaS 面板 | 开源、可视化、Git 集成、轻量级、基于 Docker | 个人开发者、小团队自托管应用 |
| **Heroku / Vercel** | 云 PaaS | 极致简化、全托管、生态丰富、按需付费 | 追求效率、不愿管理服务器的用户 |
| **Portainer** | Docker 管理面板 | 通用型容器、镜像、网络、卷管理 | 需要精细管理 Docker 环境的管理员 |
| **Coolify / CapRover** | 自托管 PaaS 面板 | 与 Dokploy 定位高度重叠，功能相似 | 可作为 Dokploy 的替代选择进行对比 |
| **Kubernetes** | 容器编排平台 | 企业级、高扩展性、功能强大但复杂 | 大型系统、微服务架构、需要弹性伸缩的场景 |

 如何开始？

1. 访问 Dokploy 官方网站获取最新文档和安装指南：[https://dokploy.com](https://dokploy.com)
2. 查看开源代码和社区贡献：[https://github.com/Dokploy/dokploy](https://github.com/Dokploy/dokploy)

 总结

Dokploy 填补了“完全托管的云服务”与“手动服务器运维”之间的空白，让开发者能专注于编写代码，而将部署与运维的复杂性封装在一个美观、易用的界面之后。对于追求自主权、控制权和成本效益的开发者而言，Dokploy 是一个极具吸引力的现代部署解决方案。如果您正在寻找一种比手动操作更高效、比大型云平台更自主的部署方式，Dokploy 绝对值得一试。


