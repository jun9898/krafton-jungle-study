import sys
input = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = start
        return

    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)

    if arr[tree[node * 2]] < arr[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2]
    else:
        tree[node] = tree[node * 2 + 1]

def query(start, end, node, left, right):
    if right < start or end < left:
        return -1
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_node = query(start, mid, node * 2, left, right)
    right_node = query(mid + 1, end, node * 2 + 1, left, right)

    if left_node == -1:
        return right_node
    elif right_node == -1:
        return left_node

    if arr[left_node] <= arr[right_node]:
        return left_node
    else:
        return right_node

def get_max(left, right):
    m = query(1, n, 1, left, right)

    area = (right - left + 1) * arr[m]
    if left <= m - 1:
        tmp = get_max(left, m - 1)
        area = max(area, tmp)

    if m + 1 <= right:
        tmp = get_max(m + 1, right)
        area = max(area, tmp)

    return area

n = int(input())
arr = [0] + list(map(int, input().split()))

tree = [0] * (n * 4)
init(1, n, 1)

print(get_max(1, n))
