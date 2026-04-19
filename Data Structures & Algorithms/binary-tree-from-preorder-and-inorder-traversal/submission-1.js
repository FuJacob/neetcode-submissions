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
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        if (preorder.length === 0 && inorder.length === 0) return null;

        const node = new TreeNode(preorder[0]);
        const index = inorder.indexOf(preorder[0]);
        node.left = this.buildTree(preorder.slice(1, index + 1), inorder.slice(0, index));
        node.right = this.buildTree(preorder.slice(index + 1), inorder.slice(index + 1));
        return node;
    }
}
