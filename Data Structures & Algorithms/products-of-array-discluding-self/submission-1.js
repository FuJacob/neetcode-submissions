class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        if (n === 0) return nums;

        const prefix = new Array(n);
        const postfix = new Array(n);

        prefix[0] = 1;
        postfix[n-1] = 1;

        for (let i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i-1];
        }

        for (let i = n - 2; i >= 0; i--) {
            postfix[i] = postfix[i + 1] * nums[i+1];
        }


        const sol = [];
        for (let i = 0; i < nums.length; i++) {
            sol.push(postfix[i] * prefix[i]);
        }
        return sol;


    }


    // const product = nums.reduce((acc, elem) => acc*elem, 1);
    //     const arr = [];
    //     for (let i = 0; i < nums.length; i++) {
    //         arr.push(product/nums[i]);
    //     }
    //     return arr;
}
