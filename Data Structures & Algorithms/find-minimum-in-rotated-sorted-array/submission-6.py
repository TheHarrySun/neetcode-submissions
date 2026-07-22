class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            if nums[l] < nums[r]:
                return nums[l]
            if nums[m] >= nums[l]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
        return nums[l]