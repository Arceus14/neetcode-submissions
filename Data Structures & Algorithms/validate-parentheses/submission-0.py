class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm_brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        for l in s:
            if l in hm_brackets:
                if stack and hm_brackets[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        
        return True if not stack else False

        