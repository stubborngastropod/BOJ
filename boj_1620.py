import sys

a, b = map(int, input().split())
dct1 = dct2 = {}
for i in range(a):
    name = sys.stdin.readline().strip()
    dct1[name] = i+1
    dct2[i+1] = name

for i in range(b):
    inp = sys.stdin.readline().strip()
    if inp.isdigit():
        print(dct2[int(inp)])
    else:
        print(dct1[inp])