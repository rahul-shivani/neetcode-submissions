class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False

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
                
        