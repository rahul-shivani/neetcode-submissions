class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uNums = set(nums)
        cLen = defaultdict(int)
        result = 0
        for n in uNums:
            if n-1 in cLen:
                cLen[n] = cLen[n-1]+1
            else:
                count = 0
                while n-count in uNums:
                    count+=1
                cLen[n] = count
            result = max(cLen[n], result)
        return result