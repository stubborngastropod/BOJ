N = int(input())
dic = {1: 0}
def mini(n):
    if n in dic.keys():
        return dic[n]
    else:
        if not n % 3 and not n % 2:
            dic[n] = min(mini(n//3) + 1, mini(n//2) + 1)
        elif not n % 3:
            dic[n] = min(mini(n//3) + 1, mini(n - 1) + 1)
        elif not n % 2:
            dic[n] = min(mini(n//2) + 1, mini(n - 1) + 1)
        else:
            dic[n] = mini(n - 1) + 1
        return dic[n]

print(mini(N))
