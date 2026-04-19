class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        roots = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    roots.append((r,c, 0))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque(roots)
        visited = set([(r,c) for r,c,_ in roots])
        while q:
            r,c, dist = q.popleft()
            for dr,dc in dirs:
                new_r, new_c = dr+r, dc+c
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] != -1:
                    if (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        grid[new_r][new_c] = dist +1
                        q.append((new_r,new_c, dist+1))


                    


            