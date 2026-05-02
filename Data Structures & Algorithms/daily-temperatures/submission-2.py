class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        _stack = []
        for idx in range(len(temperatures)):
            while _stack and temperatures[_stack[-1]]<temperatures[idx]:
                _i = _stack.pop()
                res[_i] = idx - _i
            _stack.append(idx)            
        return res
        