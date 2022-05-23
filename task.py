with open('107_26.txt') as f:
    n = int(f.readline())
    d = dict()
    for i in range(n):
        row, mesto = map(int, f.readline().split())
        if row in d:
            d[row].append(mesto)
        else:
            d[row] = [mesto]
for row in sorted(d):
    d[row].sort()
    for a, b in zip(d[row], d[row][1:]):
        if b - a == 14:
            print(row, a)






