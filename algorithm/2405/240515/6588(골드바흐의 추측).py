import sys
input = sys.stdin.readline

decimal_arr = [True] * 1000001
m = int(1000001**0.5)

for i in range(2, m+1):
    if decimal_arr[i]:
        tmp = i
        for j in range(i + i, 1000001, tmp):
            decimal_arr[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(2, m+3):
        if decimal_arr[i] and decimal_arr[n - i]:
            print("%d = %d + %d" % (n, i, n - i))
            break
