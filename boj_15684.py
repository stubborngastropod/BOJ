import sys
input = sys.stdin.readline

def go(lst):
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if lst[j][now]:
                now += lst[j][now]
        if now != i:
            return False
    return True

def dfs(y, x, cnt):
    global ans
    if cnt == 3:
        if ans == 4 and go(ladder):
            ans = 3
            return
        return
    if y == H + 1:
        if cnt < ans and go(ladder):
            ans = cnt
            return
        return
    if x == N - 1:
        ny, nx = y + 1, 1
    else:
        ny, nx = y, x + 1

    if cnt < 3 and not ladder[y][x] and not ladder[y][x+1]:
        ladder[y][x], ladder[y][x+1] = 1, -1
        dfs(ny, nx, cnt + 1)
        ladder[y][x] = ladder[y][x + 1] = 0
    dfs(ny, nx, cnt)

    

N, M, H = map(int, input().split())
ladder = [[0] * (N + 1) for _ in range(H + 1)]
for _ in range(M):
    y, x = map(int, input().split())
    ladder[y][x] = 1
    ladder[y][x + 1] = -1
ans = 4
dfs(1, 1, 0)
if ans == 4:
    print(-1)
else:
    print(ans)