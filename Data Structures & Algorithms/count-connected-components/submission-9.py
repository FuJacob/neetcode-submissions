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
            if px == py:
                return
            if self.size[px] > self.size[py]:
                self.parents[py] = px
                self.size[px] += self.size[py]
            else:
                self.parents[px] = py
                self.size[py] += self.size[px]


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UnionFind(n)
        count = n
        for a,b in edges:
            px,py = uf.find(a), uf.find(b)
            if px != py:
                uf.union(a,b)
                count -=1
        ## cuz this way were actualyl reudicng # of conected conpoentns
        return count
        
            