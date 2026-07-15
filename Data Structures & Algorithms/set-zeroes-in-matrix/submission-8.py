class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for j in range(m):
                        if matrix[j][c] != 0:
                            matrix[j][c] = 'X'
                    for k in range(n):
                        if matrix[r][k] != 0:
                            matrix[r][k] = 'X'
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 'X':
                    matrix[r][c] = 0

        