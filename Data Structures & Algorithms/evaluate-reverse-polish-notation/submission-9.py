class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        while tokens:
            t = tokens.pop(0)
            ops = ['+', '-', '/', '*']

            if stack and t in ops:
                b, a = stack.pop(), stack.pop()
                res = eval(f'{a} {t} {b}')
                stack.append(int(res))
            else:
                stack.append(t)
        return int(stack[0])