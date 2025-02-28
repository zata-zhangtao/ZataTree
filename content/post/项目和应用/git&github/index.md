---
title: git&github使用
description: git&github使用指南
date: 2025-02-28
slug: git&github/index.md ## 必填，文件夹名/index.md
image: image/index/index.png
categories:
    # - DeepLearning
    # - 画图
    # - Python
    # - LLM
    # - Library
    # - PaperReading
    - Study

---

#  git基本使用
## 简单常用命令


```bash
%%设置用户签名%%
git config --global user.name [username]      
git config --global user.email [useremail]

%%设置对于非ASCII字符的显示方式%%
git config--global core.quotepath false

%%设置init分支名%%
git config --global init.defaultBranch main

%%初始化本地库%%
git init

%% 设置远端库别名
git remote add <别名> <网址>

%% 查看远端库
git remote -v


%%查看本地库状态%%
git status

%%追踪文件，放入暂存区%%
git add [filename]
git add .  #所有文件放入暂存区
%%撤销追踪%%
git restore 【file】

%%删除暂存区的文件%%
git rm --cache 【filename】

%%提交本地库%%
git commit -m "[提交信息]" 【文件名（可以不加）】

%%撤销commit提交%%
git reset --soft HEAD     


%%推送远程库
git push [<远程主机名>] [<本地分支>:<远程分支>] #如果不加分支对应信息就默认上次记录的全部分支

%%拉取远程库%%
git pull [<远程主机名>] [<远程分支>:<本地分支>]   # 从远程仓库（名为 origin）的 main 分支拉取代码并自动与本地的 main 分支合并 ,如果方括号里面的不加就默认拉去上一次的



%%查看引用日志版本信息%%
git reflog 
%%查看详细日志%%
git log

%%版本穿梭%%  一般用soft多一点
git reset --hard  【版本号】

--.gitignore--------------------
test* 忽略以test开头的文件
```

## 复杂命令

### pull
```bash
git pull origin master --allow-unrelated-histories    # 无视没有共同历史合并  
```

### remote

```bash

# 仓库路径查询
git remote -v

#添加远程仓库：
git remote add <远程仓库名> <你的项目地址> 

#删除指定的远程仓库
git remote rm origin

# 修改远程仓库地址
git remote set-url origin <remote-url>



```


### branch 

```bash
# 重命名分支
​ git branch -m oldName newName


---
# 2、 远程分支重命名
# 重命名远程分支对应的本地分支
git branch -m oldName newName
#删除远程分支
git push --delete origin oldName
#上传新命名的本地分支
git push origin newName
#把修改的本地分支与远程分支关联
git branch --set-upstream-to origin/newName
---


#3、查看当前代码仓库源
#查看当前源
git remote -v

#重设
git remote set-url origin xxxx_url
```


### bundle  用于备份
https://blog.csdn.net/penriver/article/details/126579266

```bash
# 打包
git bundle create <打包名>.bundle HEAD <分支名>

# 验证文件合法
git bundle verify <打包名>.bundle

# 恢复
git clone <打包名>.bundle

```



### merge 

```bash 
# 合并分支
git merge feature

# 如果是远程分支合并
git merge origin/feature

```

