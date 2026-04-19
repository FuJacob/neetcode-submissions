
class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        if (!head) return null;
        
        const randomMap = new Map();

        // First pass: create all nodes and store in map
        let cur = head;
        while (cur) {
            const newNode = new Node(cur.val);
            randomMap.set(cur, newNode);
            cur = cur.next;
        }

        // Second pass: set next and random pointers
        let cur2 = head;
        while (cur2) {
            const newListNode = randomMap.get(cur2);
            newListNode.random = cur2.random ? randomMap.get(cur2.random) : null;
            newListNode.next = cur2.next ? randomMap.get(cur2.next) : null;
            cur2 = cur2.next;
        }
        
        return randomMap.get(head);
    }
}
