class Solution:

    def encode(self, strs: List[str]) -> str:

        estr = "".join([f"{len(s)}#" + s for s in strs])

        return estr

    def decode(self, s: str) -> List[str]:
        dlist = [] 

        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            
            _len = int(s[i:j])

            j = j + 1
            dlist.append(s[j:j+_len])
            i = j + _len

        return dlist