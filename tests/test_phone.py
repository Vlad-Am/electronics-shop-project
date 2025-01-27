

from src.phone import Phone


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    assert phone1 + phone1 == 10

