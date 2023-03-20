import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
q = []
temp = []
ans = 0
while lst:
    now = lst.pop()
    heapq.heappush(q, now)
    if len(q) == M:
        out = heapq.heappop(q)
        ans += out
        for i in range(M - 1):
            q[i] -= out
        while q and q[0] == 0:
            heapq.heappop(q)
if q:
    ans += max(q)

print(ans)