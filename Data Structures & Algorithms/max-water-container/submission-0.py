class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxArea = 0
        while r>0:
            l=0
            while l<r:
                area = (r-l) * min(heights[l], heights[r])
                maxArea = max(maxArea, area)
                l = l+1
            r = r-1
        return maxArea
        