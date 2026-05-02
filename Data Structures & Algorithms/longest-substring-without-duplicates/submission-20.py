class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        _len = len(s)

        l = 0 
        r = 0
        maxLen = 0
        charSet = {}

        while l<=r and r<_len:
            print(l, r, maxLen)
            if s[r] not in charSet.keys() or charSet[s[r]]<l:
                maxLen = max(maxLen, r - l + 1)                
                charSet[s[r]] = r
                r+=1
            else:
                l = charSet[s[r]] + 1
                charSet.pop(s[r])
            
        return maxLen