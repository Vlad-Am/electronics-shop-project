from src.item import Item


# class MixinLog:
#
#     def __init__(self, name: str, price: float, quantity: int, language="EN"):
#         super().__init__(name, price, quantity)
#         if language != "EN":
#             self.__language = language
#
#     def change_lang(self):
#         if self.__language == "EN":
#             self.__language = "RU"
#         else:
#             self.__language = "EN"
#
#     @property
#     def language(self):
#         return self.__language


class Keyboard(Item):
    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):
        if self.__language != "EN":
            self.__language = "EN"
        else:
            self.__language = "RU"

    @property
    def language(self):
        return self.__language


# k1 = Keyboard('Dark Project KD87A', 9600, 5)
# print(Keyboard.__mro__)
