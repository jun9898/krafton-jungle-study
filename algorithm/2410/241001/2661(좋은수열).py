import sys
input = sys.stdin.readline

def is_valid(num_list, count):
    for i in range(1, count // 2 + 1):
        if num_list[-i:] == num_list[-2*i:-i]:
            return False
    return True

def choose_num(num_list, count):
    if count == N:
        print(''.join(map(str, num_list)))
        exit(0)

    for i in range(1, 4):
        num_list.append(i)
        if is_valid(num_list, count + 1):  # 추가한 후 유효성 검사
            choose_num(num_list, count + 1)
        num_list.pop()

N = int(input())
choose_num([], 0)
