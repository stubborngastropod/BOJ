import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K + 1)]
items = []
for i in range(N):
    items.append(tuple(map(int, input().split())))
items.sort(reverse=True)

for i in range(1, N + 1):
    W, V = items.pop()
    dp.append([0] * (K + 1))
    for j in range(1, K + 1):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max([dp[i-1][j-W] + V, dp[i-1][j]])

print(dp[-1][-1])