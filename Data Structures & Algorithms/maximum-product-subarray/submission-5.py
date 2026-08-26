class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMin = 1
        currMax = 1
        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
                continue
            temp = n * currMax
            currMax = max(n * currMin, n * currMax, n)
            currMin = min(n * currMin, temp, n)
            if res < currMax:
                res = currMax
        return res