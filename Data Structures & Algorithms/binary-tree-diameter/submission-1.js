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
    diameterOfBinaryTree(root) {
        let bestDia = 0;
        if (!root) return 0;
        let leftPath = this.getLongestPath(root.left);
        let rightPath = this.getLongestPath(root.right);
        let currDia = leftPath + rightPath;
        bestDia = Math.max(currDia, this.diameterOfBinaryTree(root.left), this.diameterOfBinaryTree(root.right));
        return bestDia;
    }

    getLongestPath(root) {
        if (!root) return 0;
        return 1 + Math.max(this.getLongestPath(root.left), this.getLongestPath(root.right));
    }
}
