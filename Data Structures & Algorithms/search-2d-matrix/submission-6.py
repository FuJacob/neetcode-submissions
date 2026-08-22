class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        l,r = 0, m - 1

        while l < r:
            m = l + (r-l)//2
            if matrix[m][-1] >= target: ## bigger or equal to target? coudl be our ans or smaelr
                r = m
            else:
                l = m + 1 # smamelr ? no good 
        ## then our answer is left on l . thats the row 
        row = l
        l, r = 0, n - 1
        while l <= r:
            m = l + (r-l) // 2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1 
        return False

