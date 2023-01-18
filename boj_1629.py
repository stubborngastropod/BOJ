A, B, C = map(int, input().split())
a = A
b = B

while True:
    if b == 1:
        a = a % C
        break
    elif b % 2 == 0:
        a = (a * a) % C
        b = b // 2
    elif b % 2 == 1:
        a = ((a * a) * A) % C
        b = b // 2

print(a)