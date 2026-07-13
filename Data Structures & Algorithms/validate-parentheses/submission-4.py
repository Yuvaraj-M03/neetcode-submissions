class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        colsetoopen = {")":"(","}":"{","]":"["}
        for c in s:
            if c in colsetoopen:
                if stack and stack[-1] == colsetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        