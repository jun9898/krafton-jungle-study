import sys
input = sys.stdin.readline

n = int(input())
tmp = input().rstrip()

arr = ""
result = 0
for i in tmp:
    if i.isalpha():
        if len(arr) != 0:
            result += int(arr)
            arr = ""
        continue
    arr += i

if len(arr) != 0:
    result += int(arr)

print(result)

