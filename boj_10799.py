ps = input()
pipes = 0
cut = 0
for i in range(len(ps)):
    if ps[i] == '(':
        pipes += 1
    elif ps[i] == ')' and ps[i-1] == '(':
        pipes -= 1
        cut += pipes
    elif ps[i] == ')':
        pipes -= 1
        cut += 1
print(cut)