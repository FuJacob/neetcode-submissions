class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        for (let i = 0; i < board.length; i++) {
            const dup = new Set();
            for (let j = 0; j < board.length; j++) {

                if (board[i][j] !== ".") {
                    if (dup.has(board[i][j])) return false;
                    dup.add(board[i][j]);
                }
            }
        }

        for (let i = 0; i < board.length; i++) {
            const dup = new Set();
            for (let j = 0; j < board.length; j++) {
                if (board[j][i] !== ".") {
                    if (dup.has(board[j][i])) return false;
                    dup.add(board[j][i]);
                }
            }
        }

        for (let i = 0; i < board.length; i += 3) {
            for (let j = 0; j < board.length; j += 3) {
                const dup = new Set();
                for (let k = 0; k < 3; k++) {
                    for (let l = 0; l < 3; l++) {
                        if (board[i + k][j + l] !== ".") {
                            if (dup.has(board[i + k][j + l])) return false;
                            dup.add(board[i + k][j + l]);
                        }
                    }
                }
            }
        }
        return true;



    }
}
