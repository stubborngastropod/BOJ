import sys
input = sys.stdin.readline

N = int(input())
relation = [list(input().strip()) for _ in range(N)]
ans = 0
for i in range(N):
    friends = set()
    for j in range(N):
        if relation[i][j] == 'Y':
            friends.add(j)
        else:
            if j == i:
                continue
            for k in range(N):
                if relation[j][k] == relation[i][k] == 'Y':
                    friends.add(j)
    ans = max(ans, len(friends))
print(ans)
