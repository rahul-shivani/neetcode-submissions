class Solution:
    def hasEveryChar(self, sRep, tRep):
        for i in range(58):
            if tRep[i]>sRep[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        tRep = [0]*58
        for c in t:
            tRep[ord(c)-ord('A')]+=1

        _len=len(s)
        l=0
        minLen = _len
        res = ""
        sRep = [0]*58
        for r in range(_len):
            sRep[ord(s[r])-ord('A')]+=1
            while self.hasEveryChar(sRep, tRep):
                subLen = r-l+1
                if minLen>=subLen:
                    res = s[l:r+1]
                    minLen = subLen
                minLen = min(minLen, r-l+1)
                sRep[ord(s[l])-ord('A')]-=1
                l+=1

        return res
            

