import sys
input = sys.stdin.readline

n = int(input())

res = 0
if n == 3:
    print(1)
    exit(0)
# 7까지는 3, 5로 만들 수 있는 조합이 아님
if n == 7:
    print(-1)
    exit(0)
else:
    if n < 5:
        print(-1)
        exit(0)
    res += n // 5
    tmp = n % 5
    if tmp == 1 or tmp == 3:
        res += 1
    elif tmp == 2 or tmp == 4:
        res += 2

print(res)
