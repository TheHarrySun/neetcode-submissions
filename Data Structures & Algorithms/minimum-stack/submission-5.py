class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mins) == 0:
            self.mins.append(0)
        else:
            self.mins.append(len(self.mins) if val < self.stack[self.mins[-1]] else self.mins[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.mins[-1]]
