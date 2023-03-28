N, M = map(int, input().split())
lst = [[0] * (N + 1) for _ in range(M + 1)]
cnt = 0
def dfs(y, x):
    global cnt
    if y > M:
        cnt += 1
        return
    if x == N:
        ny, nx = y + 1, 1
    else:
        ny, nx = y, x + 1

    dfs(ny, nx)
    if not lst[y - 1][x] or not lst[y][x - 1] or not lst[y - 1][x - 1]:
        lst[y][x] = 1
        dfs(ny, nx)
        lst[y][x] = 0

dfs(1, 1)
print(cnt)