import sys
input = sys.stdin.readline

n = int(input())

cur_min = list(map(int, input().split()))
cur_max = cur_min[:]

for i in range(1, n):
    new_values = list(map(int, input().split()))
    new_min = [0] * 3
    new_max = [0] * 3

    new_min[0] += new_values[0] + min(cur_min[0], cur_min[1])
    new_min[1] += new_values[1] + min(cur_min[0], cur_min[1], cur_min[2])
    new_min[2] += new_values[2] + min(cur_min[1], cur_min[2])

    new_max[0] += new_values[0] + max(cur_max[0], cur_max[1])
    new_max[1] += new_values[1] + max(cur_max[0], cur_max[1], cur_max[2])
    new_max[2] += new_values[2] + max(cur_max[1], cur_max[2])

    cur_min = new_min
    cur_max = new_max
print(max(cur_max), min(cur_min))