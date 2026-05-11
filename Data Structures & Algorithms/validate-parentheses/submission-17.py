class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in brackets_map.values():
                stack.append(ch)
            elif len(stack)!=0 and stack[-1]==brackets_map[ch]:
                stack.pop()
            else:
                return False
        return not stack
                
        