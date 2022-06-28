# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
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
# 1. Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры. Остальные цифры должны заменяться звездочками
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
# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
#
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
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