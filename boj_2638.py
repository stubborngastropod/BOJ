from collections import deque
N, M = map(int, input().split())
lst = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0
for i in range(N):
    a = list(map(int, input().split()))
    lst.append(a)

while True:
    cheeze = deque([])
    # 공기부분 -1로 변환
    lst[0][0] = -1
    queue = deque([(0, 0)])
    visited = [[False] * M for _ in range(N)]
    while queue:
        a = queue.pop()
        visited[a[0]][a[1]] = True
        temp = []
        for k in range(4):
            if a[0] + dx[k] not in range(N) or a[1] + dy[k] not in range(M):
                continue
            elif lst[a[0] + dx[k]][a[1] + dy[k]] == -1 and not visited[a[0] + dx[k]][a[1] + dy[k]]:
                visited[a[0] + dx[k]][a[1] + dy[k]] = True
                queue.appendleft((a[0] + dx[k], a[1] + dy[k]))
            elif lst[a[0] + dx[k]][a[1] + dy[k]] == 0 and not visited[a[0] + dx[k]][a[1] + dy[k]]:
                temp.append((a[0] + dx[k], a[1] + dy[k]))
                visited[a[0] + dx[k]][a[1] + dy[k]] = True
                queue.appendleft((a[0] + dx[k], a[1] + dy[k]))
            elif lst[a[0] + dx[k]][a[1] + dy[k]] == 1 and not visited[a[0] + dx[k]][a[1] + dy[k]]:
                visited[a[0] + dx[k]][a[1] + dy[k]] = True
                cheeze.appendleft((a[0] + dx[k], a[1] + dy[k]))
        for i in temp:
            lst[i[0]][i[1]] = -1
    # 빈 리스트인지 확인
    cnt = 0
    for i in lst:
        if i == [-1] * M:
            cnt += 1
    if cnt == N:
        break
    # 녹는 치즈 찾기
    time += 1
    visited = [[False] * M for _ in range(N)]
    temp = []
    while cheeze:
        a = cheeze.pop()
        visited[a[0]][a[1]] = True
        air = 0
        for k in range(4):
            if lst[a[0] + dx[k]][a[1] + dy[k]] == -1:
                air += 1
        if air >= 2:
            temp.append(a)
    for i in temp:
        lst[i[0]][i[1]] = -1
print(time)