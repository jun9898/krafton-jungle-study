# 시간복잡도 개선을 위해 import sys 
import sys
input = sys.stdin.readline

# 반복횟수 설정
n = int(input())
# 명령어 리스트에 저장
commend = []
# queue 리스트 준비
queue = []


# 반복 시작
for i in range(n):
    # commend에 명령어 입력
    commend.append(input().split())
    # 만약 commend 안에 push 명령어가 있다면
    if "push" in commend[i]:
        # queue 자료형에 commend에 push와 함께 입력한 숫자 삽입
        queue.append(commend[i][-1])
    # 만약 commend 안에 pop 명령어가 있다면
    elif "pop" in commend[i]:
        try:
            # queue 리스트 첫번째 숫자를 대상으로 pop 명령어를 사용하고 출력함
            print(queue.pop(0))
        except:
            # 불가능하다면 print(-1)
            print(-1)
    # 만약 commend 안에 size 명령어가 있다면
    elif "size" in commend[i]:
        # queue 리스트의 전체 길이를 출력
        print(len(queue))
    # 만약 commend 안에 empty 명령어가 있다면
    elif "empty" in commend[i]:
        # queue 리스트의 전체 길이가 0이 아닐경우
        if len(queue) != 0:
            # print(0)
            print(0)
        # 전체길이가 0이라면
        else:
            #print(1)
            print(1)
    # 만약 commend 안에 front 명령어가 있다면
    elif "front" in commend[i]:
        try:
            # queue 리스트의 첫번째 숫자를 출력
            print(queue[0])
        except:
            # queue 리스트의 첫번째 숫자가 비어있다면 print(-1)
            print(-1)
    # 만약 commend 안에 back 명령어가 있다면
    elif "back" in commend[i]:
        try:
            # queue 리스트의 마지막 숫자 출력
            print(queue[-1])
        except:
            # queue 리스트의 마지막 숫자가 비어있다면 print(-1)
            print(-1)

