import sys
input = sys.stdin.readline

N = int(input())
def dq(a, b, c, flag):
    if c == i:
        if flag:
            for _ in range(a, b):
                print('A', end='')
        else:
            for _ in range(a, b):
                print('B', end='')
        return
    dq(a, (a + b) // 2, c + 1, True)
    dq((a + b) // 2, b, c + 1, False)

for i in range(1, 8):
    if 2 ** (i - 1) >= N:
        cnt = 0
        while cnt < N:
            if cnt < N // 2:
                print('B', end = '')
            else:
                print('A', end = '')
            cnt += 1
        print('')
    else:
        dq(0, N, 0, True)
        print('')