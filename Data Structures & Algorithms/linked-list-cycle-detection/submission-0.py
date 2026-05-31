class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Get default slow and fast pointers
        slow = fast = head
        # Case 1: Input has a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        # Case 2: Input is a DAG
        return False 
        