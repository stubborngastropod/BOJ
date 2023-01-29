import sys

N = int(sys.stdin.readline())
stack = []
for i in range(N):
    cmd = str(sys.stdin.readline().strip())
    if cmd == 'pop':
        if stack == []:
            print('-1')
        else:
            print(stack.pop(-1))
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack == []:
            print('1')
        else:
            print('0')
    elif cmd == 'top':
        if stack == []:
            print('-1')
        else:
            print(stack[-1])
    else:
        num = cmd.strip('push ')
        stack.append(int(num))