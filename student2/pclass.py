# 1막이 끝나면 직업 생성
from player import *
import random
from skill import *
import random
from image import Image

class Player_Class:
    def __init__(self):
        pass

    def warrior(self, player):
        player.job = '전사'
        num = [20,0,-10,0,50]
        player.str += num[0]
        player.dex += num[1]
        player.int += num[2]
        player.luck += num[3]
        player.max_HP += num[4]
        player.HP += num[4]
        player.skill = [
        Skill("파쇄격", damage=player.str * 1.3, cost=10),
        Skill("자루 치기", damage=player.str, cost=10, effect=True),
        Skill("강타", damage=player.str * 2, cost=50)
        ]
        print(Image.image_[player.job])
        print(f'전사로 전직 하였다.')
        player.status_info()
        print(f'스탯 증감 : str {num[0]}, dex {num[1]}, int {num[2]}, luck {num[3]}, HP {num[4]}')
        time.sleep(3)

    def mage(self, player):
        player.job = '마법사'
        num = [-15,-5,30,0,50]
        player.str += num[0]
        player.dex += num[1]
        player.int += num[2]
        player.luck += num[3]
        player.max_MP += num[4]
        player.MP += num[4]
        player.skill = [
        Skill("마나 폭발", damage=player.int * 1.3, cost=10),
        Skill("회복", heal=player.int, cost=50),
        Skill("프리즈", damage=player.int * 0.5,cost=15 ,effect=True)
        ]
        print(Image.image_[player.job])
        print(f'마법사로 전직 하였다.')
        player.status_info()
        print(f'스탯 증감 : str {num[0]}, dex {num[1]}, int {num[2]}, luck {num[3]}, MP {num[4]}')
        time.sleep(3)

    def thief(self, player):
        player.job = '도적'
        num = [-10,15,0,5]
        player.str += num[0]
        player.dex += num[1]
        player.int += num[2]
        player.luck += num[3]
        player.skill = [
        Skill("급습", damage=player.dex * 1.5, cost=20),
        Skill("뭐라도 던지기", damage=player.dex * 5, cost=80, effect=True),
        Skill("은신", damage=player.dex * 0.5, cost=10)
        ]
        print(Image.image_[player.job])
        print(f'도적으로 전직 하였다.')
        player.status_info()
        print(f'스탯 증감 : str {num[0]}, dex {num[1]}, int {num[2]}, luck {num[3]}')
        time.sleep(3)

    def gambler(self, player):
        player.job = '도박사'
        num = [random.randint(-20,99) for _ in range(4)]
        player.str += num[0]
        player.dex += num[1]
        player.int += num[2]
        player.luck += num[3]
        player.skill = [
        Skill("신께 기도하기", damage=random.randint(1, 500), cost=50),
        Skill("대화를 시도하기", damage=1 * 5, cost=10, effect=True),
        Skill("살려주세요...", damage=1, cost=0 , effect=True)
        ]
        print(Image.image_[player.job])
        print(f'도박사로 전직 하였다.')
        player.status_info()
        print(f'스탯 증감 : str {num[0]}, dex {num[1]}, int {num[2]}, luck {num[3]}')
        time.sleep(3)

    def player_warrior(self,name):
        self.warrior()



#? ======================배타 테스트==========================
if __name__ == "__main__":
    pass