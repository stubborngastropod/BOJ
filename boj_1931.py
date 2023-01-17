N = int(input())
meetings = []
meetingnum = 1

for i in range(N):
    m = list(map(int, input().split()))
    meetings.append(m)

meetings.sort(key = lambda x: (x[1], x[0]))

endtime = meetings[0][1]

for i in range(1, N):
    if meetings[i][0] >= endtime:
        meetingnum += 1
        endtime = meetings[i][1]

print(meetingnum)