# 값을 입력받는다
n = int(input())
# 계산에 사용할 수를 지정해준다
n2 = n
# 사이클이 돌아갈때마다 값을 더해줄 변수
count = 0

while True:
    # n2의 첫째자리수와 둘째자리수를 구한다.
    num1 = n2 // 10
    num2 = n2 % 10
    # 두 수를 더한값의 첫째자리 수를 구한다.
    num3 = (num1 + num2) % 10
    # n2에 각 자리수를 더해서 구한다.
    n2 = (num2 * 10) + num3
    count += 1
    # 만약 그렇게 계산한 수가 초기값 n과 같으면 break
    if(n2 == n):
        break

print(count)

"""
시간초과로 폐기
"""
# import sys
# input = sys.stdin.readline

# n = input().rstrip()
# n2 = n
# count = 0

# while True:
#     if len(n2) < 2:
#         n2 = "0" + n2
#     add = str(int(n2[0]) + int(n2[1]))
#     n2 = n2[-1] + add[-1]
#     count += 1
#     if n2 == n:
#         print(count)
#         break

    



    