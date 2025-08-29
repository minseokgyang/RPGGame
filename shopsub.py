class Player:
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.attack = 0
        self.dex = 0
        self.intelligence = 0
        self.luck = 0
        self.exp = 0
        self.gold = 0

    def show_status(self):
        print(f"{self.name}의 상태")
        print(f"HP : {self.hp}, 공격력:{self.attack} ,민첩:{self.dex},지능:{self.intelligence}, 행운:{self.luck},경험치:{self.exp} 골드:{self.gold}")


class Shop:
    def buy(self, player, item):
        self.player = player
    
    def enter(self):
        print("🏛️상점에 오신걸 환영합니다.")
        print("1️⃣. 랜덤 스탯 강화 (랜덤으로 스탯1~10으로 강화됩니다. )")
        print("2️⃣. 랜덤 경험치 획득")
        print("나가고 싶으시면 3번을 입력해주세요.")
        
        choice = int(input("1~3번을 입력해주세요 : "))
        
        if choice == "1":
            stat_up = random.randint(1,10)
            self.player.attack += stat_up
            print(f"공격력이 {stat_up}만큼 증가했습니다. 현재 공격력은 {self.player.attack}")
            self.player.dex += stat_up
            print(f"민첩이 {stat_up}만큼 증가했습니다. 현재 민첩은 {self.player.dex}")
            self.player.intelligence += stat_up
            print(f"지능이 {stat_up}만큼 증가했습니다. 현재 지능은 {self.player.intelligence}")
            self.player.luck += stat_up
            print(f"행운이 {stat_up}만큼 증가했습니다. 현재 행운은 {self.player.luck}")