class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def addNode(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.addNode(node)
            self.cache[key] = self.head.next
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.deleteNode(node)
            self.addNode(node)
            self.cache[key] = self.head.next
        else:
            if len(self.cache) < self.capacity:
                new_node = Node(key, value)
                self.addNode(new_node)
                self.cache[key] = self.head.next
            else:
                last_node = self.tail.prev
                self.deleteNode(last_node)
                del self.cache[last_node.key]
                new_node = Node(key, value)
                self.addNode(new_node)
                self.cache[key] = self.head.next
