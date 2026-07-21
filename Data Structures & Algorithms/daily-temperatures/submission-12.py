class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            
            while stack and temp >= stack[-1][0]:
                stack.pop()
            
            if len(stack) != 0:
                res[i] = stack[-1][1] - i
            stack.append((temp, i))
        return res
