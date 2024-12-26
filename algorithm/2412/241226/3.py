import sys
input = sys.stdin.readline

a = int(input())

# 에라토스테네스의 체 방식 채택
# 소수의 곱은 더이상 소수가 아님을 이용
isPrime = [True] * (a + 1)
# 0, 1은 소수가 아님으로 초기화 해줌
isPrime[0], isPrime[1] = False, False

# 모든 합성수는 소수의 배수임으로 a ** 0.5까지만 탐색해도 된다.
for i in range(2, int(a ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i * i, a + 1, i):
            isPrime[j] = False

# 살아남은 소수를 result에 누적시킴
# DP를 사용한 방식을 채택할 수도 있지만 단 한번의 계산만 하면 됨으로 단순 반복문으로 처리
result = 0
for i in range(1, a + 1):
    if isPrime[i]:
        result += i

print(result)