from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
    print(1)
if N < K:
    visited = [[0, 1] for _ in range(100001)]
    queue = deque([N])

    while queue:
        now = queue.popleft()
        if now == K:
            break
        if 0 <= now + 1 <= 100000:
            if not visited[now + 1][0]:
                visited[now + 1][0] = visited[now][0] + 1
                visited[now + 1][1] = visited[now][1]
                queue.append(now + 1)
            elif visited[now + 1][0] == visited[now][0] + 1:
                visited[now + 1][1] += visited[now][1]
        if 0 <= now - 1 <= 100000:
            if not visited[now - 1][0]:
                visited[now - 1][0] = visited[now][0] + 1
                visited[now - 1][1] = visited[now][1]
                queue.append(now - 1)
            elif visited[now - 1][0] == visited[now][0] + 1:
                visited[now - 1][1] += visited[now][1]
        if 0 <= now * 2 <= 100000:
            if not visited[now * 2][0]:
                visited[now * 2][0] = visited[now][0] + 1
                visited[now * 2][1] = visited[now][1]
                queue.append(now * 2)
            elif visited[now * 2][0] == visited[now][0] + 1:
                visited[now * 2][1] += visited[now][1]

    print(visited[K][0])
    print(visited[K][1])

if N > K:
    print(N - K)
    print(1)