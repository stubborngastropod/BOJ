n = int(input())
count = 0
for i in range(1, n+1):
    if len(str(i)) < 3:
        count += 1
    elif len(str(i)) > 2:
        str_list = []
        for j in range(1, len(str(i))):
            str_list.append(int(str(i)[j])-int(str(i)[j-1]))
        if len(set(str_list)) == 1:
            count += 1

print(count)