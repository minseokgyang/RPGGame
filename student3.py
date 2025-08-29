def student3():
    print("안녕하세요. 수강생 3번 입니다.")


#-----------------------------------------
import random
import time

def skills(skill):
    try:
        match skill:
            case 0: #평타
                return random.randint(5,10)
            case 1: #전사스킬
                return random.randint(10,20)
    except Exception as e:
        return f"error: {e}"
    
        
                    
#------------------------------------------
Monster_hp = random.randint(50,100)
Player_hp = 50
class Battle:

        print('전투가 시작되었습니다!')
        time.sleep(2)
        while Monster_hp > 0:
            print('전사가 횡베기를 사용합니다')
            time.sleep(2)
            dmg = skills(0)
            Monster_hp -= dmg
            if Monster_hp <= 0:
                print('몬스터에게 최후의 일격을 날렸습니다!')
                time.sleep(2)
                print('몬스터를 처치했습니다!')
                break

            else:
                print(f'몬스터에게 횡베기를 사용해 체력이 {Monster_hp}남았습니다!')
                time.sleep(2)
                print("몬스터에게 턴이 넘어갑니다.")
                time.sleep(2)
                print("몬스터의 강한공격!")
                dmg2 = skills(1)
                Player_hp -= dmg2
        
                if Player_hp <= 0:
                    print('플레이어가 사망했습니다!')
                    break

                time.sleep(2)
                print(f'플레이어의 체력이 {Player_hp}남았습니다!')
                time.sleep(2)
                print('당신의 공격차례입니다')
                time.sleep(2)
        
                
                
        

