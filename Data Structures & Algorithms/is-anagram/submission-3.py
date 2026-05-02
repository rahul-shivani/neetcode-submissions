class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0]*26

        for ch in s:
            idx = ord(ch)-ord('a')
            counts[idx]+=1

        for ch in t:
            idx = ord(ch)-ord('a')
            counts[idx]-=1
            if counts[idx]<0:
                return False

        return sum(counts)==0        