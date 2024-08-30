import sys
input = sys.stdin.readline

'''
?? ??? ????? ??
2? ?? ???? tmp? ?????
??? ???? 1??? ??
?? 1? ??? ???? ??? ??? 1?????
??? tmp?
'''

def check(y, x, key):
    friend = student[key]
    tmp_result = 0
    for i in range(4):
        newY, newX = y + dy[i], x + dx[i]
        if 0 <= newY < n and 0 <= newX < n and graph[newY][newX] in friend:
            tmp_result += 1
    if tmp_result != 0:
        return 10 ** (tmp_result - 1)
    else:
        return 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n = int(input())
student = dict()
for i in range(n * n):
    tmp = list(map(int, input().split()))
    # O(n)?? ???? ?? set ??? ??
    student[tmp[0]] = set(tmp[1:])

graph = [[0 for _ in range(n)] for _ in range(n)]

for key in student:
    tmp = []
    for i in range(n):
        for j in range(n):
            # ?? ????
            if graph[i][j] == 0:
                preference = 0
                black = 0
                for k in range(4):
                    newY, newX = i + dy[k], j + dx[k]
                    if 0 <= newY < n and 0 <= newX < n:
                        if graph[newY][newX] in student[key]:
                            preference += 1
                        if graph[newY][newX] == 0:
                            black += 1
                tmp.append([preference, black, i, j])
    tmp.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
    graph[tmp[0][2]][tmp[0][3]] = key

result = 0
for i in range(n):
    for j in range(n):
        result += check(i, j, graph[i][j])
print(result)