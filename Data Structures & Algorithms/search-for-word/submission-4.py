class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        board string.
        same clel cant be used more than once in a word
        this is obvioulsy some kind of thign to do with backtracking and dfs
        we can have a recursive fucntion i thin and consider every single clel, interate through them all
        then it would be recursive path finding, where we recu
        rsively check the horizintal and verticla, wihle keeping track of what index of character we're on
        take coords, and takes idx word on
        """
        ## define helper variables
        rows = len(board)
        cols = len(board[0])
        def backtrack(r, c, idx):
            ## base case is if the word is done
            if idx == len(word):
                return True
            ## otherwise, we want to check if the cell we're currently on matches the idx we're on the word
            ## and we wnat to make sure our cell is in bound still
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
                return False
            ## otherwise, it's valid, so we can just recucsorvely check the other places
            ## but the thing is we don't ever want the same cell beuing used more than once,
            ## so we must mark it, then unmark it to backtrack un case the path we go doesn't sjuccess
            temp = board[r][c]
            board[r][c] = "#"

            sol = backtrack(r-1, c, idx + 1) or backtrack(r+1, c, idx + 1) or backtrack(r, c-1, idx + 1) or backtrack(r, c+1, idx + 1)
            ## add it back
            board[r][c] = temp
            return sol
        ## okay now we want to test this out on every single cell as a starting point
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        return False

        