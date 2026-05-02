class Solution:
    def isAlphaNumeric(seld, ch:str) -> bool:
        ch = ch.lower()
        if (ch>='a' and ch<='z') or (ch>='0' and ch<='9'):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1

        while l<=r:
            if not self.isAlphaNumeric(s[l]):
                l+=1
                continue
            if not self.isAlphaNumeric(s[r]):
                r-=1
                continue
            if s[l].lower()!=s[r].lower():
                return False
            else:
                l+=1
                r-=1
        
        return True
        