class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {
        const sol = [];
        nums = nums.sort((a, b) => a - b);

        for (let i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] === nums[i-1]) continue;
            const remainTarget = -nums[i];
            let left = i + 1;
            let right = nums.length - 1;


            while (left < right) {
                const currSum = nums[left] + nums[right];
                if (currSum === remainTarget) {
                    sol.push([nums[i], nums[left], nums[right]]);
                    left++;
                    right--;
                    while (left < right && nums[left] === nums[left -1]) {
                        left++;
                    }
                }
                else if (currSum > remainTarget) {
                    right--;
                }
                else left++;
            }
        }
        return sol;
    }
}
