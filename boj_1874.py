n = int(input())
num_list = []
for i in range(n):
    num_list.append(i+1)
stack = []
seq = []
no = False

for i in range(n):
    target = int(input())
    if target not in stack and target not in num_list:
        no = True
        break
    elif target in stack:
        while target in stack:
            seq.append('-')
            stack.pop()
    elif target not in stack:
        while target in num_list:
            seq.append('+')
            stack.append(num_list.pop(0))
        seq.append('-')
        stack.pop()

if no:
    print('NO')
else:
    for i in seq:
        print(i)