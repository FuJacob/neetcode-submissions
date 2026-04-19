class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0), (-1, 0), (0, 1), (0,-1)]
        count = 0
        def dfs(r, c):
            nonlocal count
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                grid[r][c] = 0
                count +=1
                for dx,dy in dirs:
                    dfs(dx + r, dy+c)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    ans = max(ans, count)
                    count = 0
        return ans
