# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseK(node):
            cur = node
            prev = None
            for i in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        dummy = ListNode(next=head)
        last_tail = dummy
        count = 0
        cur = head
        this_head = cur
        while cur:
            count += 1
            if count == k:
                next_head = cur.next
                last_tail.next = reverseK(this_head)
                this_head.next = next_head
                count = 0
                last_tail = this_head
                this_head = next_head
                cur = next_head
                count = 0
            else:
                cur = cur.next

        return dummy.next
                
                

