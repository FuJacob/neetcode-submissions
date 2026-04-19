class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        safe = set()
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        ## colelct cells for the entire island
        def mark_safe(r,c):
            for dr,dc in dirs:
                if not (0 <= dr+r < m and 0 <= dc+c < n):
                    continue
                if board[dr+r][dc+c] == 'O' and (dr+r,dc+c) not in safe:
                    safe.add((dr+r,dc+c))
                    mark_safe(dr+r, dc+c)
        
        for r in range(m):
            if board[r][0] == 'O' and (r,0) not in safe:
                safe.add((r,0))
                mark_safe(r,0)
            if board[r][n-1] == 'O' and (r,n-1) not in safe:
                safe.add((r,n-1))
                mark_safe(r,n-1)
        for c in range(n):
            if board[0][c] == 'O' and (0,c) not in safe:
                safe.add((0,c))
                mark_safe(0,c)
            if board[m-1][c] == 'O' and (m-1,c) not in safe:
                safe.add((m-1,c))
                mark_safe(m-1,c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'
            
        
