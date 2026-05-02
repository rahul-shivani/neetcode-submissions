class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        _map = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for ch in s:
            if ch in _map.keys():
                if not stack or _map[ch]!=stack.pop():
                    return False
            else:
                stack.append(ch)
        
        return not stack
