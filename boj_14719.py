h, w = map(int, input().split())
blocks = list(map(int, input().split()))
higher = [0] * w
higher[0] = blocks[0]
water = 0

for i in range(1, w):
    # 현재 블록이 이전 블록보다 작을때 상한값을 이전의 상한값까지 올려줌
    if blocks[i] < blocks[i-1]:
        higher[i] = higher[i-1]
    # 현재 블록이 이전 블록보다 클때
    elif blocks[i] >= blocks[i-1]:
        # 현재 블록이 이전 상한값보다 작을 때, 더 큰 블록을 만날때까지 땅을 메꾸고 water 올리기
        if blocks[i] <= higher[i-1]:
            cnt = 1
            while blocks[i] > blocks[i-cnt]:
                water += blocks[i] - blocks[i-cnt]
                blocks[i - cnt] = blocks[i]
                cnt += 1
            higher[i] = higher[i-1]
        # 현재 블록이 이전 상한값보다 클 때, 이전 상한값까지 땅을 메꾸고 water 올리기
        elif blocks[i] > higher[i-1]:
            for j in range(i):
                water += higher[j] - blocks[j]
                blocks[j] = higher[j]
            higher[i] = blocks[i]
print(water)