import sys
input = sys.stdin.readline

res = 0

def hanoi(plate, start, end):
    if plate == 1:
        print(start, end)
        return
    mid = 6 - start - end
    hanoi(plate-1, start, mid)
    print(start, end)
    hanoi(plate-1, mid, end)

n = int(input())
print(2 ** n - 1)
if n <= 20:
    hanoi(n, 1, 3)