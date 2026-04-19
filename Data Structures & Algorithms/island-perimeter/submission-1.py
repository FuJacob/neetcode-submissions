class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        m,n = len(grid), len(grid[0])
        def dfs(r,c): ## dfs returns count of perimeter from that block
            if (r,c) in visited:
                return -1
            visited.add((r,c))
            sides = 4
            for dr,dc in dirs:
                if 0 <= dr+r < m and 0 <= dc+c < n and grid[dr+r][dc+c] == 1:
                    other_sides = dfs(dr+r, dc+c)
                    if other_sides > 0:
                        sides -=1
                    sides += other_sides
            return sides
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return dfs(r,c)
