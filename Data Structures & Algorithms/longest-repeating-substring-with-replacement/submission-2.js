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
        let left = 0;
        let res = 0;
        for (let right = 0; right < s.length; right++) {
            contFreqMap.set(s[right], (contFreqMap.get(s[right]) | 0) + 1);
            while (right - left + 1 - Math.max(...contFreqMap.values()) > k) {
                contFreqMap.set(s[left], (contFreqMap.get(s[left]) | 0) - 1);
                left++;
            }
            res = Math.max(res, right - left + 1);
        }

        return res;

    }
}
