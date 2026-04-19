class Node:
    def __init__(self, key=0, val=0, prev=None,nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}

        ## self head next points to the recently used
        ## self.tail.prev potins to least recently used
        self.head = Node()
        self.tail = Node()
        
        self.head.nxt = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node):
        node.nxt.prev, node.prev.nxt = node.prev, node.nxt

    def push_node(self, node):
        self.head.nxt.prev = node        
        node.nxt = self.head.nxt
        node.prev = self.head
        self.head.nxt = node

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.remove_node(node)
        self.push_node(node)
        return node.val
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self.remove_node(self.key_to_node[key])
        else:
            if self.capacity < len(self.key_to_node) + 1:
                old = self.tail.prev
                self.remove_node(old)
                del self.key_to_node[old.key]
        self.key_to_node[key] = Node(key, value)
        self.push_node(self.key_to_node[key])
        

        
