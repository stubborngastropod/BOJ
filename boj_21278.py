from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0] * (N + 1) for _ in range(N + 1)]
ans = (0, 0, 1e10)
for i in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1

def bfs(n):
    q = deque()
    q.append((n, 1))
    visited = [n]
    while q:
        now, c = q.popleft()
        for nxt in range(1, N + 1):
            if adj[now][nxt] == 1 and nxt not in visited:
                visited.append(nxt)
                adj[n][nxt] = c
                q.append((nxt, c + 1))

for i in range(1, N + 1):
    bfs(i)

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        temp = 0
        for k in range(1, N + 1):
            temp += min([adj[i][k], adj[j][k]])*2
        if temp < ans[2]:
            ans = (i, j, temp)
print(*ans)