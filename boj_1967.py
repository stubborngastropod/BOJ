import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    adj[a].append([b, c])
    adj[b].append([a, c])

def dfs(now, dis):
    global maxi
    global far
    if dis > maxi:
        maxi = dis
        far = now
    for nxt in adj[now]:
        node, d = nxt
        if not dis_list[node]:
            dis_list[node] = dis + d
            dfs(node, dis + d)

maxi = 0
far = 0
dis_list = [0] * (n + 1)
dis_list[1] = -1
dfs(1, 0)
dis_list = [0] * (n + 1)
dis_list[far] = -1
dfs(far, 0)

print(maxi)