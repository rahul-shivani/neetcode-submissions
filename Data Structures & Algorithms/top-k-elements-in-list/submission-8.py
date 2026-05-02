class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1

        freqGroups = [[] for i in range(len(nums))]
        for key, val in countMap.items():
            freqGroups[val-1].append(key)

        result = []
        for idx in range(len(nums)-1, -1, -1):
            if freqGroups[idx]:
                result += freqGroups[idx]
                print(result, len(result), k)
                if len(result) == k:
                    break
        
        return result