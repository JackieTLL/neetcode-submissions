# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        plus = 0
        while l1 and l2:
            curr.next = ListNode(l1.val + l2.val + plus)
            if curr.next.val > 9:
                curr.next.val %= 10
                plus = 1
            else:
                plus = 0
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr.next = ListNode(l1.val + plus)
            if curr.next.val > 9:
                curr.next.val %= 10
                plus = 1
            else:
                plus = 0
            curr = curr.next
            l1 = l1.next
        while l2:
            curr.next = ListNode(l2.val + plus)
            if curr.next.val > 9:
                curr.next.val %= 10
                plus = 1
            else:
                plus = 0
            curr = curr.next
            l2 = l2.next
        if plus == 1:
            curr.val %= 10
            curr.next = ListNode(1)
        return dummy.next
            
        