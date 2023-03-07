import sys
input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def up(board):
    global ans
    new = [[0] * N for _ in range(N)] # 바뀔 보드
    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[j][i] and cnt % 2: # 블록을 발견했고 합칠 블록이 있을 때
                if new[cnt // 2][i] == board[j][i]: # 같은 수면 합침
                    new[cnt // 2][i] += board[j][i]
                    if new[cnt // 2][i] > ans: # 만약 합친 블록의 숫자가 최대이면 정답 갱신
                        ans = new[cnt // 2][i]
                    cnt += 1
                else: # 다른 수면 합칠 블록을 갱신
                    cnt += 1
                    new[cnt // 2][i] = board[j][i]
                    if new[cnt // 2][i] > ans:
                        ans = new[cnt // 2][i]
                    cnt += 1
            elif board[j][i] and not cnt % 2: # 블록을 발견했고 합칠 블록이 없을 때
                new[cnt // 2][i] = board[j][i] # 합칠 블록으로 올려둠
                if new[cnt // 2][i] > ans: # 만약 올려둔 블록의 숫자가 최대이면 정답 갱신
                    ans = new[cnt // 2][i]
                cnt += 1
    return new

def down(board):
    global ans
    new = [[0] * N for _ in range(N)]
    for i in range(N):
        cnt = 0
        for j in range(N - 1, -1, -1):
            if board[j][i] and cnt % 2:
                if new[N - 1 - (cnt // 2)][i] == board[j][i]:
                    new[N - 1 - (cnt // 2)][i] += board[j][i]
                    if new[N - 1 - (cnt // 2)][i] > ans:
                        ans = new[cnt // 2][i]
                    cnt += 1
                else:
                    cnt += 1
                    new[N - 1 - (cnt // 2)][i] = board[j][i]
                    if new[N - 1 - (cnt // 2)][i] > ans:
                        ans = new[cnt // 2][i]
                    cnt += 1
            elif board[j][i] and not cnt % 2:
                new[N - 1 - (cnt // 2)][i] += board[j][i]
                if new[N - 1 - (cnt // 2)][i] > ans:
                    ans = new[N - 1 - (cnt // 2)][i]
                cnt += 1
    return new

def left(board):
    global ans
    new = [[0] * N for _ in range(N)]
    for i in range(N):
        cnt = 0
        for j in range(N):
            if board[i][j] and cnt % 2:
                if new[i][cnt // 2] == board[i][j]:
                    new[i][cnt // 2] += board[i][j]
                    if new[i][cnt // 2] > ans:
                        ans = new[i][cnt // 2]
                    cnt += 1
                else:
                    cnt += 1
                    new[i][cnt // 2] = board[i][j]
                    if new[i][cnt // 2] > ans:
                        ans = new[i][cnt // 2]
                    cnt += 1
            elif board[i][j] and not cnt % 2:
                new[i][cnt // 2] = board[i][j]
                if new[i][cnt // 2] > ans:
                    ans = new[i][cnt // 2]
                cnt += 1
    return new

def right(board):
    global ans
    new = [[0] * N for _ in range(N)]
    for i in range(N):
        cnt = 0
        for j in range(N - 1, -1, -1):
            if board[i][j] and cnt % 2:
                if new[i][N - 1 - (cnt // 2)] == board[i][j]:
                    new[i][N - 1 - (cnt // 2)] += board[i][j]
                    if new[i][N - 1 - (cnt // 2)] > ans:
                        ans = new[i][N - 1 - (cnt // 2)]
                    cnt += 1
                else:
                    cnt += 1
                    new[i][N - 1 - (cnt // 2)] = board[i][j]
                    if new[i][N - 1 - (cnt // 2)] > ans:
                        ans = new[i][N - 1 - (cnt // 2)]
                    cnt += 1
            elif board[i][j] and not cnt % 2:
                new[i][N - 1 - (cnt // 2)] = board[i][j]
                if new[i][N - 1 - (cnt // 2)] > ans:
                    ans = new[i][N - 1 - (cnt // 2)]
                cnt += 1
    return new

def game(board, c):
    if c == 5:
        return
    game(up(board), c + 1)
    game(down(board), c + 1)
    game(left(board), c + 1)
    game(right(board), c + 1)
number = 1
game(lst, 0)
print(ans)