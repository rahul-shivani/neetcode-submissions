class Solution:
    def areAnagrams(self, str1: str, str2: str):

        l1 = len(str1)
        l2 = len(str2)

        if l1 != l2:
            return False
        
        counter = [0] * 26

        for i in range(l1):
            counter[ord(str1[i])-ord('a')]+=1
            counter[ord(str2[i])-ord('a')]-=1

        for c in counter:
            if c != 0:
                return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = [0] * len(strs)

        groups = []

        for i in range(len(strs)):
            
            if grouped[i] == 1:
                continue

            group = [strs[i]]
            grouped[i] = 1
            
            for j in range(i+1, len(strs)):
                if grouped[j] == 0 and self.areAnagrams(strs[i], strs[j]):
                    group.append(strs[j])
                    grouped[j] = 1
                        
            groups.append(group)

        return groups



        