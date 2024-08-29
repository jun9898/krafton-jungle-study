import sys
input = sys.stdin.readline

def check(sign ,a, b):
    if sign == '<':
        return a < b
    elif sign == '>':
        return a > b

def dfs(arr, index):
    global result
    if len(arr) == (n + 1):
        result.append("".join(map(str, arr)))
        return
    for i in range(10):
        if arr:
            if i not in visited and check(sign_arr[index], arr[-1], i):
                arr.append(i)
                visited.add(i)
                dfs(arr, index + 1)
                visited.remove(i)
                arr.pop()
        else:
            arr.append(i)
            visited.add(i)
            dfs(arr, 0)
            visited.remove(i)
            arr.pop()

n = int(input())
visited = set()
result = []
sign_arr = list(input().split())
dfs([], 0)
print(result[-1])
print(result[0])
