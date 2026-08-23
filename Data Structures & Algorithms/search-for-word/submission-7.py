class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        m,n = len(board), len(board[0])
        dirs = [(1,0),(-1,0),(0,-1),(0,1)]
        def make_word(r,c, idx,visited):
            if not (0 <= r < m and 0 <= c < n) or (r,c) in visited:
                return False
            if word[idx] != board[r][c]:
                return False
            visited.add((r,c))
            idx+=1
            if idx == word_len:
                return True
            for dr,dc in dirs:
                if make_word(dr+r, dc+c, idx, visited):
                    return True
            visited.remove((r,c))
            return False
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if make_word(r,c, 0, set()):
                        return True
        return False