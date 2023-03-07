import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort()
dp = [1] * N
maxi = 1
for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
            if dp[i] > maxi:
                maxi = dp[i]

ans = N - maxi
print(ans)