T = int(input())
for i in range(T):
    n = int(input())
    d = []
    for i in range(2):
        d.append(list(map(int, input().split())))
    maxidict = {(0, n-1): d[0][n-1], (1, n-1): d[1][n-1]}
    def maxi(i, j):
        if j + 2 in range(n):
            maxidict[(i, j)] = d[i][j] + max([maxi(i, j + 2), maxi(abs(i-1), j + 1), maxi(abs(i-1), j + 2)])
        elif j + 1 in range(n):
            maxidict[(i, j)] = d[i][j] + maxi(abs(i-1), j + 1)
        else:
            maxidict[(i, j)] = d[i][j]
        return maxidict[(i, j)]

    print(max([maxi(0, 0), maxi(1, 0)]))
