class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0), (-1, 0), (0, 1), (0,-1)]
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                grid[r][c] = '0'
                for dx,dy in dirs:
                    dfs(dx + r, dy+c)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        return count




        