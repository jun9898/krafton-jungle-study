import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic_num = dict()
dic_name = dict()

for i in range(1, n+1):
    poket = input().rstrip()
    dic_num[i] = poket
    dic_num[poket] = i
    dic_name[poket] = i  # 이름으로도 검색할 수 있도록 추가

for i in range(m):
    input_command = input().rstrip()
    # 숫자면
    if input_command.isdigit():
        print(dic_num[int(input_command)])
    else:
        print(dic_name[input_command])
