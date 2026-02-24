---
title: Self-hosted Runner
description: ""
date: 2026-02-24T09:22:30+08:00
image: images/index/index.png
categories:
    - Project_Application
tags:
    - git&github
---


# 实现从 Windows 开发机通过 CI/CD 部署到另一台 Windows 机器的方法

要实现从一台 Windows 开发机通过 CI/CD 直接部署到另一台 Windows 机器，最主流且最稳定的做法是：在目标 Windows 机器上安装一个“自托管运行器 (Self-hosted Runner 或 Agent)”。

这样一来，CI/CD 平台就可以直接向你的目标机器发送指令，让它自动拉取最新代码（或构建好的程序包）、替换旧文件并重启软件。

以下是实现这一目标的标准流程，以目前最常用的 **GitHub Actions** 为例（GitLab CI/CD 或 Azure DevOps 的原理几乎完全相同）：

开发机上，你编写代码，然后执行 `git push` 命令将代码推送到云端仓库（如 GitHub）。

云端代码仓库（如 GitHub）检测到代码更新后，会触发 CI/CD 流程。此时，目标机器上运行的后台程序（Runner）接收到来自云端的指令，会自动在本地执行编译、覆盖文件和重启软件的脚本。

在你的目标机器上配置 Runner 是最关键的一步。你需要让目标机器和云端仓库建立连接。具体步骤如下：

在 GitHub 上，进入你的代码仓库，点击 **Settings**，然后选择 **Actions**，再进入 **Runners** 页面。点击 **New self-hosted runner**，选择 **Windows** 操作系统及对应的架构（通常是 x64）。

随后，在你的目标 Windows 机器上打开 PowerShell，按照 GitHub 页面上提供的步骤逐行复制并运行命令。这些命令会下载 Runner 程序、进行身份验证并将其注册到你的仓库中。

在配置的最后一步，建议将 Runner 安装为 **Windows 服务 (Windows Service)**，这样目标机器每次开机都会自动启动 Runner，随时准备接收部署任务。

在目标机器上更新软件时，通常会遇到“文件被占用”的问题。因此，你需要写一个简单的 PowerShell 脚本来处理部署逻辑。例如，你的软件运行在 `C:\MyApp`：

1. 停止正在运行的软件进程（或 Windows 服务）。
2. 将新编译好的文件复制到 `C:\MyApp` 并覆盖。
3. 重新启动软件。

在你的开发机上，在项目根目录下创建一个文件夹 `.github/workflows/`，并在其中新建一个文件（例如 `deploy.yml`），填入以下内容：

```yaml
name: Windows Auto Deploy

# 当推送到 main 分支时触发
on:
  push:
    branches: [ "main" ]

jobs:
  build-and-deploy:
    # 这里的 self-hosted 是关键，它告诉 GitHub 在你的目标机器上运行这些步骤
    runs-on: self-hosted 
  
    steps:
      - name: 1. 获取最新代码
        uses: actions/checkout@v4

      - name: 2. 编译项目 (根据你的语言修改)
        run: |
          echo "开始编译..."
          # 例如 C# 项目: dotnet build -c Release
          # 例如 Node 项目: npm install && npm run build
        
      - name: 3. 停止当前运行的程序
        run: |
          # 假设你的程序叫 MyApp.exe
          Stop-Process -Name "MyApp" -ErrorAction SilentlyContinue
          # 如果是 Windows 服务，使用: Stop-Service -Name "MyService"

      - name: 4. 部署/覆盖文件
        run: |
          echo "复制文件到运行目录..."
          # 将编译好的产物复制到目标文件夹 (根据实际路径修改)
          Copy-Item -Path ".\bin\Release\net8.0\*" -Destination "C:\Deployments\MyApp" -Recurse -Force

      - name: 5. 重启程序
        run: |
          echo "启动程序..."
          # 启动进程或重启服务
          Start-Process -FilePath "C:\Deployments\MyApp\MyApp.exe"
          # 如果是 Windows 服务，使用: Start-Service -Name "MyService"
```

在配置 Runner 时，需要注意权限问题。Runner 默认以配置它的用户身份运行。如果你需要操作 C 盘敏感目录或管理 Windows 服务，确保 Runner 对应的用户（或服务账号）具有**管理员权限**。

此外，如果你的目标机器性能较弱，或者不想安装编译工具链，可以将 CI/CD 拆分为两个 Job：第一个 Job 使用 GitHub 官方的云端 Windows 服务器进行编译并上传产物 (Artifacts)；第二个 Job 运行在 `self-hosted` 的目标机器上，只负责下载产物并覆盖文件。
