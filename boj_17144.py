import sys
from collections import deque
input = sys.stdin.readline
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
R, C, T = map(int, input().split())
room = []
for i in range(R):
    room.append(deque(list(map(int, input().split()))))

for i in range(R):
    if room[i][0] == -1:
        clean = i + 1
        break

for time in range(T):
    # 확산
    spread = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 미세먼지가 있을 때 임시로 퍼질 먼지를 저장
            if room[i][j] > 0:
                temp = room[i][j] // 5
                for d in range(4):
                    if i + delta[d][0] in range(R) and j + delta[d][1] in range(C):
                        if room[i + delta[d][0]][j + delta[d][1]] > -1:
                            spread[i + delta[d][0]][j + delta[d][1]] += temp
                            room[i][j] -= temp

    # 저장된 퍼질 먼지를 더해주기
    for i in range(R):
        for j in range(C):
            room[i][j] += spread[i][j]

    # 공기 정화(위)
    for i in range(clean - 2, 0, -1):
        room[i][0] = room[i - 1][0]
    room[0].popleft()
    room[0].append(0)
    for i in range(clean - 1):
        room[i][-1] = room[i + 1][-1]
    room[clean - 1].pop()
    room[clean - 1][0] = 0
    room[clean - 1].appendleft(-1)

    # 공기 정화(아래)
    for i in range(clean + 1, R - 1):
        room[i][0] = room[i + 1][0]
    room[R - 1].popleft()
    room[R - 1].append(0)
    for i in range(R - 1, clean, -1):
        room[i][-1] = room[i - 1][-1]
    room[clean].pop()
    room[clean][0] = 0
    room[clean].appendleft(-1)

ans = 2
for i in range(R):
    for j in range(C):
        ans += room[i][j]
print(ans)