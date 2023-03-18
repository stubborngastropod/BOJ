import sys
input = sys.stdin.readline

def rev(a):
    for t in range(len(a)//2):
        if a[t] != a[-1-t]:
            return False
    return True

T = int(input())
for tc in range(T):
    inp = input().strip()
    l = 0
    r = len(inp) - 1
    ans = 0
    while l < r:
        if inp[l] == inp[r]:
            l += 1
            r -= 1
        else:
            if rev(inp[l:r]) or rev(inp[l+1:r+1]):
                ans = 1
                break
            else:
                ans = 2
                break
    print(ans)
