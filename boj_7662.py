import heapq
import sys

T = int(sys.stdin.readline())
for i in range(T):
    heap1 = []
    heap2 = []
    n = int(sys.stdin.readline())
    icount = dcount = 0
    visited = [False] * n
    for j in range(n):
        com = sys.stdin.readline().split()
        if com[0] == 'I':
            icount += 1
            heapq.heappush(heap1, (int(com[1]), j))
            heapq.heappush(heap2, (-int(com[1]), j))
            visited[j] = True
        elif com[0] == 'D':
            if dcount < icount:
                dcount += 1
                if com[1] == '-1':
                    while heap1 and not visited[heap1[0][1]]:
                        heapq.heappop(heap1)
                    if heap1:
                        visited[heap1[0][1]] = False
                        heapq.heappop(heap1)
                elif com[1] == '1':
                    while heap2 and not visited[heap2[0][1]]:
                        heapq.heappop(heap2)
                    if heap2:
                        visited[heap2[0][1]] = False
                        heapq.heappop(heap2)
    while heap1 and not visited[heap1[0][1]]:
        heapq.heappop(heap1)
    while heap2 and not visited[heap2[0][1]]:
        heapq.heappop(heap2)

    if heap1:
        print(-heap2[0][0], heap1[0][0])
    else:
        print('EMPTY')