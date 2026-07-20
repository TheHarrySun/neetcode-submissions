class Solution:
    # this solution is like solution 1 but faster bc I dont need the checkSame operation
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts1 = [0] * 26
        counts2 = [0] * 26

        matches = 0
        for i in range(len(s1)):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index2_r = ord(s2[r]) - ord('a')
            index2_l = ord(s2[l]) - ord('a')
            counts2[index2_r] += 1
            counts2[index2_l] -= 1
            if s2[r] == s2[l]:
                l += 1
                continue
            
            if counts2[index2_r] == counts1[index2_r]:
                matches += 1
            if counts2[index2_r] == counts1[index2_r] + 1:
                matches -= 1
            
            if counts2[index2_l] == counts1[index2_l]:
                matches += 1
            if counts2[index2_l] == counts1[index2_l] - 1:
                matches -= 1
            l += 1
        return matches == 26