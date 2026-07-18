import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        l = 1
        r = maxk
        res = 1_000_000_000_000
        hours = 0
        while l <= r:
            k = (l + r) // 2
            hours = sum(math.ceil(p/k) for p in piles)
            if hours > h:
                l = k + 1
            elif hours <= h:
                r = k - 1
                res = min(k, res)

        return res