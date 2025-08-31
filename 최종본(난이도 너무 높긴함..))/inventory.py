import random


class Inventory:
    def __init__(self):
        self.items = {"마나물약": 0, "회복약": 0, "랜덤스탯티켓": 0}

    def add_item(self, item_name, amount=1):
        if item_name in self.items:
            self.items[item_name] += amount
        else:
            self.items[item_name] = amount
        print(f"[INVENTORY] {item_name} {amount}개가 추가되었습니다.")

    def use_item(self, player, item_name):
        if self.items.get(item_name, 0) > 0:
            if item_name == "마나물약":
                player.MP = min(player.max_MP, player.MP + 10)
                print("[ITEM] 마나가 10 회복되었습니다.")
            elif item_name == "회복약":
                player.HP = min(player.max_HP, player.HP + 20)
                print("[ITEM] 체력이 20 회복되었습니다.")
            elif item_name == "랜덤스탯티켓":
                stat = random.choice(["str", "dex", "int", "luck"])
                amount = random.randint(-3, 10)
                setattr(player, stat, getattr(player, stat) + amount)
                print(f"[ITEM] {stat} 능력이 {amount} 만큼 증가했다")
            self.items[item_name] -= 1
        else:
            print("[ERROR] 해당 아이템이 없다")

    def show(self, player):
        while True:
            print("=== 인벤토리 ===")
            item_list = list(self.items.keys()) 
            for idx, key in enumerate(item_list, start=1):  
                print(f"{idx}. {key}: {self.items[key]}개") 
            print(f"{len(item_list)+1}. 나가기")   

            try:
                choice = int(input("사용할 아이템 번호를 입력하세요: ")) 
                if 1 <= choice <= len(item_list):  
                    self.use_item(player, item_list[choice-1])  
                    return
                elif choice == len(item_list)+1:  
                    return 
                else:
                    print("[ERROR] 잘못된 번호입니다.")
            except:
                print("[ERROR] 숫자를 입력해주세요.")
