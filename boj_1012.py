from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    land = [[0] * M for _ in range(N)]
    cab = []
    cnt = 0
    for i in range(K):
        a, b = map(int, input().split())
        cab.append((a, b))
        land[b][a] = 1

    while cab:
        cnt += 1
        a = cab.pop()
        queue = deque([a])
        while queue:
            node = queue.pop()
            for j in range(4):
                if (node[0] + dx[j], node[1] + dy[j]) in cab:
                    queue.appendleft((node[0] + dx[j], node[1] + dy[j]))
                    cab.remove((node[0] + dx[j], node[1] + dy[j]))

    print(cnt)