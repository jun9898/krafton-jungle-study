minNum = int(input())
maxNum = int(input())
result = []

for i in range(minNum,maxNum+1):
    root = int(i**(1/2))
    if i == root**2:
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
