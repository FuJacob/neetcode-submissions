class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let product = 1;
        let zeroCount = 0;
        for (let i = 0; i < nums.length; i ++) {
            if (nums[i] !== 0) product *= nums[i];
            else zeroCount++;
        }

        if (zeroCount > 1) return new Array(nums.length).fill(0);

        const res = [];

        if (zeroCount === 0) {
            for (let i = 0; i < nums.length; i++) {
                res.push(product/nums[i]);
            }
        }
        else {
            for (let i = 0; i < nums.length; i++) {
                if (nums[i] === 0) res.push(product);
                else res.push(0)
            }
        }

        return res;


    }



}
