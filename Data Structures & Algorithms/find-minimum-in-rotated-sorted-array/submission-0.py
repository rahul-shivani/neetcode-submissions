class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        if nums[r]>nums[l]:
            return nums[0]

        min_ = 1001
        while l<=r:
            mid = (l+r)//2
            min_ = min(nums[mid], min_)
            if min_ < nums[r]:
                r = mid
            else:
                l = mid+1
        
        return min_
            
        