class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pre and cur pointers
        pre, cur = None, head
        # Reverse the linked list
        while cur:
            # Invert the pointers
            nxt, cur.next = cur.next, pre
            # Update the pointers
            pre, cur = cur, nxt
        # Return the linked list
        return pre
