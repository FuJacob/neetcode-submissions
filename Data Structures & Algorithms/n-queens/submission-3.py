class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curr_board = [["."] * n for _ in range(n)]
        ans = []
        cols = set()
        diag1 = set()
        diag2 = set() ## by differientating between 3 sets, diag1,diag2, and c
        def backtrack(r):
            if r == n:
                clone = []
                for row in curr_board:
                    clone.append("".join(row))
                ans.append(clone)
                return
            
            for c in range(n):
                if r-c in diag1 or r+c in diag2 or c in cols:
                    continue
                curr_board[r][c] = "Q"
                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                backtrack(r+1)
                curr_board[r][c] = "."
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)

        backtrack(0)
        return ans