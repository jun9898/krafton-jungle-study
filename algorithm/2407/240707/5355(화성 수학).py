import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    arr = list(input().split())
    result = float(arr[0])
    for j in range(1, len(arr)):
        if arr[j] == '@':
            result *= 3
        elif arr[j] == '%':
            result += 5
        elif arr[j] == '#':
            result -= 7
    print(f'{result:.2f}')

