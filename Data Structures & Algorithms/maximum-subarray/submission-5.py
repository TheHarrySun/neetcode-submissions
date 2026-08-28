class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -float('infinity')
        curSum = 0
        for i in range(0, len(nums)):
            curSum += nums[i]
            if curSum < 0:
                curSum = 0
                continue
            res = max(curSum, res)
        return res if res != -float('infinity') else max(nums)