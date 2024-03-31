import sys
input = sys.stdin.readline

n = int(input())
cost = [[0]]
for i in range(n):
    cost.append(list(map(int, input().split())))

append_arr = []
res = 99999999999999

def dfs():
    global res

    if len(append_arr) == n:
        temp = 0
        for i in range(n-1):
            if cost[append_arr[i]][append_arr[i+1]-1] == 0:
                return
            temp += cost[append_arr[i]][append_arr[i+1]-1]
        if cost[append_arr[-1]][append_arr[0]-1] == 0:
            return
        temp += cost[append_arr[-1]][append_arr[0]-1]
        res = min(res, temp)
        return

    for i in range(1, n+1):
        if i not in append_arr:
            append_arr.append(i)
            dfs()
            append_arr.pop()

dfs()

print(res)


# 따른사람의 풀이
# 탐색 탈출 조건을 앞으로
n = int(sys.stdin.readline())
costarr = []
visited = [0 for _ in range(n)]
answer = sys.maxsize


def search(start, to, cost, cnt):
    global answer

    if cost > answer:  # 비용이 넘어선 경우 더 확인하지 않음
        return

    if cnt == n:
        if costarr[to][start] == 0:  # 출발지로 돌아가는 길이 없음
            return
        else:
            cost += costarr[to][start]  # 출발지로 돌아감
        answer = min(cost, answer)
        return

    for i in range(n):
        if costarr[to][i] == 0:  # 방문 불가
            continue
        if visited[i] != 0:  # 이미 방문
            continue

        visited[i] = 1
        search(start, i, cost + costarr[to][i], cnt + 1)
        visited[i] = 0


if __name__ == '__main__':
    for _ in range(n):
        arr = list(map(int, sys.stdin.readline().split()))
        costarr.append(arr)

    # 1번 도시부터 완전탐색
    for i in range(n):
        visited[i] = 1
        search(i, i, 0, 1)
        visited[i] = 0

    print(answer)