N, M = map(int, input().split())
adj = []
cnt = 0

for i in range(N + 1):
    adj.append([0]*(N + 1))

for i in range(M):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1

visited = [False] * (N + 1)

def dfs(start, visited):
    visited[start] = True
    for i in range(1, N + 1):
        if adj[start][i] == 1 and not visited[i]:
            dfs(i, visited)

for i in range(1, N + 1):
    if visited[i] == False:
        dfs(i, visited)
        cnt += 1

print(cnt)