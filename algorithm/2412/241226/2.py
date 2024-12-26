import sys
input = sys.stdin.readline

'''
입출력 예
1 2 3 4 5
'''

# 최대 공약수를 계산하는 재귀 함수
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# 최소 공배수를 계산하는 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 입력받음과 동시에 set 자료형의 특징을 사용해 중복된 값을 지운다.
arr = list(set(map(int, input().split())))

lcmSum = 0
length = len(arr)
for i in range(length):
    for j in range(i + 1, length):
        lcmSum += lcm(arr[i], arr[j])

print(lcmSum)