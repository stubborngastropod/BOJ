import sys
input = sys.stdin.readline

a = input().strip()
temp = []
ans = []
for i in a:
    if i not in temp:
        temp.append(i)
        continue
    for j in range(len(temp)):
        if temp[j] == i:
            ans.append(temp.pop(j))
            break
if len(temp) > 1:
    print("I'm Sorry Hansoo")
elif len(temp) == 1:
    ans.sort()
    sna = reversed(ans)
    print(*ans, sep='', end = '')
    print(temp[0], end = '')
    print(*sna, sep='')
else:
    ans.sort()
    sna = reversed(ans)
    print(*ans, sep='', end = '')
    print(*sna, sep='')
