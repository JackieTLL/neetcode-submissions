# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        k = 0
        while head:
            head = head.next
            k += 1
        target = k - n
        count = 0
        prev = None
        head = dummy
        while head and count < target:
            prev = head
            head = head.next
            count += 1
        print(count)
        if prev and head:
            prev.next = head.next
        else:
            return dummy.next
        return dummy