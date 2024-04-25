import sys
input = sys.stdin.readline

div = 15746
# 배열을 선언하는 단계에서 메모리 초과가 발생하는 듯 함
def bottom_up(n):
    # 만약 n의 값이 1이면
    if n < 2:
        return n
    fib[1]= 1
    for i in range(2, n+1):
        fib[i] = (fib[i-1] + fib[i-2]) % div
    return fib[n]


# 상수를 인덱스로 변경
# 1이 입력값으로 들어오면 index는 2를 가르켜야함
n = int(input()) +1
# 피보나치의 값을 저장할 배열 선언
fib = [0] * (n + 1)
# 1 = 1 1
# 2 = 2 00 11
# 3 = 3 001 100 111
# 4 = 5 1111 0000 0011 1001 1100
# 5 = 8 11111 00001 00100 10000 00111 11100 10011 11001
# 그냥 피보나치인듯 함

print(bottom_up(n))