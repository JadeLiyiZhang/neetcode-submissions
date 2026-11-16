# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1

        dummy = ListNode()
        cur = dummy
        while heap:
            cur_val, cur_count, cur_node = heapq.heappop(heap)
            if cur_node.next:
                heapq.heappush(heap, (cur_node.next.val, count, cur_node.next))
                count += 1
            cur.next = cur_node
            cur = cur.next
        return dummy.next

        