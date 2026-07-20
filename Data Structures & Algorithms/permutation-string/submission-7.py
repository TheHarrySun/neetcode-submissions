class Solution:
    def checkSame(self, map1, map2):
        for key, val in map1.items():
            if key in map2 and map2[key] == map1[key]:
                continue
            return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map1 = defaultdict(str)
        map2 = defaultdict(str)

        for char in s1:
            map1[char] = 1 + map1.get(char, 0)
        
        l = 0
        for i in range(len(s1)):
            map2[s2[i]] = 1 + map2.get(s2[i], 0)
        if self.checkSame(map1, map2):
            return True
        r = len(s1)
        while r < len(s2):
            map2[s2[l]] -= 1
            l += 1
            map2[s2[r]] = 1 + map2.get(s2[r], 0)
            r += 1
            if self.checkSame(map1, map2):
                return True
        return False