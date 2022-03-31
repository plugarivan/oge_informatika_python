number = input()
s = []
for i in range(len(number)-2):
    s.append(number[i] + number[i + 1] + number[i + 2])
maximum = 0
for c in s:
    summa = sum(map(int, c))
    maximum = max(maximum, summa)
print(maximum)

'''
and or not == <=
'''