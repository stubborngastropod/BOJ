from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
N, M = map(int, input().split())
MAP = [list(input().strip()) for _ in range(N)]

q = deque()
q.append((0, 0, 0)) # y, x, cnt, wall
visited = [[[0, 0] for _ in range(M)] for __ in range(N)]
visited[0][0][0] = 1
ans = -1
while q:
    now_y, now_x, wall = q.popleft()
    if (now_y, now_x) == (N - 1, M - 1):
        ans = visited[now_y][now_x][wall]
        break
    for d in range(4):
        nxt_y, nxt_x = now_y + dy[d], now_x + dx[d]
        if nxt_y not in range(N) or nxt_x not in range(M):
            continue
        if not wall and MAP[nxt_y][nxt_x] == '1':
            visited[nxt_y][nxt_x][1] = visited[now_y][now_x][wall] + 1
            q.append((nxt_y, nxt_x, 1))
        if not visited[nxt_y][nxt_x][wall] and MAP[nxt_y][nxt_x] == '0':
            visited[nxt_y][nxt_x][wall] = visited[now_y][now_x][wall] + 1
            q.append((nxt_y, nxt_x, wall))

print(ans)