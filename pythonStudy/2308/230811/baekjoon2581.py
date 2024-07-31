import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

answer = []

for i in range(n,m+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                count += 1
                break
        if count == 0:
            answer.append(i)

if not answer:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))




