N = int(input())
if N == 1:
    print(3)
else:
    dp = [0] * N
    dp[0], dp[1] = 3, 7
    for i in range(2, N):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
    print(dp[N - 1])