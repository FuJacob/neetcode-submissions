class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotton = set()
        m,n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    rotton.add((r,c))
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        minutes = 0
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        while fresh and rotton:
            for r,c in list(rotton):
                rotton.remove((r,c))
                for dr,dc in dirs:
                    new_r, new_c = dr+r, dc+c               
                    if 0 <= new_r < m and 0 <= new_c < n and (new_r,new_c) in fresh:
                        fresh.remove((new_r,new_c))
                        grid[new_r][new_c] = 2
                        rotton.add((new_r,new_c))
            minutes+=1
        return minutes if not fresh else -1
                    
                


