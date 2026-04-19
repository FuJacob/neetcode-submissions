class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        treat as a 1d integer array, can just binary search it
        """
        COLS = len(matrix[0])
        ROWS = len(matrix)
        l, r = 0, COLS * ROWS - 1

        while l<=r:
            m_idx = (r + l) // 2
            m_r, m_c = m_idx//COLS, m_idx % COLS
            if matrix[m_r][m_c] == target: return True
            if matrix[m_r][m_c] < target:
                l = m_idx + 1
            else:
                r = m_idx - 1
        return False

    

