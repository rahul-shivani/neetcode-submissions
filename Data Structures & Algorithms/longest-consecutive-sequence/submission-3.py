class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        maxLen = 0
        for idx in range(len(nums)):
            if nums[idx]-1 not in unique:
                _len = 0
                while nums[idx] + _len in unique:
                    _len += 1
                maxLen = max(maxLen,_len)
        return maxLen
                    

        