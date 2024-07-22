import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

b, c = map(int, input().split())

count = 0

for i in arr:
    i -= b
    count += 1
    if i > 0:
        count += i // c
        if i % c != 0:
            count += 1

print(count)