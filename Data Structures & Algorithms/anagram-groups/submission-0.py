class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_counts = []
        for s in strs:
            char_count = {}
            for ch in s:
                char_count[ch] = char_count.get(ch, 0) + 1
            char_counts.append(char_count)

        groups = []
        grouped = [False]*len(strs)
        for i in range(len(char_counts)):
            if grouped[i]:
                continue
            group = [strs[i]]
            grouped[i]=True
            for j in range(i+1, len(char_counts)):
                if char_counts[i]==char_counts[j]:
                    group.append(strs[j])
                    grouped[j] = True
            groups.append(group)
        
        return groups
