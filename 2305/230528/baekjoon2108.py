import sys
input = sys.stdin.readline

# 반복할 횟수 입력
n = int(input())
# 입력값을 넣어줄 배열 생성
array = []

# 배열에 원하는 값을 n번 넣어준다
for i in range(n):
    array.append(int(input()))
# 오름차순으로 정리
array.sort()

# 평균값을 반올림하여 print
print(round(sum(array)/n))
# array의 중앙값을 출력한다.
print(array[(n//2)])

# 최빈값을 구현하기 위해 딕셔너리 자료구조를 사용했다.
dic = dict()
# array에 들어있는 값을 하나씩 다 넣어준다.
for i in array:
    # 만약 dic 안에 i와 같은값의 Key가 있다면
    if i in dic:
        # dic[i]에 할당된 value에 1을 더해준다.
        dic[i] += 1
    # 만약 dic 안에 i와 같은값의 key가 없다면
    else:
        # dic[1]는 1이다
        dic[i] = 1

# maxValue에 dic의 value중 가장 큰 값을 대입해준다.
maxValue = max(dic.values())

# maxDic는 최빈값이 저장된 key값을 저장해줄것이다
maxDic = []

# 딕셔너리 형식을 for문으로 돌리면 key값이 들어간다.
for i in dic:
    # 만약 최빈값의 중복 횟수인 maxValue와 dic[i]의 value가 같으면
    if maxValue == dic[i]:
        # 딕셔너리의 key값을 maxDic에 더해준다.
        maxDic.append(i)

# 만약 maxDic에 1개 이상의 값이 들어간다면
if len(maxDic)>1:
    # 2번째 값을 프린트
    print(maxDic[1])
# maxDic에 1개의 값만 있다면
else:
    # 1번째 값을 프린트
    print(maxDic[0])

# 아까 정렬해둔 배열을 기반으로 가장 끝값과 끝값을 빼준다.
print(array[-1] - array[0])

