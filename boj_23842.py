num_list = [[0, 6],[1, 2],[2, 5],[3, 5],[4, 4],[5, 5],[6, 6],[7, 3],[8, 7],[9, 6]]
stick_list = []
answer = int(input()) - 4
ok = 0

for i in range(100):
    for j in range(10):
        if i // 10 == num_list[j][0]:
            a = num_list[j][1]
        if i % 10 == num_list[j][0]:
            b = num_list[j][1]
    stick_list.append([i, a + b])

print(stick_list)

for i in range(100):
    for j in range(100):
        for k in range(100):
            if i + j == k:
                if stick_list[i][1] + stick_list[j][1] + stick_list[k][1] == answer:
                    a, b, c = i, j, k
                    ok += 1
def zero(a):
    if a < 10:
        return f'0{a}'
    else:
        return a

if ok > 0:
    print(f'{zero(a)}+{zero(b)}={zero(c)}')
else:
    print('impossible')