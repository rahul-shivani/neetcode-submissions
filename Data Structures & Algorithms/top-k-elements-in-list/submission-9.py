class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        
        freq = [[] for i in range(len(nums)+1)] # remember this obvious mistake bro
        for key, v in count.items():
            freq[v].append(key)

        res = []
        for idx in range(len(freq)-1, -1, -1):
            for n in freq[idx]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
            