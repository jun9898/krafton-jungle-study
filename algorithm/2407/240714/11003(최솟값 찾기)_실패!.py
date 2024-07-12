import sys
import heapq
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())

# 배열을 저장하는 queue
queue = deque(list(map(int, input().split())))

# min 값의 배열과 index를 저장할 heapq 하나 선언
min_heapq = []
result = []

for i in range(N):
    # 만약 요구조건을 충족하지 못할 시
    # 이 조건이 정말 필요할까
    # if i - L + 1 <= 0:
    #     heapq.heappush(min_heapq, (queue.popleft(), i))
    heapq.heappush(min_heapq, (queue.popleft(), i))
    # 만약 요구조건을 충족하면 여기서부터 복잡해지는데
    # else:
    if i - L + 1 > 0:
    # 만약 최소값의 인덱스가 요구 조건에 부적합하면 heapq에서 제외한다
        if min_heapq[0][1] < i - L + 1:
            heapq.heappop(min_heapq)

    # 최종적으로는 heapq의 0번 인덱스의 key값을 출력
    result.append(min_heapq[0][0])
print(*result)
