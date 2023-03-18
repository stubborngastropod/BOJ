import sys
input = sys.stdin.readline
from collections import deque

def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = True
    flag = 1
    while q:
        for stu in q:
            if flag:
                blue.append(stu)
            else:
                white.append(stu)
        for _ in range(len(q)):
            now = q.popleft()
            for next in adj[now]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
        flag = abs(flag - 1)

n = int(input())
adj = [0]
for i in range(n):
    a, *b = map(int, input().split())
    adj.append(b)

blue = []
white = []
visited = [False] * (n + 1)
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
blue.sort()
white.sort()
print(len(blue))
print(*blue)
print(len(white))
print(*white)