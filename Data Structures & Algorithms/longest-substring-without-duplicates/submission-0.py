class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for i, c1 in enumerate(s):
            len_ = 1
            seen = set([c1])            
            for c2 in s[i+1:]:
                if c2 in seen:
                    break
                seen.add(c2)
                len_+=1
            maxlen = max(maxlen, len_)
        return maxlen
                
        