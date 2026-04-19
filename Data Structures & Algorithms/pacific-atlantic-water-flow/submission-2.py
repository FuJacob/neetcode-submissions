class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        stat woff with each side

        in a sets
        then what?
        then we try to move backwards from water
        and sweep up
        then other side as well
        then whatever is intersected, thit can reach both sides
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
                if (dr+r, dc+c) in cells_set: ## we arleady processed it 
                    continue
                if 0 <= dr+r < m and 0 <= dc+c < n: ## in boudns 
                    if heights[r][c] <= heights[dr+r][dc+c]: ## is it increasing 
                        dfs(dr+r,dc+c, cells_set)
        for r,c in list(pacific):
            dfs(r,c, pacific)
        for r,c in list(atlantic):
            dfs(r,c, atlantic)
        return [[r,c] for r,c in list(atlantic & pacific)]
        

        