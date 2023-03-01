import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
R, C, D = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

now = [R, C, D]
while True:
    r, c, d = now[0], now[1], now[2]
    if not room[r][c]:
        room[r][c] = 2
        cnt += 1
    find = False
    for i in range(4):
        if r + dy[i] in range(1, N - 1) and c + dx[i] in range(1, M - 1):
            if not room[r + dy[i]][c + dx[i]]:
                find = True
    if find:
        now = [r, c, (d + 3) % 4]
        if r + dy[(d + 3) % 4] in range(1, N - 1) and c + dx[(d + 3) % 4] in range(1, M - 1):
            if not room[r + dy[(d + 3) % 4]][c + dx[(d + 3) % 4]]:
                now = [r + dy[(d + 3) % 4], c + dx[(d + 3) % 4], (d + 3) % 4]
    else:
        if room[r - dy[d]][c - dx[d]] == 1:
            break
        now = [r - dy[d], c - dx[d], d]

print(cnt)