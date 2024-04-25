import sys
input = sys.stdin.readline


def solve(x, y, total_length):
	global res
	if total_length <= 0:
		return
	flag = search(x,y,total_length)
	if flag == 2:
		res += "("
		solve(x, y, total_length//2)
		solve(x+total_length//2, y, total_length//2)
		solve(x, y+total_length//2, total_length//2)
		solve(x+total_length//2, y+total_length//2, total_length//2)
		res += ")"
	else:
		res += str(flag)

	

def search(x, y, total_length):
	flag = plate[y][x]
	for i in range(y, y + total_length):
		for j in range(x, x + total_length):
			if plate[i][j] != flag:
				return 2
	return flag


n = int(input())

plate = []
res = ""
for i in range(n):
	string = input().rstrip()
	row = []
	for i in string:
		row.append(int(i))
	plate.append(row)
	
solve(0,0,len(plate))
print(res)
