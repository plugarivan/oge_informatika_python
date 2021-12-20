'''

'''
a = input()
count = 0
while a != '0':
    if a[0] == a[-1]:
        count += 1
    a = input()
if count > 0:
    print(count)
else:
    print('NO')