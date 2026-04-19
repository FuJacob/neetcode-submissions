class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let code = "";
        for (let i = 0; i < strs.length; i++) {
            code += strs[i].length + "#" + strs[i];
        }
        return code;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let sol = [];
        let i = 0;

        while (i < str.length) {
            let len = 0;
            let j = i;
            while (str[j] !== "#") {
                j++;
            }
            len = +str.slice(i,j);
            sol.push(str.slice(j+1, j+1 + len));
            i = j+1 + len;
        }
        return sol;
}
}