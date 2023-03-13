import sys
input = sys.stdin.readline

def dfs(i, c):
    if i == len(str(N)):
        lst.append(c)
        return
    cnt = 0

    now = int(str(N)[i])
    while cnt < 10:
        if now > 0 and now - cnt in fine:
            dfs(i + 1, c + str(now - cnt))
        if now < 9 and now + cnt in fine:
            dfs(i + 1, c + str(now + cnt))
        cnt += 1

N = int(input())
M = int(input())
broken = list(map(int, input().split()))
fine = []
for i in range(10):
    if i not in broken:
        fine.append(i)

fine.sort()

pre = False
if fine:
    if 0 in fine:
        temp = fine[1:]
        if temp:
            pre = str(min(temp))
    else:
        pre = str(min(fine))

ans = abs(N - 100)

lst = []
dfs(0, '')

for num in lst:
    if abs(int(num) - N) + len(str(N)) < ans:
        ans = abs(int(num) - N) + len(str(N))
    if num[1:] and abs(int(num[1:]) - N) + len(str(N)) - 1 < ans:
        ans = abs(int(num[1:]) - N) + len(str(N)) - 1
    if pre and int(pre+num) <= 500000 and abs(int(pre+num) - N) + len(str(N)) + 1< ans:
        ans = abs(int(pre+num) - N) + len(str(N)) + 1

print(ans)