import time
import random
from monster import *
from player import *
from image import Image
from script import *
from skill import *
from inventory import *

# # ======================배틀 클래스==========================# # 
class Battle:
    def __init__(self, name, monster):
        self.name = name
        self.monster = monster
        self.attack = name.str
        self.evasion = 0
        
        

# # ====================== 플레이어 공격 선택 시 출력==========================# # 
    def player_turn(self): 
        monster = self.monster
        player = self.name
        monster.HP -= player.str

        if player.HP < 0 :
            return

        print(Image.image_[monster.name])
        monster.status_HP()

        print(f'{monster.name}에게 {player.str}의 피해를 입혔다.')
        player.status_HP()
        time.sleep(3)


# # ====================== 몬스터 공격 나올 시==========================# # 
    def monster_turn(self): 
        monster = self.monster
        player = self.name
        player.HP -= monster.str

        if monster.HP < 0 :
            return

        print(Image.image_[player.job])
        monster.status_HP()

        #? randnom_num = random.randint(1,3).      #몬스터 공격 or 스킬 중 랜덤으로 리턴하도록 
        #? if randnom_num == 1: 
        print(f'{monster.name}에게 {monster.str}의 피해를 받았다.')
        
        player.status_HP()
        time.sleep(3)


# # ======================플레이어 패링 선택 시 출력==========================# # 
    def player_parry(self):
        monster = self.monster
        player = self.name

        print(f'{monster.name}의 공격에 대비하여 자세를 취한다.')
        player_choice = int(input('1. 왼쪽, 2. 오른쪽, 3. 정면:'))
        system_choice = random.randint(1, 3)
        time.sleep(1)
        if player_choice == system_choice:

            print(Image.image_[monster.name])
            monster.HP -= monster.str
            monster.status_HP()

            print(f'공격을 받아 쳐내 {monster.str}의 피해를 돌려주었다')

            player.status_HP()
            time.sleep(3)

        else:
            print(Image.image_[monster.name])
            monster.status_HP()

            print(f'받아내기에 싫패하여...{int(monster.str * 1.5)}의 치명상을 입었다.')
            player.HP -= monster.str * 1.5
            player.status_HP()
            time.sleep(3)


# # ======================스킬 선택시 출력==========================# # 
    def player_skill(self):
        monster = self.monster
        player = self.name

        if not player.skill:
            print("사용 가능한 스킬이 없다.")
            time.sleep(2)
            return

        print("사용 가능한 스킬 목록:")
        for i, sk in enumerate(player.skill):
            dmg = sk.damage(player) if callable(sk.damage) else sk.damage
            heal = sk.heal(player) if callable(sk.heal) else sk.heal
            print(f"{i}. {sk.name} (DMG:{dmg}, HEAL:{heal}, COST:{sk.cost})")

        choice = int(input("사용할 스킬 번호를 선택: "))
        if 0 <= choice < len(player.skill):
            player.skill[choice].use(player, monster)
        else:
            print("잘못된 입력이다.")



# # ======================도망 선택시 출력==========================# # 
    def player_run(self):
        monster = self.monster
        player = self.name
        player.HP -= monster.str

        print(f'{monster.name}로부터 도망치기를 선택했다.')
        player_choice = int(input('1. 왼쪽, 2. 오른쪽:'))
        system_choice = random.randint(1, 2)
        time.sleep(1)

        if player_choice == system_choice:
            print(Image.image_[player.job])
            print(f'도망에 성공하였다')
            player.status_HP()
            time.sleep(3)
        else:
            print(Image.image_[monster.name])
            monster.status_HP()

            print(f'싫패하여 두배로 쳐맞았다 {int(monster.str*1.5)}의 치명상을 입었다.')
            player.HP -= int(monster.str * 1.5)
            player.status_HP()
            time.sleep(3)


    def player_inter(self):
        f = GameScenario()
        monster = self.monster
        player = self.name

        print(Image.image_[monster.name])
        monster.status_HP()

        script = '1.공격  2.자세잡기  3.스킬 보기  \n4.도망  5.스테이터스  6.인벤토리'
        player.status_HP()

        f.script_battle(script)
        print("="*36)

        player_choice = int(input())
        if player_choice == 1:
            self.player_turn()
            self.monster_turn()
        elif player_choice == 2:
            self.player_parry()
        elif player_choice == 3:
            self.player_skill()
        elif player_choice == 4:
            self.player_run()
        elif player_choice == 5:
            player.status_info()
            time.sleep(3)
            self.player_inter()
        elif player_choice == 6:
            self.name.inventory.show(player)
            time.sleep(3)



#? ======================배타 테스트==========================
if __name__ == "__main__":
    f = Battle(player_spawn1(), monster_spown1_1())
    f.player_turn()
    f.player_skill()
    f.monster_turn()
    f.player_parry()
    f.player_run()
