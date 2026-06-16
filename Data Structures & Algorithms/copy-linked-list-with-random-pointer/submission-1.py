class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyList = { None : None }
        curr = head
        while curr:
            copyList[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = copyList[curr]
            copy.next = copyList[curr.next]
            copy.random = copyList[curr.random]
            curr = curr.next
        return copyList[head]