class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            elif not stack or (ch == ')' and stack.pop() != '(') or (ch == '}' and stack.pop() != '{') or (ch == ']' and stack.pop() != '['):
                return False
        if stack:
            return False
        return True
            
        