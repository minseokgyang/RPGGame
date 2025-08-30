class Monster: 
    def __init__(self, name, str=10, _int=10, HP=30, MP=30, max_HP=None, max_MP=None):
        self.name = name
        self.str = str
        self.int = _int
        self.HP = HP
        self.MP = MP
        self.max_HP = max_HP if max_HP else HP
        self.max_MP = max_MP if max_MP else MP

    def status_HP(self):
        title = f"[{self.name}]"
        max_HP = getattr(self, 'max_HP', 100)
        bar_len = 20  
        hp_ratio = max(0, min(1, self.HP / max_HP))
        hp_fill = int(hp_ratio * bar_len)
        hp_bar = "█" * hp_fill + "▒" * (bar_len - hp_fill)
        print("=" * 40)
        print(title)
        print(f"HP : [{hp_bar}] {hp_ratio*100:.0f}% ({self.HP}/{max_HP})")
        print("=" * 40)


class MonsterBook:
    monsters = dict(
        _1막=dict(
            _1=Monster('당신과_같은_망자', HP=100),
            _2=Monster('goblin', 5, 0, 50),
            _3=Monster('goblin', 5, 0, 50),
            _4=Monster('goblin 프리스트', 5, 0, 50),
            _5=Monster('홉고블린', 8, 2, 80),
        ),
        _2막=dict()
    )

def monster_spown1_1(): return MonsterBook.monsters['_1막']['_1']
def monster_spown1_2(): return MonsterBook.monsters['_1막']['_2']
def monster_spown1_3(): return MonsterBook.monsters['_1막']['_3']
def monster_spown1_4(): return MonsterBook.monsters['_1막']['_4']
def monster_spown1_5(): return MonsterBook.monsters['_1막']['_5']
