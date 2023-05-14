# 이거 하면 빨라지는건 아는데 왜 하는지 모르겠슴
import sys
input=sys.stdin.readline

# 반복 횟수를 입력받는다
n = int(input())
# 명령어를 저장할 list 생성
commendList = []
# 명령으로 인해 발생한 변수를 저장할 stacklist 생성
stack = []

# 입력한 n의 값만큼 반복문 실행
for i in range(n):
    # commendList에 명령어 입력
    commendList.append(input().split())
    # 만약 push 명령어가 commendList[i] 에 속해있다면
    if "push" in commendList[i]:
        # stack 리스트에 push와 함께 입력된 숫자를 append
        stack.append(int(commendList[i][-1]))
    # 만약 pop 명령어가 commendList[i] 에 속해있다면
    elif "pop" in commendList[i]:
        # stack.pop() 명령어를 실행 후 에러가 발생한다면 print(-1) 이 출력되도록 예외처리
        try:
            print(stack.pop())
        except:
            print(-1)
    # 만약 size 명령어가 commendList[i] 에 속해있다면
    elif "size" in commendList[i]:
        # stack 리스트의 길이를 출력한다
        print(len(stack))
    # 만약 empty 명령어가 commendList[i] 에 속해있다면
    elif "empty" in commendList[i]:
        # stack 의 길이가 0이 아니면 print(0) stack 의 길이가 0이라면 print(1)
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    # 만약 top 명령어가 commendList[i] 에 속해있다면
    elif "top" in commendList[i]:
        # stack 리스트의 마지막 요소를 print. 만약 리스트가 비어있다면 print(-1)
        try:
            print(stack[-1])
        except:
            print(-1)