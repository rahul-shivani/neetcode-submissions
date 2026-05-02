class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = set()

        second_idx = -1

        for idx in range(len(nums)):
            if target - nums[idx] in diff:
                second_idx = idx
                break
            else:
                diff.add(nums[idx])

        first_idx = -1
        for idx in range(len(nums)):
            if target - nums[second_idx] == nums[idx]:
                first_idx = idx
                break
        
        return [first_idx, second_idx]

        