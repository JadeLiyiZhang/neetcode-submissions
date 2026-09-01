class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # 创建一个哑结点
        dummy.next = head
        cur1 = cur2 = dummy  # 使用哑结点作为起始点，同时操作两个指针

        # 将cur1移动到n+1个位置，为了确保cur1和cur2之间保持n的距离
        for _ in range(n + 1):
            cur1 = cur1.next

        # 同时移动cur1和cur2，直到cur1达到链表末尾
        while cur1:
            cur1 = cur1.next
            cur2 = cur2.next

        # 删除节点，此时cur2正好位于待删除节点的前一个节点
        cur2.next = cur2.next.next

        # 返回哑结点的下一个节点，即真正的头结点
        return dummy.next
