import sys
sys.setrecursionlimit(10**3)
input = sys.stdin.readline


def recursive(row, col, length, value):

    length = length // 2

    if row < length and col < length:
        if length == 1:
            print(value)
            sys.exit(0)
        recursive(row, col, length, value)
    elif row >= length and col < length:
        if length == 1:
            print(value + 1)
            sys.exit(0)
        recursive(row - length, col, length, value + length ** 2)
    elif row < length and col >= length:
        if length == 1:
            print(value + 2)
            sys.exit(0)
        recursive(row, col - length, length, value + length ** 2 * 2)
    elif row >= length and col >= length:
        if length == 1:
            print(value + 3)
            sys.exit(0)
        recursive(row - length, col-length, length, value + length ** 2 * 3)


n, c, r = map(int,input().split())

recursive(r,c,2**n, 0)