class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        post = []

        preProd = 1
        postProd = 1

        for i in range(1, len(nums)):
            pre.append(preProd)
            post.append(postProd)

            if i != 0:
                preProd *= nums[i-1]
                postProd *= nums[len(nums) - i] # (len(nums) - 1) - i + 1

        pre.append(preProd)
        post.append(postProd)

        print(pre)
        print(post)

        out = []
        for i in range(len(nums)):
            out.append(pre[i] * post[len(nums)-1-i])
        
        return out