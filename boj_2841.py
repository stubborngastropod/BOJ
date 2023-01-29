import sys

guitar = []
for i in range(6):
    guitar.append([0])
count = 0

N, P = map(int, sys.stdin.readline().split())

for i in range(N):
    string, pret = map(int, sys.stdin.readline().split())
    if pret > guitar[string - 1][-1]:
        guitar[string - 1].append(pret)
        count += 1
    elif pret < guitar[string - 1][-1]:
        while pret < guitar[string - 1][-1]:
            count += 1
            guitar[string - 1].pop(-1)
        if pret > guitar[string - 1][-1]:
            guitar[string - 1].append(pret)
            count += 1
    else:
        pass

print(count)