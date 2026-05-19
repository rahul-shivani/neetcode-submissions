class Solution:
    def trap(self, height: List[int]) -> int:
        pre = []
        post = []

        for i in range(len(height)):
            if i == 0:
                pre.append(0)
                post.append(0)
            else:
                pre.append(max(height[i-1], pre[-1]))
                post.append(max(height[len(height) - i], post[-1]))
        
        water = 0
        for i in range(len(height)):
            water += max(min(pre[i], post[len(height)-1-i]) - height[i], 0)
        
        return water
        