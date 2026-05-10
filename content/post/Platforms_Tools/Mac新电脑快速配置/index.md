---
title: Mac 新电脑快速配置 — Git、Node 与 UV
description: "新 Mac 到手后的核心开发环境配置，Homebrew 管系统工具，fnm 管 Node，UV 管 Python"
draft: true
date: 2026-05-10T15:30:48+08:00
categories:
    - Platforms&Tools
tags:
    - Mac
    - Git
    - UV
    - Node
    - fnm
---

## 前言

新 Mac 到手，先把开发环境搭起来。本文的核心思路是**各司其职**：

| 工具 | 职责 |
|:---|:---|
| **Homebrew** | 装系统级工具（Git、fnm、ripgrep 等）|
| **fnm** | Node 版本管理 |
| **UV** | Python 版本管理 + 包管理 |

不混用职责，不 `brew install node`，避免升级时互相干扰。

> **国内用户注意**：以下步骤大量依赖 GitHub，建议先配好代理再进行安装。

---

## 一、代理配置（国内用户必看）

如果你有可用的代理工具（Clash/V2Ray/Surge 等），推荐直接写入 `~/.zshrc`，所有终端会话自动生效：

```bash
echo 'export https_proxy=http://127.0.0.1:7890' >> ~/.zshrc
echo 'export http_proxy=http://127.0.0.1:7890' >> ~/.zshrc
echo 'export all_proxy=socks5://127.0.0.1:7890' >> ~/.zshrc
source ~/.zshrc
```

> 不同代理软件的端口可能不同，常见的是 `7890`、`1080`、`6152` 等，请根据实际情况修改。

验证代理生效：

```bash
curl -I https://www.google.com
```

**临时配置（当前终端生效）**：

```bash
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
export all_proxy=socks5://127.0.0.1:7890
```

**Homebrew 镜像源（不翻墙的备选）**：

```bash
export HOMEBREW_INSTALL_FROM_API=1
export HOMEBREW_API_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles/api"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.ustc.edu.cn/homebrew-bottles"
git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
brew update
```

---

## 二、基础环境

### 2.1 Xcode Command Line Tools

系统级编译依赖，自带一个基础版 Git：

```bash
xcode-select --install
```

### 2.2 Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## 三、Git 安装与配置

### 3.1 安装

Mac 预装的 Git 版本较旧，通过 Homebrew 装最新版：

```bash
brew install git
git --version
```

### 3.2 基础配置

```bash
# 改成你自己的
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 默认分支名设为 main
git config --global init.defaultBranch main

# 默认编辑器（可选）
git config --global core.editor "code --wait"
```

### 3.3 SSH 密钥

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
pbcopy < ~/.ssh/id_ed25519.pub
```

粘贴到 GitHub/GitLab 的 SSH Keys 设置页面，然后测试：

```bash
ssh -T git@github.com
```

### 3.4 Git 代理（可选）

加速克隆 GitHub 仓库：

```bash
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
```

取消代理：

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

---

## 四、Node 环境（fnm）

[fnm](https://github.com/Schniz/fnm) 是 Rust 写的 Node 版本管理器，比 nvm 快，兼容 `.nvmrc`。

### 4.1 安装 fnm

```bash
brew install fnm
```

把 fnm 初始化写入 `~/.zshrc`：

```bash
echo 'eval "$(fnm env --use-on-cd)"' >> ~/.zshrc
source ~/.zshrc
```

### 4.2 安装 Node

```bash
# 安装并设为默认版本
fnm install 22
fnm default 22

# 验证
node -v
npm -v
```

### 4.3 常用操作

```bash
# 查看已安装版本
fnm list

# 切换版本
fnm use 20

# 安装 .nvmrc 中指定的版本
fnm install
fnm use
```

---

## 五、Python 环境（UV）

[UV](https://github.com/astral-sh/uv) 是 Astral 团队开发的极速 Python 包管理器，一个工具替代 pyenv + pip + venv。

### 5.1 安装 UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

安装脚本一般会自动配置 shell，如果没有，手动添加：

```bash
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
source ~/.zshrc
```

### 5.2 安装 Python

```bash
uv python install 3.12
```

### 5.3 常用操作

```bash
# 创建项目（自带 venv）
uv init myproject
cd myproject

# 添加依赖
uv add requests

# 运行脚本
uv run python script.py

# 同步依赖
uv sync
```

### 5.4 与 IDE 配合

- **VSCode**: `Python: Select Interpreter` → 选择 `myproject/.venv/bin/python`
- **PyCharm**: `Previously configured interpreter` → 指向 `.venv/bin/python`

---

## 六、其他常用工具

```bash
# CLI 工具
brew install tree ripgrep fd jq wget curl

# VSCode
brew install --cask visual-studio-code
```

---

## 七、验证清单

| 检查项 | 命令 | 期望结果 |
|:---|:---|:---|
| Git 版本 | `git --version` | 2.x |
| SSH 连接 | `ssh -T git@github.com` | Hi username! |
| fnm 版本 | `fnm --version` | 1.x |
| Node 版本 | `node -v` | v22.x |
| UV 版本 | `uv --version` | 0.x |
| Python 可用 | `uv run python --version` | 3.12.x |

---

## 八、一键脚本（可选）

把以上流程写成 `setup.sh`，丢进 GitHub 私有仓库，换机时一条命令跑完：

```bash
#!/bin/bash
set -e

echo "==> 检查代理"
if [ -z "$https_proxy" ]; then
    echo "⚠️  先配好代理再运行"
    exit 1
fi

echo "==> Xcode CLT"
xcode-select --install 2>/dev/null || true

echo "==> Homebrew"
command -v brew >/dev/null || \
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo "==> 工具链"
brew install git fnm tree ripgrep fd jq

echo "==> Node"
eval "$(fnm env --use-on-cd)"
fnm install 22
fnm default 22

echo "==> UV + Python"
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12

echo "==> Git 配置"
read -p "Git 用户名: " name
read -p "Git 邮箱: " email
git config --global user.name "$name"
git config --global user.email "$email"
git config --global init.defaultBranch main

echo "✅ 完成！重启终端生效。"
```

---

## 总结

| 工具 | 用途 |
|:---|:---|
| **Homebrew** | 系统工具（Git、fnm、ripgrep…）|
| **fnm** | Node 版本管理 |
| **UV** | Python 版本管理 + 包管理 |

各司其职，互不干涉。换机时一条脚本 5 分钟跑完，后续按需扩展即可。
