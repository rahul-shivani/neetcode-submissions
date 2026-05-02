class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        maxLen = 0
        for r, ch in enumerate(s):
            while ch in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(ch)
            maxLen = max(maxLen, r-l+1)
        return maxLen
            

        return maxLen