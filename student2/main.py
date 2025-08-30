import time
from player import *
from monster import *
from script import GameScenario
from image import Image
from battle import Battle
from pclass import *

#함수 호출 순서 1막 : interface start, name, status_set, status_chack, first_script, first_battle
#함수 호출 순서 2막(2막 부터 전투중 스테이터스 인벤토리 확인 가능.) : second_script, second_battle

f = GameScenario()
##==================게임 시작==================##
def interface():
    pass

def start():
    f.script_start()

def name():
    print(Image.image_['start'])
    ps = player_spawn1()
    player_name = input('이름: ')
    ps.name = player_name
    time.sleep(1)

def status_set():
    ps = player_spawn1()
    print('스테이터스를 렌덤으로 조정한다.')
    time.sleep(1)
    ps.status_set()
    time.sleep(1)

def status_chack():
    print("\n"*40)
    print(Image.image_['start'])
    ps = player_spawn1()
    ps.status_info()
    time.sleep(5)

##==================1막==================##

def first_script():
    print("\n"*40)
    a=0
    while True:
        
        try :
            a+=1
            f.script_common(f.script['_1막'][f'_{a}'])
        except :
            f.script_impect(f.script['_1막']['_최종장'])
            break
    time.sleep(1)

def first_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_1막'][f'_{a}'])
            if f.script_act['_1막'][f'_{a}'] == '':
                break
    time.sleep(2)

def first_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_1()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP < 0:
            sc = GameScenario()
            script = 'YOU DIE'
            sc.script_impect(script)
            main()
        else:
            bt.player_inter()
    print(f'[{ms.name}(을)를 짖니겼다.]')
    print('[reword]:')
    print('[허름하지만 튼튼한 주머니를 얻었다.]')
    time.sleep(3)

##==================2막==================##
def second_script():
    print("\n"*40)
    a=0
    ps = player_spawn1()
    while True:
        
        try :
            a+=1
            f.script_common(f.script['_2막'][f'_{a}'])
        except :
            f.script_impect(f.script['_2막']['_최종장'])
            break
    ps.HP = 100
    print('[reword]:')
    print('[체력이 모두 회복되었다.]')
    time.sleep(3)


def second_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_2막'][f'_{a}'])
            if f.script_act['_2막'][f'_{a}'] == '':
                break
    time.sleep(2)


def second_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_2()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP < 0:
            sc = GameScenario()
            script = 'YOU DIE'
            sc.script_impect(script)
            main()
        else:
            bt.player_inter()
    print(f'[{ms.name}(을)를 처치했다.]')
    print('[reword]:')
    print('[고블린의 몽둥이를 얻었다.(str + 20)]')
    ps.str += 20
    time.sleep(3)

##==================3막==================##
def third_script():
    print("\n"*40)
    a=0
    ps = player_spawn1()
    while True:
        
        try :
            a+=1
            f.script_common(f.script['_3막'][f'_{a}'])
        except :
            f.script_impect(f.script['_3막']['_최종장'])
            break
    time.sleep(3)


def third_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_3막'][f'_{a}'])
            if f.script_act['_3막'][f'_{a}'] == '':
                break
    time.sleep(2)


def third_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_3()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP < 0:
            sc = GameScenario()
            script = 'YOU DIE...?'
            sc.script_impect(script)
            break
        bt.player_inter()

##==================4막==================##
def fourth_script():
    print("\n"*40)
    a=0
    ps = player_spawn1()
    while True:
        
        try :
            a+=1
            f.script_common(f.script['_4막'][f'_{a}'])
        except :
            f.script_impect(f.script['_4막']['_최종장'])
            break
    ps.HP = 100
    print('[reword]:')
    print('[체력이 모두 회복되었다.]')
    time.sleep(3)


# def #상점 확인


def fourth_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_4막'][f'_{a}'])
            if f.script_act['_4막'][f'_{a}'] == '':
                break
    time.sleep(2)



def first_class():
    print('\n'*40)
    pc = Player_Class()
    ps = player_spawn1()
    while True:
        # try:
            print('"서비스다. 무기 중 골라봐"')
            player_choice = int(input("1.장검  2.단검  3.스테프  4.금화 한 닢"))
            if player_choice == 1:
                pc.warrior(ps)
                ps.status_info
                time.sleep(3)
                return
            elif player_choice == 2:
                pc.thief(ps)
                time.sleep(3)
                return
            elif player_choice == 3:
                pc.mage(ps)
                time.sleep(3)
                return
            elif player_choice == 4:
                pc.gambler(ps)
                time.sleep(3)
                return
        # except :
        #     print('"그런건 내 가게엔 없다."')
        #     continue



def fourth_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_4()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP < 0:
            sc = GameScenario()
            script = 'YOU DIE'
            sc.script_impect(script)
            main()
        else:
            bt.player_inter()
    print(f'[{ms.name}(을)를 처치했다.]')
    print('[reword]:')
    print('')
    ps.str += 20
    time.sleep(3)




def main():
    # interface()
    # start()
    # name()
    # status_set()
    # status_chack()

    # first_script()
    # first_battle_script()
    # first_battle()

    # second_script()
    # second_battle_script()
    # second_battle()

    # third_script()
    # third_battle_script()
    # third_battle()

    # fourth_script()

    first_class()
    fourth_battle()


#? ======================배타 테스트==========================
if __name__ == "__main__":
    main()