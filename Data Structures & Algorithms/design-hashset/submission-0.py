class Node:

    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self.mySet = [Node(-1) for _ in range(10000)]

    def add(self, key: int) -> None:
        bucket = self.mySet[key % 10000]
        cur = bucket
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = Node(key)
        
    def remove(self, key: int) -> None:
        bucket = self.mySet[key % 10000]
        cur = bucket
        while cur and cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
            cur = cur.next

    def contains(self, key: int) -> bool:
        bucket = self.mySet[key % 10000]
        cur = bucket
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)