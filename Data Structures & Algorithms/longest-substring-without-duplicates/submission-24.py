class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        l, r = 0, 1
        maxLen = 1
        subStrRep = set([s[l]])
        while l<=r and r<len(s):
            if s[r] in subStrRep:
                subStrRep.remove(s[l])
                l += 1
            else:
                maxLen = max(maxLen, r-l+1)
                subStrRep.add(s[r])
                r += 1
        return maxLen

        