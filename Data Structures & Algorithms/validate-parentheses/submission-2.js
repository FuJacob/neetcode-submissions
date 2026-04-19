class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        let keys = new Map([['(', ')'],['{', '}'],['[', ']']]);
        for (let i = 0; i < s.length; i++) {
            if (keys.has(s[i])) stack.push(s[i]);
            else if (stack.length === 0) return false;
            else if (keys.get(stack.pop()) !== s[i]) return false;
        }
        return stack.length === 0;
    }
}
