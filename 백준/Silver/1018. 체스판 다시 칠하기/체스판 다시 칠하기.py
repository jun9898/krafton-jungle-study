import sys
input = sys.stdin.readline


def search(x,y):
    count1 = 0
    count2 = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i+j)%2 == 0:
                if plate[i][j] != 0: 
                    count1 += 1
                if plate[i][j] != 1: 
                    count2 += 1
            else:
                if plate[i][j] != 1: 
                    count1 += 1
                if plate[i][j] != 0: 
                    count2 += 1
    answer.append(count1)
    answer.append(count2)
                

n,m = map(int,input().split())

plate = []

for i in range(n):
    string = list(input().rstrip())
    result = []
    for j in string:
        if j == "W":
            result.append(1)
        else:
            result.append(0)
    plate.append(result)

answer = []
for i in range(n-7):
    for j in range(m-7):
        search(i,j)

print(min(answer))


