class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {

        function isAlphaNum(char) {
            return 'a' <= char && char <= 'z' || 'A' <= char && char <= 'Z' || '0' <= char && char <= '9'; 
        }
        let left = 0;
        let right = s.length -1;

        while (left < right) {
            if (isAlphaNum(s[left]) && isAlphaNum(s[right])) {
                if (s[left].toLowerCase() === s[right].toLowerCase()) {
                    left++;
                    right--;
                    continue;
                }
                else return false;
            }
            else if (isAlphaNum(s[left])) {
                right--;
            }
            else left++;
        }
        return true;
            }
}
