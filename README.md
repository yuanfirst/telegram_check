# Telegram 自动签到系统

这是一个功能完整的Telegram自动签到系统，支持向多个机器人和群组发送签到消息。

## 📋 功能特性

- ✅ 支持向多个Telegram机器人发送签到消息
- ✅ 支持向多个Telegram群组发送签到消息
- ✅ 智能群组搜索和管理功能
- ✅ 防止重复签到（每日一次）
- ✅ 详细的日志记录
- ✅ 交互式群组管理工具
- ✅ 配置自动保存和加载

## 🚀 快速开始

### 1. 环境准备

确保您的系统已安装Python 3.7+和必要的依赖：

```bash
pip install telethon
```

### 2. 配置设置

在 `qiandao.py` 文件中配置您的Telegram API信息：

```python
API_ID = 24630859  # 您的 API ID
API_HASH = "9d05528948e3cca656a35ac7030c1fb3"  # 您的 API Hash
PHONE_NUMBER = "+642040610977"  # 您的手机号
```

### 3. 首次运行

首次运行时会要求您输入验证码进行身份验证：

```bash
python qiandao.py
```

## 📁 文件说明

| 文件名 | 功能描述 |
|--------|----------|
| `qiandao.py` | 主签到脚本 |
| `group_manager.py` | 交互式群组管理工具 |
| `test_group.py` | 群组访问测试工具 |
| `saved_groups.json` | 保存的群组配置（自动生成） |
| `sign_record.txt` | 签到记录文件（自动生成） |
| `qiandao.log` | 运行日志文件（自动生成） |

## 🛠️ 使用方法

### 基础签到功能

#### 执行签到
```bash
python qiandao.py
```

#### 查看帮助
```bash
python qiandao.py --help
```

### 群组管理功能

#### 列出所有群组
```bash
python qiandao.py --list-groups
```

#### 搜索特定群组
```bash
python qiandao.py --search-groups "关键词"
```

#### 交互式群组管理
```bash
python group_manager.py
```

### 群组测试功能

#### 测试群组访问权限
```bash
python test_group.py
```

## 🔧 配置说明

### 机器人配置

在 `qiandao.py` 中配置目标机器人：

```python
TARGET_BOTS = [
    {"username": "@bizuiba_bot", "message": "/checkin"},
    {"username": "@Zonesgk_bot", "message": "/qd"},
    {"username": "@haowangshegongkubot", "message": "/sign"},
    {"username": "@jiux_vpn_bot", "message": "/checkin"},
    {"username": "@share_mjj_bot", "message": "/checkin"},
]
```

### 群组配置

在 `qiandao.py` 中配置目标群组：

```python
TARGET_GROUPS = [
    {"chat_id": -1001849751823, "message": "/checkin"},
]
```

## 🎯 群组管理工具详解

### 启动交互式管理工具

```bash
python group_manager.py
```

### 功能菜单

1. **搜索群组** - 通过关键词快速查找群组
2. **查看已保存的群组** - 显示当前配置的群组
3. **添加群组到配置** - 将搜索到的群组添加到配置
4. **移除群组** - 从配置中删除不需要的群组
5. **生成配置代码** - 生成可直接使用的配置代码
6. **退出** - 退出管理工具

### 使用示例

#### 搜索群组
```
请选择操作 (1-6): 1
请输入搜索关键词: 签到
```

#### 添加群组到配置
```
是否要添加群组到配置? (y/n): y
请输入要添加的群组编号: 1
```

## 📝 日志和记录

### 日志文件
- **位置**: `qiandao.log`
- **内容**: 所有签到操作的详细记录
- **格式**: 时间戳 + 操作类型 + 详细信息

### 签到记录
- **位置**: `sign_record.txt`
- **内容**: 记录每日签到状态
- **格式**: YYYY-MM-DD

### 群组配置
- **位置**: `saved_groups.json`
- **内容**: 保存的群组配置信息
- **格式**: JSON格式

## ⚠️ 注意事项

### 安全提醒
1. **API密钥安全**: 请妥善保管您的API_ID和API_HASH
2. **手机号隐私**: 建议使用虚拟手机号进行测试
3. **群组权限**: 确保您在目标群组中有发送消息的权限

### 使用限制
1. **频率限制**: Telegram有消息发送频率限制，请合理使用
2. **群组限制**: 某些群组可能禁用了机器人或限制了消息发送
3. **账号安全**: 避免频繁的自动化操作，以免账号被限制

### 故障排除

#### 常见错误及解决方案

**错误**: `Could not find the input entity for PeerChannel`
**原因**: 群组ID不正确或未加入该群组
**解决**: 
1. 使用 `python qiandao.py --search-groups "关键词"` 查找正确群组
2. 确认已加入目标群组
3. 验证群组ID是否正确

**错误**: `A wait of X seconds is required`
**原因**: 消息发送频率过高
**解决**: 等待指定时间后重试

**错误**: `You are not a member of this chat`
**原因**: 未加入目标群组
**解决**: 先加入目标群组

## 🔄 自动化部署

### 定时任务设置

#### Linux/Mac (Cron)
```bash
# 编辑crontab
crontab -e

# 添加每日签到任务（每天上午9点执行）
0 9 * * * cd /path/to/qiandao && python qiandao.py
```

#### Windows (任务计划程序)
1. 打开任务计划程序
2. 创建基本任务
3. 设置触发器为每日执行
4. 设置操作为运行 `python qiandao.py`

### 脚本权限设置
```bash
chmod +x qiandao.py
chmod +x group_manager.py
```

## 📊 监控和维护

### 日志监控
定期检查 `qiandao.log` 文件，确保签到操作正常执行。

### 配置更新
当需要添加新的群组或机器人时：
1. 使用群组管理工具搜索并添加新群组
2. 或直接编辑配置文件

### 性能优化
- 定期清理旧的日志文件
- 监控API调用频率
- 及时更新依赖包

## 🤝 贡献和支持

如果您在使用过程中遇到问题或有改进建议，请：

1. 检查日志文件获取详细错误信息
2. 确认配置是否正确
3. 验证网络连接和API权限

## 📄 许可证

本项目仅供学习和个人使用，请遵守Telegram的使用条款和相关法律法规。

---

**最后更新**: 2024年7月28日
**版本**: 1.0.0 