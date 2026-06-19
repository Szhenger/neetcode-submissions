class ListNode:

    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, cap: int):
        # Get a capacity variable
        self.capacity = cap
        # Initialize a doubly-linked list of (key, val) pairs
        self.lru = self.mru = ListNode(-1, -1)
        self.lru.next, self.mru.prev = self.mru, self.lru
        # Initialize a hashmap of (key, ListNode) pairs
        self.cache = {}

    def delete(self, node: ListNode) -> None:
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def insert(self, node: ListNode) -> None:
        pre, nxt = self.mru.prev, self.mru
        pre.next = nxt.prev = node
        node.prev, node.next = pre, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return node.val
        return -1
    
    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = ListNode(key, val)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            node = self.lru.next
            self.cache.pop(node.key)
            self.delete(node)
    
