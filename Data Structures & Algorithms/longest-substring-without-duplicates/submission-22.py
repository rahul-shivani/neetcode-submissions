class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0 
        maxLen = 0
        subSet = set()
        for l in range(len(s)):
            while r<len(s) and s[r] not in subSet:
                subSet.add(s[r])
                r+=1
            maxLen = max(r-l, maxLen)
            subSet.remove(s[l])
        return maxLen
        