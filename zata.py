import os
from datetime import datetime
import argparse
import tkinter as tk
from tkinter import ttk, messagebox

# 原有函数保持不变，返回值改为元组以适应 GUI 使用
def create_category(category):
    """创建category目录"""
    target_path = os.path.join("content", "post", category)
    try:
        os.makedirs(target_path, exist_ok=True)
        return True, f"Category目录 '{target_path}' 创建成功！"
    except Exception as e:
        return False, f"创建category时发生错误: {str(e)}"

def create_tag(category, tag):
    """创建tag目录，必须指定category"""
    base_path = os.path.join("content", "post")
    target_path = os.path.join(base_path, category, tag)
    
    category_path = os.path.join(base_path, category)
    if not os.path.exists(category_path):
        return False, f"错误：Category目录 '{category_path}' 不存在！请先创建category"
    
    try:
        os.makedirs(target_path, exist_ok=True)
        return True, f"Tag目录 '{target_path}' 创建成功！"
    except Exception as e:
        return False, f"创建tag时发生错误: {str(e)}"

def create_folder_and_md(categories, tags, title):
    """创建文章目录和index.md文件"""
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    base_path = os.path.join("content", "post")
    
    if categories:
        target_path = os.path.join(base_path, categories, tags, title)
        parent_path = os.path.join(base_path, categories, tags)
        
        if not os.path.exists(parent_path):
            return False, f"错误：父目录 '{parent_path}' 不存在！请先创建相应的categories和tags目录"
    else:
        matched_paths = []
        for category in os.listdir(base_path):
            category_path = os.path.join(base_path, category)
            if os.path.isdir(category_path):
                tag_path = os.path.join(category_path, tags)
                if os.path.exists(tag_path) and os.path.isdir(tag_path):
                    matched_paths.append(tag_path)
        
        if len(matched_paths) == 0:
            return False, f"错误：未在任何category下找到tags '{tags}'！请先创建相应的tags目录"
        elif len(matched_paths) > 1:
            error_msg = f"错误：找到多个匹配的tags '{tags}'：\n"
            for path in matched_paths:
                error_msg += f"  - {path}\n"
            error_msg += "请指定具体的category以避免歧义"
            return False, error_msg
        else:
            parent_path = matched_paths[0]
            target_path = os.path.join(parent_path, title)
            categories = os.path.basename(os.path.dirname(parent_path))

    try:
        os.makedirs(target_path, exist_ok=True)
        md_file_path = os.path.join(target_path, "index.md")
        
        header_content = f"""---
title: {title}
description: ""
date: {current_time}
image: images/index/index.png
"""
        if categories:
            header_content += f"""categories:
    - {categories}
"""
        header_content += f"""tags:
    - {tags}
---
"""
        
        if not os.path.exists(md_file_path):
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(header_content)
            return True, f"文件夹 '{target_path}' 和 'index.md' 创建成功！"
        return True, f"文件夹 '{target_path}' 已存在，跳过创建 'index.md'。"
    except Exception as e:
        return False, f"发生错误: {str(e)}"

# 新增函数：获取现有 Category 和 Tag 列表
def get_existing_categories():
    base_path = os.path.join("content", "post")
    if not os.path.exists(base_path):
        return []
    return [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

def get_existing_tags(category=None):
    base_path = os.path.join("content", "post")
    if not os.path.exists(base_path):
        return []
    tags = set()
    if category:
        category_path = os.path.join(base_path, category)
        if os.path.exists(category_path):
            tags.update([d for d in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, d))])
    else:
        for cat in os.listdir(base_path):
            cat_path = os.path.join(base_path, cat)
            if os.path.isdir(cat_path):
                tags.update([d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d))])
    return sorted(list(tags))

