T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if (x1 - x2)**2 + (y1 - y2)**2 < (r1 + r2)**2:
            if ((x1 - x2)**2 + (y1 - y2)**2)**(1/2) + r2 < r1 or \
                    ((x1 - x2)**2 + (y1 - y2)**2)**(1/2) + r1 < r2:
                print(0)
            elif ((x1 - x2)**2 + (y1 - y2)**2)**(1/2) + r2 == r1 or \
                    ((x1 - x2)**2 + (y1 - y2)**2)**(1/2) + r1 == r2:
                print(1)
            else:
                print(2)
        elif (x1 - x2)**2 + (y1 - y2)**2 == (r1 + r2)**2:
            print(1)
        elif (x1 - x2) ** 2 + (y1 - y2) ** 2 == (r1 - r2) ** 2:
            print(1)
        else:
            print(0)
