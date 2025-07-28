from telethon import TelegramClient
import asyncio
import logging
import os
from datetime import datetime

# ====== 配置区 ======
API_ID = 24630859  # 你的 API ID
API_HASH = "9d05528948e3cca656a35ac7030c1fb3"  # 你的 API Hash
TARGET_BOTS = [
    {"username": "@bizuiba_bot", "message": "/checkin"},
    {"username": "@Zonesgk_bot", "message": "/qd"},
    {"username": "@haowangshegongkubot", "message": "/sign"},
    {"username": "@jiux_vpn_bot", "message": "/checkin"},
    {"username": "@share_mjj_bot", "message": "/checkin"},
]
TARGET_GROUPS = [
    {"chat_id": -1001849751823, "message": "/checkin"},
]
PHONE_NUMBER = "+642040610977"  # 你的手机号
SIGN_RECORD_FILE = "sign_record.txt"

# 日志配置
logging.basicConfig(
    filename="qiandao.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

async def verify_and_send_group_messages():
    """验证群组并发送签到消息"""
    async with TelegramClient("sign_session", API_ID, API_HASH) as client:
        await client.start()
        
        # 向群组发送签到消息
        for group in TARGET_GROUPS:
            try:
                # 尝试获取群组信息
                entity = await client.get_entity(group["chat_id"])
                group_title = getattr(entity, 'title', '未知群组')
                
                # 发送消息
                await client.send_message(entity, group["message"])
                msg = f"✅ 已向群组 '{group_title}' ({group['chat_id']}) 发送：{group['message']}"
                print(msg)
                logging.info(msg)
            except ValueError as e:
                msg = f"❌ 群组 {group['chat_id']} 不存在或您未加入该群组"
                print(msg)
                logging.error(msg)
            except Exception as e:
                msg = f"❌ 向群组 {group['chat_id']} 发送失败：{str(e)[:100]}"
                print(msg)
                logging.error(msg)

async def send_sign_messages():
    """发送签到消息"""
    async with TelegramClient("sign_session", API_ID, API_HASH) as client:
        await client.start()
        
        # 向机器人发送签到消息
        for bot in TARGET_BOTS:
            try:
                entity = await client.get_entity(bot["username"])
                await client.send_message(entity, bot["message"])
                msg = f"✅ 已向机器人 {bot['username']} 发送：{bot['message']}"
                print(msg)
                logging.info(msg)
            except Exception as e:
                msg = f"❌ 向机器人 {bot['username']} 发送失败：{str(e)[:50]}"
                print(msg)
                logging.error(msg)
        
        # 向群组发送签到消息
        for group in TARGET_GROUPS:
            try:
                # 尝试获取群组信息
                entity = await client.get_entity(group["chat_id"])
                group_title = getattr(entity, 'title', '未知群组')
                
                # 发送消息
                await client.send_message(entity, group["message"])
                msg = f"✅ 已向群组 '{group_title}' ({group['chat_id']}) 发送：{group['message']}"
                print(msg)
                logging.info(msg)
            except ValueError as e:
                msg = f"❌ 群组 {group['chat_id']} 不存在或您未加入该群组"
                print(msg)
                logging.error(msg)
            except Exception as e:
                msg = f"❌ 向群组 {group['chat_id']} 发送失败：{str(e)[:100]}"
                print(msg)
                logging.error(msg)

async def search_groups_by_keyword(keyword):
    """通过关键词搜索群组"""
    async with TelegramClient("sign_session", API_ID, API_HASH) as client:
        await client.start()
        
        print(f"正在搜索包含关键词 '{keyword}' 的群组...")
        found_groups = []
        
        try:
            async for dialog in client.iter_dialogs():
                if dialog.is_group or dialog.is_channel:
                    group_name = dialog.name.lower()
                    keyword_lower = keyword.lower()
                    
                    # 检查群组名称是否包含关键词
                    if keyword_lower in group_name:
                        found_groups.append({
                            'name': dialog.name,
                            'id': dialog.id,
                            'type': '频道' if dialog.is_channel else '群组'
                        })
            
            if found_groups:
                print(f"\n找到 {len(found_groups)} 个匹配的群组:")
                print("=" * 60)
                for i, group in enumerate(found_groups, 1):
                    print(f"{i}. 群组名称: {group['name']}")
                    print(f"   群组ID: {group['id']}")
                    print(f"   群组类型: {group['type']}")
                    print("-" * 40)
            else:
                print(f"❌ 未找到包含关键词 '{keyword}' 的群组")
                
        except Exception as e:
            print(f"搜索群组时发生错误: {str(e)}")

async def list_my_groups():
    """列出用户加入的所有群组"""
    async with TelegramClient("sign_session", API_ID, API_HASH) as client:
        await client.start()
        
        print("正在获取您加入的群组列表...")
        try:
            async for dialog in client.iter_dialogs():
                if dialog.is_group or dialog.is_channel:
                    print(f"群组名称: {dialog.name}")
                    print(f"群组ID: {dialog.id}")
                    print(f"群组类型: {'频道' if dialog.is_channel else '群组'}")
                    print("-" * 50)
        except Exception as e:
            print(f"获取群组列表失败: {str(e)}")

def has_signed_today():
    today_str = datetime.now().strftime("%Y-%m-%d")
    if os.path.exists(SIGN_RECORD_FILE):
        with open(SIGN_RECORD_FILE, "r", encoding="utf-8") as f:
            last_date = f.read().strip()
            return last_date == today_str
    return False

def mark_signed_today():
    today_str = datetime.now().strftime("%Y-%m-%d")
    with open(SIGN_RECORD_FILE, "w", encoding="utf-8") as f:
        f.write(today_str)

def main():
    import sys
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] == "--list-groups":
            print("正在列出您加入的群组...")
            asyncio.run(list_my_groups())
            return
        elif sys.argv[1] == "--search-groups" and len(sys.argv) > 2:
            keyword = sys.argv[2]
            asyncio.run(search_groups_by_keyword(keyword))
            return
        elif sys.argv[1] == "--help":
            print("使用方法:")
            print("  python qiandao.py                    # 执行签到")
            print("  python qiandao.py --list-groups      # 列出所有群组")
            print("  python qiandao.py --search-groups <关键词>  # 搜索群组")
            print("  python qiandao.py --help             # 显示帮助")
            return
    
    # 启用签到检测，防止重复签到
    if has_signed_today():
        msg = "⚠️ 今天已经签到过，跳过本次签到。"
        print(msg)
        logging.info(msg)
        return
    asyncio.run(send_sign_messages())
    mark_signed_today()

if __name__ == "__main__":
    main()