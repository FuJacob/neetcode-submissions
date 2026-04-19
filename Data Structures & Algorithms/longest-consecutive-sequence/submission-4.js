class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const set = new Set(nums);
        let max = 0;

        for (let elem of set) {
            if (!set.has(elem - 1)) {
                let currMax = 1;
                while (set.has(elem + currMax)) {
                    currMax++;
                }
                max = Math.max(currMax, max);
            }
        }
        return max;
    }
}
