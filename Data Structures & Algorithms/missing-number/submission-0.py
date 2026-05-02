class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        out = 0
        for n in nums:
            out ^= n
        for i in range(len(nums)+1):
            out ^= i
        return out
        