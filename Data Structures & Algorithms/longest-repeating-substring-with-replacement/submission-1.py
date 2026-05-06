class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        subStrRep = [0]*26
        maxFreq = 0
        maxFreqChar = ''
        maxSubStrLen = 0
        r=-1
        for l in range(len(s)):
            while r<len(s)-1:
                r+=1
                subStrLen = r-l+1
                subStrRep[ord(s[r])-ord('A')] += 1
                if maxFreq<subStrRep[ord(s[r])-ord('A')]:
                    maxFreq=subStrRep[ord(s[r])-ord('A')]
                    maxFreqChar=s[r]
                # print(s[l:r+1], subStrLen, maxFreqChar, maxFreq)
                if k < subStrLen - maxFreq:
                    break
                maxSubStrLen = max(maxSubStrLen,subStrLen)
            subStrRep[ord(s[l])-ord('A')] -= 1
            if maxFreqChar == s[l]:
                maxFreq -= 1
        return maxSubStrLen
            
            