class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        leftBounds = [-1] * len(heights)
        stack = []
        for i, height in enumerate(heights):
            while stack and stack[-1][0] >= height:
                stack.pop()
            if len(stack) != 0:
                leftBounds[i] = stack[-1][1]
            stack.append((height, i))
        
        rightBounds = [len(heights)] * len(heights)
        stack2 = []
        for i in range(len(heights) - 1, -1, -1):
            while stack2 and stack2[-1][0] >= heights[i]:
                stack2.pop()
            if len(stack2) != 0:
                rightBounds[i] = stack2[-1][1]
            stack2.append((heights[i], i))
        print(leftBounds)
        print(rightBounds)
        
        res = 0
        for i in range(len(heights)):
            area = heights[i] * (rightBounds[i] - leftBounds[i] - 1)
            res = max(res, area)
        return res

        # [-1, 0, 0, 2, 2, ]