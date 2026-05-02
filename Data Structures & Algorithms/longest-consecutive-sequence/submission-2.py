class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in numSet:
                seqLen = 1
                nextNum = n+1
                while nextNum in numSet:
                    seqLen += 1
                    nextNum = nextNum+1
                longest = max(seqLen, longest)
        return longest

                    

        