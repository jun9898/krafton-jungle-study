import sys
#intertools의 combinations 기능을 사용한다.
from itertools import combinations as combi
input = sys.stdin.readline

# 도시의 범위인 N과 최소 치킨거리를 계산할 M을 입력받는다.
n, m  = map(int,input().split())
# 도시의 정보를 2차원 list로 입력받는다.
cityMap = list(list(map(int, input().split())) for _ in range(n))
# house의 위치를 저장할 리스트 생성
house = []
# 치킨집의 위치를 저장할 리스트 생성
chickenHouse = []
# 최종 출력할 결과값 을 설정해준다. 이 값을 크게 주는건 나중 치킨거리를 계산할 for문에서 
# 나온 cityLen 값보다 커야 정상적으로 min 명령어가 작동하기 떄문에 값을 크게 준다.
result = 99999

# 치킨집과 집의 위치를 입력받을 2중 for문 시작
for i in range(n):
    for j in range(n):
        # 만약 citymap[i][j]의 값이 1이라면
        if cityMap[i][j] == 1:
            # 집의 위치를 리스트에 저장
            house.append([i,j])
        # 만약 citymap[i][j]의 값이 2이라면
        elif cityMap[i][j] == 2:
            # 치킨집의 위치를 리스트에 저장
            chickenHouse.append([i,j])

# 저장해놨던 치킨집을 m의 개수로 묶을 수 있는 모든 경우의 수로 for문을 돌린다.
for chicken in combi(chickenHouse,m):
    # 1번의 루프가 끝나면 cityLen을 초기화해준다. 
    cityLen = 0
    # 집의 위치를 하나씩 추출해서 치킨집과의 거리를 계산해줄거다. 
    for houseDistens in house:
        # 여기서 chickinLen의 길이를 크게 주는 이유는 마찬가지로 min 명령어를 작동시키기 위해 크게 준다.
        chickenLen = 999999
        # 이제부터 m개씩 분할된 chickin과 집의 거리를 계산해준다.
        for j in range(m):
            # house의 거리와 치킨집의 거리를 계산해 절댓값으로 반환한다.
            # chickinLen은 루프가 반복될때마다 자기 자신과 비교해서 더 작은 값을 저장해준다.
            chickenLen = min(chickenLen, abs(houseDistens[0] - chicken[j][0]) + abs(houseDistens[1] - chicken[j][1]))
        # 그렇게 나온 값을 cityLen에 더해 저장한다.
        cityLen += chickenLen
    # 치킨집의 m개의 집합에 대한 비교가 끝날때마다 각 배열의 최솟값을 result 자신의 값과 비교해 저장한다.
    result = min(result,cityLen)

# 최종적으로 나온 최솟값을 print
print(result)
