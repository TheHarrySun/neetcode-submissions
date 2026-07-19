class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for c in s:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1
        for c in t:
            if not c in hash_map:
                return False
            else:
                hash_map[c] -= 1
        for key, val in hash_map.items():
            if val != 0:
                return False
        return True