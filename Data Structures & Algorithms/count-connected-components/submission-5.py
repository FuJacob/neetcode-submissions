class Solution:
    class UnionFind:
        def __init__(self,n):
            self.parents = [i for i in range(n)]
            self.size = [1] * n

        def find(self, x):
            if self.parents[x] != x: 
                self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        def union(self, x,y):
            px, py = self.find(x), self.find(y)
            if self.size[px] > self.size[py]:
                self.parents[py] = px
            else:
                self.parents[px] = py


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        for p in range(n):
            uf.find(p)
        return len(set(uf.parents)) 
        
            