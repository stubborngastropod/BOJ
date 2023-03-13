import sys
input = sys.stdin.readline

N = int(input())

def ispromising(n):
    for i in range(n):
        if board[n] == board[i] or abs(board[n] - board[i]) == abs(n - i):
            return False
    return True

def queen(n):
    global ans
    if n == N:
        ans += 1
        return
    for i in range(N):
        board[n] = i
        if ispromising(n):
            queen(n + 1)

board = [0] * N
ans = 0
queen(0)
print(ans)