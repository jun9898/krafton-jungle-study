import sys
input = sys.stdin.readline

n = int(input())
students = []

for i in range(n):
    tmp = input().rstrip().split()
    name = tmp[0]
    scores = list(map(int, tmp[1:]))
    students.append([name] + scores)
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in students:
    print(student[0])