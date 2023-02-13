import sys
import heapq

N = int(sys.stdin.readline())
heap = []
clslst = []
cnt = 0
for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    heapq.heappush(clslst, (a, b))
for i in range(N):
    x = heapq.heappop(clslst)
    while heap and heap[0] <= x[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, x[1])
    if len(heap) > cnt:
        cnt = len(heap)
print(cnt)