class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length != t.length) return false
        let s_map = new Map()

        for (let elem of s)
        {
            s_map.set(elem, (s_map.get(elem) || 0) + 1)
        }

           for (let elem of t) {
            if (!s_map.has(elem) || s_map.get(elem) == 0) return false
            s_map.set(elem, s_map.get(elem) - 1)
           }
           return true
           }
}
