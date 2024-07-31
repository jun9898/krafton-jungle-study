import sys
input = sys.stdin.readline

# 문자열을 입력받는다.
string = list(input().rstrip())
# 셈을 하며 result에 더해줄 값을 설정해준다.
tmp = 1
# 해당 문제의 결과값이다.
result = 0
# 괄호가 열리고 닫혔음을 저장해줄 stack이다.
stack = []

# 문자열의 길이만큼 반복을 시작한다.
for i in range(len(string)):
    # 만약 ( 괄호가 열리면
    if string[i] == "(":
        # tmp에 2를 곱해준다.
        tmp *= 2
        # stack엔 괄호가 열렸음을 표현하기 위해 ( 기호를 더해준다.
        stack.append(string[i])
    # 만약 [ 괄호가 열리면
    elif string[i] == "[":
        # tmp에 3을 곱해준다.
        tmp *= 3
        # stack엔 괄호가 열렸음을 표현하기 위해 [ 기호를 더해준다.
        stack.append(string[i])
    # 만약 괄호가 닫혔을땐
    elif string[i] == ")":
        # stack 안에 괄호가 남아있지 않고 stack의 끝에 해당 괄호의 짝이 아닌 다른 기호가 있다면
        if len(stack) == 0 or stack[-1] != "(":
            # 잘못된 수식임으로 바로 종료한다.
            result = 0
            break
        # 만약 string i와 string i-1의 쌍이 맞는다면
        if string[i-1] == "(":
            # result에 tmp값을 더해준다
            result += tmp
        # 괄호 한쌍의 수식이 종료되었음으로 stack에 마지막 수를 pop해주고 tmp를 2로 나눠준다.
        stack.pop()
        tmp //= 2
    # 만약 괄호가 닫혔을땐
    elif string[i] == "]":
        # stack 안에 괄호가 남아있지 않고 stack의 끝에 해당 괄호의 짝이 아닌 다른 기호가 있다면
        if len(stack) == 0 or stack[-1] != "[":
            # 잘못된 수식임으로 바로 종료한다.
            result = 0
            break
        # 만약 string i와 string i-1의 쌍이 맞는다면
        if string[i-1] == "[":
            # result에 그동안 누적되어왔던 tmp값을 더해준다.
            result += tmp
        # 괄호 한쌍의 수식이 종료되었음으로 stack에 마지막 수를 pop해주고 tmp를 3로 나눠준다.
        stack.pop()
        tmp //= 3

# stack에 뭔가 남아있다면 print(0)
if len(stack) != 0:
    print(0)
# 아니면 result 값 출력
else:
    print(result)