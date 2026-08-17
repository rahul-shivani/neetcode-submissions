class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = defaultdict(int)
        for n in nums:
            num_counts[n] += 1
        
        m_freq = [[] for i in range(len(nums)+1)]
        for key, val in num_counts.items():
            m_freq[val].append(key)
        
        result = []
        for i in range(len(m_freq)-1, -1, -1):
            for n in m_freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        # return result
        