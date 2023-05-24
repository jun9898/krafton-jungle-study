# 이 문제는 해설을 봐서 가져왔다. 우선 트리와 그래프 모든 자료형의 개념을 익히고 다시 풀어보자.
def dfs(res, i, add, sub, mul, div):
    global N
    if i == N:
        res_li.append(res)
    else:
        if add:
            dfs(res + nums[i], i+1, add-1, sub, mul, div)            
        if sub:
            dfs(res - nums[i], i+1, add, sub-1, mul, div)
        if mul:
            dfs(res * nums[i], i+1, add, sub, mul-1, div)
        if div:
            dfs(int(res / nums[i]), i+1, add, sub, mul, div-1)          
    
N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
res_li = []

dfs(nums[0], 1, add, sub, mul, div)
print(max(res_li))
print(min(res_li))