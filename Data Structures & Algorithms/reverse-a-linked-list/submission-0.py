class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pre and cur pointers
        pre, cur = None, head
        # Reverse the implicit linked list
        while cur:
            # Invert the pointers
            nxt, cur.next = cur.next, pre
            # Update the pointers
            pre, cur = cur, nxt
        return pre
