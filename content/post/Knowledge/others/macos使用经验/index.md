---
title: mac os使用经验
description: ""
date: 2025-04-30T00:20:54+08:00
image: images/index/index.png
categories:
    - Knowledge
tags:
    - others
---


## 常用快捷键

* 全屏截图 control+shift+alt+3
* 区域截图 control+shift+alt+4
* 截图/录屏启动器 shift+command+5
* 左右切换空间 control + 左右
* 显示所有应用窗口 control + 上箭头
* 显示当前应用窗口 control + 下箭头
* 同一个应用之间切换窗口 Command + ～
* 显示/隐藏拓展坞  command +  option + D
* 打开强制退出窗口 Command ⌘ + Option ⌥ + Esc
* 直接强制退出 Command ⌘ + Option ⌥ + Shift ⇧ + Esc
* 最小化当前窗口 Command ⌘ + M
* 启动台，可以通过触发角或者设置默认F5打开


![快捷键](images/index/image.png)





## GUI实战

### 一个软件打开了多个窗口，但你只看到一个窗口？

1. 在菜单栏中，点击应用的 “窗口”（Window） 菜单，最下面就可以看到有哪些窗口

2. 使用 Mission Control（三指/四指上滑）查看所有打开的窗口。或者使用键盘上面的control+上箭头

3. 鼠标右键点击 Dock 上该应用的图标，有多个窗口的选项。



### mac OS中哪个剪辑软件最好用

Final Cut Pro


直接去官网下载90天试用

在控制台中执行以下代码刷新试用期限

mv -v ~/Library/Application\ Support/.ffuserdata ~/.Trash,



### mac OS设置环境变量

` 编辑 ~/.zshrc 或 ~/.bash_profile 前，建议备份。`



 **确认当前 Shell**
在终端运行以下命令，确认你使用的是哪种 shell：
```bash
echo $SHELL
```
- 如果输出是 `/bin/zsh`，你用的是 zsh。
- 如果输出是 `/bin/bash`，你用的是 bash。

---


- 方法 1：临时添加（仅当前终端会话有效）
    在终端输入：
    ```bash
    export 变量名=变量值
    ```
    例如：
    ```bash
    export PATH=$PATH:/usr/local/bin
    ```
    这种方式在关闭终端后会失效。

-  方法 2：永久添加（写入配置文件）


    - **对于 zsh**：

    1. 执行以下命令追加环境变量到～/.zshrc文件中
    
    ```zsh
    echo "export 变量名='变量值'" >> ~/.zshrc
    ```

    也可以手动修改

        1. 打开终端，编辑 `~/.zshrc` 文件：
            ```bash
            nano ~/.zshrc
            ```
        2. 在文件末尾添加：
            ```bash
            export 变量名=变量值
            ```
        3. 保存并退出 在nano编辑器中，按Ctrl + X，接着按Y，再按Enter以保存并关闭文件。



    2. 应用更改：

        ```bash
        source ~/.zshrc
        ```
    3. 验证
        重新打开一个终端窗口，然后执行
        ```zsh
        echo $变量名
        ```

    - **对于 bash**：
    1. 执行以下命令追加到 `~/.bash_profile`：
        ```bash
        echo "export 变量名='变量值'" >> ~/.bash_profile
        ```
    当然你也可以手动修改，不在赘述


    2. 应用更改：
        ```bash
        source ~/.bash_profile
        ```
    3. 验证
        ```zsh
        echo $变量名
        ```

- 注意：
    - 如果需要添加到 `PATH`，建议用 `$PATH` 保留现有路径，例如：
    ```bash
    export PATH=$PATH:/新路径
    ```
    - 确保路径正确，避免语法错误。

---


3. **删除环境变量**

方法 1：临时删除（仅当前终端会话）
使用 `unset` 命令：
```bash
unset 变量名
```


方法 2：永久删除
1. 打开对应的 shell 配置文件（`~/.zshrc` 或 `~/.bash_profile`）。
2. 找到包含 `export 变量名=变量值` 的行，删除或注释掉（在行首加 `#`）。
3. 保存并退出。
4. 应用更改：
   ```bash
   source ~/.zshrc
   ```
   或
   ```bash
   source ~/.bash_profile
   ```

---

- 查看所有环境变量：
  ```bash
  printenv 或者 env
  ```

---


## 命令行实战

### macOS 下更改文件夹及文件所有者为 zata 用户的教程

`目标`

将指定文件夹及其下所有文件的权限更改为 `zata` 用户。

`步骤`

1. **打开终端**：
   - 使用 `Command + T` 或在应用程序中打开「终端」。

2. **更改所有者**：
   - 运行以下命令，将文件夹及其内容的所有者设为 `zata`：
     ```bash
     sudo chown -R zata /path/to/your/folder
     ```
     - 替换 `/path/to/your/folder` 为实际文件夹路径（如 `/Users/yourname/Documents`）。
     - `sudo` 需要管理员密码。

3. **（可选）设置权限**：
   - 若需设置具体权限（例如只给 `zata` 读写权限），运行：
     ```bash
     sudo chmod -R u=rwX,go= /path/to/your/folder
     ```

4. **验证更改**：
   - 检查文件所有者和权限：
     ```bash
     ls -l /path/to/your/folder
     ```
   - 包含隐藏文件：
     ```bash
     ls -ld /path/to/your/folder/* /path/to/your/folder/.*
     ```

` 注意事项`

- 确保 `zata` 用户存在（用 `id zata` 检查）。
- 确认路径正确，避免误操作。
- 更改权限前备份重要数据。


