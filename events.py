import random

import questionary

from Enemy.enemy import Enemy
from Player.character import Character
from fight import Fight


class Event:

    def __init__(self, name: str, description: str, base_chance, category: str, level_multiplier: float = None,
                 level_additive: float = None):
        self.name = name
        self.description = description
        self.base_chance = base_chance
        self.category = category
        self.level_multiplier = level_multiplier
        self.level_additive = level_additive

    def get_chance(self, player_level: int):
        chance = self.base_chance
        if self.level_multiplier:
            chance *= (1 + self.level_multiplier * player_level)
        if self.level_additive:
            chance += (self.level_additive * player_level)
        return max(0, min(chance, 1))

    def trigger(self, player: Character):

        if self.category == "Бой":
            print(self.description)
            if self.name == "Нападение бандитов":
                enemy = Enemy("Бандиты", 34, 1, "Клинок", 8, 3, 5, 2)
                fight = Fight(player, enemy)
                fight.battle()

        elif self.category == "Находка":
            question = questionary.select(
                self.description,
                choices=[
                    "Обыскать",
                    "Пройти мимо"
                ]
            ).ask()
            if self.name == "Найти потерянный кошелек":
                if question == "Обыскать":
                    player.money += random.randint(1, 20)
                    print(f"Вы заработали! Теперь у вас {player.money} денег.")
                else:
                    print("Вы прошли мимо...")




        elif self.category == "Мини-квест":
            pass


events = [
    # Боевые события
    Event("Нападение бандитов", "Группа бандитов пытается ограбить вас!", 0.2, "Бой", level_multiplier=-0.01),
    # Шанс уменьшается с уровнем
    Event("Дикие звери атакуют", "Вы подверглись нападению диких зверей.", 0.15, "Бой", level_additive=0.005),
    # Шанс немного увеличивается с уровнем
    Event("Засада гоблинов", "Гоблины устроили засаду на дороге.", 0.1, "Бой"),

    # События находок
    Event("Найти потерянный кошелек", "Вы нашли кошелек, полный монет!", 0.25, "Находка"),
    Event("Обнаружить тайник", "Вы обнаружили тайник с полезными припасами.", 0.1, "Находка", level_multiplier=0.02),
    # Шанс увеличивается с уровнем
    Event("Найти редкий цветок", "Вы нашли редкий цветок, который можно продать.", 0.05,
          "Находка"),

    # Мини-квесты
    Event("Помощь фермеру", "Фермер просит вас помочь ему защитить его скот от волков.", 0.15, "Мини-квест"),
    Event("Найти пропавшего ребенка", "Жители деревни просят вас найти пропавшего ребенка.", 0.08, "Мини-квест"),
    Event("Доставить письмо", "Вас просят доставить важное письмо в соседний город.", 0.12, "Мини-квест"),

    # Мирные события
    Event("Встретить торговца", "Вы встретили торговца, который предлагает редкие товары.", 0.2, "Мирное"),
    Event("Отдых у костра", "Вы отдохнули у костра и восстановили силы.", 0.15, "Мирное"),
    Event("Разговор с мудрецом", "Вы поговорили с мудрым человеком, который поделился с вами ценными знаниями.", 0.07,
          "Мирное", level_multiplier=0.01),  # Шанс немного увеличивается с уровнем
    Event("Наткнулись на руины", "Вы наткнулись на руины древнего храма.", 0.04, "Мирное")
]


def choose_event(player_level, category=None, previous_event=None):
    """Выбирает событие на основе его шанса и категории.
       Исключает повторение предыдущего события.
    """
    available_events = events[:]  # Создаем копию списка

    if previous_event:
        available_events = [e for e in available_events if e != previous_event]

    if category:
        available_events = [e for e in available_events if e.category == category]

    weighted_events = []
    for event in available_events:
        chance = event.get_chance(player_level)
        weighted_events.append((event, chance))

    if not weighted_events:
        return None  # Если нет доступных событий

    chosen_event = random.choices([e[0] for e in weighted_events], weights=[e[1] for e in weighted_events], k=1)[0]
    return chosen_event
