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


###目录
- [相关教程](#相关教程)

**安装**
  - [windows安装通过wsl](#windows安装通过wsl)

**配置其他模型api** 

  - [配置kimi-k2-api](#配置kimi-k2-api)





### 使用技巧

- 我感觉上，最好把一个任务拆分成非常细的list，然后每一步人工检查一下claude做的对不对，如果让它一次性做很多，最后可能会不太可用，而且需要返工很久







### 相关教程
- [非常好用，在windows通过wsl使用claude，我就是看的这个](https://itecsonline.com/post/how-to-install-claude-code-on-windows)
- [claude code 官方实战](https://docs.anthropic.com/en/docs/claude-code/overview)
- [claude code 仓库](https://github.com/anthropics/claude-code)
- [Claude Code 實戰教學：三大超好用功能公開！【2025年6月更新】【AI寫程式】](https://vocus.cc/article/6854309dfd89780001335549)
- [Claude Code 最佳实践](https://gaccode.com/document/claude-code-best-practices-zh)
- [让claude更加好用](https://itecsonline.com/post/claude-code-tips-tricks)






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

#或者如果网络不行，使用下面的国内镜像去拉取
# curl -o- https://cdn.jsdelivr.net/gh/nvm-sh/nvm@v0.40.3/install.sh | bash

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



### 配置其他模型api

#### 配置kimi-k2-api

https://zhuanlan.zhihu.com/p/1928071611342393465



![alt text](images/index/image.png)

export ANTHROPIC_AUTH_TOKEN=sk-xxxxxxx..xxxxx
export ANTHROPIC_BASE_URL="https://api.moonshot.cn/anthropic/"

#### 配置GLM4.5
https://zhuanlan.zhihu.com/p/1935092461279117856

# ZHIPU-GLM4.5
export ANTHROPIC_AUTH_TOKEN=xxxxxxx..xxxxx
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"


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


#### The Permission System Hack That Changes Everything

 Tips: `--dangerously-skip-permissions`  这个参数只能执行在非root用户下执行，因此如果只有root用户需要创建一个账户

```bash
sudo useradd -m -s /bin/bash username  # 创建新用户

su - username # 切换用户

curl --resolve raw.githubusercontent.com:443:185.199.108.133 -fsSL https://raw.githubusercontent.com/mklement0/n-install/stable/bin/n-install | bash -s 22   # 安装 node 其中--resolve表示自动去找可用的地址， 也可以安装nvm

npm install -g https://gaccode.com/claudecode/install --registry=https://registry.npmmirror.com  # 安装gac站的claude code

claude --dangerously-skip-permissions
```



Here's the single most impactful tip for Claude Code: the `--dangerously-skip-permissions` flag. By default, Claude interrupts your flow constantly, asking permission for every file edit and command. This quickly becomes maddening when you're in the zone.

Picture this: You ask Claude to refactor a component. You switch to check email, grab coffee, and return to find Claude sitting idle, waiting to ask if it can edit the exact file you told it to modify. This happens dozens of times daily with default settings.

The solution: Run `claude --dangerously-skip-permissions` when starting your session. Despite the intimidating name, this simply tells Claude to proceed with the operations you've explicitly requested. It's like switching from "Mother may I?" mode to actually getting work done.

##### Power User Tip
Create an alias in your shell configuration: `alias cc='claude --dangerously-skip-permissions'`. Now you can just type 'cc' to start Claude in productivity mode.








#### VS Code Extension: Multiple Instances for Maximum Productivity

The Claude Code extension works seamlessly with VS Code, Cursor, and Windsurf. While the extension itself is minimal—functioning primarily as a launcher—this simplicity enables a powerful workflow: running multiple Claude Code instances in parallel.

**Pro tip**: Open 2-3 Claude instances simultaneously, each focused on different parts of your codebase. Use your IDE's split pane feature to have one instance handling backend logic while another works on frontend components. This parallel processing transforms how you tackle complex features.


#### Terminal Interface Navigation Tricks

The terminal UI might seem basic at first, but it's packed with powerful features that aren't immediately obvious:

**Smart File References**: Use @ symbols to reference files instantly. Instead of typing full paths, just type `@UserSer` and hit Tab for autocomplete. This works across your entire project structure.

**Command History**: The up arrow doesn't just show your last command—it persists across sessions. You can access complex prompts from days ago, making it easy to rerun similar tasks.

**Quick Context Clearing**: Use `/clear` religiously. Every new feature or bug fix should start fresh. This prevents token waste and keeps responses focused. Think of it as closing browser tabs—essential for mental clarity.


#### Terminal Interface Quirks And Solutions

Every powerful tool has its idiosyncrasies. Here are the non-obvious terminal behaviors that trip up new users and their solutions:

##### Multi-line Input Fix
Shift+Enter doesn't work for new lines by default—incredibly frustrating when writing detailed prompts. Solution: Run `/terminal-setup` once. Claude will configure your terminal properly, and Shift+Enter will work as expected forever after.

##### File Dragging Secret
Dragging files into the terminal normally opens them in a new IDE tab. To reference files in Claude, hold Shift while dragging. This small detail isn't documented anywhere but makes file handling seamless.

##### Image Pasting Trick
Command+V won't paste images from clipboard. Use Control+V instead (yes, even on Mac). This catches everyone initially, but muscle memory adapts quickly.

##### Stopping Claude Properly
Your instinct says Control+C to stop execution, but that exits the program entirely. Use Escape instead. Press Escape twice for a bonus feature: a searchable list of all previous messages in your conversation.

##### Essential Claude Code Shortcuts
```
- Escape: Stop current operation
- Escape x2: Show message history
- Up Arrow: Command history (persistent)
- Tab: Autocomplete file paths
- Ctrl+V: Paste images (not Cmd+V)
- /clear: Start fresh conversation
- /help: Show all commands
```


#### GitHub Integration: Automated Reviews That Actually Help

The `/install-github-app` command enables one of Claude's most underutilized features: intelligent PR reviews. But out of the box, Claude's reviews are verbose, commenting on every minor detail. Here's how to make them valuable:

```yaml
# claude-code-review.yml
# Focused reviews that catch real issues
direct_prompt: |
  Please review this pull request and look for bugs and
  security issues. Only report on bugs and potential
  vulnerabilities you find. Be concise.
```

This configuration transforms Claude from an overeager reviewer into a focused bug-finder. You'll get actionable feedback on logic errors and security issues while skipping the noise about variable naming preferences.

Additional GitHub commands worth knowing:
- `/pr-review [url]` - Review a specific PR
- `/pr-comments` - Pull in PR comments and address them
- `/commit` - Generate commit messages based on changes


#### Advanced Techniques For Power Users

##### Message Queuing: The Productivity Multiplier
Unlike traditional coding assistants, Claude Code allows intelligent message queuing. This fundamentally changes your workflow. Instead of waiting for each task to complete, queue multiple prompts:

```
"Add user authentication to this module"
"Include proper error handling"
"Write comprehensive Jest tests"
"Update the README with usage examples"
```

Claude processes these intelligently, pausing for input when needed and continuing autonomously when possible. You can outline an entire morning's work, then return to find most tasks completed.

##### Custom Hooks: Enforce Your Standards Automatically
Create a `.claude/hooks.mjs` file to enforce code quality automatically:

```javascript
// .claude/hooks.mjs
// Run before accepting any edit
export async function preEdit({ filePath, oldContent, newContent }) {
  // Auto-format TypeScript/JavaScript files
  if (filePath.match(/\.(ts|tsx|js|jsx)$/)) {
    execSync(`npx prettier --write "${filePath}"`, { stdio: 'pipe' });
  }

  // Prevent editing protected files
  const protected = ['package-lock.json', '.env.production'];
  if (protected.includes(path.basename(filePath))) {
    throw new Error(`Cannot edit protected file: ${filePath}`);
  }

  return { proceed: true };
}
```

These hooks run automatically, ensuring every Claude edit meets your standards without manual intervention.

##### Custom Slash Commands
Create project-specific commands by adding markdown files to `.claude/commands/`:

```markdown
# .claude/commands/test.md
Create comprehensive tests for: $ARGUMENTS

Requirements:
- Use Jest and React Testing Library
- Test all major functionality
- Include edge cases
- Mock external dependencies
- Aim for 80%+ coverage
```

Now `/test MyComponent` generates perfect tests following your exact standards. Create commands for common tasks: `/refactor`, `/optimize`, `/document`.


#### Memory Systems: Building Persistent Context

Claude's memory system lets you build context that improves over time. Use the # symbol for quick memories:

```
# always use Tailwind for styling
# prefer composition over inheritance
# use our custom error boundary pattern
```

These memories cascade hierarchically. Place CLAUDE.md files at project root and in subdirectories for granular context:

```markdown
# CLAUDE.md
# Project Overview
Tech stack: React 18, TypeScript, MobX, Tailwind

## Key Commands
- `npm run dev` - Start development server
- `npm test` - Run Jest tests
- `npm run lint` - ESLint with auto-fix

## Architecture Patterns
- Feature-based folder structure
- Container/Presenter component pattern
- Custom hooks for business logic
- MobX for state management

## Coding Standards
- Prefer functional components
- Use TypeScript strict mode
- 80% test coverage minimum
```

Claude automatically uses the most specific context for each task.


#### Handling Large Files And Complex Refactoring

One area where Claude Code truly excels is handling massive files that crash other AI assistants. Here's how to work effectively with large codebases:

##### The 18,000 Line Test
When working with extremely large files, use these strategies:

**Targeted Context**: Instead of `@LargeComponent.tsx refactor this`, be specific: `@LargeComponent.tsx refactor the user authentication section (lines 5000-6000)`

**Incremental Updates**: Break large refactoring into queued messages: "First, update the state management pattern" then "Next, modernize the event handlers" then "Finally, update the render logic"

**Pattern Recognition**: Claude excels at finding patterns across large files. Use prompts like "Find all instances of the legacy API pattern and list them" before "Now update all instances to use the new pattern"

##### Complex Navigation Commands
Claude understands architectural queries that go beyond simple search:
- "Show me how user authentication flows through the app"
- "Find all components that depend on the UserContext"
- "Trace the data flow from API call to UI rendering for products"
- "Identify circular dependencies in the module structure"


#### Best Practices From Thousands of Hours of Usage

##### Context Management Mastery
**The 3-File Rule**: Only include files that directly relate to your current task. More context isn't better—it's noise that degrades response quality.

**Explicit Over Implicit**: Instead of "fix the bug," say "@auth/login.ts fix the race condition in the OAuth callback handler on line 145"

**Session Hygiene**: Start each new feature with `/clear`. Think of conversations like git branches—keep them focused and disposable.

##### Prompt Patterns That Work
**The Specification Pattern**:
```
Create a user profile component that:
- Displays user avatar, name, and bio
- Uses our standard Card component
- Includes edit mode with form validation
- Has Jest tests for all interactions
```

**The Constraint Pattern**:
```
Refactor this function to be more efficient. Constraints: maintain the same API, keep it under 50 lines, use no external dependencies
```

**The Example Pattern**:
```
Update this component to follow the same pattern as @components/UserCard.tsx
```

##### Workflow Integration Tips
- **Test-Driven Claude**: Write your tests first, then prompt: "Implement code to make these tests pass"
- **Documentation-First**: Have Claude write docs, review them, then implement: "Based on this documentation, implement the feature"
- **Pair Programming Mode**: Work alongside Claude in real-time: "Watch for TypeScript errors as I type and suggest fixes"

##### Ultimate Productivity Hack
Set up keyboard shortcuts: Cmd+1 through Cmd+4 for different Claude instances, Cmd+` to return to editor. Combined with message queuing, you can orchestrate complex features across multiple files simultaneously.


#### Troubleshooting Common Issues

##### When Claude Gets Confused
**Symptom**: Responses seem to ignore your context or give generic answers
**Solution**: You've accumulated too much conversation history. Use `/clear` and restate your task with fresh context.

**Symptom**: Claude keeps asking permission despite using skip-permissions flag
**Solution**: Some operations still require confirmation. Create a hook to auto-approve specific operations you trust.

**Symptom**: File changes aren't being recognized
**Solution**: Claude caches file contents. Use `@filename --refresh` to force a reload.

##### Performance Optimization
- **Slow Responses**: Check if you're including unnecessary files. Each @ reference adds to processing time.
- **Token Limits**: Watch the token counter. When approaching limits, start a fresh conversation with `/clear` rather than letting Claude compress history.
- **Model Switching**: If Opus is being slow, manually switch to Sonnet with `/model sonnet` for faster responses on simpler tasks.


#### Hidden Features Most Developers Miss

**The Double-Tab Trick**: Hit Tab twice on any partial command or file path to see all available options. Works for slash commands too.

**Regex in File References**: Use patterns like `@**/*test*.ts` to reference all test files at once.

**Conversation Forking**: Use `/fork` to create a branch of your current conversation. Perfect for exploring different solutions without losing context.  （这个是没有 fork 命令的 ，可以使用git 的worktree）

**Silent Mode**: Add `--quiet` to any command to suppress Claude's explanations and get just the code.

**Batch Operations**: Process multiple files at once: `@{file1,file2,file3} add error handling to all exports`

**Time Travel**: Use `/history 2024-12-01` to see all conversations from a specific date.

**Export Workflows**: `/export cookbook` creates a markdown file of your most successful prompt patterns.

##### Advanced Hidden Commands
```bash
# Hidden gems
/analyze @src --complexity  # Complexity analysis
/diagram @components       # Generate component diagrams
/benchmark @utils/*.ts     # Performance analysis
/security @api            # Security audit
/deps @package.json       # Dependency analysis
```

