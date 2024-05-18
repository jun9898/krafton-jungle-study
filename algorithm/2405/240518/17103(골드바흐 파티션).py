import sys
input = sys.stdin.readline

decimal_arr = [True] * 1000001
m = int(1000001**0.5)

for i in range(2, m+1):
    if decimal_arr[i]:
        tmp = i
        for j in range(i + i, 1000001, tmp):
            decimal_arr[j] = False

k = int(input())

for i in range(k):
    n = int(input())
    result = 0
    for j in range(2, n//2+1):
        if decimal_arr[j] and decimal_arr[n - j]:
            result += 1
    print(result)