import sys
input = sys.stdin.readline

def dfs(n):
    global cnt
    global ans
    if not n:
        cnt += 1
        if cnt == K:
            ans = visited[0:]
        return
    for i in range(1, 4):
        visited.append(i)
        if n >= i:
            dfs(n - i)
        visited.pop()
N, K = map(int, input().split())
cnt = 0
ans = []
visited = []
dfs(N)
if ans:
    print(*ans, sep='+')
else:
    print(-1)