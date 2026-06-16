class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Get an copy mapping of empty Nodes
        copyList = { None : None }
        # Create the deep copy of input nodes
        curr = head
        while curr:
            copyList[curr] = Node(curr.val)
            curr = curr.next
        # Link the deep copy of input nodes
        curr = head
        while curr:
            copy = copyList[curr]
            copy.next = copyList[curr.next]
            copy.random = copyList[curr.random]
            curr = curr.next
        # Return the deep copy of input list 
        return copyList[head]