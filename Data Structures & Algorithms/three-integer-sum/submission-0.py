class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique = set(nums)
        result = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) * -1 in unique:
                    for k in range(j+1, len(nums)):
                        if nums[i]+nums[j]+nums[k] == 0:
                            result.add(tuple(sorted([nums[i], nums[j], nums[k]])))        
        result = [list(t) for t in result]
        return result