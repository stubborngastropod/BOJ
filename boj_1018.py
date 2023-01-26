a, b = map(int, input().split())

newboard = []
for i in range(a):
    newboard.append(list(input()))

board_bw = []
count = 0

for i in range(8):
    board_bw.append([])
    count += 1
    for j in range(8):
        if count % 2 == 1:
            board_bw[i].append('B')
            count += 1
        else:
            board_bw[i].append('W')
            count += 1

changelist = []
for k in range(a - 7):
    for l in range(b - 7):
        bw = 0
        wb = 0
        for i in range(k, k+8):
            for j in range(l, l+8):
                if newboard[i][j] != board_bw[i-k][j-l]:
                    bw += 1
                else:
                    wb += 1
        if bw <= wb:
            changelist.append(bw)
        else:
            changelist.append(wb)

print(min(changelist))