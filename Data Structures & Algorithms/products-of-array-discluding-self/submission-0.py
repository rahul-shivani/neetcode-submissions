class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = len(nums)
        prefix = [1]*count
        postfix = [1]*count
        for i in range(1, count):
            prefix[i]=prefix[i-1]*nums[i-1]
            postfix[count-1-i]=postfix[count-i]*nums[count-i]
        res = []
        for i in range(count):
            res.append(prefix[i]*postfix[i])
        return res



        