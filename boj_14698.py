import sys
import heapq

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    mult = 1

    if len(lst) > 1:
        while True:
            a = heapq.heappop(lst)
            if lst:
                a *= heapq.heappop(lst)
                heapq.heappush(lst, a)
                mult *= a

            else:
                break

    print(mult % 1000000007)