# 2
# def polind(text):
#
#     text1 = text.replace(" ", "")
#
#     if text1[::-1] == text1[::1]:
#         print("Это палиндром!")
#     else:
#         print("Это не палиндром!")
# text2 = input("Введите текс:")
# polind(text2)

# def new_card(card):
#     for i in card:
#         if len(card) == 16:
#
#
#          return card[-1], card[-2], card[-3], card[-4]
#
#
#
# cardnew = input("Введите номер карты без пробелов")
# print(new_card(cardnew))

# 1 задача
# def new_card(card):
#     result = ''
#     index = 12
#     for i, num in enumerate(card):
#         if i >= 12:
#             result += num
#         else:
#             result += '*'
#
#     return result
#
#
# cardnew = input("Введите номер карты без пробелов")
# print(new_card(cardnew))


#
class Tomato:
    states = {1: "green", 2: "yellow", 3: "red"}

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return "Томат созрел"
        else:
            return "Еще не созрел"


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if all(tomato.is_ripe()):
                return True
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Gardener работает и plant становится более зрелым")

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Plants созрели и урожай собран")
        else:
            print("Урожай еще не созрел!!!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:......")

Gardener.knowledge_base()
tomat = TomatoBush(12)
worker = Gardener("DIMA", tomat)
worker.work()
worker.harvest()