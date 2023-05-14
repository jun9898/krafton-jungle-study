num, index = map(int,input().split())   #해당 숫자와 리스트의 인덱스를 구할 수를 입력받는다.
numList = []    #조건이 맞는 숫자가 추가될 리스트

for i in range(1, num+1):   #반복문을 통해 조건에 맞는 숫자를 리스트에 추가한다
    if num % i == 0:
        numList.append(i)

try:    #리스트에 추가된 값에 index - 1을 출력한다
    print(numList[index-1])
except:  #만약 index의 값이 numList의 인덱스 값에 포함되지 않을시 0을 출력한다.
    print(0)

