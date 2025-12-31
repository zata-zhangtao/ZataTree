---
title: 通用模板规范GeneralTemplateSpecifications
description: ""
date: 2025-12-31T07:03:54+08:00
image: images/index/index.png
categories:
    - Grammar
tags:
    - general
---



# Template
## commit 

Git commit 消息的格式有多种最佳实践，其中最流行和推荐的是 **Conventional Commits**（约定式提交）规范。这是一种轻量级的规范，能让 commit 历史更清晰、可读性强，便于自动化生成 changelog、语义化版本号（SemVer）等。

Conventional Commits 标准格式
基本结构：
```
<type>([optional scope]): <subject>

[optional body]

[optional footer(s)]
```

- **type**（必填）：提交类型，常见的有：
  - `feat`：新功能（feature）
  - `fix`：修复 bug
  - `docs`：文档修改
  - `style`：代码格式调整（不影响功能，如空格、缩进）
  - `refactor`：重构（既不是新功能也不是 bug 修复）
  - `perf`：性能优化
  - `test`：添加或修改测试
  - `build`：影响构建系统或外部依赖的变更（如 npm、gulp）
  - `ci`：CI 配置变更（如 GitHub Actions）
  - `chore`：其他杂项（不修改 src 或 test）

- **scope**（可选）：影响范围，用圆括号括起，例如 `(parser)` 或 `(login)`，表示修改了哪个模块。

- **subject**（必填）：简短描述，使用**祈使语气、现在时**（如 “添加” 而非 “添加了” 或 “添加过”），首字母小写（规范推荐），长度控制在 50 字符以内。

- **body**（可选）：详细说明，为什么修改、改了什么。换行分段，每行建议不超过 72 字符。用空行与 subject 分隔。

- **footer**（可选）：脚注，用于标注破坏性变更或关联 issue。
  - 破坏性变更：`BREAKING CHANGE: <描述>`（会导致 major 版本升级）
  - 关联 issue：`Closes #123` 或 `Refs #456`

 示例
1. 简单 commit：
   ```
   feat(login): 添加用户登录功能
   ```

2. 带 body 和 footer：
   ```
   fix(cache): 防止缓存数据过期

   使用请求 ID 来跟踪缓存有效性，移除旧的超时逻辑。

   BREAKING CHANGE: 移除旧 API 接口
   Closes #42
   ```

一般最佳实践（即使不严格用 Conventional Commits）
- 第一行（subject）不超过 50 字符。
- 用空行分隔 subject 和 body。
- body 每行不超过 72 字符。
- 使用祈使语气（Imperative mood）：如 “修复 bug” 而非 “修复了 bug”。
- 解释**为什么**修改，而不是只说**改了什么**（代码本身已显示改了什么）。
- 避免无意义消息如 “fix” 或 “update”。

