class Solution:
    def search(self, nums: List[int], target: int) -> int:
        _len = len(nums)
        r = _len-1
        l = 0

        while l<=r:
            m = (l+1)//2 + r//2
            if nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
            else:
                return m
        
        return -1