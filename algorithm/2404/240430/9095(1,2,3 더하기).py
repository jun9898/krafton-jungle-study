import sys
input = sys.stdin.readline

n = int(input())

dp_table = [0,1,2,4]

for i in range(n):
    a = int(input())
    # dp_table에 해당 값의 인덱스가 있으면
    if len(dp_table)-1 >= a:
        print(dp_table[a])
    else:
        # dp 테이블에 값 추가
        while len(dp_table)-1 <= a:
            dp_table.append(dp_table[-3]+dp_table[-2]+dp_table[-1])
        print(dp_table[a])