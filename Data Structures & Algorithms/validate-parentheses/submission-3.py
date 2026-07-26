class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []

        for c in s:
            if c in hmap and stack:
                if stack[-1] != hmap[c]:
                    return False
                else:
                    stack.pop()
                    continue
            stack.append(c)
        return True if not stack else False