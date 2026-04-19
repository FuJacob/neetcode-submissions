class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    COUNTER = 3
    /** STATE: X
     * XYYAX K = 2 -> 0 -> 2
     *  L 
     * 
     * O(N) * O (K)
     * L = 0
     * R = 0
     * FOR LOOP:
     *      
     *      WHILE LOOP:
     * 
     */
    characterReplacement(s, k) {
        const contFreqMap = new Map();
        let l = 0;
        let res = 0;

        for (let r = 0; r < s.length; r++) {
            contFreqMap.set(s[r], (contFreqMap.get(s[r]) | 0) + 1);


            if (r - l + 1 - Math.max(...contFreqMap.values()) > k) {
                contFreqMap.set(s[l], contFreqMap.get(s[l]) - 1);
                l++;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;

    }
}
