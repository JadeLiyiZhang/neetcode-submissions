class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [Node(-1, -1) for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        cur = self.map[key % 10000]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key=key, val=value)

    def get(self, key: int) -> int:
        cur = self.map[key % 10000]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[key % 10000]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)