class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = collections.defaultdict(int)

        for n in nums:
            if hmap[n] == 1:
                return True
            else:
                hmap[n] += 1
        return False
