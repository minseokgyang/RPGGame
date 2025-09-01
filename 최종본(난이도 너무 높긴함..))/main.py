import time
import random
from player import *
from monster import *
from script import GameScenario
from image import Image
from battle import Battle
from pclass import *
from weapon import *
from inventory import Inventory
from shop import Shop

#함수 호출 순서 1막 : interface start, name, status_set, status_chack, first_script, first_battle
#함수 호출 순서 2막(2막 부터 전투중 스테이터스 인벤토리 확인 가능.) : second_script, second_battle

f = GameScenario()
##==================게임 시작==================##
# ------------게임 시작 인터페이스-------------
def interface():
    print(Image.image_['start'])
    f.script_common('몰입을 위해 화면 비율을 이미지에 맞춰주세요.')
    f.script_common('Press enter to start')
    input()
# ------------게임 시작 대사-------------
def start():
    print("\n"*40)
    f.script_start()
# ------------이름 지정-------------
def name():
    print(Image.image_['start'])
    ps = player_spawn1()
    player_name = input('이름: ')
    ps.name = player_name
    time.sleep(1)
# ------------스테이터스 랜덤 조정-------------
def status_set():
    ps = player_spawn1()
    print('스테이터스를 렌덤으로 조정한다.')
    time.sleep(1)
    ps.status_set()
    time.sleep(1)
# ------------스테이터스 확인-------------
def status_chack():
    print("\n"*40)
    print(Image.image_['start'])
    ps = player_spawn1()
    ps.status_info()
    time.sleep(5)

##==================1막==================##
# ------------첫 대사-------------
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
# ------------첫 배틀 대사-------------
def first_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_1막'][f'_{a}'])
            if f.script_act['_1막'][f'_{a}'] == '':
                break
    time.sleep(2)
# ------------첫 배틀-------------
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
            ps.gold.gold += 1000
    print(f'[{ms.name}(을)를 짖이겼다.]')
    print('[reword]:')
    print('[허름하지만 튼튼한 주머니를 얻었다.]')
    print('[100gold를 얻었다.]')
    time.sleep(3)

##==================2막==================##
# ------------두번째 스크립트-------------
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

# ------------두번째 전투 스크립트-------------
def second_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_2막'][f'_{a}'])
            if f.script_act['_2막'][f'_{a}'] == '':
                break
    time.sleep(2)

# ------------두번째 전투-------------
def second_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_2()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP <= 0:
            sc = GameScenario()
            script = 'YOU DIE'
            sc.script_impect(script)
            main()
        else:
            bt.player_inter()
    print(f'[{ms.name}(을)를 처치했다.]')
    print('[reword]:')
    ps.weapon = '고블린의 몽둥이'
    print('[고블린의 몽둥이를 얻었다.(str + 20)]')
    time.sleep(3)

##==================3막==================##
# ------------세번째 전투 스크립트-------------
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

# ------------세번째 전투 스크립트-------------
def third_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_3막'][f'_{a}'])
            if f.script_act['_3막'][f'_{a}'] == '':
                break
    time.sleep(2)

# ------------세번째 전투-------------
def third_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_최종장()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP < 0:
            sc = GameScenario()
            script = 'YOU DIE...?'
            sc.script_impect(script)
            break
        bt.player_inter()

##==================4막==================##
# ------------네번째 스크립트-------------
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

# ------------첫번째 상점 조우-------------
#상점 확인
def store():
    ps = player_spawn1()  # Player에 money, inventory 포함되어 있어야 함
    sh = Shop(ps.inventory, ps)
    sh.visit(ps)

# ------------첫번째 전직-------------
def first_class():
    print('\n'*40)
    pc = Player_Class()
    ps = player_spawn1()
    while True:
        try:
            print(Image.image_['store'])
            print('='*36)
            script = '"싸우려면 무기가 필요하지 않겠나?\n 서비스다. 무기 중 골라봐."'
            f.script_common(script)
            print('='*36)
            player_choice = int(input("1.철검  2.단검  3.스테프  4.금화 한 닢"))
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
        except :
            print('"그런건 내 가게엔 없네."')
            continue

