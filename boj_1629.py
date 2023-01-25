A, B, C = map(int, input().split())

def rest(a,b,c):
    if b == 1:
        return a ** b % c
    elif b % 2 == 1:
        return (rest(a, (b-1)//2, c)) ** 2 * a % c
    else:
        return (rest(a, b//2, c)) ** 2 % c

print(rest(A, B, C))