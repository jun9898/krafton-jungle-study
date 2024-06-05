import sys
import math
input = sys.stdin.readline

total_team = []

red_team_min = math.inf
blue_team_min = math.inf

for i in range(8):
    tmp = list(input().rstrip().split())
    tmp1 = list(tmp[0].split(":"))
    score = int(tmp1[0])* 100000 + int(tmp1[1]) * 1000 + int(tmp1[2])
    total_team.append((score, tmp[1]))
    if tmp[1] == "R":
        red_team_min = min(red_team_min, score)
    else:
        blue_team_min = min(blue_team_min, score)

total_team.sort()

red_team = 0
blue_team = 0

score = 10
for i in total_team:
    if i[1] == "R":
        red_team += score
    else:
        blue_team += score
    score -= 2

if red_team < blue_team:
    print("Blue")
elif red_team > blue_team:
    print("Red")
else:
    if red_team_min < blue_team_min:
        print("Red")
    else:
        print("Blue")



