class ListNode:

    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, cap: int):
        # Get a integer variable of capacity
        self.capacity = cap
        # Initialize a doubly-linked list of (key, val) pairs
        self.lru = self.mru = ListNode(-1, -1)
        # Maintain a hashmap of (key, ListNode) pairs
        self.cache = {}
        # Update the doubly-linked list pointers
        self.lru.next, self.mru.prev = self.mru, self.lru

    def insert(self, node: ListNode) -> None:
        # Insert the node at the tail of doubly-linked list
        pre, nxt = self.mru.prev, self.mru
        pre.next = nxt.prev = node
        node.prev, node.next = pre, nxt

    def delete(self, node: ListNode) -> None:
        # Delete the node from doubly-linked list
        pre, nxt = node.prev, node.next
        pre.next, nxt.prev = nxt, pre

    def get(self, key: int) -> int:
        # Get the (key, val) pair in the cache instance
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, val: int) -> None:
        # Put the (key, val) pair into the cache instance
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = ListNode(key, val)
        self.insert(self.cache[key])
        
        # Remove the least-recently used (key, val) from the cache instance
        if len(self.cache) > self.capacity:
            self.cache.pop(self.lru.next.key)
            self.delete(self.lru.next)
    
