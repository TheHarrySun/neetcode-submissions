class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
        # say that left side is least recently used, right is most recnetly used
        self.capacity = capacity
        self.map = {}

    def _use(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.right.prev
        self.right.prev.next = node

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            self._use(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._use(self.map[key])
            self.map[key].val = value
            return
        newnode = Node(key, value)
        self.map[key] = newnode

        newnode.prev = self.right.prev
        self.right.prev.next = newnode

        newnode.next = self.right
        self.right.prev = newnode

        if len(self.map) > self.capacity:
            deleted_key = self.left.next.key
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            del self.map[deleted_key]