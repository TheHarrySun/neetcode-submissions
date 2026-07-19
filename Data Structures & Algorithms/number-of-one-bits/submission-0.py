class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(32):
            temp = (n >> 1)
            if 2 * temp + 1 == n:
                res += 1
            n = temp
        return res