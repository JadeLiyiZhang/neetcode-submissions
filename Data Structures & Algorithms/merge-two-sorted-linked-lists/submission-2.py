# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2
        dummy = ListNode(0)
        cur = dummy
        while cur_1 and cur_2:
            if cur_1.val <= cur_2.val:
                cur.next = cur_1
                cur_1 = cur_1.next
                cur = cur.next
            else:
                cur.next = cur_2
                cur_2 = cur_2.next
                cur = cur.next
        cur.next = cur_1 if cur_1 else cur_2
        return dummy.next