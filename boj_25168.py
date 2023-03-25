import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ans = [0] * (N + 1)
for _ in range(M):
    S, E, W = map(int, input().split())
    if not ans[S]:
        ans[S] = 1
    if W >= 7:
        W += 1
    ans[E] = max([ans[S] + W, ans[E]])
print(max(ans))