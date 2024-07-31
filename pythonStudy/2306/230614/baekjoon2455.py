import sys
input = sys.stdin.readline

result = 0
arr = []
for i in range(4):
    n,m = map(int, input().split())
    result += m-n
    arr.append(result)

print(max(arr))
