import sys
'''
입출력 예
3 <- 전체 문제의 개수
1 5 <- 정답의 번호, 점수
5 5
2 4
'''

# 전체 문제의 개수 입력
n = int(input())

if n <= 0:
    print("Error: Number of problems must be a positive integer")
    sys.exit(1)  # 프로그램 종료

# 점수를 저장할 딕셔너리 초기화 (각 응시자 이름을 키로 사용)
scores = {"a": 0, "b": 0, "c": 0}

# 정답 번호와 응시자 이름의 매핑
answers = {1: "a", 3: "b", 5: "c"}

for _ in range(n):
    try:
        answer, score = map(int, input().split())
    except ValueError:
        # 입력값이 숫자가 아니면 에러 메시지 출력 후 종료
        print("Error: Answer or score is not a number")
        sys.exit(1)

    # 예외처리 코드를 작성했지만 너무 많은 글자수때문에 가독성을 헤쳐 제외했습니다.

    # 유효한 정답 번호에 해당하는 응시자 점수 누적
    if answer in answers:
        scores[answers[answer]] += score

# 최고 점수 계산
maxScore = max(scores.values())

# 최고 점수를 받은 응시자를 찾음
result = [f"{key} : {maxScore}" for key, value in scores.items() if value == maxScore]

# 결과 출력 (최고 점수를 받은 모든 응시자를 콤마로 구분)
print(", ".join(result))