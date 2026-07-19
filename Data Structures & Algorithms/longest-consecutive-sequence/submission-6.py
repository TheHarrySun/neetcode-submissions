class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for num in numset:
            if not (num - 1) in numset:
                length = 1
                while (num + length) in numset:
                    length += 1
                ans = max(length, ans)
        return ans