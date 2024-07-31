import sys
input = sys.stdin.readline

x, y = input().split()

x = int(x[::-1])
y = int(y[::-1])

add = str(x+y)
print(int(add[::-1]))

