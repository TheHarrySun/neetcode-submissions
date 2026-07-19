class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in value_to_index:
                return [value_to_index[diff], i]
            value_to_index[n] = i
        return []