from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def puyo(color):
    global ispuyo
    temp = []
    cnt = 1
    while queue:
        qpop = queue.popleft()
        temp.append(qpop)
        for d in range(4):
            ni, nj = qpop[0] + dy[d], qpop[1] + dx[d]
            if ni < 0 or ni >= 12 or nj < 0 or nj >= 6:
                continue
            if visited[ni][nj]:
                continue
            if field[ni][nj] == color:
                visited[ni][nj] = 1
                queue.append((ni, nj))
                cnt += 1

    if cnt >= 4:
        for delete in temp:
            field[delete[0]][delete[1]] = '.'
        ispuyo = True

def down():
    for column in range(6):
        while True:
            find = False
            for row in range(11, 0, -1):
                if field[row][column] == '.' and field[row - 1][column] != '.':
                    field[row][column], field[row - 1][column] = field[row - 1][column], '.'
                    find = True
            if not find:
                break

field = [list(input()) for _ in range(12)]
queue = deque()

puyopuyo = 0

while 1:
    ispuyo = False
    # 방문하면서 뿌요뿌요하기
    visited = [[0] * 6 for _ in range(12)]
    for r in range(12):
        for c in range(6):
            if field[r][c] != '.':
                queue.append((r, c))
                visited[r][c] = 1
                puyo(field[r][c])
    if ispuyo:
        down()
        puyopuyo += 1
    else:
        break

print(puyopuyo)