class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let sum = -Infinity;
        let currSum = 0;
        for (let i = 0; i < nums.length; i++) {
            currSum = Math.max(nums[i] + currSum, nums[i]);
            sum = Math.max(sum, currSum);
        }

        return sum;
    }
}
