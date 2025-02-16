import math
import random
import time

from Player.inventory import Inventory


class Character:

    def __init__(self, name: str):
        ### Stats ###
        self.agility = 1
        self.level = 1
        self.experience = 0.0
        self.hp = 100
        self.money = 0
        self.skill_points = 0
        self.armor = 0
        self.strength = 1

        ### Base Info ###
        self.name = name
        self.weapon = "Кулаки"
        self.inventory = Inventory()

        ### For Fighting ###
        self.damage = 1
        self.fight_coefficient = 0

    def get_info_player(self) -> dict:
        """
        Возвращает словарь с информацией об игроке, готовый для сохранения в JSON.
        """
        data = {
            "name": self.name,
            "level": self.level,
            "experience": self.experience,
            "hp": self.hp,
            "weapon": self.weapon,
            "money": self.money,
            "inventory": self.serialize_inventory()
        }
        return data

    def serialize_inventory(self) -> list:
        """
        Преобразует инвентарь в формат, который можно сериализовать в JSON.
        """

        serialized_items = []
        for item in self.inventory.items:
            if hasattr(item, 'to_dict'):
                serialized_items.append(item.to_dict())
            else:
                serialized_items.append(str(item))
        return serialized_items

    def set_weapon(self, weapon: str):
        self.weapon = weapon  # TODO: СДЕЛАТЬ ВЫБОР ОРУЖИЯ В ИНВЕТОРЕ И МЕНЯТЬ DAMAGE В ЗАВИСИМОСТИ ОТ ОРУЖИЯ И СИЛЫ

    def set_money(self, money: float):
        self.money = money

    def set_hp(self, hp: int):
        self.hp = hp

    def set_level(self, level: int):
        self.level = level

    def set_experience(self, experience: float):
        self.experience = experience

    def set_damage(self, damage: int):
        self.damage = damage

    def set_fight_coefficient(self, fight_coefficient: float):
        self.fight_coefficient = fight_coefficient

    def get_health_bar(self):
        return "[" + "+" * self.hp + " " * (100 - self.hp) + "]"

    def is_alive(self) -> bool:
        if self.hp > 0:
            return True
        return False

    def attack(self, target):
        """Производит атаку на цель."""
        # Шанс попадания (зависит от ловкости атакующего и защищающегося)
        hit_chance = max(0.1, min(0.9, 0.5 + 0.15 * math.log(self.agility / target.agility)))

        if random.random() <= hit_chance:
            # Расчет урона (с учетом защиты цели)
            damage = max(0, self.damage - target.armor)  # Урон не может быть отрицательным
            target.hp -= damage
            print(f"{self.name} попадает по {target.name} и наносит {damage} урона!")
        else:
            print(f"{self.name} промахивается!")

    def travel(self):
        import os
        rand_steps = random.randint(1, 5)  # не забудь поменять на 20 и 60
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Идём дальше...")
        for i in range(rand_steps):
            time.sleep(0.1)
