import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dp = [1] * N
ans = 1
for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1
            if dp[i] > ans:
                ans = dp[i]

print(ans)