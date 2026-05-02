class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        u = max(piles)
        l = sum(piles)//h

        ans = u
        while l<=u:
            m = (l+1)//2 + u//2
            if m == 0 :
                break
            hours = 0 
            for p in piles:
                hours += p//m + (1 if p%m else 0)
            if hours>h:
                l = m+1
            elif hours<=h:
                u = m-1
                ans = m
            else:
                ans = m
                break
        
        return ans

        