T = int(input())
for i in range(T):
    ps = input()
    stack = 0
    for j in ps:
        if j == '(':
            stack += 1
        elif j == ')':
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')