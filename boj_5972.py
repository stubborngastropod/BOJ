import sys
input = sys.stdin.readline
import heapq
inf = 1e8

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

mini = [inf for _ in range(N + 1)]
mini[1] = 0
heap = []
heapq.heappush(heap, (0, 1))
while heap:
    dist, now = heapq.heappop(heap)
    if mini[now] < dist:
        continue
    for next in adj[now]:
        if mini[now] + next[0] < mini[next[1]]:
            mini[next[1]] = mini[now] + next[0]
            heapq.heappush(heap, [mini[next[1]], next[1]])

print(mini[N])