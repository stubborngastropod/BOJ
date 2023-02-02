n = int(input())
a, b = map(int, input().split())
m = int(input())
adj = []
visited = [False] * (n+1)
for i in range(n+1):
    adj.append([0]*(n+1))
for i in range(m):
    x, y = map(int, input().split())
    adj[x][y] = adj[y][x] = 1

def dfs(graph, start, end, visited, cnt):
    global res
    visited[start] = True
    if start == end:
        res = cnt
    else:
        for i in range(1, n+1):
            if graph[start][i] == 1 and not visited[i]:
                dfs(graph, i, end, visited, cnt+1)

res = 0
dfs(adj, a, b, visited, 0)

if res == 0:
    print(-1)
else:
    print(res)