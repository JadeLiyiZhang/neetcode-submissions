# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = l1
        cur_2 = l2
        dummy = ListNode()
        carry = 0
        cur = dummy
        while cur_1 and cur_2:
            temp_sum = cur_1.val + cur_2.val + carry
            num, carry = temp_sum % 10, temp_sum // 10
            cur.next = ListNode(num)
            cur = cur.next
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        
        while cur_1:
            temp_sum = cur_1.val + carry
            num, carry = temp_sum % 10, temp_sum // 10
            cur.next = ListNode(num)
            cur = cur.next
            cur_1 = cur_1.next
        
        while cur_2:
            temp_sum = cur_2.val + carry
            num, carry = temp_sum % 10, temp_sum // 10
            cur.next = ListNode(num)
            cur = cur.next
            cur_2 = cur_2.next
        if carry:
            cur.next = ListNode(carry)        

        return dummy.next
