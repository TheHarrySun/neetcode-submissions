class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}

        l = 0
        res = 0
        max_char = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            max_char = max(max_char, hashmap[s[r]])

            while r - l + 1 - max_char > k:
                hashmap[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
        return res