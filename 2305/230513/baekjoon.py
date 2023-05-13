num, index = map(int,input().split())
numList = []

for i in range(1, num+1):
    if num % i == 0:
        numList.append(i)

try:
    print(numList[index-1])
except:
    print(0)
