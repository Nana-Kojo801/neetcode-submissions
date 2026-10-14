class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
                continue
            if not stack or stack[-1] != pairs[ch]:
                return False
            else:
                stack.pop()
        return len(stack) == 0