import math
import random


class Enemy:
    def __init__(self, name: str, hp: int, level: int, weapon: str, damage: int, armor: int, agility: int,
                 skill_points_given: int) -> None:
        self.name = name
        self.hp = hp
        self.agility = agility
        self.level = level
        self.skill_points_given = skill_points_given
        self.weapon = weapon
        self.damage = damage
        self.armor = armor

    def is_alive(self) -> bool:
        if self.hp > 0:
            return True
        return False

    def get_health_bar(self):
        return "[" + "+" * int(self.hp / 100 * 20) + " " * (20 - int(self.hp / 100 * 20)) + "]"

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
