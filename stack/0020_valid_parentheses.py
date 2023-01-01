class Solution:
    # using stack
    def isValid(self, s: str) -> bool:
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if c != pair[top]:
                    return False
        return len(stack) == 0

    # using stack (simpler way)
    def isValid2(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c not in pair:
                stack.append(c)
                continue
            if not stack or stack[-1] != pair[c]:
                return False
            stack.pop()
        return not stack
