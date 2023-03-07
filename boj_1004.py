import sys
input = sys.stdin.readline
# 해당 좌표가 원 안에 있는지 확인하는 함수
def isin(cx, cy, r, x, y):
    if (cx - x) ** 2 + (cy - y) ** 2 < r ** 2:
        return True
    return False

T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for planet in range(n):
        cx, cy, r = map(int, input().split())
        if isin(cx, cy, r, x1, y1) != isin(cx, cy, r, x2, y2): # 장미와 왕자 중 하나만 포함된 원이라면 카운트
            cnt += 1
    print(cnt)