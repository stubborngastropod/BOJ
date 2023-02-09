import sys

n = int(input())
deque = []
for i in range(n):
    com = sys.stdin.readline().strip()
    if com[:4] == 'push':
        if com[5:9] == 'back':
            deque.append(int(com[10:]))
        else:
            deque.insert(0, int(com[11:]))
    elif com[:3] == 'pop':
        if com[4:8] == 'back':
            if deque:
                print(deque.pop())
            else:
                print(-1)
        else:
            if deque:
                print(deque.pop(0))
            else:
                print(-1)
    elif com == 'size':
        print(len(deque))
    elif com == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif com == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)