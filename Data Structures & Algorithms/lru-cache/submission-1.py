class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.key_to_node = {}
    
    def _remove_node(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
    
    def _add_node_to_front(self, node: Node) -> None:
        prev_front = self.head.next
        self.head.next = node
        prev_front.prev = node
        node.next = prev_front
        node.prev = self.head

    def get(self, key: int) -> int:
        """
        1. check if exsits - return -1 if not
        2. get the value
        3. udpate recently used cache
        """
        if key not in self.key_to_node:
            return -1
        self._remove_node(self.key_to_node[key])
        self._add_node_to_front(self.key_to_node[key])
        return self.key_to_node[key].val
        

    def put(self, key: int, value: int) -> None:
        """
        1. check if exists: updtae in place - otherwise add pair to cache
        2. udpate recently used cache
        """
        if key in self.key_to_node:
            self.key_to_node[key].val = value
            self._remove_node(self.key_to_node[key])
        else:
            self.key_to_node[key] = Node(key, value)
            if self.capacity < len(self.key_to_node):
                last = self.tail.prev
                self._remove_node(last)
                del self.key_to_node[last.key]
        self._add_node_to_front(self.key_to_node[key])
        
        
            
    """
    udpate recnetly used cahce:
    1. move to front
    2. remove X node
    """

    """
    data sturctuers
    - linked list to maintain cache
    - then we also need -> ahshmap for easy quick access to value
    """
        
