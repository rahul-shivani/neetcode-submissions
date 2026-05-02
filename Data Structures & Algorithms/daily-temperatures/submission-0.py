class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, t1 in enumerate(temperatures):
            count = 0
            consider = False
            for t2 in temperatures[i:]:
                if t2<=t1:
                    count+=1
                else: 
                    consider = True
                    break
            if not consider:
                count = 0
            res.append(count)
        return res