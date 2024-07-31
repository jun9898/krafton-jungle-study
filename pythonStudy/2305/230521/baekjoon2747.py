import sys
input = sys.stdin.readline
# n의 값을 입력받는다.
n = int(input())
# m은 피보나치의 값을 저장해줄 변수
m = 0
# pList는 모든 피보나치수열을 저장해줄 리스트이다
pList = []

# 입력 횟수만큼 반복
for i in range(n):
    # 만약 반복 횟수가 2번 이하라면
    if i <= 1:
        # 피보나치 수열의 특성상 첫번째와 두번째 숫자가 1이여야 함으로
        # pList에 1을 2번 더해준다
        pList.append(1)
        # 피보나치 수를 저장할 변수 m에 1을 더해준다
        m += 1
    # 만약 반복 횟수가 2번을 초과한다면
    else:
        # m의 값은 pList의 가장 마지막 두 수를 더해준 값이다.
        m = pList[i-1] + pList[i-2]
        # 그 수를 pList에 append
        pList.append(m)
# pList의 마지막에 추가된 수를 print
print(pList[-1])
