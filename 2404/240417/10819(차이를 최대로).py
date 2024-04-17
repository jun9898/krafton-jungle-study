import sys
input = sys.stdin.readline


def calc(path):
    global res
    tmp = 0
    for i in range(1,len(path)):
        tmp += abs(path[i-1] - path[i])
    res = max(res, tmp)


def solve(elements, n, path):
    if len(path) == n:
        calc(path)
    for i, element in enumerate(elements):
        solve(elements[:i] + elements[i+1:], n, path + [element])


res = 0
n = int(input())
arr = list(map(int, input().split()))
solve(arr, n, [])

print(res)