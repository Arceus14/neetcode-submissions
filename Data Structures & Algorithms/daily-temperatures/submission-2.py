class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair of elements and indices
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                ele, index = stack.pop()
                res[index] = i - index
            stack.append((n, i))
        return res
            