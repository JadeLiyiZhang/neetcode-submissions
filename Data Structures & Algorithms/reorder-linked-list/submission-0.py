# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=, Sequence0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        while second:
            temp_1, temp_2 = first.next, second.next
            first.next = second
            second.next = temp_1
            first, second = temp_1, temp_2
            