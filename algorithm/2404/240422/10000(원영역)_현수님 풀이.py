import sys
input = sys.stdin.readline
N = int(input())
line = []
s =[]
for _ in range(N):
    x, r = map(int,input().split())
    line.append((x - r, 1,'('))
    line.append((x + r, 0, ')'))
line.sort()
cnt = 0
for i in range(N*2):
    if line[i][2] == '(':
        s.append(line[i])
        print(line[i])
    if line[i][2] == ')':
        pop = s.pop()
        print(pop)
        sum = 0
        while pop[0] == None:
            sum += pop[1]
            pop = s.pop()
        if sum == pop[0] - line[i][0]:
            cnt += 2
            s.append((None, sum))
        else:
            cnt += 1
            s.append((None,pop[0] - line[i][0]))
print(cnt+1)