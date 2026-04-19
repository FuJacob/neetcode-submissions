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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root, k) {
        const vals = [];

        function dfs(root) {
            if (root) {
                vals.push(root.val);
                dfs(root.left);
                dfs(root.right);
            }
        }
        dfs(root);
        return vals.sort((a, b) => a - b)[k - 1];
    }
}
