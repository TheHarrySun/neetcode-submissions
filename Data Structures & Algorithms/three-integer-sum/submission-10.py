class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            target = -num
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                    continue
                if nums[l] + nums[r] > target: 
                    r -= 1
                    continue
                if not [num, nums[l], nums[r]] in res:
                    res.append([num, nums[l], nums[r]])
                l += 1
                r -= 1
        return res