import sys
input = sys.stdin.readline

n, k = map(int, input().split())

Array = [i for i in range(1, n+1)]
result = []
k = k-1
reset = k

while Array:
    result.append(Array.pop(k))
    k += reset
    while Array:
        if k >= len(Array):
            k = k % len(Array)
        else:
            break

print(str(result).replace("[", "<").replace("]", ">"))