关于merge的详解可见参考[git merge](#git-merge详解)



# 一些问题





## git merge详解


如果没有冲突，Git 会自动完成合并，并创建一个合并提交（merge commit，如果需要的话）。如果有冲突，Git 会暂停合并，提示你解决冲突（后面会讲怎么处理）。

1. 无冲突的合并（Fast-forward）

如果 main 分支没有额外改动，而 feature 分支只是基于 main 增加了提交，Git 会执行“快进合并”（fast-forward）。这时候历史记录会变成一条直线，看起来像是直接在 main 上开发了一样。

2. 有额外提交的合并（Merge Commit）

如果 main 和 feature 都有各自的提交，Git 会创建一个新的合并提交，保留两个分支的历史。
命令一样：
```bash
git merge <分支名>
```
但是，合并后，Git 会自动生成一个 Merge commit，这样，从历史上看，分支信息就非常清楚。

3. 冲突的合并
当两个分支修改了同一文件的同一部分，Git 无法自动决定用哪个版本，就会报冲突。这时你需要手动解决：

运行 git merge feature 后，Git 会提示冲突文件。
打开这些文件，冲突部分会被标记为：
```
<<<<<<< HEAD
（main 分支的内容）
=======
（feature 分支的内容）
>>>>>>> feature
```
编辑文件，保留你想要的部分，删除标记。
解决完后，标记文件为已解决："git add <filename>"，然后提交："git commit -m '解决冲突'

- 实用技巧
查看合并状态：用 git status 检查当前是否在合并过程中。
中止合并：如果合并出了问题，想放弃，可以用：

git merge --abort

- 指定合并策略：默认情况下 Git 会自动选择合并方式，但你可以用选项调整，比如强制非快进合并：

git merge --no-ff feature



## |git pull|merge| git 多人协作的时候怎么解决冲突？


使用git-pull 然后git-commit 最后git-push 

如果有冲突可以看[get merge使用](#git-merge详解)

![alt text](image/git@github/git@github.jpg)




## |公式 | github | github不显示md文件中的公式
`第一种方法：使用github推荐的公式写法（推荐）`
在写md的时候，使用
```
$`  和  `$  
```
来包围行内公式
```
```math  
和
	```
```
来包围单行公式，如下

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/230396f603874e5e82ae2bbb1c7010e3.jpeg)
`第二种方法： 插件`

但是还是会有一部分显示不正确
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/2fc1936490f84904b8a12ab12eb47ad4.jpeg)
解决方法：安装插件：https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/9db763b4137e473d8c7eac94d6044c17.jpeg)



## git 使用ssh密钥登录github
` 注意一个密钥只能登录一个github，如果你想要在新的github账户上面添加旧的ssh密钥，就会报错`
准备工作：本地先下载安装好git，注册并登陆github账号
在注册好后的github账号中先创建一个仓库
在本地git创建SSH key
第一步：设置全局的用户名和邮箱（这样主要是不用总是重填）
```cpp
git config --global user.name '用户名' // 切换到你的github用户名上
git config --global user.email 'github账号注册用的邮箱'
```
第二步：生成密钥，有可能提示没有这个库，需要安装一下，去搜索一下
```cpp
ssh-keygen -t rsa -C "你的邮箱地址"
```

第三步：查看自己本地的密钥，执行以下命令

```cpp
ls -al ~/.ssh // 查看本机是否有秘钥文件 没有秘钥文件生成秘钥文件
cd ~/.ssh
ls  // 查看 .ssh 中有什么文件
cat id_rsa.pub // 查看本地的公钥
cat id_rsa // 查看本地的私钥
（如果是windows系统可以直接到C盘的对应用户名文件夹下的.ssh文件夹中查看）
```
	
	
第四步：将公钥复制粘贴到github上

> github上点击头像，点击Settings，进入后点击 SSH and GPS keys，接着点击 New SSH key
> 将公钥粘贴在key输入框那里，Title则随便输入可以就行

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/655a1a04316a483c8bb21b535aca31f6.jpeg)



## `git 使用token登录github 并拉取项目` （如果电脑上已经登录过了，需要把账户信息清除掉。**如果是用ssh密钥登录的也不行**，清除token账户信息请看下面“清除电脑上已经登录的github账户信息”）

<table>
    <tr>
        <td >
        	<img src="https://i-blog.csdnimg.cn/direct/29000ed66efe469eab478a184d1df37d.png" >图1  打开设置
        </td>
        <td >
       		<img src="https://i-blog.csdnimg.cn/direct/efd91004eb7c436895145fe70886154e.png"  >图2 开发者设置
       	</td>
       	        <td >
       		<img src="https://i-blog.csdnimg.cn/direct/a3ac8181595f40cba51f74aa46678595.png"  >图3 点击Token
       	</td>
    </tr>
        <tr>
        <td >
        	<img src="https://i-blog.csdnimg.cn/direct/e9b8e868a98a46faa2808c257dd4a8c4.png" >图4  生成classic Token
        </td>
        <td >
       		<img src="https://i-blog.csdnimg.cn/direct/4050e0ba1fc044cca920a96e04e7ed21.png"  >图5 设置命名和权限
       	</td>
    </tr>
