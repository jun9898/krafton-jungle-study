import sys
from collections import deque

input = sys.stdin.readline

'''
지금 로직은 한눈에 봐도 문제가 많아보임
visited 처리를 어떻게 해야할지가 관건
내 가설
만약 동생이 도착한곳에 이미 visited 처리가 되어있다면
수빈이는 왓다리 갔다리 움직이며 해당 장소에 머물 수 있음

여기서 또 문제 발생
홀수와 짝수 레벨에 따라 엇갈리는 상황 발생!
이를 해결하기 위해 visited를 홀, 짝으로 나눠주는게 필요할듯
'''

def bfs(n, k):
    visited = [[False] * 500001 for _ in range(2)]
    queue = [n]
    curTime = 1
    k += curTime
    visited[0][n] = True
    while True:
        if k > 500000: return -1
        tmpQueue = set()
        for loc in queue:
            for nextLoc in (loc + 1, loc - 1, loc * 2):
                if 0 <= nextLoc <= 500000 and not visited[curTime % 2][nextLoc]:
                    tmpQueue.add(nextLoc)
                    visited[curTime % 2][nextLoc] = True

        if visited[curTime % 2][k] == True:
            return curTime

        curTime += 1
        k += curTime
        queue = list(tmpQueue)
    return -1


n, k = map(int, input().split())
if n == k:
    print(0)
    sys.exit(0)
print(bfs(n, k))


