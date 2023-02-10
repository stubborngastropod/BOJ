T = int(input())
for i in range(T):
    n = int(input())
    # 스티커 입력
    d = []
    for j in range(2):
        d.append(list(map(int, input().split())))
    # n = 1 edgecase
    if n == 1:
        print(max(d[0][0], d[1][0]))
    # 각 스티커 선택 시 최대값 누적 저장할 리스트 생성
    else:
        maxi = [[0] * n for _ in range(2)]
        for j in range(2):
            for k in range(2):
                maxi[j][k] = d[j][k]
        maxi[0][1] += maxi[1][0]
        maxi[1][1] += maxi[0][0]
        # 최대값 갱신
        for j in range(2, n):
            maxi[0][j] = max(d[0][j] + maxi[0][j-2], d[0][j] + maxi[1][j-1], d[0][j] + maxi[1][j-2])
            maxi[1][j] = max(d[1][j] + maxi[1][j-2], d[1][j] + maxi[0][j-1], d[1][j] + maxi[0][j-2])
        # 출력
        print(max(maxi[0][n-1], maxi[0][n-2], maxi[1][n-1], maxi[1][n-2]))