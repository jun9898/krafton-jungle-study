import sys
input = sys.stdin.readline

# def quick_sort(arr, left, right):
#     # start, end pivot index
#     pl = left
#     pr = right
#     pivot = arr[(left + right) // 2]
#
#     # 해당 값이 피봇보다 작거나 같은 동안 left += 1
#     while pl <= pr:
#         while arr[pl] < pivot:
#             pl += 1
#         # 해당 값이 피봇보다 크거나 같은 동안 right -= 1
#         while arr[pr] > pivot:
#             pr -= 1
#
#         # 탐색이 끝나고 교차가 이뤄지지 않으면 swap
#         if pl <= pr:
#             arr[pl], arr[pr] = arr[pr], arr[pl]
#             pl += 1
#             pr -= 1
#
#     if left < pr : quick_sort(arr, left, pr)
#     if pl < right : quick_sort(arr, pl, right)
#
# arr = [1,32,6,7]
# quick_sort(arr, 0, len(arr)-1)
# print(arr)
#

def quick_sort(arr, left, right):
    pl = left
    pr = right
    pivot = arr[(left + right)//2]

    while pl <= pr:
        while arr[pl] < pivot: pl += 1
        while arr[pr] > pivot: pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    if left < pr: quick_sort(arr, left, pr)
    if right > pl: quick_sort(arr, pl, right)

arr = [1,6,34,2,5,6,8,54,4,31,4,76,8]

quick_sort(arr, 0, len(arr) - 1)
print(*arr)























