class MinStack:

    def __init__(self):
        self.minStack = []
        self.ls = []        

    def push(self, val: int) -> None:
        self.ls.append(val)
        min_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_val)

    def pop(self) -> None:
        self.minStack.pop()
        return self.ls.pop()

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
