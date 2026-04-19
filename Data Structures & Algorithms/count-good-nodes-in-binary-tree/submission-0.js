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
     * @return {number}
     */
    goodNodes(root) {

        function dfs(root, largestValSoFar) {
            if (!root) return 0;
            if (root.val >= largestValSoFar) {
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val);
            }
            return dfs(root.left, largestValSoFar) + dfs(root.right, largestValSoFar);

        }

        return dfs(root, -Infinity);
    }
}
