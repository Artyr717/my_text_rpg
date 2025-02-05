import random
import time

from Player.inventory import Inventory


class Character:

    def __init__(self, name: str):
        ### Stats ###
        self.level = 1
        self.experience = 0.0
        self.hp = 100
        self.money = 0
        self.skill_points = 0

        ### Base Info ###
        self.name = name
        self.weapon = "Кулаки"
        self.inventory = Inventory()

    def __str__(self):
        data = f"""
    ------------------------
    Имя персонажа: {self.name}
    Уровень персонажа: {self.level}
    Опыт: {self.experience}
    Здоровье: {self.hp}
    Оружие: {self.weapon}
    Деньги: {self.money}
    ------------------------
    """

        return data

    def set_weapon(self, weapon: str):
        self.weapon = weapon

    def set_money(self, money: float):
        self.money = money

    def set_hp(self, hp: int):
        self.hp = hp

    def set_level(self, level: int):
        self.level = level

    def set_experience(self, experience: float):
        self.experience = experience

    def travel(self):
        import os
        rand_steps = random.randint(20, 60)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Идём дальше...")
        for i in range(rand_steps):
            time.sleep(0.1)
