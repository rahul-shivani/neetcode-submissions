class Solution:
    def findMin(self, nums: List[int]) -> int:
        _len = len(nums)

        l = 0 
        r = _len - 1
        while l<=r:
            if _len==1 or nums[0]<nums[-1]:
                return nums[0]
            m = (l+1)//2 + r//2
            if nums[m]<nums[m-1]:
                return nums[m]
            elif nums[m]>nums[r]:
                l = m+1
            else:
                r = m-1
                
        
            
        