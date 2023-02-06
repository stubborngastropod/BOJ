import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
ans = []
idx1 = 0
idx2 = n-1

while idx2 - idx1 > 0:
    ans.append([abs(lst[idx1] + lst[idx2]), lst[idx1], lst[idx2]])
    diff = abs(lst[idx1] + lst[idx2])
    if abs(lst[idx1+1] + lst[idx2]) <= diff:
        idx1 += 1
    elif abs(lst[idx1] + lst[idx2-1]) <= diff:
        idx2 -= 1
    else:
        ans.append([abs(lst[idx1] + lst[idx2]), lst[idx1], lst[idx2]])
        idx1 += 1
        idx2 -= 1

ans.sort()

print(ans[0][1], ans[0][2])
