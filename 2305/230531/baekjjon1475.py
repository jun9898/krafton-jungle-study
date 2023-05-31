import sys
input = sys.stdin.readline

# 값을 문자열로 입력받는다
n = str(input().rstrip())

# 결과값을 더해줄 list를 만들어준다.
listIndex = [0] * 10 

# for 문으로 돌리기 위해 문자열로 입력받았다.
for i in n:
    # 만약 i의 값이 6이나 9면 
    if i == '6' or i == '9':
        # list에 6번째나 9번째에 위치한 값이 더 작은쪽에 1을 더해준다.
        if listIndex[6] < listIndex[9]:
            listIndex[6] += 1
        else:
            listIndex[9] += 1
    # 값이 6이나 9가 아닐경우
    else:
        # 해당 인덱스에 1을 더해준다.
        i = int(i)
        listIndex[i] += 1

# list에 최댓값을 출력
print(max(listIndex))
        