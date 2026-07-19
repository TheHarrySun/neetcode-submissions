class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        prevs = {}
        index = 0
        
        for word in strs:
            curr = [0] * 26
            for char in word:
                curr[ord(char) - ord('a')] += 1
            if str(curr) in prevs.keys():
                res[prevs[str(curr)]].append(word)
            else:
                prevs[str(curr)] = index
                res.append([word])
                index += 1
        return res