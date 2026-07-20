class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        for entry in nums:
            if (entry - 1) not in hashset:
                length = 1
                while entry + length in hashset:
                    length += 1
                res = max(length, res)
        return res