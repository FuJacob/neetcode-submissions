class Solution:
    class UnionFind:
        def __init__(self,n):
            self.parents = [i for i in range(n)]
            self.size = [1] * n

        def find(self, x):
            if self.parents[x] != x: ## if parent no titself find its end goal parent
                self.parents[x] = self.find(self.parents[x]) ## this way we can preform the proper udpate
            return self.parents[x] ## return parent
        def union(self, x,y):
            px, py = self.find(x), self.find(y)
            if self.size[px] > self.size[py]:
                self.parents[py] = py
            else:
                self.parents[py] = px


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = self.UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        ## overcounting
        ## OVERCOUTNING BECAUSE WE DIDNT FINALIZE UPDATING THE PARENTS OF ALL THE NODES TO BE TEH TRUE PARENTS
        for p in range(n):
            uf.find(p)
        return len(set(uf.parents)) 
        
            