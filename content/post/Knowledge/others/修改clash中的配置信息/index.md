---
title: 修改clash中的配置信息
description: ""
date: 2025-03-06T10:51:58+08:00
# image: images/index/index.png
categories:
    - Knowledge
tags:
    - others
---





### 修改clash中的配置信息

<span style="color:red"> 改过配置之后不要刷新订阅，不然就没了，不过不更新又不会加载规则，可以通过切换订阅文件的方式加载规则</span>




#### **1. 获取代理服务器信息**
你需要从你的代理服务提供商（比如 V2Ray、Shadowsocks、Trojan 等）那里拿到服务器信息，通常包括：
- 服务器地址（IP 或域名）
- 端口号
- 加密方式
- 密码或 UUID
- 协议类型（如 vmess、vless、ss 等）

例如，一个简单的 Shadowsocks 服务器信息可能是：
```
服务器地址: example.com
端口: 8388
加密: aes-256-gcm
密码: yourpassword
```

#### **2. 创建基础配置文件**
创建一个 `config.yaml` 文件，然后用文本编辑器（如 Notepad++、VS Code）打开。以下是一个简单的配置文件模板：

```yaml
# 基本设置
port: 7890                # 本地 HTTP 代理端口
socks-port: 7891          # 本地 SOCKS5 代理端口
allow-lan: false          # 是否允许局域网连接，false 表示仅本地使用
mode: rule                # 工作模式：rule（规则分流）、global（全局代理）、direct（直连）
log-level: info           # 日志级别，可选 silent/info/warning/error/debug

# 代理节点列表
proxies:
  - name: "ss1"           # 节点名称，自定义即可
    type: ss              # 协议类型，这里是 Shadowsocks
    server: example.com   # 服务器地址
    port: 8388            # 端口
    cipher: aes-256-gcm   # 加密方式
    password: "yourpassword"  # 密码

# 代理组（用于选择节点）
proxy-groups:
  - name: "auto"          # 组名称
    type: select          # 类型：select 表示手动选择
    proxies:
      - "ss1"             # 这里引用上面定义的节点

# 规则
rules:
  - DOMAIN-SUFFIX,google.com,auto    # 匹配 google.com 的流量走 auto 组
  - DOMAIN-SUFFIX,baidu.com,DIRECT   # 百度直连
  - MATCH,auto                       # 其他未匹配的流量走 auto 组
```

#### **3. 解释配置文件的主要部分**
- **端口设置**：`port` 和 `socks-port` 是 Clash 在本地监听的端口，应用程序通过这些端口连接代理。
- **proxies**：这里列出你的所有代理节点。可以添加多个，比如 `ss1`、`ss2` 等。
- **proxy-groups**：代理组用来组织节点，可以手动选择或设置自动选择（如 `url-test`）。
- **rules**：规则决定哪些流量走代理，哪些直连。可以用域名、IP 等条件匹配。

#### **4. 保存并加载配置文件**
- 将文件保存为 `config.yaml`。
- 打开 Clash 客户端，把文件拖进去，或者在设置中指定文件路径。
- 启动 Clash，检查是否能正常连接。

#### **5. 测试**
- 打开浏览器，设置代理为 `127.0.0.1:7890`（HTTP）或 `127.0.0.1:7891`（SOCKS5）。
- 访问一个被代理的网站（比如 google.com），看看是否成功。

---

#### **进阶配置示例**
如果你有多个节点，想自动选择延迟最低的，或者需要更复杂的规则，可以参考以下示例：

```yaml
port: 7890
socks-port: 7891
allow-lan: false
mode: rule
log-level: info

proxies:
  - name: "ss1"
    type: ss
    server: example1.com
    port: 8388
    cipher: aes-256-gcm
    password: "yourpassword1"
  - name: "ss2"
    type: ss
    server: example2.com
    port: 8388
    cipher: aes-256-gcm
    password: "yourpassword2"

proxy-groups:
  - name: "auto"
    type: url-test        # 自动选择延迟最低的节点
    proxies:
      - "ss1"
      - "ss2"
    url: "http://www.gstatic.com/generate_204"  # 测试延迟的 URL
    interval: 300         # 每 300 秒测试一次

rules:
  - DOMAIN-SUFFIX,google.com,auto
  - DOMAIN-SUFFIX,baidu.com,DIRECT
  - GEOIP,CN,DIRECT      # 中国 IP 直连
  - MATCH,auto           # 其他走 auto 组
```

