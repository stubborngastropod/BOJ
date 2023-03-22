import sys
input = sys.stdin.readline

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

def tictactoe(y, x, ox):
    for d in range(8):
        if y + dy[d] not in range(3) or x + dx[d] not in range(3):
            continue
        if lst[y + dy[d]][x + dx[d]] == ox:
            if y + dy[d]*2 in range(3) and x + dx[d]*2 in range(3):
                lst[y + dy[d]*2][x + dx[d]*2] = ox
            else:
                lst[y - dy[d]][x - dx[d]] = ox
            return
        if y + dy[d]*2 not in range(3) or x + dx[d]*2 not in range(3):
            continue
        if lst[y + dy[d]*2][x + dx[d]*2] == ox:
            lst[y + dy[d]][x + dx[d]] = ox


T = int(input())
for tc in range(1, T + 1):
    lst = [list(input().strip()) for _ in range(3)]
    ox = input().strip()
    for r in range(3):
        for c in range(3):
            if lst[r][c] == ox:
                tictactoe(r, c, ox)
    print(f'Case {tc}:')
    for _ in range(3):
        print(*lst[_], sep='')