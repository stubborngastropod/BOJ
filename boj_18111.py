import sys

N, M, B = map(int, sys.stdin.readline().split())
land = []

for i in range(N):
    block = list(map(int, sys.stdin.readline().split()))
    land += block

shortest_time = 64000000

for i in range(min(land), max(land) + 1):
    spendtime = 0
    spendblock = 0
    for j in land:
        if j <= i:
            spendtime += (i - j)
            spendblock += i - j
        else:
            spendtime += (j - i) * 2

    if spendblock <= B and spendtime <= shortest_time:
        shortest_time = spendtime
        final_height = i

print(f'{shortest_time} {final_height}')



