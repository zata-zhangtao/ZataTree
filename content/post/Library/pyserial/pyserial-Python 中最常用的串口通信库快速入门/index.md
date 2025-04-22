---
title: pyserial-Python 中最常用的串口通信库快速入门
description: ""
date: 2025-04-03T10:15:25+08:00
image: images/index/index.svg
categories:
    - Library
tags:
    - pyserial
---


### 1. 安装 pyserial
首先，你需要安装 `pyserial` 库。可以通过 pip 安装：
```bash
pip install pyserial
```

---

### 2. 基本概念
串口通信（Serial Communication）是通过串行端口（如 USB 转串口设备、COM 端口等）进行数据传输的一种方式。常见用途包括与微控制器（如 Arduino）、传感器或其他硬件设备通信。

在 Python 中，`pyserial` 提供了一个简单的接口来操作串口。

---

### 3. 基础代码示例
以下是一个简单的示例，展示如何打开串口、发送数据和接收数据：

```python
import serial
import time

# 配置串口参数
port = 'COM3'  # Windows 示例，Linux/Mac 可能是 '/dev/ttyUSB0'
baudrate = 9600  # 波特率，根据设备设置
timeout = 1  # 读取超时时间（秒）

# 初始化串口
try:
    ser = serial.Serial(
        port=port,
        baudrate=baudrate,
        timeout=timeout
    )
    print(f"已连接到 {port}")
except serial.SerialException as e:
    print(f"连接失败: {e}")
    exit()

# 发送数据
message = "Hello, Serial!\n"
ser.write(message.encode('utf-8'))  # 将字符串编码为字节并发送
print(f"已发送: {message.strip()}")

# 接收数据
time.sleep(1)  # 等待一秒，确保有数据返回
if ser.in_waiting > 0:  # 检查是否有数据在缓冲区
    data = ser.readline().decode('utf-8').strip()  # 读取一行并解码
    print(f"收到: {data}")

# 关闭串口
ser.close()
print("串口已关闭")
```

---

### 4. 代码解释
- **`serial.Serial()`**: 创建一个串口对象，参数包括端口号、波特率和超时时间。
- **`port`**: 串口名称。Windows 上是 `COMx`（如 `COM3`），Linux/Mac 上是 `/dev/ttyUSBx` 或 `/dev/ttySx`。
- **`baudrate`**: 数据传输速率，常见值有 9600、115200 等，需与设备一致。
- **`timeout`**: 读取超时，避免程序无限等待。
- **`write()`**: 发送数据，需将字符串编码为字节（如 `encode('utf-8')`）。
- **`readline()`**: 读取一行数据（以换行符 `\n` 结束）。
- **`in_waiting`**: 检查缓冲区是否有数据。

---

### 5. 如何找到串口号
在连接设备后，你需要知道设备的串口号。可以用以下代码列出所有可用串口：
```python
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"端口: {port.device}, 描述: {port.description}")
```

运行后会显示类似：
```
端口: COM3, 描述: USB Serial Port (COM3)
端口: COM1, 描述: Communications Port (COM1)
```
根据描述选择正确的端口。

---

### 6. 常见问题与解决
- **端口被占用**: 确保没有其他程序（如 Arduino IDE 的串口监视器）占用端口。
- **波特率不匹配**: 确认波特率与设备一致。
- **无数据返回**: 检查设备是否正确连接并发送数据。

---

### 7. 高级示例：持续读取数据
以下是一个循环读取串口数据的示例：
```python
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            print(f"收到: {data}")
        time.sleep(0.1)  # 短暂休眠，避免占用过多 CPU
except KeyboardInterrupt:
    print("程序终止")
finally:
    ser.close()
    print("串口已关闭")
```

---

### 8. 与硬件交互示例（如 Arduino）
假设 Arduino 运行以下代码：
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String msg = Serial.readString();
    Serial.println("收到: " + msg);
  }
}
```

Python 端可以这样与之交互：
```python
import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # 等待 Arduino 重启

ser.write("Test\n".encode('utf-8'))
time.sleep(1)

if ser.in_waiting > 0:
    response = ser.readline().decode('utf-8').strip()
    print(response)  # 输出: 收到: Test

ser.close()
```

---

### 9. 更多资源
- 官方文档: [pyserial 文档](https://pyserial.readthedocs.io/)
- 示例项目: 搜索 “Python serial Arduino” 可找到更多与硬件交互的案例。