# 修改后的 GUI
def create_gui():
    root = tk.Tk()
    root.title("Zata - 博客管理工具")
    root.geometry("500x400")

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, fill="both", expand=True)

    # Category选项卡
    category_frame = ttk.Frame(notebook)
    notebook.add(category_frame, text="创建Category")

    ttk.Label(category_frame, text="Category名称:").pack(pady=5)
    category_entry = ttk.Entry(category_frame, width=40)
    category_entry.pack(pady=5)

    def create_category_btn():
        category = category_entry.get().strip()
        if not category:
            messagebox.showerror("错误", "请输入Category名称")
            return
        success, msg = create_category(category)
        messagebox.showinfo("结果", msg)
        # 成功后刷新下拉框
        if success:
            update_category_combobox()

    ttk.Button(category_frame, text="创建Category", command=create_category_btn).pack(pady=10)

    # Tag选项卡
    tag_frame = ttk.Frame(notebook)
    notebook.add(tag_frame, text="创建Tag")

    ttk.Label(tag_frame, text="所属Category:").pack(pady=5)
    tag_category_entry = ttk.Entry(tag_frame, width=40)
    tag_category_entry.pack(pady=5)
    
    ttk.Label(tag_frame, text="Tag名称:").pack(pady=5)
    tag_entry = ttk.Entry(tag_frame, width=40)
    tag_entry.pack(pady=5)

    def create_tag_btn():
        category = tag_category_entry.get().strip()
        tag = tag_entry.get().strip()
        if not category or not tag:
            messagebox.showerror("错误", "请输入Category和Tag名称")
            return
        success, msg = create_tag(category, tag)
        messagebox.showinfo("结果", msg)
        # 成功后刷新下拉框
        if success:
            update_tag_combobox()

    ttk.Button(tag_frame, text="创建Tag", command=create_tag_btn).pack(pady=10)

    # 文章选项卡
    post_frame = ttk.Frame(notebook)
    notebook.add(post_frame, text="创建文章")

    # Category 下拉框
    ttk.Label(post_frame, text="选择Category（可选）:").pack(pady=5)
    category_combobox = ttk.Combobox(post_frame, width=37, state="readonly")
    category_combobox.pack(pady=5)
    
    # Tag 下拉框
    ttk.Label(post_frame, text="选择Tag:").pack(pady=5)
    tag_combobox = ttk.Combobox(post_frame, width=37, state="readonly")
    tag_combobox.pack(pady=5)
    
    ttk.Label(post_frame, text="文章标题:").pack(pady=5)
    post_title_entry = ttk.Entry(post_frame, width=40)
    post_title_entry.pack(pady=5)

    # 更新下拉框内容的函数
    def update_category_combobox():
        categories = get_existing_categories()
        category_combobox["values"] = [""] + categories  # 空字符串表示可选
        if categories:
            category_combobox.set("")
    
    def update_tag_combobox(event=None):
        selected_category = category_combobox.get()
        if selected_category:
            tags = get_existing_tags(selected_category)
        else:
            tags = get_existing_tags()
        tag_combobox["values"] = tags
        if tags:
            tag_combobox.set(tags[0])
        else:
            tag_combobox.set("")

    # 绑定 Category 下拉框的选择事件
    category_combobox.bind("<<ComboboxSelected>>", update_tag_combobox)

    # 初始化下拉框
    update_category_combobox()
    update_tag_combobox()

    def create_post_btn():
        category = category_combobox.get() or None
        tag = tag_combobox.get()
        title = post_title_entry.get().strip()
        if not tag or not title:
            messagebox.showerror("错误", "请选择Tag并输入文章标题")
            return
        success, msg = create_folder_and_md(category, tag, title)
        messagebox.showinfo("结果", msg)

    ttk.Button(post_frame, text="创建文章", command=create_post_btn).pack(pady=10)

    root.mainloop()

def main():
    parser = argparse.ArgumentParser(prog="zata", description="博客目录和文件管理工具")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    create_parser = subparsers.add_parser("create", help="创建文章文件夹和index.md")
    create_parser.add_argument("-c", "--categories", help="博客分类（可选）")
    create_parser.add_argument("-t", "--tags", required=True, help="博客标签")
    create_parser.add_argument("-b", "--title", required=True, help="博客标题")

    category_parser = subparsers.add_parser("create-category", help="创建category目录")
    category_parser.add_argument("-c", "--category", required=True, help="要创建的category名称")

    tag_parser = subparsers.add_parser("create-tag", help="创建tag目录")
    tag_parser.add_argument("-c", "--category", required=True, help="所属category")
    tag_parser.add_argument("-t", "--tag", required=True, help="要创建的tag名称")

    gui_parser = subparsers.add_parser("gui", help="启动图形界面")

    args = parser.parse_args()

    if args.command == "create":
        success, msg = create_folder_and_md(args.categories, args.tags, args.title)
        print(msg)
    elif args.command == "create-category":
        success, msg = create_category(args.category)
        print(msg)
    elif args.command == "create-tag":
        success, msg = create_tag(args.category, args.tag)
        print(msg)
    elif args.command == "gui":
        create_gui()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


"""
#### 1. 通过命令行使用
在命令行中运行 `zata.exe`，支持以下命令：
- **创建Category**：
  ```
  zata.exe create-category -c "tech"
  ```
  输出：`Category目录 'content/post/tech' 创建成功！`
- **创建Tag**：
  ```
  zata.exe create-tag -c "tech" -t "python"
  ```
  输出：`Tag目录 'content/post/tech/python' 创建成功！`
- **创建文章**：
  - 指定Category：
    ```
    zata.exe create -c "tech" -t "python" -b "my-python-post"
    ```
    输出：`文件夹 'content/post/tech/python/my-python-post' 和 'index.md' 创建成功！`
  - 只使用Tag（假设Tag唯一）：
    ```
    zata.exe create -t "python" -b "my-python-post"
    ```
    输出：`文件夹 'content/post/tech/python/my-python-post' 和 'index.md' 创建成功！`
- **查看帮助**：
  ```
  zata.exe
  ```
  显示所有可用命令和参数。

#### 2. 通过GUI使用
运行以下命令启动图形界面：
```
zata.exe gui
```
- **界面功能**：
  - **创建Category**：在“创建Category”选项卡输入名称，点击按钮。
  - **创建Tag**：在“创建Tag”选项卡输入Category和Tag名称，点击按钮。
  - **创建文章**：在“创建文章”选项卡选择Category（可选）、Tag，输入标题，点击按钮。
- **操作结果**：通过弹窗显示成功或错误信息。
- **动态更新**：创建新Category或Tag后，文章选项卡的下拉框会自动刷新。

"""