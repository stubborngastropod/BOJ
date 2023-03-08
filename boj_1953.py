import sys
input = sys.stdin.readline

N = int(input())
hate = [[0] * (N + 1) for _ in range(N + 1)]
students = [s for s in range(1, N + 1)]
for i in range(1, N + 1):
    inp = input().strip()
    if len(inp) != 1:
        h, *p = map(int, inp.split())
        for j in range(h):
            hate[i][p[j]] = hate[p[j]][i] = 1

team = [1]
def teaming(start):
    visited[start] = 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if hate[i][j]:
                visited[j] = 1
        if not hate[start][i] and not visited[i]:
            team.append(i)
            teaming(i)

for person in range(1, N + 1):
    visited = [0] * (N + 1)
    team = [person]
    teaming(person)
    temp = list(set(students) - set(team))
    goodteam = True
    for i in temp:
        for j in temp:
            if hate[i][j]:
                goodteam = False
    if goodteam:
        blue = team
        blue.sort()
        white = temp
        white.sort()
        break
print(len(blue))
print(*blue)
print(len(white))
print(*white)