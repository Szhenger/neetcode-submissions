class ListNode:

    def __init__(self, key: int, val: int) -> None:
        self.key, self.val = key, val
        self.pre = self.nxt = None

class LRUCache:

    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.lru = self.mru = ListNode(-1, -1)
        self.lru.nxt, self.mru.pre = self.mru, self.lru
        self.cache = {} # key -> ListNode(key, val, pre, nxt)
    
    def insert(self, node: "ListNode") -> None:
        pre, nxt = self.mru.pre, self.mru
        node.pre, node.nxt = pre, nxt
        pre.nxt = nxt.pre = node 

    def remove(self, node: "ListNode") -> None:
        pre, nxt = node.pre, node.nxt
        pre.nxt, nxt.pre = nxt, pre

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, val)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            self.cache.pop(self.lru.nxt.key)
            self.remove(self.lru.nxt)
