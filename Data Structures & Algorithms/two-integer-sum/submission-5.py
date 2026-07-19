class Solution:
    # we want a O(n) time solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = {}
        
        for i in range(len(nums)):
            if (target - nums[i]) in prevs.keys():
                return [prevs[target - nums[i]], i]
            prevs[nums[i]] = i
        return None