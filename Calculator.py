# # 1.решение с помощью if, elif и встроенного пакета math
# a = float(input('Введите число:'))
# b = (input('Введите операцию(+ или - или / или * или % или ** или //):'))
# c = float(input('Введите число:'))
#
# if b == '+':  # можно в строке print сразу записывать
#     d = a + c  # print(a+c)
#     print('Ответ:', d)
# elif b == '-':
#     d = a - c
#     print('Ответ:', d)
# elif b == '*':
#     d = a * c
#     print('Ответ:', d)
# elif b == '/':
#     d = a / c
#     print('Ответ:', d)
# elif b == '**':
#     d = a ** c
#     print('Ответ:', d)
# elif b == '%':
#     d = a % c
#     print('Ответ:', d)
# elif b == '//':
#     d = a // c
#     print('Ответ:', d)
#
# import math
#
# x = int(input('Введите число:'))
# y = int(input('Введите число:'))
# c = input('Введите:+,-,/,*,%,**,fac,log,sqrt,pow:')
# if c == '+':
#     print(x + y)
# elif c == 'fac':
#     print(math.factorial(x))
#     print(math.factorial(y))
# elif c == 'sqrt':
#     print(math.sqrt(x))
#     print(math.sqrt(y))
# elif c == 'pow':
#     print(math.pow(x, y))

# 2.решение с помощью функции def
# print("Добрый день! Вы вошли в калькулятор!")
# while True:
#     try:
#         choiсe = (input('Введите операцию, которую хотите совершить(+ , - , / , * , % , ** , //), 0- если хотите выйти!:'))
#         # if choiсe == "0":
#         #     print("Выход! До свидания!")
#         #     break
#         def exit():
#             return 0
#
#
#         if choiсe == "0":
#             print("Выход! До свидания!")
#             break
#         operations = ['+', '-', '/', '*', '%', '**', '//']
#         if choiсe not in operations:
#             raise ValueError('Error')
#             # print("Ошибка!!! Попробуйте еще раз!")
#             continue
#         a = float(input('Введите число:'))
#         b = float(input('Введите число:'))
#     # except ValueError:
#     #     print("Mistake")
#     #     continue
#
#     except Exception:
#         print("Что-то пошло не так! Произошла ошибка!!! Попрорбуйте еще раз!!!")
#         continue
#
#
#     def sum(a, b):
#         return a + b
#
#
#     if choiсe == '+':
#         print('Сумма равна:', round(sum(a, b), 2))
#
#
#     def razn(a, b):
#         return a - b
#
#
#     if choiсe == '-':
#         print('Разница равна:', round(razn(a, b), 2))
#
#
#     def pr(a, b):
#         return a * b
#
#
#     if choiсe == '*':
#         print('Произведение равно:', round(pr(a, b), 2))
#
#
#     def ost_delen(a, b):
#         return a % b
#
#
#     if choiсe == '%':
#         print('Остаток от деления равен:', round(ost_delen(a, b), 2))
#
#     try:
#         c = a/b
#     except ZeroDivisionError:
#         c = 0
#         print("Деление на ноль!!! Попробуйте еще раз!!!")
#         continue
#     def delen(a, b):
#         return a / b
#
#
#     if choiсe == '/':
#         print('Деление равно:', round(delen(a, b), 2))
#
#     def stepen(a, b):
#         return a ** b
#
#
#     if choiсe == '**':
#         print('Возведение в степень равно:', round(stepen(a, b), 2))