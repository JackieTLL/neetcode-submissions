# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def mergeList(head1, head2):
            dummy = ListNode()
            curr = dummy
            while head1:
                curr.next = head1
                head1 = head1.next
                curr = curr.next
                curr.next = head2
                if head2:
                    head2 = head2.next
                    curr = curr.next
            return dummy.next
        def reverseList(head):
            prev = None
            while head:
                head_next = head.next
                head.next = prev
                prev = head
                head = head_next
            return prev
        def partition(head):
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            head2 = slow.next
            slow.next = None
            return head2
        head1 = head
        head2 = partition(head)
        head2 = reverseList(head2)
        mergeList(head1, head2)
