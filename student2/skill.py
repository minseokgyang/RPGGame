from player import Player
import random
import time

# ====================== 스킬 클래스 =========================== #
class Skill:
    def __init__(self, name, damage=0, heal=0, cost=0, effect=False):
        self.name = name        # 스킬 이름
        self.damage = damage    # 가하는 데미지
        self.heal = heal        # 회복량
        self.cost = cost        # 소모 MP
        self.effect = effect

    def use(self, player, monster):
        """스킬 사용 효과"""
        # MP 체크
        if player.MP < self.cost:
            print("MP가 부족하다!")
            return

        player.MP -= self.cost

        # 공격 스킬
        if self.damage > 0:
            from battle import Battle
            bt = Battle(player, monster)
            monster.HP -= self.damage
            print(f"{monster.name}에게 {self.name}으로 {self.damage} 피해를 입혔다!")
            time.sleep(2)
            if self.effect == True:
                rand_effect = random.randint(1, 3)
                if rand_effect == 2:
                    print(f'{monster.name}(이)가 기절 했다.')
                    time.sleep(2)
                else:
                    print(f'하지만 아무 일도 일어나지 않았다.')
                    time.sleep(2)
                    bt.monster_turn()

        # 회복 스킬
        if self.heal > 0:
            player.HP += self.heal
            print(f"{player.name}의 체력이 {self.heal}만큼 회복되었다!")
            time.sleep(2)


# ====================== 플레이어 전직 예시 =========================== #

def class_worrior():
    p = Player("용사")  
    p.skill = [
        Skill("파이어볼", damage=15, cost=5),
        Skill("힐", heal=10, cost=3),
        Skill("강타", damage=25, cost=10)
    ]
    return p