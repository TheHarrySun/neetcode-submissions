class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}
        for i in range(len(nums)):
            if target - nums[i] in value_to_index:
                return [value_to_index[target-nums[i]], i]
            value_to_index[nums[i]] = i
        return []