class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                continue
            left_max[i] = max(left_max[i - 1], height[i - 1])
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                continue
            right_max[i] = max(right_max[i + 1], height[i + 1])
        ans = 0
        for i in range(len(height)):
            surr = min(left_max[i], right_max[i])
            ans += (surr - height[i] if (surr - height[i]) > 0 else 0)
        return ans