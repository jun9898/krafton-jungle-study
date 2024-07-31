import sys
input = sys.stdin.readline

n = int(input())

# 1팀과 2팀의 득점 시간
teamTime1 = 0
teamTime2 = 0

# 플레그 = 1팀과 2팀이 각각 몇점을 득점중인지 표시해줌
flag = 0

# n번 반복 시작
for i in range(n):
    # 팀과 시간을 따로 입력받음
    team, time = input().rstrip().split()
    # 입력받은 시간은 : 를 기준으로 int형으로 나눠준다
    m, s = map(int, time.split(":"))
    # 만약 1팀이 득점했다면
    if team =='1':
        # 만약 지금부터 이기기 시작한다면
        if flag == 0:
            # 전체 시간에서 현제 시간을 빼서 이기기 시작한 시간의 총량을 구한다.
            teamTime1 += 48*60-(60*m+s)
        # 그리고 나서 flag에 1을 더해 현재 이기고 있음을 나타낸다
        flag += 1
        # 만약 flag에 1을 더했을때부터 비기기 시작했다면
        if flag == 0:
            # 동점 상황이 됐음으로 2팀이 이긴 시간의 총량에서 현재 시간을 빼준다.
            if teamTime2 > 0:
                teamTime2 = teamTime2 - (48*60-(60*m+s))
    # 2팀도 마찬가지로 반복
    else:
        if flag == 0:
            teamTime2 += 48*60-(60*m+s)
        flag -= 1
        if flag == 0:
            if teamTime1 > 0:
                teamTime1 = teamTime1 - (48*60-(60*m+s))

# 시간의 총량을 format 함수를 이용해 문자열로 print
# 여기서 해당 문자열이 2자리보다 작으면 빈자리에 0을 넣어준다.
print('{:0>2}:{:0>2}'.format(teamTime1//60,teamTime1%60))
print('{:0>2}:{:0>2}'.format(teamTime2//60,teamTime2%60))