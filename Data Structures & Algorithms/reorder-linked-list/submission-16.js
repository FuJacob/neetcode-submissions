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
     * @return {void}
     */
    reorderList(head) {
        // consider empty or single node list exxplcitly, so no need to go tjhrough entire loop
        if (!head || !head.next) return head;
        const dummy = head;
        let [fast, slow] = [head, head];

        /// get middle node
        // let cutOffNode = null;
        while (fast && fast.next) {
            fast = fast.next.next;
            // cutOffNode = slow;
            slow = slow.next;
        }
        let cutOff = slow;
        slow = slow.next
        cutOff.next = null;
        // reverse 2nd half now
        let prev = null;

        while (slow) {
            const next = slow.next;
            slow.next = prev;
            prev = slow;
            slow = next;
        }


        // now merge, patern is basically 1 then insert 2 tjen 1 then insert 2

        while (head && prev) {
            const headNext = head.next;
            const prevNext = prev.next;
            head.next = prev;
            // if (!headNext) break;
            prev.next = headNext;
            head = headNext;
            prev = prevNext;
            
        }

        return dummy;
    }
}
