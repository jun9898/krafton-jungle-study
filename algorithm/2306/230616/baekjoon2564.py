import sys
input = sys.stdin.readline

def get_distance(x,y):
    if x==1:
        return y
    if x==2:
        return w + h + w - y
    if x==3:
        return w + h + w + h - y
    if x==4:
        return w + y

w, h = map(int,input().split())
n = int(input())

course = []

for _ in range(n+1):
    x, y = map(int,input().split())
    course.append(get_distance(x,y))

answer = 0

for i in range(n):
    in_course = abs(course[-1] - course[i])
    out_course = 2 * (w+h) - in_course
    answer += min(in_course,out_course)

print(answer)