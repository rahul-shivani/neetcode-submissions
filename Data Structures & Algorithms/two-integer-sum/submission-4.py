class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hashmap = {}
        for idx in range(len(nums)):
            _hashmap[nums[idx]]=idx
        
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in _hashmap and _hashmap[diff]!=idx:
                return [idx, _hashmap[diff]]
                
        