import sys
input = sys.stdin.readline

n = int(input())
minOperations = [0] * (n + 1)
previousNumber = [0] * (n + 1)

for i in range(2, n + 1):
    minOperations[i] = minOperations[i - 1] + 1
    previousNumber[i] = i - 1

    if i % 3 == 0:
        operations = minOperations[i // 3] + 1
        if operations < minOperations[i]:
            minOperations[i] = operations
            previousNumber[i] = i // 3

    if i % 2 == 0:
        operations = minOperations[i // 2] + 1
        if operations < minOperations[i]:
            minOperations[i] = operations
            previousNumber[i] = i // 2

print(minOperations[n])

path = []
current = n
while current > 1:
    path.append(current)
    current = previousNumber[current]
path.append(1)

print(' '.join(map(str, path)))
