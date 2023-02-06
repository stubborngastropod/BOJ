import sys

K, N = map(int, sys.stdin.readline().split())
cable = []
for i in range(K):
    cable.append(int(sys.stdin.readline()))

maxi = max(cable)
mini = 1
length = (maxi + mini)//2
ans_list = []
cables = 0

for i in cable:
    cables += i // maxi
if cables >= N:
    ans_list.append(maxi)

while abs(maxi - mini) > 1:
    cables = 0
    for i in cable:
        cables += i // length

    if cables > N:
        ans_list.append(length)
        mini = length
        length = round((maxi + length) / 2)
    elif cables == N:
        ans_list.append(length)
        mini = length
        length = round((maxi + length) / 2)
    else:
        maxi = length
        length = round((mini + length) / 2)
        continue

ans_list.append(mini)
print(max(ans_list))