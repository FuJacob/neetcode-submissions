class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        perimeter = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    sides = 4
                    for dr,dc in dirs:
                        if 0 <= dr+r < m and 0 <= dc+c < n:
                            if grid[dr+r][dc+c] == 1:
                                sides -=1
                    perimeter += sides
        return perimeter
                            


