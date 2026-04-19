class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let left = 0;
        let right = nums.length - 1;
        let middle = Math.floor((left+right) / 2);

        while (left <= right) {
            if (nums[middle] === target) return middle;
            else if (nums[middle] < target) {
                left = middle + 1;
            }
            else {
                right = middle -1 ;
            }
            middle = Math.floor((left+right) / 2);
        }
        return -1;
    }
}
