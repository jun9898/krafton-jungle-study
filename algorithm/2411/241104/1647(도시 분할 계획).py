import heapq
import sys

input = sys.stdin.readline

def solution():
    n, edge_count = map(int, input().split())
    all_edges = []

    for _ in range(edge_count):
        start, end, weight = map(int, input().split())
        heapq.heappush(all_edges, (weight, start, end))

    class DisjointSet:
        def __init__(self, size):
            self.size = size
            self.rank = [0] * (size + 1)
            self.root = list(range(size + 1))

        def get_root(self, x):
            if self.root[x] != x:
                self.root[x] = self.get_root(self.root[x])
            return self.root[x]

        def merge_sets(self, x, y):
            root_x = self.get_root(x)
            root_y = self.get_root(y)

            if root_x != root_y:
                if self.rank[root_x] < self.rank[root_y]:
                    root_x, root_y = root_y, root_x
                self.root[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1
                return True
            return False

    def find_mst():
        ds = DisjointSet(n)
        total_weight = 0
        used_edges = []

        while all_edges:
            weight, start, end = heapq.heappop(all_edges)
            if ds.merge_sets(start, end):
                total_weight += weight
                used_edges.append(weight)

        return total_weight - used_edges[-1]

    return find_mst()


print(solution())