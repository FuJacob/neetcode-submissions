class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ## dfs. trying the diff options definitely. 
        ## this is also backtracking
        ## also kidna liek dfs.
        last_letter = [-1,-1]
        rows = len(board)
        cols = len(board[0])
        ## now we wnat to dop pathfinding
        def findPath(r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            res = findPath(r-1, c, idx + 1) or findPath(r+1, c, idx+ 1) or findPath(r, c-1, idx + 1) or findPath(r, c+1, idx + 1)
            ## visited now
            ## dont try to visit this shitter again it doesnt work or works 
            ## can't reuse
            board[r][c] = temp
            return res
        for r in range(len(board)):
            for c in range(len(board[0])):
                if findPath(r, c, 0):
                    return True
        return False


            

        
            
        