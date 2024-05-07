import sys
input = sys.stdin.readline

n = int(input())
tmp = abs(100 - n)
m = int(input())
if m:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    for i in str(num):
        if i in broken:
            break
    else:
        tmp = min(tmp, len(str(num)) + abs(num - n))

print(tmp)


