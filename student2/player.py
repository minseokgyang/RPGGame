import random
import time

class Player: 
    def __init__(self, name = '무명', job = '무직'): #케릭터
        self.name = name #케릭터 이름
        self.job = job #캐릭터 직업
        #케릭터 스탯
        self.str = 20 #힘
        self.dex = 20 #민첩
        self.int = 20 #지능
        self.luck = 20 #운
        self.HP = 100
        self.MP = 100
        self.max_HP = 100
        self.max_MP = 100
        # self.level = 0
        self.skill = []
        self.weapon = '돌'
        self.ammer = '허름한 옷'

# ===================체력바 만 불러오는 메서드=======================

    def status_HP(self):
        title = f"[{self.name}] [{self.job if self.job else '무직'}]"

        # 바 길이
        bar_len = 20

        # 비율 계산
        hp_ratio = max(0, min(1, self.HP / self.max_HP))
        mp_ratio = max(0, min(1, self.MP / self.max_MP))

        # 바 생성
        hp_fill = int(hp_ratio * bar_len)
        mp_fill = int(mp_ratio * bar_len)

        hp_bar = "█" * hp_fill + "▒" * (bar_len - hp_fill)
        mp_bar = "▓" * mp_fill + "▒" * (bar_len - mp_fill)

        # 화면 폭 계산
        width = max(len(title), len(hp_bar)+10, len(mp_bar)+10) + 6

        print("=" * width)
        print(f"{title.center(width-6)}")
        print(f"HP : [{hp_bar}] {hp_ratio*100:.0f}% ({self.HP}/{self.max_HP})".center(width-4))
        print(f"MP : [{mp_bar}] {mp_ratio*100:.0f}% ({self.MP}/{self.max_MP})".center(width-4))
        print("=" * width)


# ===================랜덤으로 스탯을 정해주는 메서드=======================

    def status_set(self): #게임 스타트 시 가장 먼저 실행되는 메서드
        a=5
        while a > 0 :
            a-=1
            self.str = random.randint(1, 97)
            self.dex = random.randint(1, 100 - self.str - 2)
            self.int = random.randint(1, 100 - self.str - self.dex - 1)
            self.luck = 100 - (self.str + self.dex + self.int)
            if self.luck > 0:
                print(f'힘:{self.str}, 민첩{self.dex}, 지능{self.int}, 운{self.luck}')
            A = input(f'만족 하는가?(y/n)(남은 초기화 {a}회):')
            if A == 'y':
                break
            else :
                continue

# ===================스테이터스 불러오는 메서드=======================

    def status_info(self):
        title = f"[{self.name}] [{self.job if self.job else '무직'}]"
        bar_len = 20  

        # 체력바 / 마나바 비율 계산
        hp_ratio = self.HP / self.max_HP
        mp_ratio = self.MP / self.max_MP
        hp_fill = max(0, min(bar_len, int(hp_ratio * bar_len)))
        mp_fill = max(0, min(bar_len, int(mp_ratio * bar_len)))

        hp_bar = "█" * hp_fill + "▒" * (bar_len - hp_fill)
        mp_bar = "▓" * mp_fill + "▒" * (bar_len - mp_fill)

        # 표시용
        stats = [
            f"HP   : [{hp_bar}] {int(hp_ratio*100)}% ({self.HP}/{self.max_HP})",
            f"MP   : [{mp_bar}] {int(mp_ratio*100)}% ({self.MP}/{self.max_MP})",
            f"STR  : {self.str}",
            f"DEX  : {self.dex}",
            f"INT  : {self.int}",
            f"LUCK : {self.luck}"
        ]

        width = max(len(title), max(len(s) for s in stats)) + 6

        print("=" * width)
        print(f"== {title.center(width-6)} ==")
        for s in stats:
            print(f"== {s.center(width-6)} ==")
        print("=" * width)





class PlayerBook:
    # 최대 3명 플레이어 등록
    players = dict(
        _1 = Player("영웅1"),
        _2 = Player("영웅2"),
        _3 = Player("영웅3")
    )

# ============================플레이어 호출 함수============================

def player_spawn1(): #?클래스에서 플레이어의 정보 최신화 할 때 player_spawn1() 사용
    return PlayerBook.players['_1']

def player_spawn2():
    return PlayerBook.players['_2']

def player_spawn3():
    return PlayerBook.players['_3']


#? ======================배타 테스트==========================
if __name__ == "__main__":
    pass