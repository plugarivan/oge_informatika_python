'''
Напишите программу, которая по двум данным натуральным числам a и b, не превосходящим 30000,
подсчитывает количество чётных натуральных чисел на отрезке [a, b] (включая концы отрезка).
Программа получает на вход два натуральных числа a и b, при этом гарантируется, что что 1 <= a <= b <= 30000.
Программа должна вывести одно число: количество чётных чисел на отрезке [a, b].
'''
a = int(input())
b = int(input())
count = 0
for i in range(a, b+1):
    if i % 2 == 0:
        count += 1
print(count)