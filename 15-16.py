'''
Напишите программу, которая в последовательности натуральных чисел определяет максимальное число, оканчивающееся на 3.
Программа получает на вход количество чисел в последовательности, а затем сами числа.
'''
k = int(input())
maximum = 0
for i in range(k):
    number = int(input())
    if number % 10 == 3:
        maximum = max(maximum, number)
print(maximum)