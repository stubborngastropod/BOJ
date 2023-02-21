N, M = map(int, input().split())
def dfs(n, visited):
    if len(visited) == M:
        print(*visited)
    for i in range(1, N + 1):
        if i not in visited:
            dfs(i, visited + [i])

for j in range(1, N + 1):
    dfs(j, [j])