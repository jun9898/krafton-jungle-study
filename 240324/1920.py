# 일곱난쟁이 온몸비틀기
import sys
input = sys.stdin.readline

def binary_search(start, end, target):
    if start > end:
        print(0)
        return
    mid = (start+end) // 2
    if arr[mid] == target:
        print(1)
        return
    elif arr[mid] < target:
        binary_search(mid + 1, end, target)
    elif arr[mid] > target:
        binary_search(start, mid - 1, target)

# 힙 정렬
def heapify(arr, index, total_len):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < total_len and arr[largest] < arr[left]:
        largest = left
    if right < total_len and arr[largest] < arr[right]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify(arr, largest, total_len)

def heap_sort(arr):
    total_len = len(arr)
    for i in range(total_len//2-1, -1, -1):
        heapify(arr, i, total_len)

    for i in range(total_len-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

n = int(input())
arr = list(map(int, input().split()))

# 힙정렬
heap_sort(arr)

m = int(input())
targets = list(map(int, input().split()))
for i in targets:
    binary_search(0, len(arr) -1, i)

