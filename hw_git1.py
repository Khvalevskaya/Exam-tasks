text ="В текстовый файл построчно записаны фамилия и имя учащихся класса\nи его оценка за контрольную.\nВывести на экран всех учащихся,\nчья оценка меньше 3 баллов \nпосчитать средний балл по классу"
print(text)
# with open("1.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines)
#     summa = 0
# for line in lines:
#     ochenka = int(line[-2])              #определяем место оценки
#     if ochenka < 3 and ochenka > 0:      # если оценка меньше 3
#         print(line)
#     summa += ochenka                     # считаем сумму всех оценок
# # print(summa)
# # print(len(lines))
# print("Средний балл по классу:", summa/len(lines))

with open("1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
students = []
suma = 0
for i in lines:
    i = i.replace("\n", "")
    i = i.split()
    students.append(i)
print(students)
for a in students:
    suma += int(a[2])
    if int(a[2]) < 3:
        print('Ниже 3 баллов:', a[0], a[1])
print("Средний балл: %.2f" % (suma / len(students)))