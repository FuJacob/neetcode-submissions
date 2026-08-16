class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m,n = len(board), len(board[0])
        for r in range(m):
            seen = set()
            for cell in board[r]:
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)                
        for c in range(n):
            seen = set()
            for r in range(m):
                cell = board[r][c]
                if cell != '.':
                    if cell in seen:
                        return False
                    seen.add(cell)
        for r in range(0,m,3):
            for c in range(0,n,3):
                seen = set()
                for i in range(r, r+3):
                    for j in range(c, c+3):
                        cell = board[i][j]
                        if cell != '.' and cell in seen:
                            return False
                        seen.add(cell)
        return True




        

                
                





