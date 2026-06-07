class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Divide evenly the input linked list into two disjoint linked lists 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        tail, slow.next = slow.next, None
        # Reverse the second linked list
        pre, cur = None, tail
        while cur:
            nxt, cur.next = cur.next, pre
            pre, cur = cur, nxt
        # Merge the linked lists
        ptr1, ptr2 = head, pre
        while ptr2:
            temp1, temp2 = ptr1.next, ptr2.next
            ptr1.next, ptr2.next = ptr2, temp1
            ptr1, ptr2 = temp1, temp2
        return None

    