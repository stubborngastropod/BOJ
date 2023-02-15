import heapq
import sys

T = int(input())
for i in range(T):
    N = int(sys.stdin.readline())
    heap = []
    pass_list = []
    for j in range(N):
        a, b = map(int, input().split())
        heapq.heappush(heap, (a,b))
    pass_list.append(heapq.heappop(heap))
    while heap:
        a = heapq.heappop(heap)
        if a[1] < pass_list[-1][1]:
            pass_list.append(a)
    print(len(pass_list))