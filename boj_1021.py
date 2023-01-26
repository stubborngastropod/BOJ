def two(list_):
    a = list_.pop(0)
    list_.append(a)
    return list_

def three(list_):
    a = list_.pop(-1)
    list_.insert(0, a)
    return list_

N, M = map(int, input().split())
num_list = []
for i in range(1, N+1):
    num_list.append(i)
pop_list = list(map(int, input().split()))
twocount, threecount = 0, 0

while True:
    if len(pop_list) == 0:
        break
    n = pop_list.pop(0)
    if num_list.index(n) == 0:
        num_list.remove(n)
        N -= 1
    elif num_list.index(n) < (N / 2):
        for i in range(num_list.index(n)):
            two(num_list)
            twocount += 1
        num_list.remove(n)
        N -= 1
    elif num_list.index(n) >= (N / 2):
        for i in range(N - num_list.index(n)):
            three(num_list)
            threecount += 1
        num_list.remove(n)
        N -= 1

print(twocount + threecount)