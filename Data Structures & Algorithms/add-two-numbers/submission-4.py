class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Get a head list node
        head = tail = ListNode(0, None)
        # Add the two linked lists by node
        carry = 0
        while l1 or l2 or carry:
            # Compute the arithmetic by node
            d1, d2 = l1.val if l1 else 0, l2.val if l2 else 0
            total = d1 + d2 + carry
            digit, carry = total % 10, total // 10
            # Allocate a node to store the digit
            tail.next = ListNode(digit, None)
            # Udpate the pointers
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            tail = tail.next
        # Return the sum linked list
        return head.next

