class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right_bounds = [len(heights)] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_bounds[i] = stack[-1]
            stack.append(i)
        
        stack = []
        left_bounds = [-1] * len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_bounds[i] = stack[-1]
            stack.append(i) 

        print(right_bounds)
        print(left_bounds)
        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i] * (right_bounds[i] - left_bounds[i] - 1))
        return res