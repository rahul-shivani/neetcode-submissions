class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() ## sorting will help us decide if we have to increase r or l

        output = set()
        for idx in range(len(nums)):
            l=0
            r=len(nums)-1
            target = nums[idx]
            while l<r and l!=idx and r!=idx:
                # print(l, r, idx)
                if target == -1 * (nums[l] + nums[r]):
                    # print("-->", nums[l], nums[r], nums[idx])
                    output.add((nums[l], nums[r], nums[idx]))
                    if r>idx+1:
                        r-=1
                    elif l<idx-1:
                        l+=1
                    else:
                        break
                        
                elif target > -1 * (nums[l] + nums[r]):
                    if r>idx+1:
                        r-=1
                    else:
                        break
                elif l<idx-1:
                    l+=1
                else:
                    break
        
        return list(output)
            





        