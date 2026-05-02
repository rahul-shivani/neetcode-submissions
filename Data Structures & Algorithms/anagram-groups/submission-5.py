class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = {}
        for s in strs:
            rep = [0]*26
            for ch in s:
                rep[ord(ch)-ord('a')]+=1
            rep = tuple(rep)
            if rep in _dict:
                _dict[rep].append(s)
            else:
                _dict[rep] = [s]
        return [v for k, v in _dict.items()]
