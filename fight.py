from random import choice

from Enemy.enemy import Enemy
from Player.character import Character
import questionary


def player_choice():
    return questionary.select(
        "Выберите действие:",
        [
            "Атаковать",
            "Использовать предмет",
            "Сбежать"]
    ).ask()


class Fight:
    def __init__(self, player: Character, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.round = 1
        self.win = False
        self.skip = False  # Для побега !!!!!!!!!

    def battle(self):
        while self.player.is_alive() and self.enemy.is_alive():
            print(f"\n--- Раунд {self.round} ---")
            print(f"{self.player.name}\n{self.player.get_health_bar()}")
            print(f"{self.enemy.name}\n{self.enemy.get_health_bar()}")

            print("\nВаш ход!")
            turn_choice = player_choice()
            if turn_choice == "Атаковать":
                self.player.attack(self.enemy)
            # TODO: Доделать "Использовать предмет" и "Сбежать"

            if not self.enemy.is_alive():
                print(f"{self.enemy.name} повержен! Победа!")
                self.win = True
                break

            print("\nХод противника!")
            self.enemy.attack(self.player)

            if not self.player.is_alive():
                print(f"Вы повержены! {self.enemy.name} победил!")
                break  # TODO: Продумать, как реализовать респавн игрока

            self.round += 1

        if self.win:
            pass  # TODO: Выдать награду за противника игроку (награда прописана в противнике)
