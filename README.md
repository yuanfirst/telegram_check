# Telegram 自动签到系统 - 快速入门
##  PS：所有代码包括指导文件全部由cursor生成，本人只做测试验证通过后存档。
##  主要功能包括：群组chat_id自动获取，自动发送签到命令至机器人或群组。


## 🚀 5分钟快速上手

### 第一步：安装依赖
```bash
pip install telethon
```

### 第二步：配置API信息
编辑 `qiandao.py` 文件，填入您的Telegram API信息：
```python
API_ID = 您的API_ID
API_HASH = "您的API_HASH"
PHONE_NUMBER = "您的手机号"
```

### 第三步：首次运行
```bash
python qiandao.py
```
首次运行会要求输入验证码，输入后即可完成身份验证。

## 🎯 常用命令

| 命令 | 功能 |
|------|------|
| `python qiandao.py` | 执行签到 |
| `python qiandao.py --search-groups "关键词"` | 搜索群组 |
| `python group_manager.py` | 启动群组管理工具 |
| `python test_group.py` | 测试群组访问 |

## 🔍 快速查找群组

如果您有几百个群组，想要快速找到特定群组：

```bash
# 搜索包含"签到"关键词的群组
python qiandao.py --search-groups "签到"

# 搜索包含"VPN"关键词的群组  
python qiandao.py --search-groups "VPN"
```

## ⚙️ 添加新群组

### 方法1：使用搜索功能
```bash
python qiandao.py --search-groups "群组名称关键词"
```

### 方法2：使用交互式工具
```bash
python group_manager.py
# 选择 "1. 搜索群组"
# 输入关键词
# 选择要添加的群组
```

## 📝 配置文件说明

### 机器人配置
```python
TARGET_BOTS = [
    {"username": "@机器人用户名", "message": "/签到命令"},
]
```

### 群组配置
```python
TARGET_GROUPS = [
    {"chat_id": -100xxxxxxxxx, "message": "/签到命令"},
]
```

## ⚠️ 常见问题

### Q: 群组ID在哪里找？
A: 使用搜索功能：
```bash
python qiandao.py --search-groups "群组名称"
```

### Q: 提示"群组不存在"怎么办？
A: 
1. 确认已加入该群组
2. 使用搜索功能找到正确的群组ID
3. 检查群组名称是否正确

### Q: 如何设置定时签到？
A: 
- **Linux/Mac**: 使用crontab设置定时任务
- **Windows**: 使用任务计划程序

## 📞 获取帮助

```bash
# 查看所有可用命令
python qiandao.py --help

# 查看详细文档
cat README.md
```

---

**提示**: 首次使用建议先测试单个群组，确认无误后再添加更多群组。 
