/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let len = 0;
        let dummy = head;
        while (dummy) {
            len++
            dummy = dummy.next;
        }

        let diff = len-n;

        if (diff === 0) {
            return head.next;
        }

        let dummy2 = head;
        while (diff > 1) {
            dummy2 = dummy2.next;
            diff--
        }
        dummy2.next = dummy2.next.next;
        return head;
    }
}
