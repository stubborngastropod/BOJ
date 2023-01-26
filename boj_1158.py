N, K = map(int, input().split())
num_list = []
new_list = []
for i in range(1, N + 1):
    num_list.append(i)

n = K

while len(num_list) > 2:
    new_list.append(num_list.pop(n-1))
    n += K - 1
    while n > len(num_list):
        n -= len(num_list)

if N == 1:
    print('<1>')

elif n % 2:
    new_list.append(num_list[0])
    new_list.append(num_list[1])

    print('<', end='')
    for i in new_list[:-1]:
        print(i, end=', ')
    print(new_list[-1], end='')
    print('>')

else:
    new_list.append(num_list[1])
    new_list.append(num_list[0])

    print('<', end = '')
    for i in new_list[:-1]:
        print(i, end = ', ')
    print(new_list[-1], end = '')
    print('>')