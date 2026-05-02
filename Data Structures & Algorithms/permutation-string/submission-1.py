class Solution:
    def shouldExpand(self, rep1, rep2):
        for i in range(0,26):
            if rep2[i]>rep1[i]:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Rep = [0]*26
        for ch in s1:
            s1Rep[ord(ch)-ord('a')] += 1
        
        l=0
        r=0
        _len = len(s2)
        subRep = [0]*26

        while r<_len and l<=r:
            print(l, r, subRep, s1Rep)
            if subRep == s1Rep:
                return True
            elif subRep[ord(s2[r])-ord('a')]+1<=s1Rep[ord(s2[r])-ord('a')]:
                subRep[ord(s2[r])-ord('a')]+=1
                r+=1
            else:
                if subRep[ord(s2[l])-ord('a')]>0:
                    subRep[ord(s2[l])-ord('a')]-=1
                l+=1
                if l>r:
                    r=l
        if r==_len and subRep == s1Rep:
            return True


        return False

