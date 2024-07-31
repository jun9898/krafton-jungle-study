#math의 inf는 무한대 값을 의미한다.
from math import inf
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

groud = [list(map(int,input().split())) for _ in range(N)]

# ground에 포함된 최대값과 최소값을 구해줄 list를 하나 더 만든다
listMaxMin = []
for _ in range(N):
    listMaxMin.extend(groud[_])

# 최대값과 최솟값
minGroud = min(listMaxMin)
maxGroud = max(listMaxMin)
# 완전 탐색을 위해 시간은 최대한 큰 수를 설정해준다.
time = inf

# 최소 높이 블록부터 최대 높이 블록까지 탐색
for i in range(minGroud, maxGroud +1):
    # 제거한 블록
    take = 0
    # 인벤토리에서 사용한 블록
    use = 0
    # i 열을 기준으로 모든 블록을 평탄화 작업한다.
    # 완전탐색 시작
    for j in range(N):
        for z in range(M):
            # 만약 해당 배열이 i 번째 블록보다 높으면
            if groud[j][z] > i:
                # 제거한 블록의 값을 take에 더해준다.
                take += groud[j][z] -i
            else:
                # 해당 배열이 i 번째 블록보다 낮으면 블록을 사용해 채워놓는다.
                use += i - groud[j][z]
    
    # 만약 인벤토리의 블록보다 더 많은 블록을 사용했을 때
    if use > take + B:
        # 이 경우의 수는 스킵한다.
        continue

    # 시간을 계산해준다.
    result = take * 2 + use
    
    # 만약 i열을 평탄화 할때 걸린 시간이 저번 탐색의 결과값보다 작을시 time에 대입해준다.
    if result <= time:
        time = result 
        # 그리고 해당 열이 몇번째 열인지 저장해준다.
        glevel = i

print(time, glevel)





