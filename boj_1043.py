N, M = map(int, input().split())
truth = input()
all_party = []
if truth[0] == '0':
    nolie_num = 0
    for i in range(M):
        input()
    print(M)
else:
    truth = list(map(int, truth.split()))
    nolie_num = truth[0]
    nolie_list = set(truth[1:])

    for i in range(M):
        party = list(map(int, input().split()))
        people_num = party[0]
        people = party[1:]
        all_party.append(people)

    while True:
        nolie = nolie_list.pop()
        temp = []
        for p in all_party:
            if nolie in p:
                temp.append(p)
                p.remove(nolie)
                nolie_list = nolie_list | set(p)
        for p in temp:
            if p in all_party:
                all_party.remove(p)
        if not nolie_list or not all_party:
            break
    print(len(all_party))