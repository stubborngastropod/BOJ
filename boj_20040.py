import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = 0
parent = [_ for _ in range(n)]

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    global ans
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x, y)] = min(x, y)
    elif not ans:
        ans = i + 1

for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

print(ans)