class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let left = 0;
        let right = 0;
        let maxLen = 0;
        const subStr = new Map();
        if (s.length <= 1) return s.length
        while (right <= s.length - 1) {
            if (subStr.has(s[right]) && subStr.get(s[right]) >= left) {
                left = subStr.get(s[right]) + 1;
            }
            subStr.set(s[right], right);
            maxLen = Math.max(right - left + 1, maxLen);
            right++;
        }
        return maxLen;
    }
}