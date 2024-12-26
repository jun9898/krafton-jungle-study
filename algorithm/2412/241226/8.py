import sys
input = sys.stdin.readline

'''
입출력 방식
n m <- n은 배열의 개수, m은 순열의 길이 
'''

result = []

def backtracking(cur_arr, visited, n, m):
    if len(cur_arr) == m:
        result.append(cur_arr[:])  # 완성된 순열 추가
        return
    for i in range(1, n + 1):
        if not visited[i]:  # 방문하지 않은 원소만 선택
            visited[i] = True
            cur_arr.append(i)
            backtracking(cur_arr, visited, n, m)
            cur_arr.pop()  # 백트래킹: 원상복구
            visited[i] = False  # 방문 상태 해제

n, m = map(int, input().split()) # n은 배열의 개수, m은 순열의 길이
visited = [False] * (n + 1)  # 방문 여부 체크 배열
backtracking([], visited, n, m)

print(len(result))