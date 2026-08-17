class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num2idx_map = {}
        for i in range(len(nums)):
            j = num2idx_map.get(target - nums[i], -1)
            if j != -1 and j != i:
                return [j, i]
            else:
                num2idx_map[nums[i]] = i
        
