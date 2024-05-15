import sys
input = sys.stdin.readline

decimal = []
decimal_arr = [0]
max_value = 0


def update_decimal(n):

    cur = n - max_value
    # arr extend
    decimal_arr.extend([1] * cur)

    for i in range(2, n + 1):
        if decimal_arr[i] == 1:
            tmp = i
            for j in range(i * 2, n + 1, tmp):
                decimal_arr[j] = 0

    for i in range(max_value, n + 1):
        if i == 1 or i == 0:
            continue
        if decimal_arr[i] == 1:
            decimal.append(i)


while True:
    n = int(input())
    if n == 0:
        break
    if n > max_value:
        update_decimal(n)
        max_value = n

    start = 0
    end = len(decimal)
    while start < end:
        end_value = decimal[end-1]
        result = []
        for i in range(start, end):
            if end_value + decimal[i] == n:
                result.append(decimal[i])
                result.append(end_value)
        if result:
            break
        else:
            end -= 1
    print("%d = %d + %d" % (n, result[0], result[1]))





