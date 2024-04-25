import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

queue = []
for i in range(n):
    queue.append(int(input()))

queue.sort()
queue = deque(queue)

res = 0

# 일반 queue로 진행하면 최소값을 찾기위해 계속 정렬해줘야 해서 엄청나게 복잡해진다
while len(queue) >= 2:
    tmp1 = queue.popleft()
    tmp2 = queue.popleft()
    res += tmp1 + tmp2
    queue.append(tmp1+tmp2)

print(res)

