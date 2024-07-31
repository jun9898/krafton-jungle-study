import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stringArray = list(list(input().split()))
    for i in range(len(stringArray)):
        stringArray[i] = stringArray[i][::-1]
    print(*stringArray)

