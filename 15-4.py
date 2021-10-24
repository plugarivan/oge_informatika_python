'''
Напишите программу, которая в последовательности натуральных чисел находит наименьшее число, кратное 3.
Программа получает на вход целые числа, количество введённых чисел неизвестно, последовательность чисел заканчивается
числом 0 (0 – признак окончания ввода, не является членом последовательности).
Количество чисел не превышает 1000. Введённые числа не превышают 30000.
Гарантируется, что в последовательности есть хотя бы одно число, кратное 3.
Программа должна вывести наименьшее число, кратное 3.
'''

a = int(input('Введите число: '))
minimum = 30001
while a != 0:
    if a % 3 == 0:
        minimum = a
    a = int(input('Введите число: '))
print(minimum)