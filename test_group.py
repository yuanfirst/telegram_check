from telethon import TelegramClient
import asyncio

# 使用相同的配置
API_ID = ****
API_HASH = "****"
TARGET_GROUP_ID = -****

async def test_group_access():
    """测试群组访问权限"""
    async with TelegramClient("sign_session", API_ID, API_HASH) as client:
        await client.start()
        
        print(f"正在测试群组ID: {TARGET_GROUP_ID}")
        
        try:
            # 尝试获取群组信息
            entity = await client.get_entity(TARGET_GROUP_ID)
            group_title = getattr(entity, 'title', '未知群组')
            group_type = '频道' if entity.broadcast else '群组'
            
            print(f"✅ 成功访问群组!")
            print(f"群组名称: {group_title}")
            print(f"群组类型: {group_type}")
            print(f"群组ID: {entity.id}")
            
            # 尝试发送测试消息
            try:
                await client.send_message(entity, "/checkin")
                print("✅ 成功发送签到消息!")
            except Exception as e:
                print(f"❌ 发送消息失败: {str(e)}")
                
        except ValueError as e:
            print(f"❌ 群组不存在或您未加入该群组: {str(e)}")
            print("\n建议:")
            print("1. 确认您已经加入该群组")
            print("2. 确认群组ID是否正确")
            print("3. 运行 'python qiandao.py --list-groups' 查看您加入的群组")
            
        except Exception as e:
            print(f"❌ 访问群组时发生错误: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_group_access()) 
