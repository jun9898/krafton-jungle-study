import sys
input = sys.stdin.readline

MyTeam = list(map(int,input().split()))
otherTeam = list(map(int,input().split()))

count = 0

myScore = 0
otherScore = 0

for i in range(len(MyTeam)):
    myScore += MyTeam[i]
    if myScore > otherScore:
        count += 1
    otherScore += otherTeam[i]

if count < 1:
    print('No')
else:
    print('Yes')




