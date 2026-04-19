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

        if (root == null) return 0;
        let leftHeight = this.getMaxHeight(root.left);
        let rightHeight = this.getMaxHeight(root.right);
        let diameter = leftHeight + rightHeight;
        let sub = Math.max(this.diameterOfBinaryTree(root.left), this.diameterOfBinaryTree(root.right));

        return Math.max(diameter, sub);


    }

    getMaxHeight(root) {
        if (!root) return 0;
        return 1 + Math.max(this.getMaxHeight(root.left), this.getMaxHeight(root.right));
    }
}
