
# def make_tree(arr):
#     for i in range(len(arr)):
#         while True:
#         # 만약 부모 노드보다 본인이 더 크면
#             if i == 0:
#                 break
#             if arr[i] > arr[(i-1)//2]:
#                 arr[i], arr[(i - 1) // 2] = arr[(i-1)//2], arr[i]
#                 i = (i - 1) // 2
#             else:
#                 break
#     return arr

# 결국 재귀함수를 사용하는게 최선이였던 것 같다.
# def heap_sort(arr):
#     length = len(arr) -1
#     while length != 0:
#         arr[0], arr[length] = arr[length], arr[0]
#         length -= 1
#         i = 0
#         while True:
#             left = arr[(i * 2) + 1]
#             right = arr[(i * 2) + 2]
#             if arr[i] < left or arr[i] < right:
#                 max_index = arr.index(max(left, right))
#                 arr[i], arr[max_index] = arr[max_index], arr[i]
#                 i = max_index
#             else:
#                 break
#     return arr


# 힙정렬 재귀함수
def heapify(arr, n, i):
    # 왼쪽, 오른쪽 자식노드의 위치를 구한다.
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 만약 탐색 범위가 전체 배열의 길이를 넘어가지 않고, 자식 노드의 값이 더 크면
    if left < n and arr[left] > arr[largest]:
        # 최대값에 왼쪽 노드의 인덱스를 저장
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right
    # 만약 최초로 입력된 노드의 위치와 최대값이 다르면
    if largest != i:
        # 서로의 위치를 바꾸고 다시 한번 탐색 시작
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 초기 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        # 뒤에서부터 탐색하는 이유는 가장 자식 노드부터 탐색하는것이 효율적이기 때문
        heapify(arr, n, i)

    # 반대로 힙정렬은 최상위 노드로부터 탐색을 해야하기 때문에 0번 노드부터 탐색을 이어나간다.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 최대값(루트)을 배열 끝으로 이동
        heapify(arr, i, 0)  # 이동한 후에 다시 최대 힙 구성

    return arr

# 사용 예시
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("정렬된 배열:", sorted_arr)

