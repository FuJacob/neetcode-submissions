class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let sum = -Infinity;
        if (nums.length === 0) return 0;
        if (nums.length === 1) return nums[0]
        let currSum = 0;
        for (let i = 0; i < nums.length; i++) {
            currSum += nums[i];
            if (currSum < 0) {
                sum = Math.max(sum, currSum);
                currSum = 0;
            }
            else {
                sum = Math.max(sum, currSum);
            }
        }

        return sum;
    }
}
