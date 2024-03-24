# 파이썬 온몸비틀기
import sys
input = sys.stdin.readline

arr = []

def find_subsets(nums, target):
    result = []
    dfs(nums, target, [], result)
    return result

def dfs(elements, target, path, result):
    if sum(path) == target and len(path) == 7:
        result.extend(path[:])  # 결과에 현재 경로 추가
        return True  # 원하는 조합을 찾았으므로 True 반환

    if sum(path) > target:
        return False  # 합이 타겟을 넘으면 해당 조합은 유효하지 않으므로 False 반환

    for i, element in enumerate(elements):
        # 재귀 호출하여 다음 요소를 추가한 경우
        if dfs(elements[i+1:], target, path + [element], result):
            return True  # 원하는 조합을 찾았으므로 True 반환

    return False  # 모든 경우를 탐색했지만 원하는 조합을 찾지 못했으므로 False 반환

def heapify(arr, index, total_len):
    least = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < total_len and arr[least] > arr[left]:
        least = left
    if right < total_len and arr[least] > arr[right]:
        least = right
    if least != index:
        arr[index], arr[least] = arr[least], arr[index]
        heapify(arr, least, total_len)


nums = []
for _ in range(9):
    nums.append(int(input()))
target = 100
subsets = find_subsets(nums, target)

for i in range(len(subsets)//2 - 1, -1, -1):
    heapify(subsets, i, len(subsets))

for i in range(len(subsets)-1, -1, -1):
    subsets[0], subsets[i] = subsets[i], subsets[0]
    print(subsets.pop(-1))
    heapify(subsets, 0, i)
