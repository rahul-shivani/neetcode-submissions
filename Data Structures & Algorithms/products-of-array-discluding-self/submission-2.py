class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []

        _pre = 1
        _post = 1
        for i in range(len(nums)):
            if i != 0: 
                _pre *= nums[i-1]
                _post *= nums[len(nums)-i] 
            pre.append(_pre)
            post.append(_post)   

        # print(pre, post)             
        
        res = []
        for i in range(len(nums)):
            res.append(pre[i]*post[len(nums)-1-i])
        
        return res