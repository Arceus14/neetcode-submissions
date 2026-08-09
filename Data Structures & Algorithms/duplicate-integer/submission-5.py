class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        els = set()
        for n in nums:
            if n not in els:
                els.add(n)
            else:
                return True
        return False
        