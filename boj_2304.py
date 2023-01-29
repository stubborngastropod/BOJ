N = int(input())
cols = []
for i in range(N):
    LH = list(map(int, input().split()))
    cols.append(LH)
cols1 = sorted(cols, key = lambda x: x[0])
cols2 = sorted(cols, reverse = True, key = lambda x: x[0])

list1, list2 = [], []
for i in cols:
    list1.append(i[0])
    list2.append(i[1])
A = max(list1) - min(list1) + 1
B = max(list2)

s1 = 0
a, b = cols1[0][0], cols1[0][1]
for i in cols1[1:]:
    if i[1] > b:
        a = i[0] - a
        s1 += a * (i[1] - b)
        a = cols1[0][0]
        b = i[1]

s2 = 0
a, b = cols2[0][0], cols2[0][1]
for i in cols2[1:]:
    if i[1] > b:
        a = a - i[0]
        s2 += a * (i[1] - b)
        a = cols2[0][0]
        b = i[1]

print((A * B) - (s1 + s2))