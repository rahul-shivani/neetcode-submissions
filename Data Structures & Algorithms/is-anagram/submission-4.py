class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        chars = [0]*26
        for idx in range(len(s)):
            chars[ord(s[idx])-ord('a')]+=1
            chars[ord(t[idx])-ord('a')]-=1
        
        for count in chars:
            if count!=0:
                return False
        return True
        