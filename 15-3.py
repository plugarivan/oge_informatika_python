'''
Напишите программу, которая в последовательности целых чисел определяет количество чётных чисел, кратных 7.
Программа получает на вход целые числа, количество введённых чисел неизвестно, последовательность чисел заканчивается
числом 0 (0 – признак окончания ввода, не входит в последовательность).
Количество чисел не превышает 1000. Введённые числа по модулю
не превышают 30 000.
Программа должна вывести одно число: количество чётных чисел, кратных 7.
'''

a = int(input('Введите число: '))
count = 0
while a != 0:
    if a % 7 == 0:
        count += 1
    a = int(input('Введите число: '))
print(count)