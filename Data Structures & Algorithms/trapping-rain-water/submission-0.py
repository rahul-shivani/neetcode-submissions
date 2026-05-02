class Solution:
    def trap(self, height: List[int]) -> int:
        peak = max(height)
        area = peak*len(height) - sum(height)
        print(area)

        lastMax = height[0]
        for n in height[1:]:
            area = area - (peak-lastMax)
            lastMax = max(lastMax, n)
            if n == peak:
                break
        print(area)

        lastMax = height[-1]
        for n in height[:-1][::-1]:
            area = area - (peak-lastMax)
            lastMax = max(lastMax, n)
            if n == peak:
                break

        return area