---
title: 一个自动签到的py并且使用github action每日执行
description: 一个自动签到的py并且使用github action每日执行
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
    - github
    - 爬虫

---

###
```py
import requests
import schedule
import time
from datetime import datetime
Cookie = os.environ.get("YOUR_COOKIE")  # 把Cookie放置在action的环境变量中
# 签到函数
def checkin():
    # 替换为实际的签到接口 URL
    url = XXXXX

    # 准备请求头（可能需要 Cookie 或 Token 来验证身份）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/json",
        # 如果需要登录凭证，可以在这里添加 Cookie 或 Authorization
        "Cookie": Cookie,
        # "Authorization": "Bearer your_token_here"
    }

    # 准备请求数据（根据实际接口要求调整）
    data = {
        "userId": "your-user-id",  # 替换为你的用户 ID
        "timestamp": int(time.time())  # 可选：发送当前时间戳
    }

    try:
        # 发送签到请求
        response = requests.post(url, headers=headers)
        response_json = response.json()

        # 检查签到是否成功
        if response.status_code == 200 :
            print(f"{datetime.now()} 签到成功：{response_json.get('msg')}")
        else:
            print(f"{datetime.now()} 签到失败：{response_json.get('msg')}")
    except Exception as e:
        print(f"{datetime.now()} 签到请求失败：{str(e)}")


# 脚本主循环
if __name__ == "__main__":
    print("自动签到脚本已启动...")
    # 首次运行时立即签到（可选）
    checkin()
```


