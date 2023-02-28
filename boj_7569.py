from collections import deque
import sys
input = sys.stdin.readline

dz = [0, 0, 0, 0, -1, 1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]

def bfs():
    global ripe
    day = 0
    while queue:
        qpop = queue.popleft()
        a, b, c, day = qpop[0], qpop[1], qpop[2], qpop[3]
        visited[a][b][c] = True

        for d in range(6):
            if a + dz[d] in range(H) and b + dy[d] in range(N) and c + dx[d] in range(M):
                if tomato[a + dz[d]][b + dy[d]][c + dx[d]] == 0 and not visited[a + dz[d]][b + dy[d]][c + dx[d]]:
                    visited[a + dz[d]][b + dy[d]][c + dx[d]] = True
                    tomato[a + dz[d]][b + dy[d]][c + dx[d]] = 1
                    ripe += 1
                    queue.append((a + dz[d], b + dy[d], c + dx[d], day + 1))

    if ripe != cnt_0:
        print(-1)
    else:
        print(day)



M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
visited = [[[False] * M for _ in range(N)] for __ in range(H)]
queue = deque()
cnt_0 = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x] == 0:
                cnt_0 += 1
            if tomato[z][y][x] == 1:
                queue.append([z, y, x, 0])
ripe = 0
bfs()
