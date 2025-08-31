import random
import time
from image import *
from player import *

class Weapon:
    def __init__(self, name, type ,str = 0, int = 0, dex = 0, luck = 0):
        self.type = type
        self.str = str #힘
        self.dex = dex #민첩
        self.int = int #지능
        self.luck = luck #운
        self.name = name
        self.level = 0
        self.fail_count = 0
        self.base_chance = {
            0: 0.5,
            1: 0.5,
            2: 0.4,
            3: 0.4,
            4: 0.3,
            5: 0.3,
            6: 0.2,
            7: 0.2,
            8: 0.05,
            9: 0.01,
        }
        self.success_exp = 0


    def try_upgrade(self):
        base_chance = self.base_chance.get(self.level, 0.1)
        bonus = min(self.fail_count * 0.05, 0.2)
        chance = min(base_chance + bonus, 0.5)
        rest_exp = {
            0: 20,
            1: 15,
            2: 10
        }


        if self.success_exp >= 100:
            self.level += 1
            self.success_exp = 0
            self.fail_count = 0
            print('성공의 기운이 최대치에 도달하여 자동으로 강화에 성공했습니다!')
            time.sleep(1)
            return


        print(Image.image_['blacksmith'])
        print("강화를 시도합니다...")
        bar_length = 20
        for i in range(bar_length + 1):
            bar = "█" * i + "-" * (bar_length - i)
            percent = int((i / bar_length) * 100)
            print(f"\r[{bar}] {percent}%", end="")
            time.sleep(0.1)
        print("\n")  # 줄바꿈
        dice = random.random()  # 0.0 ~ 1.0 사이의 랜덤 실수 생성      
        time.sleep(1)

        if dice < chance:
            self.level += 1

            if self.type == 'sword':
                self.str += 20

            elif self.type == 'staff':
                self.int += 20

            elif self.type == 'knife':
                self.dex += 20

            elif self.type == 'coin':
                self.luck += 20

            self.fail_count = 0
            print(f'강화에 성공했습니다! +{self.level} {self.name} 강화수치 : {self.str}')
            self.success_exp = 0
            
        if dice > chance:
            self.fail_count += 1
            self.success_exp += (rest_exp.get(self.level, 5))
            print(f'강화에 실패했습니다. +{self.level} {self.name} 다음 강화시도시 보너스 확률이 5%만큼 추가됩니다.')
            
            if self.fail_count == 4:
                print('보너스 확률이 더이상 증가하지 않습니다')
            print(f'강화 성공의 기운이 {rest_exp.get(self.level)}만큼 쌓였습니다. 현재 기운: {min(self.success_exp,100)}/100')
            if self.success_exp >= 100:
                print('성공의 기운이 최대치에 도달하여 다음 강화시도시 자동으로 강화에 성공합니다!')
                


# my_weapon = Weapon("허름한 검")
# print(f"현재 무기 상태: +{my_weapon.level} {my_weapon.name}")
# time.sleep(1)


# ================================무기 도감=========================================


weapons = dict(
        강철검 = Weapon('강철검', 'sword', str=20),
        단도 = Weapon('단도', 'knife', dex=20),
        나무지팡이 = Weapon('나무지팡이', 'staff', int=20),
        황금코인 = Weapon('황금코인', 'coin', luck=20),
)



# ================================강화_실행_함수=========================================

def renforce(weapon, player):
    while weapon.level < 10:
        user_input = input("[1. 강화 2. 중단] ")
        if user_input == '1':
            # 강화 전 스탯 저장
            old_str = weapon.str
            old_dex = weapon.dex
            old_int = weapon.int
            old_luck = weapon.luck

            weapon.try_upgrade()

            # 증가량 계산
            inc_str = weapon.str - old_str
            inc_dex = weapon.dex - old_dex
            inc_int = weapon.int - old_int
            inc_luck = weapon.luck - old_luck

            # 플레이어 스탯에 반영
            player.str += inc_str
            player.dex += inc_dex
            player.int += inc_int
            player.luck += inc_luck

            # 증가량 출력
            print(f"\n강화 완료! 증가 스탯:")
            print(f"현재 플레이어 스탯: STR {player.str}, DEX {player.dex}, INT {player.int}, LUCK {player.luck}\n")

        else:
            print('강화를 중단합니다.\n')
            break



if __name__ == '__main__':
    renforce(weapons['강철검'])