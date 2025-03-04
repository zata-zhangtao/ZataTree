import os
from datetime import datetime
import argparse

def create_category(category):
    """创建category目录"""
    target_path = os.path.join("content", "post", category)
    try:
        os.makedirs(target_path, exist_ok=True)
        print(f"Category目录 '{target_path}' 创建成功！")
    except Exception as e:
        print(f"创建category时发生错误: {str(e)}")

def create_tag(category, tag):
    """创建tag目录，必须指定category"""
    base_path = os.path.join("content", "post")
    target_path = os.path.join(base_path, category, tag)
    
    # 检查category是否存在
    category_path = os.path.join(base_path, category)
    if not os.path.exists(category_path):
        print(f"错误：Category目录 '{category_path}' 不存在！请先创建category")
        return
    
    try:
        os.makedirs(target_path, exist_ok=True)
        print(f"Tag目录 '{target_path}' 创建成功！")
    except Exception as e:
        print(f"创建tag时发生错误: {str(e)}")

def create_folder_and_md(categories, tags, title):
    """创建文章目录和index.md文件"""
    # 获取当前时间并格式化
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    # 基础路径
    base_path = os.path.join("content", "post")
    
    # 如果提供了categories，使用categories/tags的路径
    if categories:
        target_path = os.path.join(base_path, categories, tags, title)
        parent_path = os.path.join(base_path, categories, tags)
        
        # 检查父目录是否存在
        if not os.path.exists(parent_path):
            print(f"错误：父目录 '{parent_path}' 不存在！请先创建相应的categories和tags目录")
            return
    else:
        # 只使用tags时，遍历所有categories寻找匹配的tags
        matched_paths = []
        for category in os.listdir(base_path):
            category_path = os.path.join(base_path, category)
            if os.path.isdir(category_path):
                tag_path = os.path.join(category_path, tags)
                if os.path.exists(tag_path) and os.path.isdir(tag_path):
                    matched_paths.append(tag_path)
        
        # 根据匹配结果处理
        if len(matched_paths) == 0:
            print(f"错误：未在任何category下找到tags '{tags}'！请先创建相应的tags目录")
            return
        elif len(matched_paths) > 1:
            print(f"错误：找到多个匹配的tags '{tags}'：")
            for path in matched_paths:
                print(f"  - {path}")
            print("请指定具体的category以避免歧义")
            return
        else:
            # 找到唯一匹配的tags
            parent_path = matched_paths[0]
            target_path = os.path.join(parent_path, title)
            # 获取对应的category用于生成header
            categories = os.path.basename(os.path.dirname(parent_path))

    try:
        # 创建目标文件夹
        os.makedirs(target_path, exist_ok=True)
        
        # 创建index.md文件的路径
        md_file_path = os.path.join(target_path, "index.md")
        
        # 创建头部内容，根据是否有categories动态调整
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
        
        # 写入index.md文件
        if not os.path.exists(md_file_path):
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(header_content)
            print(f"文件夹 '{target_path}' 和 'index.md' 创建成功！")
        else:
            print(f"文件夹 '{target_path}' 已存在，跳过创建 'index.md'。")
    except Exception as e:
        print(f"发生错误: {str(e)}")

def main():
    # 设置命令行参数解析器
    parser = argparse.ArgumentParser(prog="zata", description="博客目录和文件管理工具")
    subparsers = parser.add_subparsers(dest="command", help="可用命令")

    # 添加 'create' 子命令（创建文章）
    create_parser = subparsers.add_parser("create", help="创建文章文件夹和index.md")
    create_parser.add_argument("-c", "--categories", help="博客分类（可选）")
    create_parser.add_argument("-t", "--tags", required=True, help="博客标签")
    create_parser.add_argument("-b", "--title", required=True, help="博客标题")

    # 添加 'create-category' 子命令
    category_parser = subparsers.add_parser("create-category", help="创建category目录")
    category_parser.add_argument("-c", "--category", required=True, help="要创建的category名称")

    # 添加 'create-tag' 子命令
    tag_parser = subparsers.add_parser("create-tag", help="创建tag目录")
    tag_parser.add_argument("-c", "--category", required=True, help="所属category")
    tag_parser.add_argument("-t", "--tag", required=True, help="要创建的tag名称")

    # 解析参数
    args = parser.parse_args()

    # 根据命令执行操作
    if args.command == "create":
        create_folder_and_md(args.categories, args.tags, args.title)
    elif args.command == "create-category":
        create_category(args.category)
    elif args.command == "create-tag":
        create_tag(args.category, args.tag)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()


"""

打包方式 pyinstaller -F --noconsole zata.py

使用示例：
假设目录结构如下：


content/post/
    tech/
        python/
    programming/
        python/



# 创建category
python zata create-category -c "tech"

# 创建tag
python zata create-tag -c "tech" -t "python"

# 指定categories创建文章
python zata create -c "tech" -t "python" -b "my-python-post"
# 输出：文件夹 'content/post/tech/python/my-python-post' 和 'index.md' 创建成功！

# 只使用tags创建文章（假设只有一个python tags）
python zata create -t "python" -b "my-python-post"
# 输出：文件夹 'content/post/tech/python/my-python-post' 和 'index.md' 创建成功！

# 只使用tags创建文章（假设有多个python tags）
python zata create -t "python" -b "my-python-post"
# 输出：
# 错误：找到多个匹配的tags 'python'：
#   - content/post/tech/python
#   - content/post/programming/python
# 请指定具体的category以避免歧义

# 只使用tags创建文章（假设没有对应的tags）
python zata create -t "java" -b "my-java-post"
# 输出：错误：未在任何category下找到tags 'java'！请先创建相应的tags目录
注意事项：
如果不指定 categories，脚本会自动查找所有匹配的 tags。
如果 tags 在多个 category 下存在，会要求用户明确指定 category。
生成的 index.md 文件会包含从路径推断出的 category（如果适用）。
如果 tags 不存在，仍会提示用户先创建对应的 tags 目录。
"""