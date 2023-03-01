from collections import deque
import sys
input = sys.stdin.readline

def rotate(n):
    if direction == 1:
        gears[n].appendleft(gears[n].pop())
    else:
        gears[n].append(gears[n].popleft())

gears = [0] + [deque(list(map(int, input().strip()))) for _ in range(4)]
K = int(input())
for i in range(K):
    gear_num, direction = map(int, input().split())

    if gear_num == 1:
        if gears[1][2] != gears[2][6]:
            if gears[2][2] != gears[3][6]:
                if gears[3][2] != gears[4][6]:
                    direction = -direction
                    rotate(4)
                    direction = -direction
                rotate(3)
            direction = -direction
            rotate(2)
            direction = -direction
        rotate(1)

    if gear_num == 2:
        if gears[1][2] != gears[2][6]:
            direction = -direction
            rotate(1)
            direction = -direction
        if gears[2][2] != gears[3][6]:
            if gears[3][2] != gears[4][6]:
                rotate(4)
            direction = -direction
            rotate(3)
            direction = -direction
        rotate(2)

    if gear_num == 3:
        if gears[3][2] != gears[4][6]:
            direction = -direction
            rotate(4)
            direction = -direction
        if gears[2][2] != gears[3][6]:
            if gears[1][2] != gears[2][6]:
                rotate(1)
            direction = -direction
            rotate(2)
            direction = -direction
        rotate(3)

    if gear_num == 4:
        if gears[3][2] != gears[4][6]:
            if gears[2][2] != gears[3][6]:
                if gears[1][2] != gears[2][6]:
                    direction = -direction
                    rotate(1)
                    direction = -direction
                rotate(2)
            direction = -direction
            rotate(3)
            direction = -direction
        rotate(4)

ans = 0
for j in range(1, 5):
    ans += 2**(j-1) * gears[j][0]

print(ans)