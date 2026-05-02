class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts = defaultdict(int)
        # for n in nums:
        #     counts[n]+=1
        # counts = list(counts.items())
        # counts.sort(key=lambda x: x[1], reverse=True)
        # result = []
        # for i in range(k):
        #     result.append(counts[i][0])
        # return result
        
        counts = defaultdict(int)
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        freq = [[] for i in range(len(nums)+1)]
        for n, c in counts.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                   return res
                

        