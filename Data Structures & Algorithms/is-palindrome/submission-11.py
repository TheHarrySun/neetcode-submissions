class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        end = len(s) - 1
        while front < end:
            if not s[front].isalnum():
                front += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            front_char = s[front].lower()
            end_char = s[end].lower()
            if front_char != end_char:
                return False
            front += 1
            end -= 1
        return True
