import sys
input = sys.stdin.readline

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

def move(i, j):
    n = lst[i][j]
    for d in range(1, 5):
        yy = i + dy[D[n][now_D[n]][d]]
        xx = j + dx[D[n][now_D[n]][d]]
        if yy not in range(N) or xx not in range(N):
            continue
        if not smell[yy][xx]:
            now_D[n] = D[n][now_D[n]][d]
            return yy, xx

    for d in range(1, 5):
        yy = i + dy[D[n][now_D[n]][d]]
        xx = j + dx[D[n][now_D[n]][d]]
        if yy not in range(N) or xx not in range(N):
            continue
        if smell[yy][xx][0] == n:
            now_D[n] = D[n][now_D[n]][d]
            return yy, xx

N, M, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
smell = [[[] for _ in range(N)] for __ in range(N)]
now_D = [0] + list(map(int, input().split()))

D = [[]]
for _ in range(M):
    temp_D = [[0] * M]
    for __ in range(4):
        temp_D.append([0] + list(map(int, input().split())))
    D.append(temp_D)
time = 0
shark = M

while shark > 1 and time <= 1000:
    time += 1
    # 냄새 처리
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j][1] -= 1
                if not smell[i][j][1]:
                    smell[i][j].clear()
            if lst[i][j]:
                smell[i][j] = [lst[i][j], k]
    # 이동
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if lst[i][j]:
                y, x = move(i, j)
                if temp[y][x]:
                    if temp[y][x] > lst[i][j]:
                        temp[y][x] = lst[i][j]
                    shark -= 1
                else:
                    temp[y][x] = lst[i][j]
    lst = temp
if time > 1000:
    print(-1)
else:
    print(time)