class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n]+=1
        counts = list(counts.items())
        counts.sort(key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(counts[i][0])
        return result

        