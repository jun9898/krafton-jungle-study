import sys
input = sys.stdin.readline
result = sys.maxsize

'''
백트래킹을 활용해야 할것같다. 특히 분할정복.
1. 우선 재귀를 수행하며 팀을 정확히 절반으로 나눠야할것같음.
2. 그렇게 팀이 절반으로 나뉘게 되면 그때부터 조건에 따른 파워 계산 시작. (어떻게?)
우선 여기까지라도 구현해보자
'''

def backTracking(dep, index):
    global result
    # 2. 정확히 나뉜 순간
    if dep == n // 2:
        tmp1, tmp2 = 0, 0
        for i in range(n):
            for j in range(n):
                # 절반 나뉜 시점에 visited가 짝지어진 인원들끼리 묶어서 연산
                if visited[i] and visited[j]:
                    tmp1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    tmp2 += graph[i][j]
        # 계산 시작. visited 연산으로 방문 처리된것, 안된것 끼리끼리 묶어서 계산하면 될듯
        # 계산이 끝나면 두 값의 차를 구한다
        result = min(result, abs(tmp1 - tmp2))
        return

    # 1. 재귀를 수행하며 팀을 정확히 절반으로 나눈다. 모든 조합을 수행하기 위해 index를 받아와야할듯
    # 다른 재귀들과 같이 index -> n 까지 연산 수행
    for i in range(index, n):
        # 만약 처음 만나는 숫자면
        if not visited[i]:
            # 방문처리 -> 방문처리의 인덱스를 list로 처리하는 방법도 생각해봐야할듯
            visited[i] = True
            # 절반으로 나뉘었는지 계산하기 위해 dep에 +1, 일곱난쟁이마냥 index + 1
            backTracking(dep + 1, i + 1)
            # 다른 경우의 수도 판단하기 위해 visited를 False로
            visited[i] = False




n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n

backTracking(0, 0)

print(result)

