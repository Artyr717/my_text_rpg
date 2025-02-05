from .items import Weapon, Potion
from tabulate import tabulate


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str, quantity: int = 1):
        if item not in self.items:
            self.items[item] = quantity
        else:
            self.items[item] += quantity

    def list_items(self):  # Теперь для tabulate
        """
        Выводит список предметов с помощью tabulate.
        """
        if not self.items:
            print("Ваш инвентарь пуст.")
            return

        headers = ["Название", "Тип", "Цена", "Урон", "Восстановление", "Количество"]
        table_data = []

        for item, quantity in self.items.items():
            # Получаем значения атрибутов предмета
            row = [
                item.name,
                item.item_type,
                item.price,
                item.damage if isinstance(item, Weapon) else "-",  # Урон, если это Weapon
                item.effect_amount if isinstance(item, Potion) else "-",  # Восстановление, если это Potion
                quantity
            ]
            table_data.append(row)

        print(tabulate(table_data, headers=headers, tablefmt="heavy_grid"))
