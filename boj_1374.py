import sys
import heapq

classlist = []
heap = []
ans_list = []
N = int(sys.stdin.readline())
for i in range(N):
    classnum, start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(classlist, [start, end])

while classlist:
    a = heapq.heappop(classlist)
    a[0], a[1] = a[1], a[0]
    while heap and heap[0][0] <= a[1]:
        heapq.heappop(heap)
    heapq.heappush(heap, a)
    ans_list.append(len(heap))

print(max(ans_list))