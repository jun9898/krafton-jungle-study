import sys
input = sys.stdin.readline

def make_postorder(preorder, inorder_map, in_start, in_end, pre_index) :
    if in_start > in_end:
        return [], pre_index

    root = preorder[pre_index]
    pre_index += 1
    idx = inorder_map[root]

    left, pre_index = make_postorder(preorder, inorder_map, in_start, idx - 1, pre_index)
    right, pre_index = make_postorder(preorder, inorder_map, idx + 1, in_end, pre_index)

    return left + right + [root], pre_index

for _ in range(int(input())) :
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))

    inorder_map = {value: i for i, value in enumerate(inorder)}

    result, _ = make_postorder(preorder, inorder_map, 0, n - 1, 0)
    print(*result)
