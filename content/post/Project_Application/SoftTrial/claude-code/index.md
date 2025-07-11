---
title: claude-code
description: ""
date: 2025-06-23T19:57:52+08:00
image: images/index/index.png
categories:
    - Project_Application
tags:
    - SoftTrial
---


- [相关教程](#相关教程)



### 相关教程
- [非常好用，在windows通过wsl使用claude，我就是看的这个](https://itecsonline.com/post/how-to-install-claude-code-on-windows)
- [claude code 官方实战](https://docs.anthropic.com/en/docs/claude-code/overview)
- [claude code 仓库](https://github.com/anthropics/claude-code)
- [Claude Code 實戰教學：三大超好用功能公開！【2025年6月更新】【AI寫程式】](https://vocus.cc/article/6854309dfd89780001335549)
- [Claude Code 最佳实践](https://gaccode.com/document/claude-code-best-practices-zh)




### 安装

#### windows安装通过wsl

[安装参考](https://itecsonline.com/post/how-to-install-claude-code-on-windows)

1. wsl --install  # 如果出现问题就要去 https://blog.csdn.net/no1xium/article/details/131285182
2. wsl --list --online  # 查看有哪些可用的镜像,如果没有Ubuntu-24.04进行第三步
3. wsl --install -d Ubuntu-24.04

进入到wsl里面

sudo apt update
sudo apt full-upgrade -y


安装node
其中，我拉取nvm的时候出错了，外网连接不上，原因是vpn的问题，去把vpn的选项都开开



```bash
cd ~  # Switch to Linux Home Directory

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash   #  Install Node.js via NVM (Recommended)

. "$HOME/.nvm/nvm.sh"  # Activate NVM without restarting:

nvm install 20  # Install Node.js version 20 (LTS):

node --version && npm --version  #  Verify Installation
```

Install Additional Dependencies

```bash
sudo apt install python3 python3-pip -y #  Install Python (if needed)

sudo apt install git ripgrep -y # Install Git and Ripgrep (Recommended)


mkdir -p ~/.npm-global


```



### 实战

#### 修复 macOS 上 Claude Code 需要 sudo 运行的问题 （没有修复）

##### 问题
Claude Code 安装在 `/usr/local/lib`，需要 `sudo claude` 运行，导致权限问题。卸载 `https://gaccode.com/claudecode/install` 失败，因为使用了错误包名。

##### 解决步骤
1. **卸载 Claude Code**
   ```bash
   sudo npm uninstall -g @anthropic-ai/claude-code
   ```
   验证卸载：
   ```bash
   npm list -g --depth=0
   sudo rm -f /usr/local/bin/claude
   ```

2. **配置 npm 全局路径到用户目录**
   ```bash
   mkdir -p ~/.npm-global
   npm config set prefix ~/.npm-global
   echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc
   source ~/.zshrc
   ```

3. **重新安装 Claude Code**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
   可选使用镜像源：
   ```bash
   npm install -g @anthropic-ai/claude-code --registry=https://registry.npmmirror.com
   ```

4. **验证运行**
   ```bash
   which claude  # 应输出 ~/.npm-global/bin/claude
   claude --help  # 应显示帮助信息
   ```

##### 注意事项
- 如果仍有错误，检查：
  - `npm config get prefix` 是否为 `~/.npm-global`。
  - `echo $PATH` 是否包含 `~/.npm-global/bin`。
- 避免使用 `sudo claude`，否则可能导致文件权限混乱或配置丢失。



#### claude code 使用git worktree 开启多线程工作


##### 1. 创建 Git Worktree
为每个任务创建独立工作目录和分支。例如，开发 `feature-auth` 和 `feature-ui`：

```bash
git worktree add ../my-project-auth -b feature-auth
git worktree add ../my-project-ui -b feature-ui
```

验证：
```bash
git worktree list
```

##### 2. 配置环境
复制配置文件（如 `.env`）并设置不同端口以避免冲突：
```bash
cp .env ../my-project-auth/.env
cp .env ../my-project-ui/.env
```
- `my-project-auth/.env`：`PORT=3000`
- `my-project-ui/.env`：`PORT=3001`

安装依赖：
```bash
cd ../my-project-auth && npm install
cd ../my-project-ui && npm install
```

##### 3. 启动 Claude Code
在每个 Worktree 中运行 Claude Code：
- 终端 1：
  ```bash
  cd ../my-project-auth
  claude "Implement JWT-based authentication with refresh tokens"
  ```
- 终端 2：
  ```bash
  cd ../my-project-ui
  claude "Redesign UI with responsive Tailwind CSS layout"
  ```

##### 4. 提交和合并
提交代码：
```bash
cd ../my_search-project-auth
git add .
git commit -m "Add JWT authentication"
cd ../my-project-ui
git add .
git commit -m "Update UI with Tailwind CSS"
```

合并到主分支：
```bash
cd ../my-project
git checkout main
git merge feature-auth
git merge feature-ui
```

##### 5. 清理
删除 Worktree 和分支：
```bash
git worktree remove ../my-project-auth
git worktree remove ../my-project-ui
git branch -d feature-auth
git branch -d feature-ui
```

##### 优化技巧
- **自动化脚本**：
  ```bash
  function wt() {
    git worktree add ../worktrees/$1 -b $1
    cd ../worktrees/$1
    cp ../my-project/.env .env
    npm install
    claude
  }
  ```
  使用：`wt feature-auth`

- **任务文件**：在每个 Worktree 创建 `CLAUDE.md` 记录指令，调用 `claude @CLAUDE.md`。
- **IDE 集成**：使用 VS Code 的 Git Worktrees 扩展切换 Worktree。

##### 注意事项
- 确保不同 Worktree 使用不同分支。
- 为数据库任务配置独立实例（如 Docker 容器）。
- 监控资源使用，避免并行任务过多导致过载。

