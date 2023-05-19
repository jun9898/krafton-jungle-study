import sys
# 이 문제는 deque의 기능을 적극적으로 사용할것이다.
from collections import deque
input = sys.stdin.readline

# 사람 수 n과 k의 값을 입력한다.
n, k = list(map(int, input().split()))
# deque 리스트를 만들어준다.
dequeList = deque()

# deque 리스트에 1부터 n까지의 값을 넣어준다.
for i in range(1, n+1):
    dequeList.append(i)

# 결과값을 저장할 리스트
listResult = []
    
# 사람 수만큼 루프를 돌려준다.
for i in range(n):
    # 1 부터 k까지 j에 대입해서 루프를 돌려준다.
    for j in range(1, k+1):
        # 만약 k번 루프를 돌렸을때
        if j == k:
            # listResult 리스트에 dequeList의 첫번째 값을 추가해준다.
            listResult.append(dequeList[0])
            # deque 리스트 가장 왼쪽 데이터를 추출, 제거
            dequeList.popleft()
        # 만약 아직 k번 루프가 돌지 않았을때
        else:
            # dequeList 내부의 값을 한바퀴 돌려준다.
            # rotate는 사용자가 입력한 값 만큼 list 내부의 값을 한바퀴 돌린다.
            # ex) [1, 2, 3] => [2, 3, 1] 정말 편리한 기능인것같다
            dequeList.rotate(-1)
    
# 예제와 같이 출력하려면 약간의 노가다가 필요하다.
print("<", end= "")
for i in range(len(listResult)-1):
    print(listResult[i], end=", ")
print(str(listResult[len(listResult)-1])+ ">")

# 문제 제출 후 다른사람의 풀이를 보니
print(str(listResult).replace('[' , '<').replace(']', '>'))
# 이 방법도 있는것같다.