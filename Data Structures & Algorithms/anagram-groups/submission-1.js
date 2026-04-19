class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();


        for (let i = 0; i < strs.length; i++) {
            const sortedStr = strs[i].split('').sort().join('');
            if (map.has(sortedStr)) {
                map.set(sortedStr, map.get(sortedStr).concat(strs[i]));
            }
            else {
                map.set(sortedStr, [strs[i]]);
            }
        }

        const sol = [];
        for (let val of map.values()) {
            sol.push(val);
        }
        return sol
    }
}
