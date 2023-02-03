T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    imp = 9
    cnt = 0
    breaker = True

    while breaker:
        for j in range(N):
            while imp not in lst:
                imp -= 1

            if lst[j] == imp and j == M:
                cnt += 1
                breaker = False
                break

            elif lst[j] == imp:
                lst[j] = 0
                cnt += 1

    print(cnt)