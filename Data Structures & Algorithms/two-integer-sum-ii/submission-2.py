class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            diff = target - numbers[l]
            if diff < numbers[r]:
                r -= 1
            elif diff > numbers[r]:
                l += 1
            else:
                return [l + 1, r + 1]
        return None