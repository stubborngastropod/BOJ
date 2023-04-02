import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for __ in range(n):
        lst.append(input().strip())
    lst.sort(key=lambda x: len(x))
    no = False
    for i in range(n - 1):
        for j in range(i + 1, n):
            if len(lst[j]) > len(lst[i]) and lst[i] == lst[j][:len(lst[i])]:
                no = True
    if no:
        print("NO")
    else:
        print("YES")
