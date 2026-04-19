/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        return this.dfs(root)[0]


    }

    dfs(root) {
        if (!root) return [true, 0];
        let [left, right] = [this.dfs(root.left), this.dfs(root.right)]
        const balanced = (Math.abs(left[1] - right[1]) <= 1) && left[0] && right[0];
        return [balanced, 1 + Math.max(left[1], right[1])];
    }

}
