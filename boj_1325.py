from collections import deque
import sys

def bfs():
    cnt = 0
    while queue:
        now = queue.popleft()
        cnt += 1
        for n in adj[now]:
            if not visited[n]:
                visited[n] = True
                queue.append(n)
    return cnt

N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
hacking = [0] * (N + 1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[b].append(a)

for start in range(1, N + 1):
    visited = [False] * (N + 1)
    visited[start] = True
    queue = deque([start])
    hacking[start] = bfs()

ans_list = []
temp = 0
for i in range(1, N + 1):
    if hacking[i] > temp:
        ans_list.clear()
        temp = hacking[i]
        ans_list.append(i)
    elif hacking[i] == temp:
        ans_list.append(i)

print(*ans_list)