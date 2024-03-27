import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1 = 강수량 1 ~ n+1
# 전체 탐색 시작
result = 0
def search_safe(result, max_value):
    for i in range(0, max_value + 1):
        visited = set()
        safe = 0
        for y in range(n):
            for x in range(n):
                safe += dfs(i, x, y, visited)
        result = max(result, safe)
    return result

# 시간날때 bfs로 풀어보기
# queue를 사용하면 됨

def dfs(i, x, y, visited):
    if x < 0 or n <= x or 0 > y or y >= n or (x,y) in visited or arr[y][x] <= i:
        return 0
    visited.add((x, y))
    # 동
    if x + 1 <= n:
        dfs(i, x + 1, y, visited)
    # 서
    if x - 1 >= 0:
        dfs(i, x - 1, y, visited)
    # 남
    if y - 1 >= 0:
        dfs(i, x, y - 1, visited)
    # 북
    if y + 1 <= n:
        dfs(i, x, y + 1, visited)
    return 1


n = int(input())
arr = list(list(map(int, input().split())) for _ in range(n))
max_value = max(max(row) for row in arr)
print(search_safe(result, max_value))

