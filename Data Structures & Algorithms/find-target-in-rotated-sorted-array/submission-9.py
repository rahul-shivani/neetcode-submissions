class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## SOLUTION:
        ## Find sorted side, check if the target can lie in sorted side
        ## if yes, move to sorted side else move to unsorted side

        l = 0 
        r = len(nums)-1

        while l<=r:
            mid = l//2 + (r+1)//2

            if nums[mid] == target:
                return mid
            elif nums[l] < nums[mid]: # is left side sored?
                if target >= nums[l] and target < nums[mid]: # can target lie in left sorted side
                    r = mid - 1
                else: # if not, move to other side
                    l = mid + 1 
            else:
                if target > nums[mid] and target <= nums[r]: # can targer lie right sorted side
                    l = mid + 1                
                else: # if not, move to other side
                    r = mid - 1
        
        return -1 
        