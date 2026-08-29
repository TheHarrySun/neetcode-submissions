class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ans = 0
        i = 0
        while i < len(nums):
            jumpLength = nums[i]
            currMax = -1
            currMaxIdx = -1
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums) - 1:
                    currMaxIdx = j
                    break
                maxDist = j + nums[j]
                if maxDist > currMax:
                    currMaxIdx = j
                    currMax = maxDist
            i = currMaxIdx
            ans += 1
            if i >= len(nums) - 1:
                break
        return ans