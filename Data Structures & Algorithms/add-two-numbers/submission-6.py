class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode(0, None)
        carry = 0
        while l1 or l2 or carry:
            d1, d2 = l1.val if l1 else 0, l2.val if l2 else 0
            total = d1 + d2 + carry
            digit, carry = total % 10, total // 10
            tail.next = ListNode(digit, None)
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
            tail = tail.next
        return head.next 