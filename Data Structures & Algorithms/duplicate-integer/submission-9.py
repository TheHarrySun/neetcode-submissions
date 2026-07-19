class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set()

        for entry in nums:
            if entry in uniques:
                return True
            uniques.add(entry)
        return False;