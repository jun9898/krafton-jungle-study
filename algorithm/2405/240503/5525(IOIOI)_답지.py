import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
tmp_string = input().rstrip()

answer, i, count = 0, 0, 0

tmp_res = []
while i <= m-1:
    # 만약 특정 패턴 발견시
    if "IOI" == tmp_string[i:i+3]:
        # 연속되는 IOI가 몇게 있는지 count
        i += 2
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)






