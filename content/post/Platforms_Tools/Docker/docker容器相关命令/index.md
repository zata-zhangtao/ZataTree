---
title: docker使用教程
description: ""
date: 2025-03-18T09:57:06+08:00
image: images/index/index-10.png
categories:
    - Platforms&Tools
tags:
    - Docker
---

```bash 
# 容器管理
docker run -itd --name <container_name> -p <host_port>:<container_port> <image> # 运行容器（后台，指定名称，端口映射）
docker run exec -it  <container_name>  /bin/bash
docker ps # 查看运行中的容器
docker ps -a # 查看所有容器（包括已停止）
docker stop <container_id> # 停止容器
docker start <container_id> # 启动容器
docker restart <container_id> # 重启容器
docker rm <container_id> # 删除容器
docker logs <container_id> # 查看容器日志

# 镜像管理
docker pull <image> # 拉取镜像
docker images # 查看本地镜像
docker rmi <image_id> # 删除镜像
docker build -t <image_name> . # 构建镜像（当前目录的Dockerfile）
docker commit <container_id> <image_name>:<tag> # 将容器构建成为镜像，tag通常用 latest 或版本号（如 v1.0）

# 容器操作
docker exec -it <container_id> /bin/bash # 进入容器（交互式）
docker cp <container_id>:<path> <local_path> # 从容器复制文件到本地
docker cp <local_path> <container_id>:<path> # 从本地复制文件到容器

# 网络和卷
docker network ls # 查看网络
docker network create <network_name> # 创建网络
docker volume ls # 查看卷
docker volume create <volume_name> # 创建卷

# 系统管理
docker info # 查看Docker信息
docker system prune # 清理未使用的容器、网络、镜像等
docker system df # 查看Docker磁盘使用情况
```




### docker容器相关命令
#### 1. 拉取镜像

```bash
docker pull ubuntu
```

#### 2.查看镜像是否拉取成功

```bash
docker images
```

#### 3. 运行容器

```bash
docker run -itd --name <容器名称>  -p <主机端口>:<容器端口> --cpus=30  ubuntu
# -p设置端口   --cpus/-c 设置核心 
```

#### 4. 通过 exec 命令进入 ubuntu 容器

```bash
docker exec -it <容器名>  /bin/bash
```
#### 5. 安装ssh
```bash
apt-get updata

apt-get install openssh-client
apt-get install openssh-server

```
#### 6. 安装vim

```bash
apt-get install vim
```

#### 7. 安装conda 
https://zhuanlan.zhihu.com/p/307923089
注意，可能要手动配置环境变量


![](images/index/index.png)

![](images/index/index-1.png)

![](images/index/index-2.png)


#### 8. 安装zip、unzip

```bash
apt-get install zip 
apt-get install unzip 
```
#### 9. 解决中文乱码问题

```python
export LC_ALL="C.UTF-8"
source /etc/bash.bashrc
```

#### 10. 安装sudo

```bash
apt-get install sudo
```





-------------
-------------
-------------
-------------

### Docker使用技巧

#### 使用已有容器创建镜像

```bash
docker commit container-name  new-image-name
```
#### 开启/重启ssh服务

```bash
service ssh start 
service ssh restart 
```

#### docker 文件传输
宿主机到容器
```bash
# docker cp 宿主机文件/路径 容器名：容器内路径
docker cp /home/Download/index.html wordpress-lee:/var/www/html
```

容器到宿主机
```bash
# docker cp 容器名：文件/路径 宿主机路径 
docker cp wordpress-lee:/root/example.sh /root
```

#### 修改服务器配置允许通过此服务器进行ssh转发
进入配置文件，不要cd..然后在vim，直接vim  ...
```bash
vim /etc/ssh/sshd_config
```
配置文件内容

![](images/index/index-3.png)

修改其中的：

![](images/index/index-4.png)
![](images/index/index-5.png)

 重启ssh服务

```bash
 service ssh restart
```

#### docker容器添加对外映射端口

|参考：|
|---|
|https://www.cnblogs.com/zhumengke/articles/13525837.html|


最简单省事方法：将现有的容器打包成镜像，然后在使用新的镜像运行容器时重新指定要映射的端口

![打包镜像重新运行容器](images/index/index-7.png)


#### docker设置可用CPU核心数量

|参考：|
|---|
|https://www.cnblogs.com/sparkdev/p/8052522.html|


![CPU数量](images/index/index-8.png)

![指定CPU](images/index/index-9.png)



