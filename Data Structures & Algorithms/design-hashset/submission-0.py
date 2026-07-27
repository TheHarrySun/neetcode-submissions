class MyHashSet:

    def __init__(self):
        self.hashset = []
        for i in range(1024):
            self.hashset.append([])

    def hashfunc(self, key):
        return key % 1024

    def add(self, key: int) -> None:
        hashed = self.hashfunc(key)
        if not self.contains(key):
            self.hashset[hashed].append(key)

    def remove(self, key: int) -> None:
        hashed = self.hashfunc(key)
        if key in self.hashset[hashed]:
            self.hashset[hashed].remove(key)

    def contains(self, key: int) -> bool:
        hashed = self.hashfunc(key)
        return True if key in self.hashset[hashed] else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)