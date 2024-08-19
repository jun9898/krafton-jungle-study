import sys
from collections import deque

input = sys.stdin.readline

'''
무지성 BFS로 탐색
여기서 특이점은 버튼을 누를 수 있는 횟수가 정해져있다는것
queue를 정확히 주어진 갯수만큼만 순회해야함
'''

def bfs():
    queue = deque([(n, 0)])
    visited = {n}
    while queue:
        curN, curT = queue.popleft()
        if curN == g:
            print(curT)
            return
        if curT == t: continue
        newPlus = curN + 1
        newMul = curN * 2
        if newPlus <= 99999 and newPlus not in visited:
            visited.add(newPlus)
            queue.append((newPlus, curT + 1))
        if newMul <= 99999:
            newMulStr = str(newMul)
            firstDigit = int(newMulStr[0])
            if firstDigit >= 1:
                newFirstDigit = firstDigit - 1
                newMul = int(str(newFirstDigit) + newMulStr[1:])
                if 0 < newMul <= 99999 and newMul not in visited:
                    visited.add(newMul)
                    queue.append((newMul, curT + 1))

    print("ANG")


n, t, g = map(int, input().split())
bfs()


