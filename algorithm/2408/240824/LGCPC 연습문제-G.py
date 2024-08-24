import sys
input = sys.stdin.readline

'''
경로적 특성만 뽑아내면 되는데 굳이 graph를 그려야할까?
DFS 사용, 경로적 특성을 이용해 탐색.
상하좌우 모두 방문했다면 visited의 인자 개수를 구하고 
만약 R * C와 일치할 시 True return
만약 True라면 return 경로

10점
내 예상으로는 시간초과 발생하는듯
bfs로 돌려서 visited 처리를 다른 방식으로 해야하나
DP 메모이제이션 사용해서 최적화 해야할듯
시간 없으니 PASS
'''
d = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

def dfs(Y, X, y, x, visited, path):
    if len(visited) == Y * X:
        return path
    # 4방향 탐색
    for i in range(4):
        dy, dx, curPath = d[i]
        newY, newX, newPath = y + dy, x + dx, path + curPath
        if 1 <= newY <= Y and 1 <= newX <= X and (newY, newX) not in visited:
            visited.add((newY, newX))
            result = dfs(Y, X, newY, newX, visited, path + curPath)
            if result:
                return result
            visited.remove((newY, newX))
    return None

T = int(input())

for _ in range(T):
    Y, X, y, x = map(int, input().split())
    visited = {(y, x)}
    result = dfs(Y, X, y, x, visited, "")
    if result:
        print(result)
    else:
        print("IMPOSSIBLE")

