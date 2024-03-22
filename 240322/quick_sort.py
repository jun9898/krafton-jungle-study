# 너무 복잡하게 생각했다.
# def quick_sort(arr):
#     length = len(arr)-1
#     if length <= 1:
#         return arr
#     # 피봇값
#     pivot = arr[-1]
#     # 비교할 인덱스의 값
#     i = 0
#     j = length - 1
#     while i <= j:
#         if arr[i] > pivot > arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#         elif arr[i] < pivot < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#         elif arr[i] > pivot and arr[j] > pivot:
#             j -= 1
#         elif arr[i] < pivot and arr[j] < pivot:
#             i += 1
#         print(arr)
#     arr[i], arr[-1] = arr[-1], arr[i]
#
#     sort_left = quick_sort(arr[i:])
#     sort_right = quick_sort(arr[:i])
#
#     sort_left.extend(sort_right)
#
#     return sort_left

# 이렇게 풀이하면 훨씬 더 깔끔하다
def quick_sort(arr, low, high):
    if low < high:
        # 파티션 함수를 사용하여 피벗의 위치를 찾음
        pi = partition(arr, low, high)

        # 피벗을 기준으로 분할하여 재귀적으로 정렬
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    # 피벗 선택 (여기서는 마지막 요소를 사용)
    pivot = arr[high]
    i = low -1 # 작은 요소들의 마지막 인덱스

    # 배열을 피벗을 기준으로 분할
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗의 올바른 위치를 찾아서 정렬
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 퀵 정렬 호출
arr = [3, 5, 9, 7, 1, 2, 4]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
