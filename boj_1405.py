dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, E, W, S, N = map(int, input().split())
dirs = [E, W, S, N]
def dfs(y, x, direction, visited, cnt):
    global percentage
    if (y, x) in visited:
        temp = 1
        for i in direction:
            temp *= dirs[i] / 100
        percentage -= temp
        return
    if cnt == n:
        return
    for d in range(4):
        dfs(y + dy[d], x + dx[d], direction + [d], visited + [(y, x)], cnt + 1)

percentage = 1
dfs(0, 0, [], [], 0)

print(percentage)