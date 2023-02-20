import sys

string = list(map(str, sys.stdin.readline().strip()))
bomb = str(sys.stdin.readline().strip())
stack = []
for i in string:
    stack.append(i)
    while len(stack) >= len(bomb):
        if stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()
        else:
            break
if stack:
    print(*stack, sep = '')
else:
    print('FRULA')