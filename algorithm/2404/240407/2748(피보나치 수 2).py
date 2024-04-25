import sys
input = sys.stdin.readline


def top_down(n):
    # 만약 입력값이 0이나 1이면
    if (n < 2):
        fib_memo[n] = n
        return n
    # 만약 메모에 계산된 값이 있으면 바로 반환
    # 약간 BFS, DFS의 방문처리 하는거 생각난다.
    if fib_memo[n] > 0:
        return fib_memo[n]

    fib_memo[n] = top_down(n - 1) + top_down(n - 2)

    return fib_memo[n]

# 기존 풀이와 똑같음
def bottom_up(n):
    fib_table[0], fib_table[1] = 0, 1
    for i in range(2, n+1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    return fib_table[n]


n = int(input())
fib_memo = [0] * (n+1)
fib_table = [0] * (n+1)
print(bottom_up(n))

