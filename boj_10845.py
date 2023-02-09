import sys

n = int(input())
queue = []
for i in range(n):
    com = sys.stdin.readline().strip()
    if com[:4] == 'push':
        queue.append(int(com[5:]))
    elif com == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif com == 'size':
        print(len(queue))
    elif com == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)