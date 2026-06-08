class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        result = max(piles)
        # print(sum(piles)//h, max(piles)+1)
        # for k in range(sum(piles)//h, max(piles)+1):
        #     hours = 0
        #     for p in piles:
        #         hours += (p+k-1)//k
        #     if hours<=h:
        #         result = min(result, k)

        minK = max(sum(piles)//h, 1) ## Good Edge Case
        maxK = max(piles)

        while minK<=maxK:
            k = minK + (maxK-minK)//2
            hours = 0
            for p in piles:
                hours += (p+k-1)//k
            if hours<=h:
                result = min(result, k)
                maxK = k-1
            else:
                minK = k+1

        return result
        