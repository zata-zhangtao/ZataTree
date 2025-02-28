# nginx

## nginx 使用
###  简介
Nginx（发音同engine x）是一个异步框架的 Web 服务器，也可以用作反向代理，负载平衡器 和 HTTP 缓存。该软件由 Igor Sysoev 创建，并于2004年首次公开发布。同名公司成立于2011年，以提供支持。Nginx 是一款免费的开源软件，根据类 BSD 许可证的条款发布。一大部分Web服务器使用 Nginx ，通常作为负载均衡器。


**特点**

- 更快：
单次请求会得到更快的响应。
在高并发环境下，Nginx 比其他 WEB 服务器有更快的响应。
- 高扩展性：
Nginx 是基于模块化设计，由多个耦合度极低的模块组成，因此具有很高的扩展性。许多高流量的网站都倾向于开发符合自己业务特性的定制模块。
- 高可靠性：
Nginx 的可靠性来自于其核心框架代码的优秀设计，模块设计的简单性。另外，官方提供的常用模块都非常稳定，每个 worker 进程相对独立，master 进程在一个 worker 进程出错时可以快速拉起新的 worker 子进程提供服务。
- 低内存消耗：
一般情况下，10000个非活跃的 HTTP Keep-Alive 连接在 Nginx 中仅消耗 2.5MB 的内存，这是 Nginx 支持高并发连接的基础。
单机支持10万以上的并发连接：理论上，Nginx 支持的并发连接上限取决于内存，10万远未封顶。
- 热部署:
master 进程与 worker 进程的分离设计，使得 Nginx 能够提供热部署功能，即在 7x24 小时不间断服务的前提下，升级 Nginx 的可执行文件。当然，它也支持不停止服务就更新配置项，更换日志文件等功能。
- 最自由的 BSD 许可协议:
这是 Nginx 可以快速发展的强大动力。BSD 许可协议不只是允许用户免费使用 Nginx ，它还允许用户在自己的项目中直接使用或修改 Nginx 源码，然后发布。

### 安装
####  ubuntu系统下安装

```bash
# Ubuntu官方列表的Nginx版本不一定是最新的。所以请添加Nginx安装列表：
# 这一步不是必须的，但建议执行，不然安装的Nginx版本会挺旧的。
$ sudo apt install software-properties-common
$ sudo add-apt-repository ppa:nginx/stable

# 更新列表
$ sudo apt-get update

# 安装 Nginx
$ sudo apt-get install nginx

$ nginx -v       # 查看Nginx版本号
$ dpkg -L nginx  # 查看Nginx安装位置，输出/usr/share/doc/nginx。其他文件在/etc/nginx
$ dpkg --list    # 查看已安装的包

$ sudo apt-get remove nginx nginx-common  # 删除Nginx（保留配置文件)
$ sudo apt-get purge nginx nginx-common   # 删除Nginx（且不保留配置文件)
$ sudo apt-get autoremove                 # 删除依赖（dependencies）

$ service nginx status   # 查看Nginx状态，默认在运行ing
# 此时访问服务器的IP地址即可看到"Welcome to nginx!"的页面

# 每次更新 Nginx 配置后，都建议重启一下 Nginx
$ service nginx start    # Nginx启动命令
$ service nginx stop     # Nginx停止命令
$ service nginx restart  # Nginx重启命令
```





参考地址：
[nginx安装](https://xuexb.github.io/learn-nginx/guide/linux-install.html#%E4%B8%8B%E8%BD%BD%E5%AE%89%E8%A3%85%E5%8C%85%E5%B9%B6%E8%A7%A3%E5%8E%8B) 
 [nginx安装包括一些相关配置](https://blog.csdn.net/qq_39420519/article/details/126322909)
 [ubuntu使用nginx部署静态网页，含https配置](https://github.com/Qingquan-Li/blog/issues/141)


### nginx 代理后端服务的配置|fastapi|flask

**nginx配置**

进入到配置文件中

```bash
vim /etc/nginx/sites-available/update-server
```
修改以下代码
```python
server {
    listen 80; # 也就是其他地方访问需要的端口，nginx默认是80，也就是不需要额外加端口可以访问,记得把防火墙打开，还要就是没有被其他程序占用，
    server_name zata.cc;  # 自己的域名或者ip地址

    location / {
        proxy_pass http://127.0.0.1:5000; # 需要代理的地址
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```


然后创建符号链接让配置生效
```bash
# 创建符号链接
sudo ln -s /etc/nginx/sites-available/update-server /etc/nginx/sites-enabled/
```

查看符号链接是否创建成功
```bash
ls -l /etc/nginx/sites-enabled/
```

查看配置是否有问题
```bash
sudo nginx -t
```

启动nginx  
```bash
cd /etc/nginx
servce nginx start
```

再检查一下是否有问题
```bash
sudo nginx -t
```

然后直接访问域名或者ip

![alt text](image/软件自动更新/软件自动更新-2.jpg)

可以看到不加端口也可以访问了
到这一步说明flask和nginx都配成功了，不过如果遇到：
```bash
<html>
<head><title>413 Request Entity Too Large</title></head>
<body>
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx/1.18.0 (Ubuntu)</center>
</body>
</html>
```
这个是由于nginx也有上传文件大小的要求，可以修改nginx的配置文件
---