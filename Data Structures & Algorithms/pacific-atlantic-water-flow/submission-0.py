class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
(r,c)        


ohhh its saying take all the left and top row/col

then we sttart off thats conected to apcific


then look at atlantic

bottom row and right col.

this stuff is atnaltci


we can dfs, keeping i nmind viisted, se how far we can get, onoly going to places that increase in height or equal

then after colelcting set, we diff the set with the atnlatic ones
those are the cells taht can access both
we only access each cell prcoess once so it shoudl be good 
        """
        pacific = set()
        atlantic = set()
        m,n = len(heights), len(heights[0])
        for r in range(m):
            pacific.add((r,0))
        for c in range(n):
            pacific.add((0,c))
        for r in range(m):
            atlantic.add((r,n-1))
        for c in range(n):
            atlantic.add((m-1, c))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r,c, cells_set):
            cells_set.add((r,c))
            for dr, dc in dirs:
                if (dr+r, dc+c) not in cells_set and 0 <= dr+r < m and 0 <= dc+c < n and heights[r][c] <= heights[dr+r][dc+c]:
                    dfs(dr+r,dc+c, cells_set)
        for r,c in list(pacific):
            dfs(r,c, pacific)
        for r,c in list(atlantic):
            dfs(r,c, atlantic)
        
        both = list(atlantic & pacific)
        return [[r,c] for r,c in both]
        

        