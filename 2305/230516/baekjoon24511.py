# 오답 이유 : 시간초과

import sys
input = sys.stdin.readline
# 배열의 갯수
n = int(input())

# 배열의 형식 (stack, queue)
dataA = list(map(int, input().split()))

# 배열에 들어갈 숫자
dataB = list(map(int, input().split()))

# 수열의 갯수
m = int(input())

# 수열
c = list(map(int,input().split()))

#결과값 저장
result = []

# 수열의 갯수만큼 반복문 시작
for i in range(m):
    # 배열의 갯수만큼 2중 반복문 시작
    for j in range(n):

        # 쓸대없는 리스트 삭제
        # listTest = []
        # listTest.append(dataB[j])
        # listTest.append(c[i])

        # 만약 수열의 형식이 큐라면
        if dataA[j] == 0:
            # c[i] 값과 dataB 값을 바꿔줌
            dataB_1 = c[i]
            c[i] = dataB[j]
            dataB[j] = dataB_1

        # 배열의 구조가 스택일 시 그냥 스킵해도 됨
        # else:
        #     c[i] = dataB[-1]
        # dataB[j] = c[i]

    # 최종적으로 바뀐 c[i]값을 result에 append
    result.append(c[i])
    
#출력
print(*result)