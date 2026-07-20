class Solution:
    # this solution uses two pointers
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        leftMax = height[l]
        rightMax = height[r]

        res = 0
        while l < r:
            leftMax = max(height[l], leftMax)
            rightMax = max(height[r], rightMax)
            if leftMax < rightMax:
                res += leftMax - height[l]
                l += 1
            if rightMax <= leftMax:
                res += rightMax - height[r]
                r -= 1
        return res