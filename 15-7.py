'''

'''
a = int(input())
summa, count = 0, 0
while a != 0:
    if 9 < a < 100:
        summa += a
        count += 1
    a = int(input())
if count > 0:
    print(round(summa / count, 1))
else:
    print('NO')