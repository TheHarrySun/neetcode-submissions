class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i, pos in enumerate(position):
            time = (target - pos) / speed[i]
            stack.append((pos, time))
        stack.sort()

        res = 0
        slowest = 0
        while len(stack) != 0:
            _, time = stack.pop()
            if time > slowest:
                slowest = time
                res += 1
        return res