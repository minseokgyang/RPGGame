import random

class item:
    def __init__(self, name: str, effect: str, value: int, price: int):
        self.name
        self.effect
        self.value
        self.price
    
    def __str__(self):
        return f"{self.name}({self.effect} + {self.value}) - {self.price}g"
    
def generate_stat_item():
    stat_value = random.randint(-3,10)
    return item("stat tome","stat",stat_value, price=20 + stat_value)

def generate_exp_item():
    exp_value = random.randint(0,20)
    return item("Experience Scroll", "exp", exp_value, price=15 + exp_value)

def mana_potion():
    return item("mana potion","mana", 10, price=10)

def health_potion():
    return item("health potion","hp", 20, price=15)