from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def island():
    global cnt
    while queue:
        qpop = queue.popleft()
        ci, cj = qpop[0], qpop[1]
        find = 0
        for d in range(4):
            ni, nj = ci + dy[d], cj + dx[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if visited[ni][nj]:
                continue
            if nation[ni][nj] == 1:
                nation[ni][nj] = cnt
                queue.append((ni, nj))
                find += 1
        if not find:
            nation[ci][cj] = cnt

def bridge(n):
    global ans
    while queue:
        qpop = queue.popleft()
        ci, cj, bridgelen = qpop[0], qpop[1], qpop[2]
        for d in range(4):
            ni, nj = ci + dy[d], cj + dx[d]
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if nation[ni][nj] == n:
                continue
            if visited[ni][nj]:
                continue
            if nation[ni][nj]:
                if bridgelen < ans:
                    ans = bridgelen
                    break
            visited[ni][nj] = 1
            queue.append((ni, nj, bridgelen + 1))

N = int(input())
nation = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
visited = [[0] * (N + 1) for _ in range(N + 1)]
cnt = 2
for i in range(N):
    for j in range(N):
        if nation[i][j] == 1:
            queue.append((i, j))
            island()
            cnt += 1

ans = 1e4
for i in range(N):
    for j in range(N):
        if nation[i][j]:
            visited = [[0] * (N + 1) for _ in range(N + 1)]
            visited[i][j] = 1
            queue.append((i, j, 0))
            bridge(nation[i][j])

print(ans)