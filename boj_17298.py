import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

stack = []
ans = []
for i in range(N - 1, -1, -1):
    if not stack:
        stack.append(lst[i])
    while stack:
        if stack[-1] <= lst[i]:
            stack.pop()
            if not stack:
                ans.append(-1)
        else:
            if stack:
                ans.append(stack[-1])
                break
            else:
                ans.append(-1)
    stack.append(lst[i])

ans = list(reversed(ans))
print(*ans)