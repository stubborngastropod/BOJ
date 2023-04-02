from collections import deque
import sys
input = sys.stdin.readline
def bfs(n):
    visited[f1] = True
    q = deque()
    q.append(f1)
    while q:
        now = q.popleft()
        if now == f2:
            return True
        for nxt, limit in adj[now]:
            if not visited[nxt] and limit >= n:
                q.append(nxt)
                visited[nxt] = True
    return False

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
f1, f2 = map(int, input().split())
l, r = 1, 1000000000
while l <= r:
    visited = [False] * (N + 1)
    m = (l + r) // 2
    if bfs(m):
        l = m + 1
    else:
        r = m - 1
print(r)