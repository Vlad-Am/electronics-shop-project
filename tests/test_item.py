"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item1.calculate_total_price() == 200000

    assert item1.apply_discount() == 10000
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 5000
    item1.add_item_to_list()
    assert len(Item.all) == 1


def test_name():
    item1 = Item("Ноутбук", 1000, 3)
    assert item1.name == "Ноутбук"
    item1.name = "Ноутбук и еще кое-что для теста вызова функции срезания данных, если наименование слишком длинное"
    assert item1.name == "Ноутбук и "


def test_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 6
    assert Item.all[2].quantity == "3"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == "Смартфон"


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
