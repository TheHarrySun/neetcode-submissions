class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = -sorted_nums[i]
            while l < r:
                value = sorted_nums[l] + sorted_nums[r]
                if value > target:
                    r -= 1
                elif value < target:
                    l += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    prev = sorted_nums[l]
                    while l < len(nums) and sorted_nums[l] == prev:
                        l += 1
        return res