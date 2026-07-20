class Solution:
    def trap(self, height: List[int]) -> int:
        left_heights = [0] * len(height)
        right_heights = [0] * len(height)

        max_left = 0
        for i, entry in enumerate(height):
            max_left = max(entry, max_left)
            left_heights[i] = max_left
        
        max_right = 0
        for i in range(len(height) - 1, -1, -1):
            max_right = max(height[i], max_right)
            right_heights[i] = max_right
        
        res = 0
        for i in range(len(height)):
            res += min(left_heights[i], right_heights[i]) - height[i]
        return res