# ------------네번째-2 스크립트-------------
def fourth_script_2():
    print("\n"*40)
    a=0
    ps = player_spawn1()
    while True:
        
        try :
            a+=1
            f.script_common(f.script['_4_1막'][f'_{a}'])
        except :
            f.script_impect(f.script['_4_1막']['_최종장'])
            break
    ps.HP = 100
    ps.max_HP += 100
    print('[reword]:')
    print('[체력이 모두 회복되었다.]')
    print('[제이든에게서 든든한 갑옷을 받았다. HP: +100]')
    time.sleep(3)

# ------------네번째 전투 스크립트-------------
def fourth_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_4막'][f'_{a}'])
            if f.script_act['_4막'][f'_{a}'] == '':
                break
    time.sleep(2)


# ------------네번째 전투-------------
def fourth_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_3()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP <= 0:
            sc = GameScenario()
            script = 'YOU DIE'
            sc.script_impect(script)
            main()
        else:
            bt.player_inter()
    print(f'[{ms.name}(을)를 처치했다.]')
    print('[reword]')
    print('')
    time.sleep(3)

# ##==================5막==================##

def fifth_script():
    print("\n"*40)
    a=0
    ps = player_spawn1()
    while True:
        
        try :
            a+=1
            f.script_common(f.script['_5막'][f'_{a}'])
        except :
            f.script_impect(f.script['_5막']['_최종장'])
            break
    ps.HP = 100
    ps.str += 100
    print('[reword]:')
    print('[체력이 모두 회복되었다.]')
    time.sleep(3)

# ------------다섯번째 전투 스크립트-------------
def fifth_battle_script():
    print('\n'*40)
    a=0
    while True:
            a+=1
            f.script_common(f.script_act['_5막'][f'_{a}'])
            if f.script_act['_5막'][f'_{a}'] == '':
                break
    time.sleep(2)


# ------------다섯번째 전투-------------
def fifth_battle():
    print("\n"*40)
    ps = player_spawn1()
    ms = monster_spown1_5()
    bt = Battle(ps, ms)
    while ms.HP > 0:
        if ps.HP <= 0:
            sc = GameScenario()
            script = 'YOU DIE'
            sc.script_impect(script)
            main()
        else:
            bt.player_inter()
    print(f'[{ms.name}(을)를 처치했다.]')
    print('[reword]')
    print('')
    ps.str += 20
    time.sleep(3)

# ------------다섯번째-1 스크립트-------------
def fifth_script_2():
    print("\n"*40)
    a=0
    ps = player_spawn1()
    while True:
        try :
            a+=1
            f.script_common(f.script['_5_1막'][f'_{a}'])
        except :
            f.script_impect(f.script['_5_1막']['_최종장'])
            break
    ps.HP = 100
    print('[reword]:')
    print('[체력이 모두 회복되었다.]')
    time.sleep(3)

# ------------두번째 상점 조우-------------
#상점 확인
def store():
    ps = player_spawn1()  # Player에 money, inventory 포함되어 있어야 함
    sh = Shop(ps.inventory, ps)
    sh.visit(ps)

# ##==================전투 뺑뺑이==================##

