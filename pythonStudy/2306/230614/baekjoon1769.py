"""
틀린 이유
num 값이 10 아래의 수가 들어왔을때 예외처리를 안함.
"""
import sys
input = sys.stdin.readline

num = list(input().rstrip())

count = 0
while len(num) > 1:
    answer = 0
    for i in num:
        answer += int(i)
    count += 1
    num = list(str(answer))

print(count)
if int(num[0]) % 3 == 0:
    print('YES')
else:
    print('NO')
