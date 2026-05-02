class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
            
        l = 0 
        r = 0 
        _len = len(s)

        charCount = [0]*26
        maxLen = 0
        charCount[ord(s[0])-ord('A')] += 1
        while r<_len and l<=r:
            subLen = (r-l+1)
            if  subLen - max(charCount) <= k:
                print("if  ", l, r, maxLen, charCount)
                maxLen = max(maxLen, subLen)                
                r+=1
                if r>=_len:
                    break
                charCount[ord(s[r])-ord('A')] += 1
            else:
                charCount[ord(s[l])-ord('A')] -= 1
                print("else", l, r, maxLen, charCount)
                l+=1
                    
        
        return maxLen
        

                        
        