</table>

**最后一步：**
在新设备上pull或者push的时候，会让你登录，有两种方式，一种是账号密码，另一种就算token，选择token，然后粘贴上一步生成的token就可以了


## github 要求2FA认证
今天上线的时候突然发现，github要求我设置2FA认证，不然就不能登录，手机号我必然是没有的，只能用安全密钥控制
具体的github说明在这里：https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication

一句话说，就是需要用TOPT密钥管理工具生成动态密码，然后输入动态密码登录，然后第一次登录会给你一个github-recovery-codes.txt,如果更换设备需要使用这个恢复码登录新设备，然后登录新设备之后也是会给你一个新的恢复码


如果是第一次登录，看到github要求进行2FA，可以安装如下  chrome插件：Github 2FA（去chrome商店搜索）
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/66753e4bf1e34c1aabfbc509e6e1951b.jpeg)
然后你回到github页面刷新，在上面图片红框的那个位置就会出现一个30s的密码，输入就可以确认，确认好之后会让你下周恢复密钥，记得下载保存


## github 清除电脑上已经登录的github账户信息
step1： 进入控制面板点击用户账户
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6f6c881d65a14a88b86455bbb3799be8.jpeg)
step2：管理windows凭证
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/4602bdbd04f8401bb2f536e5a14cb85f.jpeg)
step3：删除github相关的凭证
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/1d5c1e7d17464e869b78334963295b8f.png)

## `git clone 出现以下问题：fatal: unable to access XXX: gnutls_handshake() failed: The TLS connection was non-properly terminated.`

`git clone 出现以下问题：fatal: unable to access 'https://github.com/QwenLM/Qwen.git/': gnutls_handshake() failed: The TLS connection was non-properly terminated.`

可以参考stack overflow里面的[Stack](https://stackoverflow.com/questions/68801315/gnutls-handshake-failed-the-tls-connection-was-non-properly-terminated-while)
我是执行下面两行代码解决（ubuntu系统）

```cpp
apt-get update
apt-get install curl
```




## `[git push] ssh: connect to host github.com port 22: Connection timed out fatal: Could not....`
最有可能是防火墙问题，可以参考github官方的解决方法 用443端口解决
https://docs.github.com/en/authentication/troubleshooting-ssh/using-ssh-over-the-https-port

第一步,用以下代码测试443端口是否可用

```cpp
ssh -T -p 443 git@ssh.github.com
```

如果出现这样就是可用的，那么恭喜，十拿九稳了！
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/f77dbe16140f40efb6b5292409f9d5f4.png)
用如下ssh地址替代原来的

```cpp
git clone ssh://git@ssh.github.com:443/YOUR-USERNAME/YOUR-REPOSITORY.git
```
注意是替代，直接用原来的地址加端口是不行的。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/65e69bbb1f014c14acd56857f1cc8191.png)


拿下！




## `远程分支是v3版本，本地的v2版本，但是本地修改了文件还没有add也没有commit，应该怎么更新本地？`
**1. 第一步：首先保存你的本地修改：**

> `git stash `
> 
> 这会将你当前的修改暂时保存起来

**2. 第二步：拉取远程更新**

> `git fetch origin`

**3. 第三步：更新本地分支到远程版本**

> `git merge FETCH_HEAD`

**4. 第四步，恢复你之前的本地修改**

> ```cpp git stash pop ```

**5. 如果在恢复 stash 时遇到冲突，你需要手动解决这些冲突。解决完冲突后，你可以:**

> 添加解决冲突后的文件 git add .
> 
>  提交你的修改 git commit -m "your commit message"

**提示：**

如果你想在应用 stash 前查看保存了什么内容，可以用 git stash list 查看 stash 列表
如果你想查看具体改动，可以用 git stash show -p
如果合并时遇到问题，随时可以用 git status 查看当前状态
如果想放弃当前操作回到起点，可以用 git reset --hard HEAD（注意这会丢失未提交的修改）

