class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _len = len(s)
        unique = set()
        l = 0
        r = 0
        maxLen = 0
        while l<_len and r<_len and l<=r:
            if s[r] not in unique:
                maxLen = max(maxLen, r-l+1)
                unique.add(s[r])
                r+=1
            else:
                unique.remove(s[l])
                l+=1
        return maxLen

