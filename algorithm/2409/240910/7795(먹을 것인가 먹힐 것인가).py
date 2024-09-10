import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    result = 0
    index = 0

    for i in range(N):
        while True:
            if index == M or A[i] <= B[index]:
                result += index
                break
            else:
                index += 1
    print(result)