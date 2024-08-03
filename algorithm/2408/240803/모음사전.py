def solution(word):
    global index, answer
    index = -1
    answer = 0
    alp = ['A', 'E', 'I', 'O', 'U']

    def dfs(chars):
        global index, answer
        if len(chars) <= 5:
            index += 1
            if chars == word:
                answer = index
            for i in range(5):
                dfs(chars + alp[i])

    dfs("")
    return answer

print(solution('AUI'))