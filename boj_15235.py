n = int(input())
conlist = list(map(int, input().split()))
timelist = []
count = 0
for i in range(n):
    timelist.append(0)
success = 0
while sum(conlist) > 0:
    for i in range(n):
        if conlist[i] != 0:
            count += 1
            conlist[i] -= 1
            if conlist[i] == 0:
                timelist[i] = count
        else:
            pass

for i in timelist:
    print(i, end = ' ')
