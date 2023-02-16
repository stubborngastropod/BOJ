lst = list(input())
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
stack = []
result = ''

while lst:
    temp = lst.pop(0)
    if temp.isalpha():
        result += temp
    elif temp == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    elif temp == '(':
        stack.append(temp)
    else:
        if stack:
            while priority[stack[-1]] >= priority[temp]:
                result += stack.pop()
                if not stack:
                    break
            stack.append(temp)
        else:
            stack.append(temp)

while stack:
    result += stack.pop()
print(result)