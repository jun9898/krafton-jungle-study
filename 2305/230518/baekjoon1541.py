import sys
input = sys.stdin.readline

# 모든 입력값을 연산한 값을 저장해줄 변수 count
count = 0

# a에 입력된 값을 - 를 기준으로 나눠서 리스트에 문자열로 저장한다.
a = list(map(str, input().split("-")))

# for문을 사용해 식의 맨 처음값을 + 로 기준으로 나눈 뒤 i에 대입해서 루프를 돌린다. 
# ex) ['1+2+3+4'] => [1,2,3,4]
for i in a[0].split("+"):
    # count에 더해서 저장
    count += int(i)

# for 문을 사용해 -로 나눠진 리스트의 값을 i에 대입해서 루프를 돌린다.
# ex) ['1+2', '3+4'] 
for i in a[1:]:
    # 다시한번 for 문을 사용해 i의 값을 +를 기준으로 나눠준 뒤 j에 대입해 루프를 돌려준다.
    # ex) ['1+2', '3+4'] => [1,2,3,4]
    for j in i.split("+"):
        # 첫 + 연산 뒤의 모든 숫자는 다 -로 적용하여 계산하여도 무방하므로 다 - 연산 해준다.
        count -= int(j)
print(count)

