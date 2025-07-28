from telethon import TelegramClient
import asyncio
import json
import os

# 使用相同的配置
API_ID = 24630859
API_HASH = "9d05528948e3cca656a35ac7030c1fb3"
GROUPS_FILE = "saved_groups.json"

class GroupManager:
    def __init__(self):
        self.client = None
        self.saved_groups = self.load_saved_groups()
    
    def load_saved_groups(self):
        """加载保存的群组配置"""
        if os.path.exists(GROUPS_FILE):
            try:
                with open(GROUPS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_groups(self):
        """保存群组配置"""
        with open(GROUPS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.saved_groups, f, ensure_ascii=False, indent=2)
    
    async def start_client(self):
        """启动客户端"""
        self.client = TelegramClient("sign_session", API_ID, API_HASH)
        await self.client.start()
    
    async def search_groups(self, keyword):
        """搜索群组"""
        if not self.client:
            await self.start_client()
        
        print(f"正在搜索包含关键词 '{keyword}' 的群组...")
        found_groups = []
        
        try:
            async for dialog in self.client.iter_dialogs():
                if dialog.is_group or dialog.is_channel:
                    group_name = dialog.name.lower()
                    keyword_lower = keyword.lower()
                    
                    if keyword_lower in group_name:
                        found_groups.append({
                            'name': dialog.name,
                            'id': dialog.id,
                            'type': '频道' if dialog.is_channel else '群组'
                        })
            
            return found_groups
        except Exception as e:
            print(f"搜索群组时发生错误: {str(e)}")
            return []
    
    def display_groups(self, groups, title="搜索结果"):
        """显示群组列表"""
        if not groups:
            print(f"❌ {title}为空")
            return
        
        print(f"\n{title} ({len(groups)} 个群组):")
        print("=" * 60)
        for i, group in enumerate(groups, 1):
            print(f"{i}. 群组名称: {group['name']}")
            print(f"   群组ID: {group['id']}")
            print(f"   群组类型: {group['type']}")
            print("-" * 40)
    
    def add_group_to_config(self, group):
        """添加群组到配置"""
        group_config = {
            "chat_id": group['id'],
            "message": "/checkin",
            "name": group['name']
        }
        
        # 检查是否已存在
        for saved_group in self.saved_groups:
            if saved_group['chat_id'] == group['id']:
                print(f"⚠️ 群组 '{group['name']}' 已存在于配置中")
                return False
        
        self.saved_groups.append(group_config)
        self.save_groups()
        print(f"✅ 已添加群组 '{group['name']}' 到配置")
        return True
    
    def show_saved_groups(self):
        """显示已保存的群组"""
        if not self.saved_groups:
            print("❌ 没有保存的群组")
            return
        
        print("\n已保存的群组:")
        print("=" * 60)
        for i, group in enumerate(self.saved_groups, 1):
            print(f"{i}. 群组名称: {group.get('name', '未知')}")
            print(f"   群组ID: {group['chat_id']}")
            print(f"   签到消息: {group['message']}")
            print("-" * 40)
    
    def remove_group(self, index):
        """移除群组"""
        if 1 <= index <= len(self.saved_groups):
            removed_group = self.saved_groups.pop(index - 1)
            self.save_groups()
            print(f"✅ 已移除群组 '{removed_group.get('name', '未知')}'")
        else:
            print("❌ 无效的索引")
    
    def generate_config_code(self):
        """生成配置代码"""
        if not self.saved_groups:
            print("❌ 没有保存的群组")
            return
        
        print("\n生成的配置代码:")
        print("=" * 60)
        print("TARGET_GROUPS = [")
        for group in self.saved_groups:
            print(f"    {{\"chat_id\": {group['chat_id']}, \"message\": \"{group['message']}\"}},")
        print("]")
        print("=" * 60)

async def interactive_mode():
    """交互式模式"""
    manager = GroupManager()
    
    while True:
        print("\n" + "="*50)
        print("Telegram群组管理工具")
        print("="*50)
        print("1. 搜索群组")
        print("2. 查看已保存的群组")
        print("3. 添加群组到配置")
        print("4. 移除群组")
        print("5. 生成配置代码")
        print("6. 退出")
        print("-"*50)
        
        choice = input("请选择操作 (1-6): ").strip()
        
        if choice == "1":
            keyword = input("请输入搜索关键词: ").strip()
            if keyword:
                groups = await manager.search_groups(keyword)
                manager.display_groups(groups)
                
                if groups:
                    add_choice = input("\n是否要添加群组到配置? (y/n): ").strip().lower()
                    if add_choice == 'y':
                        try:
                            index = int(input("请输入要添加的群组编号: ")) - 1
                            if 0 <= index < len(groups):
                                manager.add_group_to_config(groups[index])
                            else:
                                print("❌ 无效的编号")
                        except ValueError:
                            print("❌ 请输入有效的数字")
        
        elif choice == "2":
            manager.show_saved_groups()
        
        elif choice == "3":
            manager.show_saved_groups()
            if manager.saved_groups:
                try:
                    index = int(input("请输入要移除的群组编号: "))
                    manager.remove_group(index)
                except ValueError:
                    print("❌ 请输入有效的数字")
        
        elif choice == "4":
            manager.show_saved_groups()
            if manager.saved_groups:
                try:
                    index = int(input("请输入要移除的群组编号: "))
                    manager.remove_group(index)
                except ValueError:
                    print("❌ 请输入有效的数字")
        
        elif choice == "5":
            manager.generate_config_code()
        
        elif choice == "6":
            print("👋 再见!")
            break
        
        else:
            print("❌ 无效的选择，请重新输入")

if __name__ == "__main__":
    asyncio.run(interactive_mode()) 
