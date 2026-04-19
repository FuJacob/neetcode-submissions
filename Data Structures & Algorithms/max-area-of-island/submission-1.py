class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0), (-1, 0), (0, 1), (0,-1)]
        count = 0
        def dfs(r, c):
            area = 0
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 0
                area += 1
                for dx,dy in dirs:
                    area += dfs(dx + r, dy+c)
            return area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        return ans
