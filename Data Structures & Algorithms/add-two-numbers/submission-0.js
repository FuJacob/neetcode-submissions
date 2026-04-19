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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        const pairs = [];

        while (l1 || l2) {
            if (!l1) {
                pairs.push([0, l2.val]);
                l2 = l2.next;
            }
            else if (!l2) {
                pairs.push([l1.val, 0]);
                l1 = l1.next;
            }
            else {
                pairs.push([l1.val, l2.val]);
                l1 = l1.next;
                l2 = l2.next;
            }
        }

        let sum = 0;

        for (let i = 0; i < pairs.length; i++) {
            sum += (10 ** i) * (pairs[i][0] + pairs[i][1]);
        }
        let answerHead = new ListNode();
        let answer = answerHead;
        let sumAnswerArray = sum.toString().split('').reverse();
        console.log(sumAnswerArray)
        for (let i = 0; i < sumAnswerArray.length; i++) {
            answer.val = Number(sumAnswerArray[i]);
            if (i === sumAnswerArray.length - 1) {
                answer.next = null;
                break;
            }
            answer.next = new ListNode();
            answer = answer.next;
        }

        return answerHead;
    }
}
