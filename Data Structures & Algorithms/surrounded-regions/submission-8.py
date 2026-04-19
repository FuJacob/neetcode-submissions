class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        safe = set()
        dirs = [(1,0), (-1,0), (0,-1), (0,1)]
        def mark_safe(r,c):
            if not (0 <= r < m and 0 <= c < n) or (r,c) in safe:
                return
            safe.add((r,c))
            for dr,dc in dirs:
                if 0 <= dr+r < m and 0 <= dc+c < n and board[dr+r][dc+c] == 'O':
                    mark_safe(dr+r, dc+c)
        
        for r in range(m):
            if board[r][0] == 'O':
                mark_safe(r,0)
            if board[r][n-1] == 'O':
                mark_safe(r,n-1)
        for c in range(n):
            if board[0][c] == 'O':
                mark_safe(0,c)
            if board[m-1][c] == 'O':
                mark_safe(m-1,c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r,c) not in safe:
                    board[r][c] = 'X'
            
        
