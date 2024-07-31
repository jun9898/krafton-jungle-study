import sys
input = sys.stdin.readline
"""
우선 배열을 입력받는다
여기서 배열은 2차원으로 입력받는다

배열을 1열 2개 2열 2개씩 슬라이싱해서 result에 집어넣는다
result에 2번째 큰값을 result2로 넣어준다
answer의 길이가 1이 아니라면 answer을 arr에 다시 넣어준다
위 과정을 요소가 1개만 남을때까지 반복

나는 이 문제를 단순 구현으로 접근했지만 블로그 해설을 보니
재귀를 이용해 푼 경우가 많았다.
재귀 함수에 더 익숙해져야한다.
"""
n = int(input())
nums = [list(map(int,input().split()))for _ in range(n)]

def pooling(size, x, y):
    mid=size//2
    if size==2:
        answer=[nums[x][y], nums[x+1][y], nums[x][y+1], nums[x+1][y+1]]
        answer.sort()
        return answer[-2]
    lt=pooling(mid, x, y)
    rt=pooling(mid, x+mid, y)
    lb=pooling(mid, x, y+mid)
    rb=pooling(mid, x+mid, y+mid)
    answer=[lt, rt, lb, rb]
    answer.sort()
    return answer[-2]

print(pooling(n,0,0))