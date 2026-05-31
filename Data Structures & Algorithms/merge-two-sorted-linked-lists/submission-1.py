class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # nitialize dummy node and tail pointer
        dummy = tail = ListNode(0, None)
        # Merge sort list1 and list2
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next 
            tail = tail.next
        # Append the remainder of either list1 or list2 
        tail.next = list1 if list1 else list2
        # Return the sorted linked lists
        return dummy.next