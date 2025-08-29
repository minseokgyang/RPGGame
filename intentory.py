class inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        try:
            self.items.append(item)
            print(f"[인벤토리] {item.name}이(가) 추가되었습니다.")
        except Exception as e:
            print(f"[오류] 인벤토리에 추가 중에 문제가 발생하였습니다.")

    def use_item(self, player, item_name: str):
        try:
            for i, item in enumerate(self.items):
                if item.name.lower() == item_name.lower():
                    if item.effect == "mana":
                        player.mana = min(player.max_mana, player.mana + item.value)
                        print(f"[아이템 사용] 마나 {item.value} 회복 -> {player.mana}/{player.max_mana}")
                    elif item.effect == "hp":
                        player.hp = min(player.max_hp, player.hp + item.value)
                        print(f"[아이템 사용] 체력{item.value} 회복 -> {player.health}/{player.max_hp}")
                    elif item.effect == "exp":
                        player.add_exp(item.value)
                    elif item.effect == "stat":
                        stat_to_increase = "str"
                        player.stats[stat_to_increase] += item.value
                        print(f"[아이템 사용] 힘 {item.value: +} 증가 -> {player.stats}")
                    self.items.pop(i)
                    
                    return True
            print("[인벤토리] 해당 아이템은 존재하지않습니다.")
            return False
        except Exception as e:
            print(f"[오류] 아이템 사용 중 문제가 발생하였습니다: {e}")
            return False
    
    def show(self):
        try:
            if not self.items:
                print("[인벤토리] 비어있음")
            else:
                print("[인벤토리]")
                for i, item in enumerate(self.items, 1):
                    print(f" {i}. {item}")
        except Exception as e:
            print(f"[오류] 인벤토리를 확인 중 문제가 발생하였습니다. {e}")