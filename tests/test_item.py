"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src import item
from src.item import Item


def test_item():
    item1 = item.Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item1.calculate_total_price() == 200000

    assert item1.apply_discount() == 10000
    item1.pay_rate = 0.5
    assert item1.apply_discount() == 5000
    item1.add_item_to_list()
    assert len(Item.all) == 1
