N, M, V = map(int, input().split())

# 2차원 인접행렬
adj_matrix = []
for i in range(N + 1):
    adj_matrix.append([0] * (N + 1))

for i in range(M):
    a, b = map(int, input().split())
    adj_matrix[a][b], adj_matrix[b][a] = 1, 1

dfs_visited = []
bfs_visited = []

def dfs(graph, root):
    dfs_visited.append(root)
    print(root, end = ' ')
    for i in range(1, N + 1):
        if graph[root][i] == 1 and i not in dsf_visited:
            newroot = i
            dfs(graph, newroot)
        else:
            None

def bfs(graph, root):
    queue = []
    bfs_visited.append(root)
    print(root, end=' ')
    for i in range(1, N + 1):
        if graph[root][i] == 1 and i not in bfs_visited:
            queue.append(i)
        else:
            None
        bfs_visited.pop()
        newroot = bfs_visited.pop()

dfs(adj_matrix, V)