class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        lst = [[p,s] for p, s in zip(position, speed)]
        lst = sorted(lst)

        for p, s in lst[::-1]:
            stack.append((target-p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
