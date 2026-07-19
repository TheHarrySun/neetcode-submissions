class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1
            if count[i] > len(nums) // 2:
                return i