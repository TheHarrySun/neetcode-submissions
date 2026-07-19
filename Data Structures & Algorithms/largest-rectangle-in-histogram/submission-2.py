class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_dist = [0] * len(heights)
        s = []

        for i, h in enumerate(heights):
            while s and h < s[-1][0]:
                left_dist[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append((h, i))
        for i in range(len(left_dist)):
            if left_dist[i] == 0:
                left_dist[i] = len(left_dist) - i
        
        right_dist = [0] * len(heights)
        s = []

        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            while s and h < s[-1][0]:
                right_dist[s[-1][1]] = s[-1][1] - i
                s.pop()
            s.append((h, i))
        for i in range(len(right_dist)):
            if right_dist[i] == 0:
                right_dist[i] = i + 1
        res = 0
        for i in range(len(heights)):
            res = max(res, (left_dist[i] + right_dist[i] - 1) * heights[i])
        return res