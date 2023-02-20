import sys
sys.setrecursionlimit(10**6)

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(y, x, visitlist):
    for d in range(8):
        if y + dy[d] in range(h) and x + dx[d] in range(w):
            if (y + dy[d], x + dx[d]) not in visitlist and MAP[y + dy[d]][x + dx[d]] == '1':
                visited[y + dy[d]][x + dx[d]] = 1
                visitlist.append((y + dy[d], x + dx[d]))
                dfs(y + dy[d], x + dx[d], visitlist)
            else:
                visited[y + dy[d]][x + dx[d]] = 1
while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    MAP = []
    for i in range(h):
        MAP.append(list(map(str, input().split())))
    visited = [[0] * w for _ in range(h)]
    visitlist = []
    cnt = 0
    for y in range(h):
        for x in range(w):
            find = False
            if not visited[y][x] and MAP[y][x] == '1':
                visitlist.append((y, x))
                visited[y][x] = 1
                dfs(y, x, visitlist)
                find = True
            if find:
                cnt += 1
    print(cnt)