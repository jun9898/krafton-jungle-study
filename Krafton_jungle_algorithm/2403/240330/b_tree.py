class BTreeNode:
    def __init__(self, t):
        self.keys = []  # 노드가 가지고 있는 키들
        self.children = []  # 노드의 자식 노드들
        self.is_leaf = True  # 리프 노드 여부
        self.t = t  # B-트리의 차수
    # 키를 삽입하는 메서드
    def insert_key(self, key):
        if not self.keys:  # 노드가 비어있는 경우
            self.keys.append(key)
        else:
            idx = 0
            while idx < len(self.keys) and key > self.keys[idx]: #sort
                idx += 1
            self.keys.insert(idx, key)
    # 자식 노드를 추가하는 메서드
    def add_child(self, child):
        self.children.append(child)
# B-트리 클래스 정의
class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)  # 루트 노드 초기화
        self.t = t  # B-트리의 차수
    # 주어진 키를 검색하는 메서드
    def search(self, key):
        return self._search_key(key, self.root)
    # 키를 재귀적으로 검색하는 내부 메서드
    def _search_key(self, key, node):
        idx = 0
        while idx < len(node.keys) and key > node.keys[idx]:
            idx += 1
        if idx < len(node.keys) and key == node.keys[idx]:
            return (node, idx)  # 키를 찾았을 때 해당 노드와 인덱스 반환
        elif node.is_leaf:
            return None  # 리프 노드인 경우 키가 존재하지 않음을 반환
        else:
            return self._search_key(key, node.children[idx])  # 자식 노드로 이동하여 재귀적으로 검색
    # 키를 삽입하는 메서드
    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:  # 루트 노드가 가득 찬 경우
            new_root = BTreeNode(self.t)  # 새로운 루트 노드 생성
            new_root.children.append(root)  # 기존 루트를 새로운 루트의 자식으로 설정
            self._split_child(new_root, 0)  # 새로운 루트를 분할
            self.root = new_root  # 새로운 루트를 트리의 루트로 설정
            self._insert_non_full(key, new_root)  # 삽입 연산 수행
        else:
            self._insert_non_full(key, root)  # 삽입 연산 수행
    # 비어있지 않은 노드에 키를 삽입하는 메서드
    def _insert_non_full(self, key, node):
        idx = len(node.keys) - 1
        if node.is_leaf:
            node.insert_key(key)  # 리프 노드인 경우 키를 삽입
        else:
            while idx >= 0 and key < node.keys[idx]:
                idx -= 1
            idx += 1
            if len(node.children[idx].keys) == 2 * self.t - 1:  # 자식 노드가 가득 찬 경우
                self._split_child(node, idx)  # 자식 노드를 분할
                if key > node.keys[idx]:
                    idx += 1
            self._insert_non_full(key, node.children[idx])  # 자식 노드로 이동하여 재귀적으로 삽입
    # 노드를 분할하는 메서드
    def _split_child(self, parent, idx):
        t = self.t
        child = parent.children[idx]
        new_child = BTreeNode(t)
        parent.insert_key(child.keys[t - 1])
        parent.add_child(new_child)
        new_child.is_leaf = child.is_leaf
        new_child.keys = child.keys[t:2 * t - 1]
        child.keys = child.keys[:t - 1]
        if not child.is_leaf:
            new_child.children = child.children[t:]
            child.children = child.children[:t]
    # 키를 삭제하는 메서드
    def delete(self, key):
        root = self.root
        if len(root.keys) == 1 and not root.children:  # 트리에 키가 한 개만 있고 리프 노드인 경우
            if key == root.keys[0]:  # 해당 키를 삭제
                root.keys = []
                return
        self._delete_key(key, root)
    # 키를 재귀적으로 삭제하는 내부 메서드
    def _delete_key(self, key, node):
        t = self.t
        idx = 0
        while idx < len(node.keys) and key > node.keys[idx]:
            idx += 1
        if idx < len(node.keys) and key == node.keys[idx]:  # 키를 찾은 경우
            if node.is_leaf:  # 리프 노드인 경우
                node.keys.pop(idx)  # 키를 삭제
            else:
                pred = node.children[idx]
                succ = node.children[idx + 1]
                if len(pred.keys) >= t:  # 왼쪽 자식 노드가 최소 차수 이상의 키를 가지고 있는 경우
                    node.keys[idx] = self._delete_max(pred)  # 왼쪽 자식 노드에서 가장 큰 키를 삭제된 위치에 복사
                elif len(succ.keys) >= t:  # 오른쪽 자식 노드가 최소 차수 이상의 키를 가지고 있는 경우
                    node.keys[idx] = self._delete_min(succ)  # 오른쪽 자식 노드에서 가장 작은 키를 삭제된 위치에 복사
                else:  # 양쪽 자식 노드 모두 최소 차수의 키를 가지고 있는 경우
                    node.keys.pop(idx)  # 키를 삭제
                    node.children.pop(idx + 1)  # 오른쪽 자식 노드를 삭제
                    self._merge(node, idx)  # 노드를 병합
        else:  # 키를 찾지 못한 경우
            child = node.children[idx]
            if len(child.keys) == t - 1:  # 자식 노드가 최소 차수의 키를 가지고 있는 경우
                if idx > 0 and len(node.children[idx - 1].keys) >= t:  # 왼쪽 형제 노드가 최소 차수 이상의 키를 가지고 있는 경우
                    self._borrow_from_prev(node, idx)  # 왼쪽 형제 노드로부터 키를 빌림
                elif idx < len(node.keys) and len(node.children[idx + 1].keys) >= t:  # 오른쪽 형제 노드가 최소 차수 이상의 키를 가지고 있는 경우
                    self._borrow_from_next(node, idx)  # 오른쪽 형제 노드로부터 키를 빌림
                else:  # 왼쪽 형제 노드와 오른쪽 형제 노드 모두 최소 차수의 키를 가지고 있는 경우
                    if idx < len(node.keys):  # 오른쪽 형제 노드가 있는 경우
                        self._merge(node, idx)  # 현재 노드와 오른쪽 형제 노드를 병합
                    else:  # 오른쪽 형제 노드가 없는 경우
                        self._merge(node, idx - 1)  # 현재 노드와 왼쪽 형제 노드를 병합
            self._delete_key(key, child)  # 자식 노드로 이동하여 재귀적으로 삭제
    # 왼쪽 형제 노드로부터 키를 빌리는 메서드
    def _borrow_from_prev(self, node, idx):
        child = node.children[idx]
        prev_child = node.children[idx - 1]
        child.keys.insert(0, node.keys[idx - 1])  # 현재 노드의 키를 자식 노드의 가장 작은 키로 이동
        node.keys[idx - 1] = prev_child.keys.pop()  # 왼쪽 형제 노드의 가장 큰 키를 현재 노드로 이동
        if not prev_child.is_leaf:  # 자식 노드가 리프 노드가 아닌 경우
            child.children.insert(0, prev_child.children.pop())  # 왼쪽 형제 노드의 가장 오른쪽 자식 노드를 자식 노드의 가장 왼쪽으로 이동
    # 오른쪽 형제 노드로부터 키를 빌리는 메서드
    def _borrow_from_next(self, node, idx):
        child = node.children[idx]
        next_child = node.children[idx + 1]
        child.keys.append(node.keys[idx])  # 현재 노드의 키를 자식 노드의 가장 큰 키로 이동
        node.keys[idx] = next_child.keys.pop(0)  # 오른쪽 형제 노드의 가장 작은 키를 현재 노드로 이동
        if not next_child.is_leaf:  # 자식 노드가 리프 노드가 아닌 경우
            child.children.append(next_child.children.pop(0))  # 오른쪽 형제 노드의 가장 왼쪽 자식 노드를 자식 노드의 가장 오른쪽으로 이동
    # 노드를 병합하는 메서드
    def _merge(self, node, idx):
        child = node.children[idx]
        next_child = node.children[idx + 1]
        child.keys.append(node.keys[idx])  # 현재 노드의 키를 자식 노드의 가장 큰 키로 이동
        child.keys.extend(next_child.keys)  # 오른쪽 형제 노드의 키를 자식 노드로 이동
        if not child.is_leaf:  # 자식 노드가 리프 노드가 아닌 경우
            child.children.extend(next_child.children)  # 오른쪽 형제 노드의 자식 노드를 자식 노드로 이동
        node.keys.pop(idx)  # 현재 노드의 키를 삭제
        node.children.pop(idx + 1)  # 오른쪽 형제 노드를 삭제
        if not node.keys and node is not self.root:  # 현재 노드가 루트 노드가 아니고 키가 없는 경우
            parent = self.root
            for i, child in enumerate(parent.children):
                if child is node:
                    parent.children[i] = child.children[0] if child.children else None
                    break
    # 주어진 노드에서 가장 작은 키를 삭제하고 반환하는 메서드
    def _delete_min(self, node):
        while not node.is_leaf:
            node = node.children[0]
        min_key = node.keys.pop(0)
        return min_key
    # 주어진 노드에서 가장 큰 키를 삭제하고 반환하는 메서드
    def _delete_max(self, node):
        while not node.is_leaf:
            node = node.children[-1]
        max_key = node.keys.pop()
        return max_key
    # 트리를 출력하는 메서드
    def print_tree(self, node=None, depth=0):
        if not node:
            node = self.root
        if node:
            print("Level ", depth, " ", end=":")
            print(node.keys)
            depth += 1
            if not node.is_leaf:
                for child in node.children:
                    self.print_tree(child, depth)
# 메인 함수
def main():
    B = BTree(2)  # 차수가 2인 B-트리 생성
    # 키들을 B-트리에 삽입
    for i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
        B.insert(i)
    B.print_tree()  # B-트리 출력
    # 특정 키가 존재하는지 확인
    if B.search(80) is not None:
        print("\n80 Found")
    else:
        print("\n80 Not found")
    # 키들을 삭제
    for val in [50, 60]:
        print(f'delete val : {val}')
        B.delete(val)
    B.print_tree()  # B-트리 출력
# 메인 함수 실행
if __name__ == '__main__':
    main()