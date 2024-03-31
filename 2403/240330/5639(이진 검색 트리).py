import sys
sys.setrecursionlimit(20_000)
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        # double linked list
        self.data = data
        self.left = None
        self.right = None


class binary_search_tree:
    def __init__(self):
        self.root = None  # 루트노드

    def __insert__(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        node = self.root
        while node is not None:
            parent = node
            if node.data > data:
                node = node.left
            else:
                node = node.right
        if parent.data == data:
            return
        if parent.data > data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)

    def postorder(self):
        root = self.root
        def postorder(root):

            if root is None:
                return
            if root != None:
                postorder(root.left)  # left
                postorder(root.right)  # left
                print(root.data)  # root
        postorder(root)


# 실행
BST = binary_search_tree()
while True:
    try:
        n = int(input())
        BST.__insert__(n)
    except:
        break
BST.postorder()
