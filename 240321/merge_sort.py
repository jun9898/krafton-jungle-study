def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 재귀적으로 왼쪽과 오른쪽 부분 배열을 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # 남은 요소들을 병합
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

arr = [1, 3, 5, 7, 4, 2, 6]
print(merge_sort(arr))



