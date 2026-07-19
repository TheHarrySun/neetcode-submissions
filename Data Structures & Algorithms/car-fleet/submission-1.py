class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [(position[i], speed[i]) for i in range(len(position))]
        stack.sort()

        res = 0
        max_time = 0
        while stack:
            pos, sp = stack.pop()
            time = (target - pos) / sp
            if time > max_time:
                res += 1
                max_time = time
        return res