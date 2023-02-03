N = int(input())
words = []
for i in range(N):
    words.append(input())

words = list(set(words))
words.sort()

lenmax = 0
for i in words:
    if len(i) > lenmax:
        lenmax = len(i)

length = 0
while True:
    length +=1
    if length > lenmax:
        break
    for i in words:
        if len(i) == length:
            print(i)