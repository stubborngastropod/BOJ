import sys
import collections

n = int(input())
num_list = []
for line in sys.stdin:
    num_list.append(int(line))

print(round(sum(num_list)/n))

num_list.sort()
print(num_list[n//2])

fre_dict = dict(collections.Counter(num_list))
fre_list = list(fre_dict.items())
fre_list.sort(key = lambda x: x[1], reverse = True)
if len(fre_list) > 1:
    if fre_list[0][1] == fre_list[1][1]:
        print(fre_list[1][0])
    else:
        print(fre_list[0][0])
else:
    print(fre_list[0][0])

print(max(num_list) - min(num_list))