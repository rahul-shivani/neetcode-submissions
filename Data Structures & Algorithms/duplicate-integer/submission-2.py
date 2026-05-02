class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for n in nums:
            if n in _set:
                return True
            _set.add(n)
        return False