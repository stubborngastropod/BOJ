import sys
from itertools import combinations
input = sys.stdin.readline

def cd(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        if city[i][j] == 1:
            house.append((i, j))

cd_list = [[] for _ in range(len(chicken))]
for i in range(len(chicken)):
    for j in range(len(house)):
        cd_list[i].append(cd(house[j][0], house[j][1], chicken[i][0], chicken[i][1]))

ans = 1e4
for i in combinations(cd_list, M):
    temp = 0
    for j in range(len(house)):
        temp += min(list(zip(*i))[j])
    if temp <= ans:
        ans = temp

print(ans)