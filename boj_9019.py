from collections import deque
import sys
input = sys.stdin.readline

def zero(n):
    while len(str(n)) < 4:
        n = '0' + str(n)
    return str(n)

def D(n):
    return (n * 2) % 10000

def S(n):
    if n > 0:
        return n - 1
    else:
        return 9999

def L(n):
    return int(n[1:] + n[0])

def R(n):
    return int(n[-1] + n[:-1])

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    queue = deque([])
    queue.append(a)
    visited = [''] * 10000
    while queue:
        now = queue.popleft()
        if now == b:
            ans = visited[now]
            break
        if now != 0 and not visited[D(now)]:
            queue.append(D(now))
            visited[D(now)] = visited[now] + 'D'
        if not visited[S(now)]:
            queue.append(S(now))
            visited[S(now)] = visited[now] + 'S'
        if not visited[(L(zero(now)))]:
            queue.append(L(zero(now)))
            visited[L(zero(now))] = visited[now] + 'L'
        if not visited[(R(zero(now)))]:
            queue.append(R(zero(now)))
            visited[R(zero(now))] = visited[now] + 'R'
    print(ans)
