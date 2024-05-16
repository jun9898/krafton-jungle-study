import sys
input = sys.stdin.readline


# 최대공약수 구하는 공식
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
for i in range(n):
    tmp = list(map(int, input().split()))
    result = 0
    for j in range(1, len(tmp)):
        for k in range(j + 1, len(tmp)):
            result += gcd(tmp[j], tmp[k])
    print(result)
