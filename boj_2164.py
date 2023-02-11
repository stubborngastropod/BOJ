import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque(i+1 for i in range(n))

while deq:
    a = deq.popleft()
    deq.rotate(-1)

print(a)
