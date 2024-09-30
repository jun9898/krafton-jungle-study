import sys
input = sys.stdin.readline

def merge_sort(arr, left, right):  # arr[left ~ right] 정렬
    if left < right:
        mid = (left + right) // 2  # 중간 지점 계산
        merge_sort(arr, left, mid)  # 왼쪽 정렬
        merge_sort(arr, mid + 1, right)  # 오른쪽 정렬
        merge(arr, left, mid, right)  # 병합

def merge(arr, left, mid, right):
    global count, result
    i, j = left, mid + 1  # 두 부분 배열의 시작점
    tmp = []  # 병합 결과를 임시로 저장할 리스트

    # 두 배열을 비교하여 병합
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    # 남은 요소 병합
    tmp.extend(arr[i:mid + 1])
    tmp.extend(arr[j:right + 1])

    # 병합 결과를 원본 배열에 반영
    for idx in range(left, right + 1):
        arr[idx] = tmp[idx - left]
        count += 1
        if count == K:
            result = arr[idx]
            break

# 입력 처리
n, K = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
result = -1

merge_sort(arr, 0, n - 1)  # 병합 정렬 수행
print(result)
