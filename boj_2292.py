N = int(input())
n = 0
cnt = 1
while True:
    if 6 * n + 1 >= N:
        break
    n += cnt
    cnt += 1

print(cnt)