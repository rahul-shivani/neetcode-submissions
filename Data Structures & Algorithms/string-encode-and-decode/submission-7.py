class Solution:
    s: str

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[~NONE~]"

        out = ""
        for s in strs:
            if out:
                out+="[~JOIN~]"
            if s == "":
                out+="[~EMPTY~]"
            else:
                out+=s

        return out


    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "[~NONE~]":
            return []
        
        out = []
        split = s.split("[~JOIN~]")
        for s in split:
            if s == "[~EMPTY~]":
                out.append("")
            else:
                out.append(s)
        
        return out
        
