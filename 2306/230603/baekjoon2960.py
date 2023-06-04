"""
deque 짱
"""
import sys
# deque를 사용할거다
from collections import deque as de

input = sys.stdin.readline

# 배열의 범위를 정해주고 K값을 입력받는다.
n, k = map(int, input().split())
# 1부터 n의 값까지 정의된 deque를 만들어준다.
array = de(i for i in range(2, n+1))
# 결과값을 저장할 배열을 만들어준다.
result = []

# array에 값이 있다면
while array:
    # a는 배열의 첫번째 수이다
    # 배열의 첫번째 수는 소수 a의 배수를 모두 제거한 수 이므로 항상 소수일수밖에 없다.
    a = array[0]
    # array의 길이만큼 반복한다.
    for _ in range(len(array)):
        # 만약 array 가장 앞의 값이 a로 나머지 없이 나눠진다면.
        if array[0] % a == 0:
            # array의 첫번째 값을 추출해서 result에 넣어준다
            result.append(array.popleft())
        # 만약 소수 a의 배수가 아니라면
        else:
            # 배열을 한바퀴 회전시켜준다.
            array.rotate(-1)

print(result[k-1])

