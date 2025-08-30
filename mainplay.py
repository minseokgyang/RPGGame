from player import Player
from inventory import Inventory
from money import Money
from shop import Shop
from monster import monster_spown1_2

if __name__ == "__main__":
    player = Player("용사", "전사")
    inventory = Inventory()
    money = Money()
    shop = Shop(inventory, money)

    # 몬스터 사냥 → 골드 획득
    monster = monster_spown1_2()
    print(f"[BATTLE] {monster.name}를 물리쳤습니다!")
    money.earn_from_monster()

    # 상점 방문
    shop.visit(player)

    # 인벤토리 확인
    inventory.show()

    # 아이템 사용 예시
    inventory.use_item(player, "마나물약")
    inventory.use_item(player, "회복약")
    inventory.use_item(player, "랜덤스탯티켓")

    # 상태 확인
    player.show_status()
