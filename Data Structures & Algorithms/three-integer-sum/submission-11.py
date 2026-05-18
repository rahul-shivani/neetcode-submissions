class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #solves uniqueness problem for me
        result = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue # need to skip for uniqueness
            target = nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                _sum = target + nums[l] + nums[r]
                if _sum == 0:
                    result.append([target, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif _sum > 0:
                    r-=1
                else:
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return result

        