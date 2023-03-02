import sys
input = sys.stdin.readline

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
lst = [[[] for _ in range(N + 1)] for __ in range(N + 1)]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    lst[r][c].append([m, s, d])
for move in range(K):
    # 이동
    temp = [[[] for _ in range(N + 1)] for __ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            while lst[i][j]:
                fireball = lst[i][j].pop()
                v, d = fireball[1], fireball[2]
                yy, xx = i + dy[d] * v, j + dx[d] * v
                if yy not in range(1, N + 1):
                    yy = yy % N
                    if yy == 0:
                        yy = -1
                if xx not in range(1, N + 1):
                    xx = xx % N
                    if xx == 0:
                        xx = -1
                temp[yy][xx].append(fireball)
    lst = temp
    temp = [[[] for _ in range(N + 1)] for __ in range(N + 1)]
    # 합체, 분리, 소멸
    for i in range(N + 1):
        for j in range(N + 1):
            if len(lst[i][j]) > 1:
                new_m = sum(list(zip(*lst[i][j]))[0]) // 5
                if new_m == 0:
                    continue
                new_s = sum(list(zip(*lst[i][j]))[1]) // len(lst[i][j])
                new_d = [0, 2, 4, 6]
                for k in range(1, len(lst[i][j])):
                    if (lst[i][j][k][2] + lst[i][j][k - 1][2]) % 2:
                        new_d = [1, 3, 5, 7]
                for d in new_d:
                    temp[i][j].append([new_m, new_s, d])
            elif lst[i][j]:
                temp[i][j].append(lst[i][j][0])
    lst = temp
ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        while lst[i][j]:
            temp = lst[i][j].pop()
            ans += temp[0]
print(ans)