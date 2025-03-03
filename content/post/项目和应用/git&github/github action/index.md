---
title: 2-github action 使用
description: GitHub Actions 是 GitHub 提供的自动化工具，可以帮助你在代码仓库中实现持续集成（CI）和持续部署（CD）。通过定义工作流（Workflow），你可以在代码推送、拉取请求或特定事件触发时自动运行测试、构建、部署等任务。
date: 2025-03-03T00:00:00+08:00
# slug: 文件夹名/index.md ## 必填，文件夹名/index.md
# image: helena-hertz-wWZzXlDpMog-unsplash.jpg
categories:
    # - DeepLearning
    # - 画图
    # - Python
    # - LLM
    - Project&Application
    # - Library
    # - PaperReading
    # - Study
    # - Other
    # - Knowledge points
tags:
    - git&github

---




### **核心概念**
1. **Workflow（工作流）**  
   工作流是一个自动化过程，定义在一或多个 YAML 文件中，存放在 `.github/workflows` 目录下。
   
2. **Event（事件）**  
   触发工作流的事件，例如 `push`（推送代码）、`pull_request`（拉取请求）或定时触发。

3. **Job（任务）**  
   工作流中的一组步骤（Steps），运行在同一个虚拟机上。多个 Job 可以并行或按顺序执行。

4. **Step（步骤）**  
   Job 中的单个操作，例如运行命令或调用一个 Action。

5. **Action（动作）**  
   可重用的代码单元，通常由社区或官方提供，简化常见任务。

6. **Runner（运行器）**  
   执行工作流的服务器，GitHub 提供托管的 Runner，也支持自托管。

---

### **快速入门教程**
#### **目标**
创建一个简单的 GitHub Actions 工作流，在每次推送代码时运行一个脚本，输出 "Hello, GitHub Actions!"。

#### **步骤**
1. **创建仓库**  
   在 GitHub 上创建一个新仓库（或使用现有仓库）。

2. **添加工作流文件**  
   - 在仓库根目录下创建文件夹 `.github/workflows`。
   - 在该文件夹中创建一个文件，例如 `hello.yml`。

3. **编写工作流文件**  
   将以下内容写入 `hello.yml`：
   ```yaml
   name: Hello World Workflow

   # 触发条件：在推送代码到 main 分支时运行
   on:
     push:
       branches:
         - main

   # 定义任务
   jobs:
     say-hello:
       runs-on: ubuntu-latest # 使用 GitHub 提供的最新 Ubuntu 虚拟机
       steps:
         - name: Checkout code
           uses: actions/checkout@v3 # 检出代码到虚拟机

         - name: Say Hello
           run: echo "Hello, GitHub Actions!" # 运行简单的 shell 命令
   ```

4. **提交文件**  
   将 `hello.yml` 提交到仓库的 `main` 分支。

5. **查看运行结果**  
   - 转到仓库的 **Actions** 标签页。
   - 你会看到名为 "Hello World Workflow" 的工作流正在运行。
   - 点击工作流名称，查看日志，确认 "Hello, GitHub Actions!" 已输出。

---

### **进阶示例**
#### **运行测试并部署**
假设你有一个 Node.js 项目，想在推送代码时运行测试并部署到服务器。

1. **工作流文件示例**  
   创建 `.github/workflows/test-and-deploy.yml`：
   ```yaml
   name: Test and Deploy

   on:
     push:
       branches:
         - main

   jobs:
     test:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Setup Node.js
           uses: actions/setup-node@v3
           with:
             node-version: '16'

         - name: Install dependencies
           run: npm install

         - name: Run tests
           run: npm test

     deploy:
       needs: test # 在 test 任务成功后运行
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Deploy to server
           run: |
             echo "Deploying to server..."
             # 这里可以添加实际部署命令，例如通过 SSH
   ```

2. **添加秘密（Secrets）**  
   如果部署需要敏感信息（如 SSH 密钥）：  
   - 转到仓库的 **Settings > Secrets and variables > Actions**。
   - 点击 **New repository secret**，添加密钥（如 `SSH_KEY`）。
   - 在工作流中通过 `secrets.SSH_KEY` 使用它。

---

### **常用配置**
1. **触发事件**  
   ```yaml
   on:
     push: # 推送时触发
       branches:
         - main
     pull_request: # 拉取请求时触发
       branches:
         - main
     schedule: # 定时触发（每天凌晨0点）
       - cron: '0 0 * * *'
   ```

2. **设置环境变量**  
   ```yaml
   env:
     MY_VAR: "Hello"
   jobs:
     example:
       runs-on: ubuntu-latest
       steps:
         - run: echo $MY_VAR # 输出 "Hello"
   ```

3. **使用社区 Action**  
   示例：使用 `actions/cache` 缓存依赖：
   ```yaml
   - name: Cache node modules
     uses: actions/cache@v3
     with:
       path: ~/.npm
       key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
   ```

---

### **调试技巧**
- **查看日志**：在 Actions 标签页点击工作流，展开每个 Job 和 Step 查看详细输出。
- **添加调试步骤**：在步骤中运行 `ls -la`（Linux）或 `dir`（Windows）检查文件。
- **使用 GitHub 提供的测试工具**：在本地安装 `act`（需要 Docker）模拟运行工作流。

---

### **常见问题**
1. **工作流没触发？**  
   检查 `on` 配置是否匹配事件和分支。

2. **权限不足？**  
   在仓库设置中确认 Actions 已启用（Settings > Actions > General）。

3. **需要更多计算资源？**  
   考虑使用自托管 Runner。

---

### **扩展阅读**
- 官方文档：https://docs.github.com/en/actions
- 社区 Actions：https://github.com/marketplace?type=actions

希望这个教程能帮你快速掌握 GitHub Actions！如果有具体问题或需要更复杂的示例，随时告诉我。