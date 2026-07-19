class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1)
            digit = n & 1
            n = (n >> 1)
            res += digit
        return res