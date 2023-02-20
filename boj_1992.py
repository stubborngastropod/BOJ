N = int(input())
video = []
for i in range(N):
    video.append(str(input()))

def quadtree(lst, n):
    isone = iszero = True
    while isone:
        for i in range(n):
            for j in range(n):
                if lst[i][j] != '1':
                    isone = False
        break
    while iszero:
        for i in range(n):
            for j in range(n):
                if lst[i][j] != '0':
                    iszero = False
        break
    if isone:
        print('1', end = '')
    elif iszero:
        print('0', end = '')
    else:
        lst1 = [lst[i][:n // 2] for i in range(0, n // 2)]
        lst2 = [lst[i][n // 2:] for i in range(0, n // 2)]
        lst3 = [lst[i][:n // 2] for i in range(n // 2, n)]
        lst4 = [lst[i][n // 2:] for i in range(n // 2, n)]
        print('(', end = '')
        quadtree(lst1, n // 2)
        quadtree(lst2, n // 2)
        quadtree(lst3, n // 2)
        quadtree(lst4, n // 2)
        print(')', end = '')

quadtree(video, N)