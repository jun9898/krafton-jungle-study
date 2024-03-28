import sys
input = sys.stdin.readline

def solve(i, j, target_i, target_j):
	global res
	x = (i+j) % 10
	res += 1
	if j == target_i and x == target_j:
		return
	solve(j, x, target_i, target_j)


n = int(input())

i = n // 10
j = n % 10

res = 0

solve(i, j, i, j)
print(res)
