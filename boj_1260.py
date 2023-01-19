N, M, V = map(int, input().split())

# 2차원 인접행렬
adj_matrix = []
for i in range(N + 1):
    adj_matrix.append([0] * (N + 1))

for i in range(M):
    a, b = map(int, input().split())
    adj_matrix[a][b], adj_matrix[b][a] = 1, 1

visited = []

def dfs(graph, root):
    visited.append(root)
    print(root, end = ' ')
    for i in range(1, N + 1):
        if graph[root][i] == 1 and i not in visited:
            newroot = i
            dfs(graph, newroot)
        else:
            None

dfs(adj_matrix, V)