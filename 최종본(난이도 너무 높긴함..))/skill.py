from player import Player
import random
import time

# ====================== 스킬 클래스 =========================== #
class Skill:
    def __init__(self, name, damage=0, heal=0, cost=0, effect=False):
        self.name = name
        self.damage = damage    
        self.heal = heal
        self.cost = cost
        self.effect = effect

    def use(self, player, monster):
        if player.MP < self.cost:
            print("MP가 부족하다!")
            time.sleep(2)
            return

        player.MP -= self.cost

        # 공격 스킬
        if callable(self.damage):
            dmg = self.damage(player)  
        else:
            dmg = self.damage

        if dmg > 0:
            from battle import Battle
            bt = Battle(player, monster)
            monster.HP -= dmg
            print(f"{monster.name}에게 {self.name}으로 {int(dmg)} 피해를 입혔다.")
            time.sleep(2)
            if self.effect == True :
                if random.randint(1, 3) == 2:
                    print(f'{monster.name}(이)가 기절 했다.')
                    time.sleep(2)
                    return
                else:
                    print('하지만 아무 일도 일어나지 않았다.')
                    time.sleep(2)
            bt.monster_turn()

        # 회복 스킬
        if callable(self.heal):
            heal_amount = self.heal(player)
        else:
            heal_amount = self.heal

        if heal_amount > 0:
            player.HP += heal_amount
            print(f"{player.name}의 체력이 {int(heal_amount)}만큼 회복되었다.")
            time.sleep(2)
            from battle import Battle
            bt = Battle(player, monster)
            bt.monster_turn()

# ====================== 플레이어 전직 예시 =========================== #

def class_worrior():
    p = Player("용사")  
    p.skill = [
        Skill("파이어볼", damage=15, cost=5),
        Skill("힐", heal=10, cost=3),
        Skill("강타", damage=25, cost=10)
    ]
    return p