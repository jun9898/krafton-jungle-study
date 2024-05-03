import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
tmp_string = input().rstrip()

IOI = "IOI"
answer, count = 0, 0,

tmp_res = []
while len(IOI) <= len(tmp_string):
    if "IOI" == tmp_string[:3]:
        tmp_string = tmp_string[2:]
        count += 1
        if count == n:
            answer += 1
            count -= 1
    else:
        tmp_string = tmp_string[1:]
        count = 0

print(answer)






