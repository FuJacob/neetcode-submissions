class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parents = [i for i in range(n+1)]
        def find(self, x):
            if self.parents[x] != x:
                self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        def union(self, x,y):
            px,py = self.find(x), self.find(y)
            if px == py:
                return False
            self.parents[py] = px
            return True
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = self.UnionFind(len(edges) + 1)
        for a, b in edges:
            pa,pb = uf.find(a), uf.find(b)
            if not uf.union(pa, pb):
                return [a,b]


