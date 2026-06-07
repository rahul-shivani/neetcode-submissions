class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        min_num = 9999
        while l<=r: 
            mid = l//2 + (r+1)//2
            min_num = min(nums[mid], min_num)

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        return min_num
        