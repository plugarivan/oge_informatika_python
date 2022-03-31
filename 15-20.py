'''

'''
number = input()
s = []
for i in range(2, len(number)):
    s.append(number[i - 2] + number[i - 1] + number[i])
print(s)
mx = 0
for c in s:
    summa = sum(map(int, c))
    mx = max(summa, mx)
print(mx)