import sys
input = sys.stdin.readline

# plate = [list([0]*6) for _ in range(6)]
# flag = True

# dic = {'A':0, "B":1, "C":2, "D":3, "E":4, "F":5,}

# for i in range(36):
#     commend = list(input().rstrip())
#     if plate[int(commend[1])-1][dic[commend[0]]] == 0:
#         plate[int(commend[1])-1][dic[commend[0]]] = 1
#         plate[int(commend[1])-1][dic[commend[0]]] = 1
#     else:
#         flag = False
# if flag:
#     print('Valid')
# else:
#     print('Invalid')

def check(now, dest):
    if abs(ord(now[0]) - ord(dest[0])) == 2 and abs(int(now[1]) - int(dest[1])) == 1:
        return 1
    elif abs(ord(now[0]) - ord(dest[0])) == 1 and abs(int(now[1]) - int(dest[1])) == 2:
        return 1

result = []
now = input().rstrip()
result.append(now)
cnt = 1

for i in range(35):
    dest = input().rstrip()
    result.append(dest)

    if check(now,dest) == 1:
        cnt += 1
        now = dest
    else:
        break

if cnt == 36 and len(set(result)) == 36 and check(result[0],result[-1]):
    print('Valid')
else:
    print('Invalid')

