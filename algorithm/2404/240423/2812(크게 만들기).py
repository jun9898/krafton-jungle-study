import sys
input = sys.stdin.readline

n, k = map(int, input().split())
input_string = input().rstrip()
tmp_stack = []
result_arr = []
flag = 0

for i in range(len(input_string)):
    # 최초로 들어가는 값은 무조건 넣기
    if flag == k:
        break
    cur_integer = int(input_string[i])
    if len(tmp_stack) == 0:
        tmp_stack.append(cur_integer)
    elif tmp_stack[-1] < cur_integer:
        while len(tmp_stack) != 0 and tmp_stack[-1] < cur_integer and flag != k:
            tmp_stack.pop()
            flag += 1
        tmp_stack.append(cur_integer)
        index = i
    else:
        tmp_stack.append(cur_integer)
        index = i
if flag != k:
    combined_string = ''.join(map(str, tmp_stack)) + input_string[index+1:]
    print(combined_string[:-k+flag])
else:
    print(''.join(map(str, tmp_stack)) + input_string[index+1:])



