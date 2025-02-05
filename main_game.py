import questionary
import events
from Player.character import Character
import random

from Player.inventory import Inventory
from Player.items import Weapon, Potion, SellableItem


class Game:
    def __init__(self, seed_map: int = 11042008, save_data_file: str = None):
        self.seed_map = seed_map
        self.save_data_file = save_data_file
        self.character: Character = None
        random.seed(seed_map)

    def load_save_data(self):  # TODO: Сделать загрузку сохранения
        pass

    def save_data(self):  # TODO: Сделать сохранение данных
        pass

    def create_player(self):
        name = input("Введите имя для персонажа\n----->\t")
        if name.strip():
            self.character = Character(name)

    def run(self):
        self.create_player()
        player = self.character
        prev_event = None
        sword = Weapon("Стальной меч", price=24, damage=20)
        small_potion = Potion("Маленькое зелье здоровья", price=10,
                              effect_amount=30)
        gold_coin = SellableItem("Золотая монета", price=1)
        player.inventory.add_item(sword)
        player.inventory.add_item(small_potion, 2)
        player.inventory.add_item(gold_coin, 50)
        while True:
            chosen_event = events.choose_event(player.level, previous_event=prev_event)
            base_question = questionary.select(
                "Выберите действие",
                choices=[
                    "Идти дальше",
                    "Заглянуть в инвентарь",
                    "Вернуться в Город",  # TODO: Сделать локации городов для игрока и логику для городов
                    "Спуститься в подземелье к Боссу"
                ]
            )
            answer = base_question.ask()  # Получаем ответ от игрока
            if chosen_event:

                if answer == "Идти дальше":
                    player.travel()
                elif answer == "Заглянуть в инвентарь":
                    player.inventory.list_items()

                chosen_event.trigger(player)
                prev_event = chosen_event
                input("Нажмите Enter для продолжения")
            else:
                print("Нет доступных событий для этой категории или все события были повторены.")


game = Game()
game.run()
