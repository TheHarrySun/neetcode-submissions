class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count = [0] * 26

        for c in s1:
            count[ord(c) - ord('a')] += 1
        
        count2 = [0] * 26
        l = 0
        r = len(s1) - 1
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        if count == count2:
            return True        
        while r < len(s2) - 1:
            print(count2)
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            print(r)
            count2[ord(s2[r]) - ord('a')] += 1
            if count == count2:
                return True

        return count == count2