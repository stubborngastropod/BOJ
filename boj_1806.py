from collections import deque
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()
ans = 1e10

qsum = 0
while arr:
    now = arr.pop()
    qsum += now
    q.append(now)
    if qsum >= S:
        while qsum - q[0] >= S:
            qsum -= q.popleft()
        if len(q) < ans:
            ans = len(q)
        qsum -= q.popleft()
if ans == 1e10:
    ans = 0
print(ans)

