class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if i >= len(word) or not char == word[i]:
                    return res
            res += char
        return res