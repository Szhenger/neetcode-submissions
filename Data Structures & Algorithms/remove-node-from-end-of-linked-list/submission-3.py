class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get the size of linked list
        size, node = 0, head
        while node:
            size += 1
            node = node.next
        # Edge case: head node == (size - n + 1)th node
        dummy = ListNode(0, head)
        # Remove the (size - n + 1)th node
        curr = dummy
        for _ in range(size - n):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next

