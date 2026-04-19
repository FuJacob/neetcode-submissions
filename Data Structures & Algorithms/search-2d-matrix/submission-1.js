class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        if (!matrix) return false;

        let i = matrix[0].length -1 ;
        let j = 0;

        while (i >= 0 && j < matrix.length) {
            const smartPtr = matrix[j][i];
            if (target === smartPtr) return true;
            if (target < smartPtr) i--;
            else j++;
        }
        return false
    }
}
