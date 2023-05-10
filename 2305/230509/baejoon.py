N = int(input())
nums = 1 #벌집의 개수
cnt = 1 #벌집까지 거리

while N > nums:
    nums += 6 * cnt
    cnt += 1
print(cnt)

# 이 문제는 굉장히 어려워 보이지만 사실 보면 정말 쉬운 문제다.
# 벌집의 개수가 6개씩 늘어난다는 규칙만 찾는다면 while문을 사용해 입력값인 N값이
# 벌집의 개수보다 작아질때까지 반복하며 count하면 쉽게 문제를 해결할 수 있다.
