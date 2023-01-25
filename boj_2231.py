N = int(input())
ans = 0

for i in range(1,N):
    sum_ = 0
    for j in range(len(str(i))):
        sum_ += int(str(i)[j])
    if i + sum_ == N:
        ans = i
        break

print(ans)