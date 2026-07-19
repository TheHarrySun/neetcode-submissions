class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        length = 0
        for i in num_set:
            if not (i - 1) in num_set:
                temp_length = 1
                curr = i + 1
                while curr in num_set:
                    temp_length += 1
                    curr += 1
                length = max(temp_length, length)
        return length