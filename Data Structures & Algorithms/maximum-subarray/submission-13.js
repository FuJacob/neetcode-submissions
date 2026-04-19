class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let sum = -Infinity;
        let currSum = 0;
        for (let i = 0; i < nums.length; i++) {
            currSum += nums[i];
            sum = Math.max(sum, currSum);
            if (currSum < 0) {
                currSum = 0;
            }

        }

        return sum;
    }
}
