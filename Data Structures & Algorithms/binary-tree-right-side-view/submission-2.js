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
     * @return {number[]}
     */
    rightSideView(root) {
        const sol = [];
        if (!root) return [];

        const q = [];
        q.push(root);

        while (q.length > 0) {
            const qLen = q.length;
            let visableNode = null;
            for (let i = 0; i < qLen; i++) {
                const currNode = q.shift();
                if (currNode) {
                    visableNode = currNode;
                    q.push(currNode.left);
                    q.push(currNode.right);
                }
            }
            if (visableNode) sol.push(visableNode.val);
        }
        return sol;
    }
}
