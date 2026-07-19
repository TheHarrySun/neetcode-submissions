class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            if (target - nums[i]) in ans:
                return [ans[target - nums[i]], i]
            ans[nums[i]] = i
        return []