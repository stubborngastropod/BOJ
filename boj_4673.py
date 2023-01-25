def self_num(n):
    for i in str(n):
        n += int(i)
    return n

num_list = []

for i in range(1, 10001):
    num_list.append(i)

for i in range(10001):
    if self_num(i) in num_list:
        num_list.remove(self_num(i))

for i in num_list:
    print(i)