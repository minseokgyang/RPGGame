import random

class Player: 
    def __init__(self, name='무명', job='무직'):
        self.name = name
        self.job = job
        self.str = 20
        self.dex = 20
        self.int = 20
        self.luck = 20
        self.HP = 100
        self.MP = 100
        self.max_HP = 100
        self.max_MP = 100
        self.skill = []
        self.weapon = '돌'
        self.armor = '허름한 옷'
        self.level = 1
        self.exp = 0
        self.gold = 0

    def add_exp(self, amount):
        self.exp += amount
        print(f"[EXP] 경험치 {amount}을 획득했습니다! (총 경험치: {self.exp})")
        if self.exp >= 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        stat_up = random.choice(["str", "dex", "int", "luck"])
        setattr(self, stat_up, getattr(self, stat_up) + random.randint(1, 5))
        print(f"[LEVEL UP] {self.level} 레벨이 되었습니다! {stat_up} 능력이 강화되었습니다.")

    def show_status(self):
        print(f"플레이어: {self.name}, 직업: {self.job}")
        print(f"레벨: {self.level}, 경험치: {self.exp}")
        print(f"HP: {self.HP}/{self.max_HP}, MP: {self.MP}/{self.max_MP}")
        print(f"힘:{self.str}, 민첩:{self.dex}, 지능:{self.int}, 운:{self.luck}")
        print(f"골드: {self.gold}")
