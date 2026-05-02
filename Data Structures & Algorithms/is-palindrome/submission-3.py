class Solution:
    def isAlphaNumeric(self, ch: str) -> bool:
        if (ch.lower()>='a' and ch.lower()<='z') or \
            (ch>='0' and ch<='9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<=right:
            if not self.isAlphaNumeric(s[left]):
                left+=1
                continue
            if not self.isAlphaNumeric(s[right]):
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
        