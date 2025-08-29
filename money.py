import random

class money:
    def __init__(self):
        self.gold = 0

    def earn_from_monster(self):
        try:
            drop = random.randint(3, 7)
            self.gold += drop
            print(f"골드획득 + {drop} (현재골드 : {self.gold})")
            return drop
        
        except Exception as e:
            print(f"[오류] 골드 획득 중 문제가 발생했습니다: {e}")
            return 0
    
    def spend(self, amount: int) -> bool:
        try:
            if self.gold >= amount:
                self.gold -= amount
                print(f"[골드지출] -{amount}(현재 골드 : {self.gold})")
                return True
            else:
                print("골드가 부족합니다.")
                return False
        except Exception as e:
            print(f"[오류] 골드 지출 중 문제가 발생하였습니다. {e}")
            return False
    
    def __str__(self):
        return f"{self.gold}g"