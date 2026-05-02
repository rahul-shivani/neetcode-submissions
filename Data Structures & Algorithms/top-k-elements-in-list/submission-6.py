class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        

        freq = [[] for i in range(len(nums)+1)]

        for n, cnt in counts.items():
            freq[cnt].append(n)

        result = []
        for i in range(len(freq)-1, -1, -1):
            if len(result)<=k:
                result+=freq[i]
                
        return result[:k]
        