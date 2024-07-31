import sys
input = sys.stdin.readline

# 반복횟수 n과 stack, 결과값을 저장할 count와 find를 할당해준다
n = int(input())
stack = []
result = []
count = 1
find = True

# 반복문 시작
for i in range(n):
    m = int(input())

    # count 의 값이 m보다 작거나 같을때
    while count <= m:
        # stack list에 count값을 더해준다
        stack.append(count)
        # 결과값에 값을 더해줬음을 뜻하는 +를 append 해준다
        result.append("+")
        # 반복 count값을 1을 더해준다
        count += 1
    # 만약 stack의 마지막 수가 입력값 m 과 같을때
    if stack[-1] == m:
        # stack 마지막 값을 제거한다
        stack.pop()
        # 결과값에 값을 pop을 수행했음을 뜻하는 +를 append 해준다
        result.append("-")
    # 만약 위 작업이 불가능 할 떈 find = False로 바꿔줘 No를 출력할 수 있게끔 해준다.
    else:
        find = False

# 출력
if find == True:
    for i in result:
        print(i)
else:
    print("NO")
