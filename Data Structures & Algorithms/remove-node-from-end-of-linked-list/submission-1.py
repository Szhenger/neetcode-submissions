class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Edge case
        dummy = ListNode(0, head)
        # Get the size of linked list
        size, node = 0, head
        while node:
            size += 1
            node = node.next
        # Remove the (size - n + 1)th node
        curr = dummy
        for _ in range(size - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

