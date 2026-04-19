class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freq = new Map();

        for (let i = 0; i < nums.length; i++) {
            freq.set(nums[i], (freq.get(nums[i]) || 0) + 1);
        }
        
        const solArr = [];

        for (let entry of freq.entries()) {
            solArr.push(entry);
        }
        solArr.sort((a, b) => b[1] - a[1]);

        return solArr.slice(0,k).map((elem) => elem[0]);
    }
}
