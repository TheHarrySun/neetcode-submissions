class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        return n * (n + 1) // 2 - total