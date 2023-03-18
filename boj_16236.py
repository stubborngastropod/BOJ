from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(y, x):
    global find
    global start
    global dist
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True
    q = []
    q.append([y, x, 0])
    while q:
        now = q.pop(0)
        if 1 <= lst[now[0]][now[1]] < size:
            find = True
            start = [now[0], now[1]]
            lst[now[0]][now[1]] = 0
            dist = now[2]
            return
        for d in range(4):
            yy = now[0] + dy[d]
            xx = now[1] + dx[d]
            if yy not in range(N) or xx not in range(N):
                continue
            if lst[yy][xx] > size:
                continue
            if visited[yy][xx]:
                continue

            visited[yy][xx] = True
            q.append([yy, xx, now[2] + 1])
            q.sort(key=lambda x: (x[2],x[0],x[1]))

# 입력값
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
# 상어 초기 위치
for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:
            start = [i, j]
            lst[i][j] = 0
size = 2
eat = 0
time = 0
while True:
    find = False
    dist = 0
    bfs(start[0], start[1])
    if not find:
        break
    time += dist
    eat += 1
    if eat == size:
        eat = 0
        size += 1

print(time)