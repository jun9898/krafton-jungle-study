import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    largestGap = 0
    score = list(map(int,input().split()))
    lenScore = score.pop(0)
    maxScore = max(score)
    minScore = min(score)
    score.sort()
    for i in range((lenScore)-1):
        gap = score[i+1] - score[i]
        if largestGap < gap:
            largestGap = gap
    arr.append([maxScore,minScore,largestGap])

for i in range(n):
    print('Class', i+1)
    print(f'Max {arr[i][0]}, Min {arr[i][1]}, Largest gap {arr[i][2]}')


    