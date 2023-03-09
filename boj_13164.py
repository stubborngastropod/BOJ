import sys
input = sys.stdin.readline

n, k = map(int, input().split())
students = list(map(int, input().split()))
diff = []

for i in range(1, n):
    diff.append(students[i]-students[i - 1])
diff.sort(reverse=True)
ans = sum(diff[k-1:])
print(ans)