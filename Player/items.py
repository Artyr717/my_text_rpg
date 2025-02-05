class Item:
    def __init__(self, name: str, price: float, item_type: str):
        self.name = name
        self.price = price
        self.item_type = item_type


class Weapon(Item):
    def __init__(self, name: str, price: float, damage: int, weapon_type: str = "melee"):
        super().__init__(name, price, item_type="Оружие")
        self.damage = damage  # Урон оружия
        self.weapon_type = weapon_type


class Potion(Item):
    def __init__(self, name: str, price: float, effect_amount: int, potion_type: str = "heal"):
        super().__init__(name, price, item_type="Зелье")
        self.effect_amount = effect_amount
        self.potion_type = potion_type
    #  TODO: Добавить проверку, чтобы hp не превышало максимальное значение


class SellableItem(Item):
    def __init__(self, name: str, price: int):
        super().__init__(name, price, item_type="Прочее")
