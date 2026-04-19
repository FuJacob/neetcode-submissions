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
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        let dummy = new ListNode;
        let newHead = dummy;
        while(list1 || list2) {
            if (!list1) {
                dummy.next = list2;
                break;
            }
            else if (!list2) {
                dummy.next = list1;
                break;
            }
            else if (list1.val < list2.val) {
                dummy.next = list1;
                list1 = list1.next;
            }
            else {
                dummy.next = list2;
                list2 = list2.next;
            }
            dummy = dummy.next;
        }

        return newHead.next;
    }
}
