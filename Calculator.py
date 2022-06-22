a = float(input('Введите число:'))
b = (input('Введите операцию(+ или - или / или * или % или ** или //):'))
c = float(input('Введите число:'))

if b == '+':  # можно в строке print сразу записывать
    d = a + c  # print(a+c)
    print('Ответ:', d)
elif b == '-':
    d = a - c
    print('Ответ:', d)
elif b == '*':
    d = a * c
    print('Ответ:', d)
elif b == '/':
    d = a / c
    print('Ответ:', d)
elif b == '**':
    d = a ** c
    print('Ответ:', d)
elif b == '%':
    d = a % c
    print('Ответ:', d)
elif b == '//':
    d = a // c
    print('Ответ:', d)

import math

x = int(input('Введите число:'))
y = int(input('Введите число:'))
c = input('Введите:+,-,/,*,%,**,fac,log,sqrt,pow:')
if c == '+':
    print(x + y)
elif c == 'fac':
    print(math.factorial(x))
    print(math.factorial(y))
elif c == 'sqrt':
    print(math.sqrt(x))
    print(math.sqrt(y))
elif c == 'pow':
    print(math.pow(x, y))