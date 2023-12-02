import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.all_price = None
        self.quantity = quantity
        self.__name = name
        self.price = price

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.all_price = self.price * self.quantity
        return self.all_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price

    def add_item_to_list(self):
        """
        Добавляет экземпляр Item в список all.
        """
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 10:
            self.__name = value
        else:
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, filename='src/items.csv'):
        # if not file_path:
        #     raise FileNotFoundError("Отсутствует файл item.csv")
        # elif not isinstance(file, InstantiateCSVError):
        #     raise InstantiateCSVError()
        # else:
        path = os.path.join(os.path.dirname(__file__), "..", filename)
        try:
            with open(path, 'r', newline='', encoding="windows-1251") as file:
                Item.all.clear()
                reader = csv.DictReader(file, delimiter=",")
                dict_reader = list(reader)
                for row in dict_reader:
                    cls.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except (KeyError, TypeError):
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(value: str) -> int:
        return int(float(value))

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name


class InstantiateCSVError(Exception):
    pass
