N = int(input())
wh_list = []

for i in range(N):
    a = list(map(int, input().split()))
    wh_list.append(a)

for i in wh_list:
    count = 0
    for j in wh_list:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    print(count + 1, end = ' ')