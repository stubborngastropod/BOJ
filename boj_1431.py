import sys
def num_sum(string):
    numsum = 0
    for i in string:
        if i.isdigit():
            numsum += int(i)
    return numsum

N = int(input())
guitars = []
for i in range(N):
    guitar = str(sys.stdin.readline().strip())
    guitars.append((guitar, len(guitar), num_sum(guitar)))

final = sorted(guitars, key = lambda x : (x[1], x[2], x[0]))
for i in range(N):
    print(final[i][0])