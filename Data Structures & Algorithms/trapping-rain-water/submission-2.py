class Solution:
    def trap(self, height: List[int]) -> int:
        left_maxes = [0] * len(height)
        for i in range(1, len(height)):
            left_maxes[i] = max(left_maxes[i - 1], height[i - 1])
            
        right_maxes = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            right_maxes[i] = max(right_maxes[i + 1], height[i + 1])
            
        res = 0
        for i in range(len(height)):
            water = min(left_maxes[i], right_maxes[i])
            res += max(0, water - height[i])
        return res