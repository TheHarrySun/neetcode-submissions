class Solution:
    # faster stack solution
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                area = stack[-1][1] * (i - stack[-1][0])
                res = max(area, res)
                start = stack[-1][0]
                stack.pop()
            stack.append((start, height))

        while stack:
            area = stack[-1][1] * (len(heights) - stack[-1][0])
            res = max(area, res)
            stack.pop()
        return res