class Solution:
    def isPermute(self, rep1: str, rep2: str) -> bool:
        for i in range(len(rep1)):
            if rep1[i]!=rep2[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len>s2_len:
            return False

        s1_rep = [0]*26
        sub_rep = [0]*26
        for idx in range(s1_len):
            s1_rep[ord(s1[idx])-ord('a')]+=1
            sub_rep[ord(s2[idx])-ord('a')]+=1
        
        if self.isPermute(s1_rep, sub_rep):
            return True
    
        idx = s1_len
        while idx<s2_len:
            sub_rep[ord(s2[idx-s1_len])-ord('a')]-=1
            sub_rep[ord(s2[idx])-ord('a')]+=1
            if self.isPermute(s1_rep, sub_rep):
                return True
            idx+=1

        return False


        