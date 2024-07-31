import sys
input = sys.stdin.readline

n = int(input())
arrayFirst = list(input().rstrip())

for i in range(n-1):
    arrayOther = list(input().rstrip())
    for j in range(len(arrayFirst)):
        if arrayFirst[j] != arrayOther[j]:
            arrayFirst[j] = "?"

print("".join(arrayFirst))

    

        