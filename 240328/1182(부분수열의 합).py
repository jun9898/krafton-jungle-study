import sys
input = sys.stdin.readline


def solve(index, sum_stack):
	global res
	if index >= n:
		return
	sum_stack += arr[index]
	if sum_stack == target:
		res += 1
	solve(index+1, sum_stack)
	solve(index+1, sum_stack-arr[index])


res = 0
n, target = map(int, input().split())
arr = list(map(int, input().split()))

solve(0,0)
print(res)

