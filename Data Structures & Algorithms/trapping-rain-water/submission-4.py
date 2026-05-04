class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        suffix = [0]

        for i in range(1, len(height)):
            prefix.append(max(prefix[-1], height[i-1]))
            suffix.append(max(suffix[-1], height[len(height)-i]))
        
        totalWater = 0
        for i in range(0, len(height)):
            # print(prefix[i], suffix[len(height)-1-i], min(prefix[i], suffix[len(height)-1-i]) - height[i])
            totalWater += max(min(prefix[i], suffix[len(height)-1-i]) - height[i], 0)
        
        return totalWater
            