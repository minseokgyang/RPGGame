def student2():
    print("안녕하세요. 수강생 2번 입니다.")



import random
import time
# ===================플레이어 클래스=======================
class Player: #플레이어 스테이터스
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


# ====================몬스터 클래스 ========================
class Monster: #몬스터 스테이터스
    def __init__(self, name, str=10, _int=10, HP=30, MP=30, max_HP=None, max_MP=None):
        self.name = name
        self.str = str
        self.int = _int
        self.HP = HP
        self.MP = MP
        self.max_HP = max_HP if max_HP is not None else HP  # 최대 HP 없으면 현재 HP 기준
        self.max_MP = max_MP if max_MP is not None else MP  # 최대 MP

# ====================체력바 만 불러오는 메서드========================

    def status_HP(self):
        title = f"[{self.name}]"

        # 최대 HP
        max_HP = getattr(self, 'max_HP', 100)  # max_HP가 없으면 100으로

        # 체력바 길이
        bar_len = 20  

        # 체력 비율
        hp_ratio = max(0, min(1, self.HP / max_HP))  # 0~1 사이로 제한

        # 체력바 생성
        hp_fill = int(hp_ratio * bar_len)
        hp_bar = "█" * hp_fill + "▒" * (bar_len - hp_fill)

        # 화면 폭 계산
        width = max(len(title), len(hp_bar)+10) + 6

        print("=" * width)
        print(f"{title.center(width-6)}")
        print(f"HP : [{hp_bar}] {hp_ratio*100:.0f}% ({self.HP}/{max_HP})".center(width-4))
        print("=" * width)

# =========================몬스터 도감 클래스=============================

class MonsterBook:
    monsters = dict(
        _1막 = dict(
            _1 = Monster('당신과_같은_망자', HP = 10000000000),
            _2 = Monster('goblin', 5, 0, 50),
            _3 = Monster('goblin', 5, 0, 50),
            _4 = Monster('goblin 프리스트', 5, 0, 50),
            _5 = Monster('홉고블린', 8, 2, 80),
        ),
        _2막 = dict()
    )


# ============================몬스터 호출 함수============================

# 이런식으로 불러 옴
def monster_spown1_1():
    A = MonsterBook #딕셔너리 클레스에서 가져옴
    B = A.monsters['_1막']['_1'] # 딕셔너리에서 인스턴스에 넣을 Monster값을 가져옴
    return B # 해당 몬스터(당신과 같은 망령) 리턴

# 
def monster_spown1_2():
    A = MonsterBook 
    B = A.monsters['_1막']['_2'] 
    return B

# 
def monster_spown1_3():
    A = MonsterBook 
    B = A.monsters['_1막']['_3'] 
    return B


# 
def monster_spown1_4():
    A = MonsterBook 
    B = A.monsters['_1막']['_4'] 
    return B

#
def monster_spown1_5():
    A = MonsterBook 
    B = A.monsters['_1막']['_5'] 
    return B


#? ======================배타 테스트==========================
if __name__ == "__main__":
    pass