---

#### **常见问题**
1. **配置文件报错怎么办？**
   - 检查 YAML 格式是否正确，比如缩进必须是 2 个空格，不能用 Tab。
   - 确保节点信息无误。
2. **想添加更多规则怎么办？**
   - 可以参考 Clash 的官方文档，或者告诉我你的需求，我帮你写。
3. **哪里找现成的规则？**
   - 网上有很多开源规则集，比如 GitHub 上，可以通过 Clash 的订阅功能导入。

---



#### 一个clash配置的信息如下

```yaml
port: 7890
socks-port: 7891
allow-lan: true
mode: Rule
log-level: info
external-controller: :9090
proxies:
  - {name: "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*", server: pfxwhz.cscsgsg.xyz, port: 16007, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: "🇬🇧 CN2-V229-英国-1x-NF&BBC*", server: epueyo.gxcvbmj.xyz, port: 58559, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: 🇳🇱 CN2-V238-荷兰-1x-NF*, server: cyjsnl.ghskgvb.xyz, port: 20020, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: 🇨🇦 CN2-V237-加拿大-1x, server: pfxwhz.cscsgsg.xyz, port: 12010, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*", server: fdksxn.kghkjasfh.xyz, port: 12232, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: 🇳🇿 CN2-V339-新西兰-1x-NF*, server: fdksxn.kghkjasfh.xyz, port: 12233, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: 🇸🇬 福利-V345-新加坡-0.1x-15M-NF, server: vdiogsnf.kghkjasfh.xyz, port: 12543, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: 🇭🇰 福利-V234-香港-0.1x-15M-NF, server: vdiogsnf.kghkjasfh.xyz, port: 12544, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
  - {name: 🇭🇰 福利-V114-香港-0.1x-仅限emby, server: vdiogsnf.kghkjasfh.xyz, port: 12545, type: vmess, uuid: 4ed1483a-8bd9-3380-8d28-fa68243292ba, alterId: 0, cipher: auto, tls: false, skip-cert-verify: true, udp: true}
proxy-groups:
  - name: 🎞️ Prime Video
    type: select
    proxies:
      - 🇭🇰 香港
      - 🇺🇸 美国
      - 🇯🇵 日本
      - 🇸🇬 新加坡
      - 🇹🇼 台湾
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🎮👑👑 HBO MAX
    type: select
    proxies:
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - 🇺🇸 CN2-V216-美国-1x-NF
      - 🇺🇸 CN2-V215-美国-2x-NF
      - "🇺🇸 CN2-V213-美国-1x-NF&HBO&Hulu&Disney*"
      - "🇺🇸 CN2-V212-美国-1x-NF&HBO&Hulu*"
      - "🇺🇸 CN2-V217-美国-1x-NF&Disney"
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 📹️ HBOGO Asia
    type: select
    proxies:
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V304-香港-1x-NF&Disney*"
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 💿 AbemaTV
    type: select
    proxies:
      - "🇯🇵 IPLC-V316-日本-0.5x-50M-NF&Abema*"
      - "🇯🇵 IPLC-V315-日本-1x-NF&Abema*（ChatGPT动态解锁测试）"
      - "🇯🇵 IPLC-V353-日本-1x-NF&Abema*"
      - "🇯🇵 IPLC-V356-日本-4x-家宽-NF&Abema*"
      - "🇯🇵 IPLC-V364-日本-0.5x-50M-NF&Abema*"
      - "🇯🇵 IPLC-V365-日本-1x-NF&Abema*（ChatGPT动态解锁测试）"
      - "🇯🇵 IPLC-V366-日本-1x-NF&Abema*（ChatGPT动态解锁测试）"
      - "🇯🇵 IPLC-V240-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
  - name: 🔞 Pornhub
    type: select
    proxies:
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V304-香港-1x-NF&Disney*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🎶 TikTok
    type: select
    proxies:
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - 🇭🇰 CN2-V241-香港-1x
      - "🇸🇬 CN2-V330-新加坡-1x-NF&Disney+*"
      - "🇸🇬 CN2-V347-新加坡-0.5x-NF&Disney+*"
      - 🇺🇸 CN2-V216-美国-1x-NF
      - 🇺🇸 CN2-V215-美国-2x-NF
      - "🇺🇸 CN2-V213-美国-1x-NF&HBO&Hulu&Disney*"
      - "🇺🇸 CN2-V212-美国-1x-NF&HBO&Hulu*"
      - "🇺🇸 CN2-V217-美国-1x-NF&Disney"
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🎧 Spotify
    type: select
    proxies:
      - 🚀 手动切换
      - 🎯 全球直连
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 CN2-V327-香港-1x-HKBN-NF&Disney*"
      - 🇭🇰 CN2-V346-香港-0.6x-HGC-NF*
      - 🇭🇰 CN2-V241-香港-1x
      - "🇸🇬 CN2-V330-新加坡-1x-NF&Disney+*"
      - "🇸🇬 CN2-V347-新加坡-0.5x-NF&Disney+*"
      - 🇺🇸 CN2-V216-美国-1x-NF
      - 🇺🇸 CN2-V215-美国-2x-NF
      - "🇺🇸 CN2-V213-美国-1x-NF&HBO&Hulu&Disney*"
      - "🇺🇸 CN2-V212-美国-1x-NF&HBO&Hulu*"
      - "🇺🇸 CN2-V217-美国-1x-NF&Disney"
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🎮️ 游戏平台
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🤖 ChatGPT、Claude、Gemini、微软AI
    type: select
    proxies:
      - 🚀 手动切换
      - 🇺🇸 美国
      - 🇯🇵 日本
      - 🇸🇬 新加坡
      - 🇹🇼 台湾
      - 🎯 全球直连
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 CN2-V327-香港-1x-HKBN-NF&Disney*"
      - 🇭🇰 CN2-V346-香港-0.6x-HGC-NF*
      - 🇭🇰 CN2-V241-香港-1x
      - "🇸🇬 CN2-V330-新加坡-1x-NF&Disney+*"
      - "🇸🇬 CN2-V347-新加坡-0.5x-NF&Disney+*"
      - 🇺🇸 CN2-V216-美国-1x-NF
      - 🇺🇸 CN2-V215-美国-2x-NF
      - "🇺🇸 CN2-V213-美国-1x-NF&HBO&Hulu&Disney*"
      - "🇺🇸 CN2-V212-美国-1x-NF&HBO&Hulu*"
      - "🇺🇸 CN2-V217-美国-1x-NF&Disney"
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: Ⓜ️ 微软服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V304-香港-1x-NF&Disney*"
      - 🇭🇰 CN2-V321-香港-0.6x-NF
      - 🇭🇰 CN2-V322-香港-0.6x-NF
      - 🇭🇰 CN2-V325-香港-0.6x-NF
      - "🇭🇰 CN2-V326-香港-1x-HKBN-NF&Disney*"
      - "🇭🇰 CN2-V327-香港-1x-HKBN-NF&Disney*"
      - 🇭🇰 CN2-V346-香港-0.6x-HGC-NF*
      - 🇭🇰 CN2-V241-香港-1x
      - "🇸🇬 CN2-V330-新加坡-1x-NF&Disney+*"
      - "🇸🇬 CN2-V347-新加坡-0.5x-NF&Disney+*"
      - 🇺🇸 CN2-V216-美国-1x-NF
      - 🇺🇸 CN2-V215-美国-2x-NF
      - "🇺🇸 CN2-V213-美国-1x-NF&HBO&Hulu&Disney*"
      - "🇺🇸 CN2-V212-美国-1x-NF&HBO&Hulu*"
      - "🇺🇸 CN2-V217-美国-1x-NF&Disney"
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 📲 电报信息
    type: select
    proxies:
      - 🚀 手动切换
      - ♻️ 自动选择
      - 🎯 全球直连
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V304-香港-1x-NF&Disney*"
      - 🇭🇰 CN2-V346-香港-0.6x-HGC-NF*
      - 🇭🇰 CN2-V241-香港-1x
      - "🇸🇬 CN2-V330-新加坡-1x-NF&Disney+*"
      - "🇸🇬 CN2-V347-新加坡-0.5x-NF&Disney+*"
      - 🇺🇸 CN2-V216-美国-1x-NF
      - 🇺🇸 CN2-V215-美国-2x-NF
      - "🇺🇸 CN2-V213-美国-1x-NF&HBO&Hulu&Disney*"
      - "🇺🇸 CN2-V212-美国-1x-NF&HBO&Hulu*"
      - "🇺🇸 CN2-V217-美国-1x-NF&Disney"
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🍎 苹果服务
    type: select
    proxies:
      - 🎯 全球直连
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V304-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V305-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V306-香港-1x-NF&Disney*"
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 📢 谷歌FCM
    type: select
    proxies:
      - 🚀 手动切换
      - 🎯 全球直连
      - ♻️ 自动选择
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🎯 全球直连
    type: select
    proxies:
      - DIRECT
      - 🚀 手动切换
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V304-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V305-香港-1x-NF&Disney*"
      - 🇸🇬 IPLC-V101-新加坡-1x
      - 🇸🇬 IPLC-V102-新加坡-1x
      - 🇰🇷 IPLC-V320-韩国-1x-NF
      - 🇰🇷 IPLC-V230-韩国家宽-1x-NF*
      - "🇺🇸 IPLC-V350-美国-1x-NF&HBO&Disney*"
      - "🇺🇸 IPLC-V351-美国-2x-夏威夷-NF&HBO"
      - "🇺🇸 IPLC-V355-美国-4x-家宽-NF&HBO&Disney*"
      - "🇺🇸 IPLC-V371-美国-1x-NF&HBO&Disney*"
      - "🇺🇸 IPLC-V372-美国-1x-NF&HBO&Disney*"
      - "🇺🇸 IPLC-V373-美国Starlink-8x-NF&HBO&Disney*"
      - "🇺🇸 IPLC-V374-美国家宽-4x-NF&HBO&Disney*"
  
      - 🇺🇸 CN2-V211-美国-1x-NF*
      - "🇯🇵 CN2-V227-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V228-日本-1x-NF&Abema*"
      - "🇯🇵 CN2-V328-日本-0.5x-NF&Abema*"
      - "🇯🇵 CN2-V329-日本-0.5x-NF&Abema*"
      - "🇬🇧 CN2-V229-英国-1x-NF&BBC*"
      - 🇳🇱 CN2-V238-荷兰-1x-NF*
      - 🇨🇦 CN2-V237-加拿大-1x
      - "🇦🇺 CN2-V338-澳大利亚-1x-NF&7plus*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
  - name: 🐟 漏网之鱼
    type: select
    proxies:
      - 🚀 手动切换
      - 🎯 全球直连
      - "🇭🇰 IPLC-V301-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V302-香港-1x-NF&Disney"
      - "🇭🇰 IPLC-V303-香港-1x-NF&Disney*"
      - "🇭🇰 IPLC-V304-香港-1x-NF&Disney*"
      - 🇳🇿 CN2-V339-新西兰-1x-NF*
      - 🇸🇬 福利-V345-新加坡-0.1x-15M-NF
      - 🇭🇰 福利-V234-香港-0.1x-15M-NF
      - 🇭🇰 福利-V114-香港-0.1x-仅限emby
rules:
  - DOMAIN,apple.comscoreresearch.com,🍎 苹果服务
  - DOMAIN-SUFFIX,aaplimg.com,🍎 苹果服务
  - DOMAIN-SUFFIX,akadns.net,🍎 苹果服务
  - DOMAIN-SUFFIX,apple-cloudkit.com,🍎 苹果服务
  - DOMAIN-SUFFIX,apple-dns.net,🍎 苹果服务
  - DOMAIN-SUFFIX,apple-mapkit.com,🍎 苹果服务
  - DOMAIN-SUFFIX,apple.co,🍎 苹果服务
  - DOMAIN-SUFFIX,apple.com,🍎 苹果服务
  - DOMAIN-SUFFIX,apple.com.cn,🍎 苹果服务
  - DOMAIN-SUFFIX,apple.news,🍎 苹果服务
  - DOMAIN-SUFFIX,appstore.com,🍎 苹果服务
  - DOMAIN-SUFFIX,cdn-apple.com,🍎 苹果服务
  - DOMAIN-SUFFIX,crashlytics.com,🍎 苹果服务
  - DOMAIN-SUFFIX,icloud-content.com,🍎 苹果服务
  - DOMAIN-SUFFIX,icloud.com,🍎 苹果服务
  - DOMAIN-SUFFIX,icloud.com.cn,🍎 苹果服务
  - DOMAIN-SUFFIX,itunes.com,🍎 苹果服务
  - IP-CIDR,13.245.112.0/23,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.245.114.0/24,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.245.127.232/30,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.245.155.128/27,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.245.155.224/27,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.245.166.128/29,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.245.166.176/29,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.248.224.0/21,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.248.232.0/23,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.250.186.0/28,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.250.186.16/29,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.250.186.128/26,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.250.186.192/28,🎥 NETFLIX,no-resolve
  - IP-CIDR,13.250.186.208/29,🎥 NETFLIX,no-resolve
  - IP-CIDR,15.152.10.0/24,🎥 NETFLIX,no-resolve
  - IP-CIDR,15.152.24.0/26,🎥 NETFLIX,no-resolve
  - IP-CIDR,15.152.24.128/29,🎥 NETFLIX,no-resolve
  - IP-CIDR,15.160.55.112/29,🎥 NETFLIX,no-resolve
  - IP-CIDR,15.161.66.0/25,🎥 NETFLIX,no-resolve
  - IP-CIDR,15.161.66.128/26,🎥 NETFLIX,no-resolve
  - IP-CIDR,15.161.135.64/26,🎥 NETFLIX,no-resolve
  - DOMAIN-SUFFIX,dlandroid.rcv.sandai.net,🚀 手动切换
  - DOMAIN-SUFFIX,hub5idx.v6.shub.sandai.net,🚀 手动切换
  - DOMAIN-SUFFIX,hub5pn.wap.sandai.net,🚀 手动切换
  - DOMAIN-SUFFIX,hub5pnc.sandai.net,🚀 手动切换
  - DOMAIN-SUFFIX,hub5pr.v6.phub.sandai.net,🚀 手动切换
  - DOMAIN-SUFFIX,hubciddata.sandai.net,🚀 手动切换
  - DOMAIN-KEYWORD,mypikpak,🚀 手动切换
  - DOMAIN-SUFFIX,acl4.ssr,🎯 全球直连
  - DOMAIN-SUFFIX,ip6-localhost,🎯 全球直连
  - IP-CIDR6,::1/128,🎯 全球直连,no-resolve
  - IP-CIDR6,fc00::/7,🎯 全球直连,no-resolve
  - DOMAIN,instant.arubanetworks.com,🎯 全球直连
  - DOMAIN,setmeup.arubanetworks.com,🎯 全球直连
  - DOMAIN,router.asus.com,🎯 全球直连
  - DOMAIN,www.asusrouter.com,🎯 全球直连
  - DOMAIN-SUFFIX,hiwifi.com,🎯 全球直连
  - DOMAIN-SUFFIX,leike.cc,🎯 全球直连
  - DOMAIN-SUFFIX,cm.steampowered.com,🎯 全球直连
  - DOMAIN-SUFFIX,steamchina.com,🎯 全球直连
  - IP-CIDR,8.128.0.0/10,🎯 全球直连,no-resolve
  - DOMAIN-SUFFIX,smtp,🎯 全球直连
  - DOMAIN-KEYWORD,aria2,🎯 全球直连
  - PROCESS-NAME,Weiyun.exe,🎯 全球直连
  - PROCESS-NAME,baidunetdisk.exe,🎯 全球直连
  - DOMAIN,alt1-mtalk.google.com,📢 谷歌FCM
  - DOMAIN,alt8-mtalk.google.com,📢 谷歌FCM
  - DOMAIN,mtalk.google.com,📢 谷歌FCM
  - IP-CIDR,64.233.177.188/32,📢 谷歌FCM,no-resolve
  - IP-CIDR,64.233.186.188/32,📢 谷歌FCM,no-resolve
  - GEOIP,CN,🎯 全球直连
  - MATCH,🐟 漏网之鱼

```