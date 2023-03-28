# 🤖 ASimpleGPTQtDemo

ASimpleGPTQtDemo 是一个基于 Pyqt5 的 GPT 工具，主要运用了官方 Demo，实现了聊天和图片生成的功能。

## 功能介绍

- 聊天功能：可以输入问题，通过 GPT 模型生成回答。
- 图片生成功能：可以输入一段文字，通过 GPT 模型生成对应的图片。

## 安装

1. 克隆本项目到本地：

```bash
git clone https://github.com/nixgnauhcuy/ASimpleGPTQtDemo.git
```

2. 安装依赖：

```bash
cd SimpleGPTQtDemo/
pip install -r requirements.txt
```

3. 运行程序：

```bash
python main.py
```

## 使用说明

使用时，请先填入自己 OpenAi 账户的 `API_KEY`，由于用的是官方接口，国内需要代理才能访问。


- **聊天功能**

    1. 在对话区输入框中输入问题；
    2. 点击“发送”按钮；
    3. 等待程序生成回答。

- **图片生成功能**

    1. 在图片生成区输入框中输入一段文字；
    2. 点击“生成”按钮；
    3. 等待程序生成对应的图片。

## 效果预览

### 出错

![Error](/assert/Error.gif)

### 对话

![Chat](/assert/Chat.gif)

### 生成图片

![creatImg](/assert/creatImg.gif)

