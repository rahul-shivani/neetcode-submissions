class Solution:
    def isAlphaNum(self, ch):
        return (ch>='a' and ch<='z') or (ch>='A' and ch<='Z') or (ch>='0' and ch<='9')

    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        s=s.lower()
        while left<right:
            while left<right and not self.isAlphaNum(s[left]):
                left+=1
            while left<right and not self.isAlphaNum(s[right]):
                right-=1
            if s[left]!=s[right]:
                return False
            left, right = left+1, right-1
        return True

        