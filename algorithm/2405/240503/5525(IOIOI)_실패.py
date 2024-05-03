import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
tmp_string = input().rstrip()

IOI = "IOI"

IOI_length = len(IOI)
tmp_res = []
while IOI_length <= len(tmp_string):
    # 만약 특정 패턴 발견시
    if IOI == tmp_string[:3]:
        # 연속되는 IOI가 몇게 있는지 count
        count = 0
        while IOI_length <= len(tmp_string):
            if "IOI" != tmp_string[:3]:
                tmp_string = tmp_string[1:]
                break
            count += 1
            tmp_string = tmp_string[2:]
        tmp_res.append(count)
    else:
        tmp_string = tmp_string[1:]

res = 1
for i in tmp_res:
    if i >= n:
        res += i - n + 1

print(res-1)






