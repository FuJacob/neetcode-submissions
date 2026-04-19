class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {

        function isAlphaNum(char) {
            return 'a' <= char && char <= 'z' || 'A' <= char && char <= 'Z' || '0' <= char && char <= '9'; 
        }


        const arr = [];

        for (let i =0; i < s.length; i++) {
            if (isAlphaNum(s[i])) arr.push(s[i]);
        }

        return arr.join('').toLowerCase() == arr.reverse().join('').toLowerCase();
    }
}
