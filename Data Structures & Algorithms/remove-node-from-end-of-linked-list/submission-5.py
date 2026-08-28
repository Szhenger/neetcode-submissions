class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dumb = ListNode(0, head)
        size, node = 0, dumb.next
        while node:
            size += 1
            node = node.next
        curr = dumb
        for _ in range(size - n):
            curr = curr.next
        curr.next = curr.next.next
        return dumb.next