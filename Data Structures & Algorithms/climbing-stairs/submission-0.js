class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    climbStairs(n) {
        let [one, two] = [1, 1];

        for (let i = 0; i < n - 1; i++) {
            const temp = one;
            one += two;
            two = temp
        }
        return one
    }
}
