from items import generate_stat_item, generate_exp_item, mana_potion, health_potion

class shop:
    def __init__(self):
        self.stock = [
            generate_stat_item(),
            generate_exp_item(),
            mana_potion(),
            health_potion()
        ]
    
    def show_items(self):
        try:
            print("=== 상점 진열 ===")
            for i, item in enumerate(self.stock, 1):
                print(f"{i}. {item}")
            print("0. 나가기")
        except Exception as e:
            print(f"[오류] 상점 진열 중 문제가 발생하였습니다.: {e}")
    
    def visit_shop(self, player):
        while True:
            self.show_items()
            try:
                choice = input("구매할 아이템 번호를 입력해주세요. (0 입력시 나가기):")
                choice = int(choice)
                if choice == 0:
                    print("[상점] 상점을 나갑니다.")
                    break
                if 1 <= choice <= len(self.stock):
                    item = self.stock[choice - 1]
                    if player.money.spend(item.price):
                        player.inventory.add_item(item)
                        print(f"[상점]{item.name}구매완료")
                        if item.effect == "exp":
                            player.add_exp(item.value)
                    else:
                        print("[상점] 골드가 부족합니다.")
                else:
                    print("[상점] 잘못된 선택입니다.")
            except ValueError:
                print("[상점] 잘못된 입력입니다. 숫자를 입력해주세요.")
            except Exception as e:
                print("[상점 오류]알 수 없는 문제가 발생했습니다.: {e}")