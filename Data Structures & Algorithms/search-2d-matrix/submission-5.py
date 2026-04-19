class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        we're given m x n 2d integer array matrix and integer target.
        each row in matrix is sorted in non decreasing order
        the first inger of every row is greater than the last ingeger of the preivous row

        so what we want to do is return true if target exists within matrix
        false otherwise


        it wants us to run sol in o(log (m*n))
        seems to be binary search.


        okay so we have matrix
        notice how each row is sorted
        and that the firs t int of each row is bigger tha nthe last int of hte prev row
        that literally means we can flatten this matrix 2d array into 1 array, m * n length
        and then it's literally just a sorted array we can run binary search on
        """

        """
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS*COLS - 1

        while l <= r:
            m = l + ( r- l) //2
            ## actual col woudk be reminder
            ## and # rows would just be floor divisoin
            m_r, m_l = m// COLS, m % COLS

            if matrix[m_r][m_l] == target:
                return True
            if matrix[m_r][m_l] < target:
                ## then we need to move obviously down, so just move left pointer
                l = m + 1
            else:
                r = m - 1
        return False
        ## og naive way would to just iterate through every single box and check if it exists 
        

        