def fight():
    while True:
        print('\n'*40)
        ps = player_spawn1()
        print(Image.image_[ps.job])
        print("="*36)
        f.script_common('1.던전에 진입하자  2.상점으로 돌아가자  \n3.고블린로드에게 도전하자')
        print("="*36)
        player_choice_1 = int(input('이동할 곳을 선택하라'))

        if player_choice_1 == 1:
            at_entrance = True  # 던전 입구 상태 변수 추가
            while at_entrance:  
                print(Image.image_[ps.job])
                print("="*36)
                f.script_common("던전 입구에 섰다. 이동할 곳을 선택하라.")
                print("="*36)
                choice = int(input('1. 던전 깊숙히 나아간다  2. 입구로 돌아간다:'))  
                if choice == 2:  
                    break 

                # 던전 깊숙히 진행
                random_gold = random.randint(1, 100)
                monster_generators = [monster_spown1_1, monster_spown1_2, monster_spown1_3, monster_spown1_4, monster_spown1_5]
                ms = random.choice(monster_generators)()   
                bt = Battle(ps, ms)

                while ms.HP > 0 and ps.HP > 0:  
                    bt.player_inter()

                if ps.HP <= 0: 
                    sc = GameScenario()
                    sc.script_impect('YOU DIE')
                    sc.script_common('돈을 모두 잃고 던전 입구에서 정신을 차렸다.')
                    ps.gold.gold = 0
                    ps.HP = 100
                    break  

                if ms.HP <= 0:
                    print(f'[{ms.name}(을)를 처치했다.]')
                    print(f'gold {random_gold}를 얻었다.')
                    ps.gold.gold += random_gold  
                    time.sleep(1)
                    print(Image.image_[ps.job])
                    print("="*36)
                    f.script_common("갈림길에 섰다. 이동할 곳을 선택하라.")
                    print("="*36)
                    player_choice_2 = int(input('1. 계속 나아가자  2. 입구로 돌아가자'))
                    if player_choice_2 == 1:
                        continue
                    else:
                        break  

        elif player_choice_1 == 2:
            sh = Shop(ps.inventory, ps)
            sh.visit(ps)
            continue

        elif player_choice_1 == 3:
            print("\n"*40)
            a=0
            ps = player_spawn1()
            while True:
                try :
                    a+=1
                    f.script_common(f.script['_6막'][f'_{a}'])
                except :
                    f.script_impect(f.script['_6막']['_최종장'])
                    break

            print('\n'*40)
            a=0
            while True:
                    a+=1
                    f.script_common(f.script_act['_6막'][f'_{a}'])
                    if f.script_act['_6막'][f'_{a}'] == '':
                        break
            time.sleep(2)


            print("\n"*40)
            ps = player_spawn1()
            ms = monster_spown1_최종장()
            bt = Battle(ps, ms)

            while ms.HP > 0:
                if ps.HP <= 0: 
                    sc = GameScenario()
                    sc.script_impect('YOU DIE')
                    sc.script_common('돈을 모두 잃고 던전 입구에서 정신을 차렸다.')
                    ps.gold.gold = 0
                    ps.HP = 100
                    break
                bt.player_inter()

            if ms.HP <= 0:  # <<<=== 처치 메시지와 클리어 스크립트는 루프 밖
                print(f'[{ms.name}(을)를 처치했다.]')
                print('[reword]')
                print('[성장 가능성을 획득했다.]')

                print("\n"*40)
                a=0
                ps = player_spawn1()
                while True:
                    try:
                        a+=1
                        f.script_common(f.script['_클리어'][f'_{a}'])
                    except:
                        f.script_impect(f.script['_클리어']['_최종장'])
                        return









def main():
    #?게임 시작과 캐릭터 생성
    interface()
    start()
    name()
    status_set()
    status_chack()
    #?1번째 시나리오
    first_script()
    first_battle_script()
    first_battle()
    #?2번째 시나리오
    second_script()
    second_battle_script()
    second_battle()
    #?3번째 시나리오
    third_script()
    third_battle_script()
    third_battle()
    #?4번째 시나리오
    fourth_script()
    store()
    first_class()
    fourth_script_2()
    fourth_battle_script()
    fourth_battle()
    #?5번째 시나리오
    fifth_script()
    fifth_battle_script()
    fifth_battle()
    fifth_script_2()
    store()

    #노가다
    store()
    fight()








#? ======================배타 테스트==========================
if __name__ == "__main__":
    main()