a,b = map(int,input().split())
lst = []
for i in range(a):
    lst.append(list(map(int,input().split())))
max = 0
for i in range(a-3):
    for j in range(b):
        sum = lst[i][j]+lst[i+1][j]+lst[i+2][j]+lst[i+3][j]
        if sum > max:max=sum
for i in range(a):
    for j in range(b-3):
        sum = lst[i][j]+lst[i][j+1]+lst[i][j+2]+lst[i][j+3]
        if sum > max:max=sum
for i in range(a-1):
    for j in range(b-1):
        sum = lst[i][j]+lst[i][j+1]+lst[i+1][j]+lst[i+1][j+1]
        if sum > max:max=sum
for i in range(a-2):
    for j in range(b-1):
        sum = lst[i][j]+lst[i+1][j]+lst[i+2][j]+lst[i+2][j+1]
        if sum > max:max=sum
        sum = lst[i][j+1]+lst[i+1][j+1]+lst[i+2][j]+lst[i+2][j+1]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i][j+1]+lst[i+1][j]+lst[i+2][j]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i][j+1]+lst[i+1][j+1]+lst[i+2][j+1]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i+1][j]+lst[i+1][j+1]+lst[i+2][j]
        if sum > max:max=sum
        sum = lst[i][j+1]+lst[i+1][j]+lst[i+1][j+1]+lst[i+2][j+1]
        if sum > max:max=sum
        sum = lst[i][j+1]+lst[i+1][j]+lst[i+1][j+1]+lst[i+2][j]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i+1][j]+lst[i+1][j+1]+lst[i+2][j+1]
        if sum > max:max=sum
for i in range(a-1):
    for j in range(b-2):
        sum = lst[i][j]+lst[i][j+1]+lst[i][j+2]+lst[i+1][j]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i+1][j]+lst[i+1][j+1]+lst[i+1][j+2]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i][j+1]+lst[i][j+2]+lst[i+1][j+2]
        if sum > max:max=sum
        sum = lst[i][j+2]+lst[i+1][j]+lst[i+1][j+1]+lst[i+1][j+2]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i][j+1]+lst[i+1][j+1]+lst[i+1][j+2]
        if sum > max:max=sum
        sum = lst[i][j+1]+lst[i][j+2]+lst[i+1][j]+lst[i+1][j+1]
        if sum > max:max=sum
        sum = lst[i][j+1]+lst[i+1][j]+lst[i+1][j+1]+lst[i+1][j+2]
        if sum > max:max=sum
        sum = lst[i][j]+lst[i][j+1]+lst[i][j+2]+lst[i+1][j+1]
        if sum > max:max=sum
print(max)
