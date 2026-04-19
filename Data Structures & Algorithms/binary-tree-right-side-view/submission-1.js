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
            for (let i = q.length - 1; i >= 0; i--) {
                if (q[i]) {
                    sol.push(q[i].val);
                    break;
                }
            }
            const qLen = q.length;
            let count = 0;
            while (count < qLen) {
                const firstNode = q.shift();
                if (firstNode) {
                    q.push(firstNode.left);
                    q.push(firstNode.right);
                }
                count++;
            }
        }
        return sol;
    }
}
