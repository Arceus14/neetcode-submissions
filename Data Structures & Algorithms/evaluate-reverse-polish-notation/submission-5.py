class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        st = []
        if len(tokens) == 1:
            return int(tokens.pop())
        while tokens:
            a = tokens.pop(0)
            try:
                st.append(int(a))
            except ValueError :
                y, x = st.pop(), st.pop()
                res = int(eval(f'{x} {a} {y}'))
                st.append(res)
        return res