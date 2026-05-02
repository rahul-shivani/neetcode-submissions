class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = []
        suffix = []

        _len = len(height)

        maxP = 0
        maxS = 0

        for i in range(_len):
            if i == 0:
                prefix.append(maxP)
                suffix.append(maxS)
            else:
                maxP = max(maxP, height[i-1])
                maxS = max(maxS, height[_len-i])

                prefix.append(maxP)
                suffix.append(maxS)
        
        suffix = suffix[::-1]

        area = 0
        for i in range(1,_len-1):
            area += max(0, min(prefix[i], suffix[i]) - height[i])
        
        return area


            