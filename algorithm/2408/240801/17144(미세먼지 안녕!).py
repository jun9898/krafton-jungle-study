import sys
from collections import deque

input = sys.stdin.readline

'''
포인트는 족적 남기기!
기존 숨바꼭질에서 각 step마다 어떤 족적을 남겼는지만 기록해두면 될듯
'''

def bfs():
    queue = deque([N])
    while queue:
        cur = queue.popleft()
        # 동생과 만나면
        if cur == K:
            # 얼마나 걸렸는지 출력
            print(dist[cur])

            # 남겨둔 족적 탐색
            result = []
            tmp = cur
            for _ in range(dist[cur] + 1):
                result.append(tmp)
                tmp = move[tmp]
            for i in range(len(result) - 1, -1, -1):
                print(result[i], end=" ")

            return
        for i in (cur + 1, cur - 1, cur * 2):
            # 처음 방문하는 곳일때만
            if 0 <= i < len(dist) and dist[i] == 0:
                queue.append(i)
                dist[i] = dist[cur] + 1
                move[i] = cur



N, K = map(int, input().split())
dist = [0] * 100001
move = [0] * 100001
bfs()

