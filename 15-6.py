'''
Введите с клавиатуры 5 положительных целых чисел. Вычислите сумму тех из них, которые делятся на 4 и при этом
заканчиваются на 6. Программа должна вывести одно число: сумму чисел, введенных с клавиатуры, кратных 4 и оканчивающихся на 6.
'''
summa = 0
for i in range(5):
    a = int(input())
    if a % 4 == 0 and a % 10 == 6:
        summa += a
print(summa)