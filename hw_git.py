text = "Сгенерировать список из 10 чисел. Диапазон чисел - 0, 9.\nПосчитайте, сколько в нем пар элементов, равных друг другу.\nЛюбые два элемента, равные друг другу образуют одну пару,которую необходимо посчитать. При этом образованная пара не участвуют в формировании других пар.\n* Вывести цифру из списка - количество пар с этой цифрой.\nНапример, [1, 1, 1, 1].\n1 - 2 Результат: 2 пары."
print(text)
# import random
#
# a = [random.randint(0, 9) for i in range(10)]
# print(a)
# p = 0
# for i in set(a):
#     p += a.count(i) // 2
#     print(i, '-', a.count(i) // 2)
# print('Пар в списке: ', p)

# text1 = "Для списка"
# print(text1)
# a = [1, 1, 1, 1, 3, 2, 3, 6]
# for i in set(a):
#     print(i, "-", a.count(i) // 2)

text2 = "Решение со словарем"
print(text2)
# a = [1, 1, 2, 4, 2, 3, 5, 2, 6, 2, 1, 3, 5]
# a.sort()
# print(a)
# r = 0
# dict = {}
# set_new = []
# for i in set(a):
#     print(i, "-", a.count(i) // 2)
#     r += a.count(i) // 2
#     res = a.count(i) // 2
#     set_new.append(res)
#     if dict.get(res):
#         dict[res] += 1
#     else:
#         dict[res] = 1
# print(dict)
# print(r)