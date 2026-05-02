class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        _len = len(nums)

        for i in range(_len):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = nums[i]
            left = i+1
            right = _len-1
            while left<right:
                _sum = target + nums[left] + nums[right]
                if _sum < 0:
                    left += 1
                elif _sum > 0:
                    right -= 1
                else:
                    result.append([target, nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return result