class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ch_counts = [0]*26
            for ch in s:
                ch_counts[ord(ch)-ord('a')]+=1
            ans[tuple(ch_counts)].append(s)
        return ans.values()
            