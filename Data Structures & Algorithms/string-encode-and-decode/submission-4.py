from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for word in strs:
            res += str(len(word))
            res += '#'
            res += word
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        while s.find('#') != -1:
            index = s.index('#')
            length = int(s[:index])
            res.append(s[(index + 1):(index + 1 + length)])
            s = s[(index + 1 + length):]
        return res