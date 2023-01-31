import sys
n = int(input())
towers = list(map(int, sys.stdin.readline().split()))
receiver = [0]*n
stack = []

for i in range(n):
    if stack:
        while True:
            if towers[i] <= stack[-1][0]:
                receiver[i] = stack[-1][1]+1
                stack.append([towers[i], i])
                break
            else:
                stack.pop()

            if stack == []:
                stack.append([towers[i], i])
                break

    else:
        stack.append([towers[i], i])

for i in receiver:
    print(i, end = ' ')
