while True:
    string = str(input())
    if string == '.':
        break
    else:
        ans = True
        stack = []
        for i in string:
            if i in '([':
                stack.append(i)
            if i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    ans = False
            if i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    ans = False

    if not stack and ans:
        print('yes')
    else:
        print('no')