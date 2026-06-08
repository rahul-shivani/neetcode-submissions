class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for s in strs[1:]:
            idx = 0
            while idx < (min(len(result), len(s))):
                if result[idx] != s[idx]:
                    break
                idx+=1
            result = result[:idx]
        return result
