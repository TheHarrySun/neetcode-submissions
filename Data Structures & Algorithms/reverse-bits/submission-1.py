class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            digit = n & 1
            n >>= 1
            if digit == 1:
                res += 2**(32 - i - 1)
        return res