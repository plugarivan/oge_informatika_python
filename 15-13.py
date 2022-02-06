'''
Напишите программу, которая находит значение суммы x + (x**2/2!) + ... + (x**n/n!). Программа получает на вход
два натуральных числа x и n. Введённые числа не превышают 10.
'''
import math
x = int(input())
n = int(input())
summa = x
for i in range(2, n+1):
    summa += (x ** i / math.factorial(i))
print(round(summa, 2))