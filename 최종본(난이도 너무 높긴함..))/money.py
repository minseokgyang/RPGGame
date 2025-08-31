import random
import player

class Money:
    def __init__(self):
        self.gold = 0

    def earn_from_monster(self):
        earned = random.randint(3, 7)
        self.gold += earned
        print(f"[GOLD] 몬스터 처치! {earned} 골드를 얻었습니다. (총 {self.gold} 골드)")

    def spend(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            print(f"[SHOP] {amount} 골드를 사용했습니다. (남은 골드: {self.gold})")
            return True
        else:
            print("[ERROR] 골드가 부족합니다!")
            return False
